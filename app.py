import http.server
import socketserver
import os
import urllib.parse
import json
import argparse
import logging
import math

DEFAULT_PORT = 8000
ALLOWED_FUNCTIONS = {"sin": math.sin, "cos": math.cos, "tan": math.tan, "log": math.log, "sqrt": math.sqrt, "exp": math.exp, "pow": math.pow, "abs": abs, "factorial": math.factorial, "pi": math.pi, "e": math.e}

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Sovrascrive il metodo do_GET per reindirizzare al file index.html nella sotto-cardella templates
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.path = os.path.join("templates", 'index.html')
            self.send_response(200)  # Success

        elif self.path == '/favicon.ico':
            self.path = os.path.join("resources", 'favicon.ico')
            self.send_response(200)  # Success

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    # Sovrascrive il metodo do_POST per gestire le richieste POST
    def do_POST(self):
        # Lgge il contenuto della richiesta POST
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        parsed_data = urllib.parse.parse_qs(post_data.decode('utf-8'))

        # Se il path è /calculate, valuta l'espressione aritmetica e restituisce il risultato
        if self.path == '/calculate':
            result = None
            error_type = None
            status = 'success'
            
            result, error_type, status = self.evaluate_expression(parsed_data)
                
            if(status == 'success'):
                self.send_response(200) # Success
            else:
                self.send_response(400) # Bad Request

            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'result': result, 'error_type': error_type, 'status': status}).encode())
        
        else:
            self.send_response(404) # Not Found
            self.end_headers()
            self.wfile.write(b'Not Found')

    # Valuta l'espressione aritmetica
    def evaluate_expression(self, parsed_data):
        result = None
        error_type = None
        status = 'success'

        # Valuta e traduce l'espressione aritmetica
        try:
            expression = parsed_data['expression'][0]
            expression = self.translate_expression(expression)
            result = eval(expression, {'__builtins__': None}, ALLOWED_FUNCTIONS)
        except Exception as e:
            if type(e) == NameError:
                error_type = 'Name Error'
            elif type(e) == ValueError:
                error_type = 'Value Error'
            elif type(e) == KeyError:
                error_type = 'Key Error'
            elif type(e) == ZeroDivisionError:
                error_type = 'Zero Division Error'
            elif type(e) == SyntaxError:
                error_type = 'Syntax Error'
            elif type(e) == TypeError:
                error_type = 'Type Error'
                logging.warning(f"possible SQL Injection attempt from {self.client_address}: {expression}")
            else:
                error_type = 'Unknown Error'
                print(e, type(e))
            status = 'error'
            logging.error(f"Error evaluating expression: {e}")

        return result, error_type, status

    # Traduce l'espressione aritmetica in un formato che può essere valutato da eval
    def translate_expression(self, expression):
        translated = expression.replace('^', '**')
        return translated

# Funzione per avviare il server    
def start_server(port):
    with socketserver.TCPServer(("", port), MyHttpRequestHandler) as httpd:
        print(f"Server successfully started on http://localhost:{port}")
        httpd.serve_forever()

def main():
    # Configura il parser degli argomenti
    parser = argparse.ArgumentParser(description="Web Calculator Application")
    parser.add_argument("command", choices=["start"], help="Command to execute")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"Port number (default: {DEFAULT_PORT})")

    args = parser.parse_args()

    if args.command == "start":
        start_server(args.port)

if __name__ == "__main__":
    main()
import os
import json
import logging
import math
import urllib.parse
from flask import Flask, request, send_from_directory

DEFAULT_PORT = 8000
ALLOWED_FUNCTIONS = {"sin": math.sin, "cos": math.cos, "tan": math.tan, "log": math.log, "sqrt": math.sqrt, "exp": math.exp, "pow": math.pow, "abs": abs, "factorial": math.factorial, "pi": math.pi, "e": math.e}
HISTORY_FILE = 'history.json'

app = Flask(__name__)
history = []

@app.route('/')
@app.route('/index.html')
def index():
    try:
        load_history()
        with open('templates/index.html', 'r') as file:
            file_content = file.read()
            file_content = file_content.replace('HISTORY_PLACEHOLDER', history_json_to_html(history))
            return file_content
    except Exception as e:
        logging.error(f"Error loading index.html: {e}")
        return '<h1>Error loading index.html</h1>'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'resources/favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/calculate', methods=['POST'])
def calculate():
    print(request.get_json())
    content = request.get_json()
    expression = content.get('expression', '')

    result, error_type, status = evaluate_expression(expression)
    
    response = {'result': result, 'error_type': error_type, 'status': status}
    
    if status == 'success':
        status_code = 200
        history.append({'expression': expression, 'result': result})
        save_history(history)
    else:
        status_code = 400

    return json.dumps(response), status_code, {'Content-Type': 'application/json'}

@app.route('/clear_history', methods=['POST'])
def clear_history():
    global history
    history = []
    save_history(history)
    return json.dumps({'status': 'success'}), 200, {'Content-Type': 'application/json'}

def evaluate_expression(expression):
    result = None
    error_type = None
    status = 'success'

    try:
        translated_expression = translate_expression(expression)
        result = eval(translated_expression, {}, ALLOWED_FUNCTIONS)
    except Exception as e:
        status = 'error'
        logging.error(f"Error evaluating expression: {e}")
        
        if isinstance(e, (NameError, ValueError, KeyError, ZeroDivisionError, SyntaxError, TypeError)):
            error_type = type(e).__name__
        else:
            error_type = 'Unknown Error'

    return result, error_type, status

def translate_expression(expression):
    return expression.replace('^', '**')

def save_history(history):
    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file)

def load_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error loading history: {e}")
        return []
        
def history_json_to_html(history):
    html = ""
    for item in history:
        html += f"<p>{item['expression']} = <span style='color:green;'>{item['result']}</span></p>"
    return html

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
    app.run(port=DEFAULT_PORT)

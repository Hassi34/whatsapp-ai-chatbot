
from typing import Union
from dotenv import load_dotenv
from flask import Flask, request
from wsgiref import simple_server
from flask_cors import CORS, cross_origin
import openai
import os

from twilio.twiml.messaging_response import MessagingResponse
from src.operations import get_conv_agent
from src.utils.common import read_yaml
import os

load_dotenv()
#openai_api_key = os.getenv('OPENAI_API_KEY')
#openai.api_key = os.environ.get("OPENAI_API_KEY")

config = read_yaml('src/config.yaml')

APP_HOST = config['serving']['APP_HOST']
APP_PORT = config['serving']['APP_PORT']

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

def generate_answer(question : str):
    conv_agent = get_conv_agent()
    llm_response = conv_agent(question)

    if 'output' in llm_response:
        output = llm_response['output']
    elif 'action_input' in llm_response:
        output = llm_response['action_input']
    else: 
        output = llm_response    
    return output

# Define a route to handle incoming requests
@app.route('/chatgpt_webhook', methods=['POST'])
@cross_origin()
def chatgpt():
    incoming_que = request.values.get('Body', '')
    print("Question: ", incoming_que)
    answer = generate_answer(incoming_que)
    print("BOT Answer: ", answer)
    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    msg.body(answer)
    return str(bot_resp)


# Run the Flask app
if __name__ == '__main__':
    httpd = simple_server.make_server(
        host=APP_HOST,
        port=APP_PORT,
        app= app
        )
    httpd.serve_forever()
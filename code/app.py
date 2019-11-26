from flask import Flask, request, jsonify
import chatbot

app = Flask(__name__)
bot = chatbot.chatbot()

@app.route("/chatbot/question", methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        entrada = request.args.get('input')
        print(entrada)
        resposta = bot.get_response(chatbot.pre_process_spacy(entrada)).text
        print(resposta)
        return jsonify(isError=False,
                       message="Success",
                       statusCode=200,
                       output=resposta,
                       input=entrada
                       ), 200


if __name__ == '__main__':
    app.run(debug=True)
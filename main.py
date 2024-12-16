from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Récupérer la clé API OpenAI depuis les Secrets de Replit
openai.api_key = os.environ['OPENAI_API_KEY']

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        answer = response['choices'][0]['message']['content']
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

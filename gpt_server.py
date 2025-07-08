# gpt_server.py
from flask import Flask, request, jsonify
import g4f  # GPT4Free

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')

    try:
        response = g4f.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": message}]
        )
        return jsonify({"reply": response})
    except Exception as e:
        return jsonify({"reply": f"エラー: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # ポート番号はRenderで自動割当される

from flask import Flask, request, jsonify
import predict
import mails

app = Flask(__name__)

@app.route('/urls', methods=['POST'])
def urls():
    urls = request.json['urls']
    return predict.prediction(urls)

@app.route('/mailer', methods=['POST'])
def mailer():
    data = request.json
    links = data.get('links', [])
    websites = data.get('websites', [])
    result = mails.mailer(links, websites)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary_sentences = summarizer(parser.document, 5)

    summary = ""
    for sentence in summary_sentences:
        if summary == "":
            summary = str(sentence)
        else:
            summary = summary + " " + str(sentence)

    return jsonify({'summary': summary})

if __name__ == '__main__':
    # IMPORTANT: listen on all network interfaces
    app.run(host='0.0.0.0', port=5000)

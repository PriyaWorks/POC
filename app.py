from flask import Flask, request, render_template, jsonify
app = Flask(__name__)
import spacy
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dataconvert')
def dataconvert():
    inputText = request.args.get('inputText')
    textTokenize = []
    textLemma = []
    textPOS = []
    textDep = []
    textShape = []
    textStop = []
    doc = nlp(inputText)
    for token in doc:
        textTokenize.append(token.text)
        textLemma.append(token.lemma_)
        textPOS.append(token.pos_)
        textDep.append(token.dep_)
        textShape.append(token.shape_)
        textStop.append(token.is_stop)
    textOutput= textTokenize
    lemmaOutput= textLemma
    posOutput= textPOS
    depOutput= textDep
    shapeOutput= textShape
    stopOutput= textStop
    return render_template('index.html', textOutput=textOutput, lemmaOutput=lemmaOutput, posOutput=posOutput, depOutput=depOutput, shapeOutput=shapeOutput, stopOutput=stopOutput )
    

if __name__ == '__main__':
    app.run(debug=True)

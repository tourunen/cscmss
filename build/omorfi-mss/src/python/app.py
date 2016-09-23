from flask import Flask, request
from flask import Response

from omorfi.omorfi import Omorfi

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/api/v1/lemmatise', methods=['POST'])
def lemmatise():
    def stream(text):
        om = Omorfi()
        om.load_from_dir('/usr/local/share/omorfi/', lemmatise=True)
        for token in om.tokenise(text):
            yield " ".join(map(lambda x: str(x), om.lemmatise(token[0])))

    return Response(stream(request.form['text']), mimetype='text/plain')


@app.route('/api/v1/analyse', methods=['POST'])
def analyze():
    def stream(text):
        om = Omorfi()
        om.load_from_dir('/usr/local/share/omorfi/', analyse=True)
        for token in om.tokenise(text):
            yield "%s\n" % token[0]
            for analyse_res in om.analyse(token):
                text, weight = analyse_res[:2]
                if len(analyse_res)>2:
                    rest = " ".join([str(x) for x in analyse_res[2:]])
                else:
                    rest=''

                yield "%s %s %s\n" % (text, weight, rest)

            yield "\n"

    return Response(stream(request.values['text']), mimetype='text/plain')

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0')

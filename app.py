#!/usr/bin/env python3
'''
import flask
app = flask.Flask(__name__)
app.run(debug=True)
'''


#configurando rotas
import flask

app = flask.Flask(__name__)

dados = {
    'acesso' : 'ok'
}
@app.route('/')
def index():
    return flask.jsonify(dados)

@app.route('/teste/<string:nome>',methods=['POST','GET'])
def teste(nome):
    return f 'teste retornando Rafael {nome}'
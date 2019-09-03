from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api')
def mi_microservicio():
    print(request)
    print(request.environ)
    respuesta =  jsonify({'Hola':'Mundo'})
    print(respuesta)
    print(respuesta.data)
    return respuesta

@app.route('/api/persona/<persona_id>')
def person(persona_id):
    response = jsonify({'Hello': persona_id})
    return response

if __name__ == '__main__':
    print(app.url_map)
    app.run()

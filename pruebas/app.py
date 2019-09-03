from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def mi_microservicio():
    return jsonify({'Hola':'Mundo'})

if __name__ == '__main__':
    app.run()

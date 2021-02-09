from flask import Flask, jsonify
from animals import animals

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message": 'pong'})

@app.route('/animals', methods=['GET'])
def getAnimals():
    return jsonify(animals)

@app.route('/animals/<id>', methods=['GET'])
def getAnimal(id):
    animal = list(filter(lambda a: a['id'] == id, animals))
    if len(animal) > 0:
        return jsonify(animal[0])
    return jsonify({"message": "Animal not found"})



if __name__ == "__main__":
    app.run(debug=True, port=8000)
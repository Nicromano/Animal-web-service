from flask import Flask, jsonify, request
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

@app.route('/animals/<id>', methods=['PUT'])
def updateAnimal(id):
    animal = list(filter(lambda a: a['id'] == id, animals))
    if len(animal) > 0: 
        animal[0]['id'] = request.json['id']
        animal[0]['animal_name'] = request.json['animal_name']
        animal[0]['scientific_name'] = request.json['scientific_name']
        animal[0]['gender'] = request.json['gender']
        animal[0]['age'] = request.json['age']
        


@app.route('/animals', methods=['POST'])
def addAnimal():
    received_animal = request.json
    new_animal = {
        "id": received_animal['id'],
        "animal_name": received_animal['animal_name'],
        "scientific_name": received_animal['scientific_name'],
        "gender": received_animal['gender'],
        "age": received_animal['age']
    }
    animals.append(new_animal)
    return jsonify({"message": "Animal added succesfull", "animals": animals})


if __name__ == "__main__":
    app.run(debug=True, port=8000)

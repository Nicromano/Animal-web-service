from flask import Flask, jsonify, request
from animals import animals

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"message": 'pong'})

#Ruta animals usando metodo GET
@app.route('/animals', methods=['GET'])
def getAnimals(): #se llama cuando se solicita la ruta
    return jsonify(animals) #jsonify devuelve un tipo JSON de los animales


#Ruta de un animal buscado mediante id, metodo GET
@app.route('/animals/<id>', methods=['GET'])
def getAnimal(id):
    #Se filtra entre el arreglo para encontrar el animal 
    animal = list(filter(lambda a: a['id'] == id, animals))
    #validamos si existe un animal, para evitar errores
    if len(animal) > 0: 
        return jsonify(animal[0]) #retorna el JSON con el animal
    #Envia un mensaje de error en formato JSON
    return jsonify({"message": "Animal not found"})

#Ruta para actualizar un animal con ID especifico mediante metodo PUT
@app.route('/animals/<id>', methods=['PUT'])
def updateAnimal(id):
    #Se busca el animal entre el arreglo de animales
    animal = [animal for animal in animals if animal['id'] == id ]
    #Se valida que se haya encontrado el animal
    if len(animal) > 0: 
        #Se actualiza los campos de los animales
        animal[0]['id'] = request.json['id']
        animal[0]['animal_name'] = request.json['animal_name']
        animal[0]['scientific_name'] = request.json['scientific_name']
        animal[0]['gender'] = request.json['gender']
        animal[0]['age'] = request.json['age']
        #retorna un JSON con un mensaje de actualización
        return jsonify({
            "message": "Animal updated", 
            "animal": animal[0]
        })
    #Envia un mensaje de error en formato JSON
    return jsonify({
        "message": "Animal not found"
    })

@app.route('/animals/<id>', methods=['DELETE'])
def deleteAnimal(id):
    animal = [animal for animal in animals if animal['id'] == id]
    if len(animal) > 0:
        animals.remove(animal[0])
        return jsonify({
            "message": "Animal deleted",
            "animal": animals
        })
    return jsonify({
        "message": "Animal not found"
    })

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

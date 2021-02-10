# Servicio web de Animales
Este servicio web programado en el lenguaje Python utiliza como base un paquete denominado Flask. Dicho paquete se instala mediante el comando pip de la siguiente manera :

~~~

pip install flask

~~~

A continuación se procede a ejecutar el archivo app.py para lanzar el servicio en modo desarrollo. 


~~~

python app.py

~~~

Las rutas existentes en dicho servicio se basa en una base de datos simulada por un objeto almacenada en el archivo animals.py. De esta forma se tiene

- ***/animals*** : Método GET, utilizado para devolver todos los animales existentes
- ***/animals***: Método POST, utilizado para agregar un nuevo animal a la lista de animales
- ***/animals/\<id\>***: Método GET, utilizado para devolver un animal especificando el ID por medio del URL
- ***/animals/\<id\>***: Método PUT, utilizado para actualizar un animal existente mediante el ID enviado por medio del URL
- ***/animals/\<id\>***: Método DELETE, utilizado para eliminar un animal existente mendiante el ID enviado por medio del URL
    
    
# Inyección de dependencias

Para incluir la inyección de dependencias lo que hemos hecho ha sido una clase para trabajar con la base de datos. Esta clase es `mondo_db.py`.
Contiene metodos para acceder a las funciones básicas de los dos microservicios.

Por otro lado tenemos separada la lógica de negocio, para el primer microservicio será `Students.py` y para el segundo microservicio será `Exams.py`. En estas dos clases lo que realizamos inyecciones al objecto de la clase de `mongo_db.py` en este caso mediante un objecto de la clase MongoDataBase, donde incluiremos la variable de entorno **DB_BD** la cúal nos da la información de si queremos usar la base de datos en local o en remoto. El nombre de la base de datos, el nombre de la colección de datos que vamos a usar, y por último los datos que vamos a tratar como datos iniciales. 

De esta forma conseguimos que las clases usen el objeto de forma abstrata. Los microservicios (API REST) solo hacen llamadas a los metodos que hay en las clases de su lógica de negocio, quedando de esta forma completamente separada la funcionalidad en capas.

![Inyeccion1](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/i1.png)
![Inyeccion2](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/i2.png)
![Inyeccion3](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/i3.png)

# Arquitectura por capas

Hemos decidido implementar uno de los microservicios descritos, en este caso el de **Gestión de Alumnos**
Tenemos una arquitectura por capas, ya que la hemos definido de esta forma:
- **Capa inferior**: donde tenemos la clase **Students.py** con su correspondiente test unitario **test_students.py** 
- **Capa superior**: donde tenemos la API REST del microservicio de gestión de alumnos en el fichero **students-rest.py** con su test de cobertura **test_students_rest.py**
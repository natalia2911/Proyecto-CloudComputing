## Calendario personalizado para los alumnos de la ETSIIT

Nuestro proyecto será capaz de proporcionar a los alumnos información mediante un calendario personalizado tanto de clases como de exámenes, debido al paso de mensajes que se genere desde los diferentes microservicios hasta la interfaz de usuario.

Nuestra intención es que el microservicio encargado de la gestión de exámenes pueda acceder a su base de datos en el que podrá hacer consultas sobre la lista de exámenes que aparecen asociadas a las diferentes asignaturas de los determinados cursos.
Por otro lado el segundo microservicio, el encargado de la gestión de los alumnos será capaz de acceder a la segunda base de datos en la cual aparecerá descrito los diferentes alumnos, asociadas a las asignaturas que tengan matriculadas.

Destacamos que el microservicio de gestión de exámenes y el microservicio de gestión de alumnos podrán comunicarse entre sí, aunque se encuentren como microservicios completamente separados.

Por otro lado encontramos un tercer microservicio en el cual se encargará de enviar mensajes, y se podrá comunicar con el microservicio de gestión de alumnos.

Este proyecto surge como solución al problema que a muchos alumnos se les presenta durante el grado o postgrado, que es que tienen asignaturas de otros cursos y diferentes clases con diferentes profesores, y realizar un horario claro y conciso puede resultar una tarea algo tediosa.

Por otro lado puede haber conflictos del tipo: que dos clases pueden coincidir o algo mas grave aun, que dos exámenes puedan coincidir.

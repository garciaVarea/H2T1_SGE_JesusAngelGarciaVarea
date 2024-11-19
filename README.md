# H2T1_SGE_JesusAngelGarciaVarea
Este proyecto es una aplicación CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar encuestas utilizando Python y una base de datos MySQL. La interfaz gráfica está desarrollada con Tkinter y se incluyen gráficos generados con Matplotlib.

## Instalación y Preparación del Proyecto
Descargar y ejecutar MySQL installer.  
https://dev.mysql.com/downloads/installer/  
Este proyecto se ha llevado a cabo con PyCharm y las instrucciones son contando con que estas utilizando PyCharm, si no tienes PyCharm descárgalo del siguiente enlace e instálalo:  
https://www.jetbrains.com/pycharm/download/?section=windows
Si no tienes licencia para utilizar la versión profesional puedes descargar la versión community, justo debajo de la profesional.

### *Configurar la Base de Datos*

Ejecuta el archivo SQL adjunto en el proyecto.  
Primero, crea la base de datos y la tabla.  
Después, inserta los datos iniciales en la tabla.  

*Instalar Python 3.11*
Descarga e instala Python 3.11.9.  
https://www.python.org/downloads/release/python-3119/  

### *Clonar el Repositorio*

En tu entorno de desarrollo, selecciona la opción *Get from VCS*.  
Ingresa la URL del repositorio: https://github.com/garciaVarea/H2T1_SGE_JesusAngelGarciaVarea.git.  
Elige el directorio donde deseas clonar el proyecto.  

### *Configurar el Intérprete de Python*

Ve a Opciones > Proyecto > Python Interpreter.  
Selecciona Add Interpreter > New Interpreter.  
Busca el ejecutable de Python 3.11 y agrégalo como intérprete.  

### *Instalar Dependencias*

Instala mysql-connector-python versión 9.0.0 (IMPORTANTE: no instales la versión 9.1.0 ya que no es compatible).  
Instala matplotlib (versión por defecto).  
Instala pandas (versión por defecto).
Instala Openpxl (versión por defecto).

### *Configurar Parámetros de Conexión a la Base de Datos*

Abre el archivo EncuestaModel.py.  
En el método conectar(), modifica los parámetros de la base de datos para que coincidan con tu configuración de MySQL.  
(Lo más probable es que la contraseña de la configuración esté vacía porque en mi equipo no tengo contraseña, en los equipos de campus se usa curso como contraseña)

### *Ejecutar el Proyecto*

Haz clic derecho en main.py y selecciona Run.

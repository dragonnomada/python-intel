#
# Autor: Roberto Enrique Barron Leon
#Mail Contac: roberto.barron.leon@intel.com
#Codigo echo para el curso Python Intel Caneti como proyecto final

#Justificacion: Es muy frecuente que en las empresas de software varios programadores realizen modificaciones en paralelo en distintos archivos de codigo dentro de un mismo proyecto de software.
#Actualmente herramientas automatizadas se encargan de juntar ese codigo, compilarlo, ejecutarlo y realizar de pruebas automatizadas. Esto permite acelerar el proceso de desarrollo sin que un solo individuo
#absorba la responsabilidad de juntar (integrar) todos los cambios realizados diariamente.
#Sin embargo, ante la falta del criterio humano, es posible que se presenten problemas al incorporar los cambios sin una inspeccion a conciencia por un humano. Como resultado, se pueden presentar problemas de
#compatibilidad entre diversos codigos o a que los cambios introducidos presenten alteraciones no esperadas o deseadas en el comportamiento del producto. Posteriormente al enfrentar alguna de estas problematicas
#los desarrolladores deben invertir tiempo para identificar y corregir el error, lo que se traduce en retrazos en el desarrollo y costo inesperados durante el desarrollo.
#Por ende, el poder identificar el tipo de error y el autor que le ha introducido en el sistema se vuelve crucial, a fin de poder corregir el error y estabilizar la funcionalidad de codigo a la brevedad para
#restablecer el ciclo de desarrollo para todos los involucrados, esto se acentua conforme el numero de usuarios incrementa y las responsabilidades de desarrollo se segmentan en distintos grupos cuya impacto
# no es transparente para todos los involucrados.
#Los errores posibles se consideran de 2 tipos:
#       1) errores de compilacion (que no permiten generar el codigo)
#       2) errores durante las pruebas de automatizacion ( el software se estimula mediante valores de entrada conocidos y se comparan frente a valores conocidos de salida. Ambos almacenados en archivos de texto)
#Los resultados de las pruebas (Compilacion exitosa o Fallo) se guardan en archivos de texto (logs) guardados periodicamente en archivos.zip. junto a una lista de los archivos que fueron modificados
#Los desarrolladores pueden revizar los resultados despues de cada integracion periodica y verificar que todo este en orden o si algun codigo debe ser arreglado o removido (error de compilacion)
#asi como si algun codigo se ejecuta correctamente, pero los resultados funcionales no son los esperados (Error funcional detectado durante las pruebas de automatizacion)

# Codigo implementado:
#El presente codigo es una version inicial de un programa automatizado para analizar los resultados de compilacion y de las pruebas automatizadas de un proyecto de software realizado en mi empresa.
#El archivo de python se encarga descomprimir los logs incluidos en un archivo .zip colocado en la misma carpeta donde fue ejecutado.
#El codigo lee cada uno de los archivos y verifica su contenido para revizar si existe un mensaje de error en alguno de los logs. Los logs se reportan por un mensaje similar al siguiente formato:
#
#            ERROR:(ID).    (String: Un texto explicativo del tipo de error)
#            ERROR:123.     Compilation Unsuccessfull. Error on file-->> example.c
#            ERROR:234.     Automated Test Failure. Failed on SED#3. Expected value: 4. Obtained Value: 3
#
#Si un error es detectado, El script obtiene los datos de contactos de los desarrolladores desde un log obtenido desde git mediante el comando "git log" y genera un reporte HTML que muestre los resultados
#  de las pruebas, los errores detectados y los desarrolladores involucrados (en base a la fecha o numeros de commits)
# #
# Nota: El envio de correo electronico a los usuarios no esta considerado en el alcance de este proyecto, solo la lectura de archivos, la compresion y
# la generacion de contenido HTML mediante el uso de python.

#Modulos desarrollados:
#Log Generator: es el archivo principal que manda ejecutar los otros modulos
#Reporter Generaror: Se encarga de leer los archivos de gitlog.txt para obtener la informacion de los desarrolladores en un diccionario, los archivos contenidos en logs.zip y genera un archivo HTML
#LinuxComander: Herramienta que usa subprocess para hacer el manejo de archivos y carpetas en Linux necesarios durante el proceso.


#Como Ejecutar
#Se manda ejecutar MainGenerator.py desde consola (correr en Linux)
#Los archicvos de Log.zip, son descomprimidos y leidos por el escript en busca de errores. Los resultados se muestran en la
#carpeta LogReport creada por el script. Abra Main.HTML para ver los resultados

import ReporterGenerator

Reporte1= ReporterGenerator.Reporte()

#Leemos Descomprimimos los archivos Logs y los leemos uno por uno para buscar errores reportados
Reporte1.parseLogs()

#Obtenemos los datos de los usuarios que participaron en la ultima integracion en caso de requerir reportar algun error
#Se utiliza un reporte en base al ultimo dia en el LOG
Reporte1.getGitLogInfo(".\\Inputs\\gitLog.txt")

#Creamos un archivo HTML para mostrar los resultados del reporte
Reporte1.createHTMLReport()





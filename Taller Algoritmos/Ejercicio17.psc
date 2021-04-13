Proceso Inicio_Ejercicio17
	Escribir "En que tiempo el vehiculo 2 alcanza al otro"
	Escribir "Ingrese distancia entre los dos vehiculos (Km)"
	Leer dist
	Escribir "Ingrese velocidad vehiculo 1 (Km/h)"
	Leer v1
	Escribir"Ingrese velocidad vehiculo 2 (Km/h)"
	Leer v2
	difvel<-(v2-v1)
	tiempoh<-(dist/difvel)
	tiempomin<-(tiempoh*60)
	Escribir "El vehiculo 2 alcanzara al vehiculo 1 en: ",tiempomin," minutos"
FinProceso
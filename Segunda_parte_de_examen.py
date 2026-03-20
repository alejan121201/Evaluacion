# Segunda parte del examen, lo facil 
from datetime import datetime

# Todas las variables 
capacidad_maxima = 300
contador_personas = 0
lista_asistentes = []

# NUEVA FUNCIÓN: obtener fecha y hora automáticamente
def obtener_fecha_hora():
    ahora = datetime.now()
    fecha = ahora.strftime("%d/%m/%Y")
    hora = ahora.strftime("%H:%M:%S")
    return fecha, hora

def mostrar_estado():
    global contador_personas
    
    if contador_personas < 250:
        estado_evento = "Evento disponible"
    elif 250 <= contador_personas < 300:
        estado_evento = "Últimos cupos disponibles"
    else:
        estado_evento = "El evento está lleno"
    
    print("\nEstado del evento:", estado_evento)
    print("Personas registradas:", contador_personas)

def registrar_asistente():
    global contador_personas
    
    if contador_personas >= capacidad_maxima:
        print("\nEl evento está lleno. No se permiten más registros.")
        return
    
    nombre = input("Ingrese el nombre del asistente: ")
    
    try:
        documento = int(input("Ingrese el número de documento: "))
    except:
        print("Documento inválido.")
        return
    
    # USAR FECHA Y HORA AUTOMÁTICAS
    fecha, hora = obtener_fecha_hora()
    
    asistente = {
        "Nombre": nombre,
        "Documento": documento,
        "Fecha": fecha,
        "Hora": hora
    }
    
    lista_asistentes.append(asistente)
    contador_personas += 1
    
    print("\nRegistro exitoso.")
    print("Fecha de ingreso:", fecha)
    print("Hora de ingreso:", hora)

    mostrar_estado()

def mostrar_asistentes():
    if len(lista_asistentes) == 0:
        print("\nNo hay asistentes registrados.")
    else:
        print("\n===== LISTA DE ASISTENTES =====")
        for i, asistente in enumerate(lista_asistentes, start=1):
            print(f"\nAsistente {i}")
            print("Nombre:", asistente["Nombre"])
            print("Documento:", asistente["Documento"])
            print("Fecha:", asistente["Fecha"])
            print("Hora:", asistente["Hora"])

# Menú principal
while True:
    
    print("\n===== SISTEMA DE CONTROL DE EVENTO =====")
    print("1. Registrar asistente")
    print("2. Ver lista de asistentes")
    print("3. Ver estado del evento")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_asistente()
        
    elif opcion == "2":
        mostrar_asistentes()
        
    elif opcion == "3":
        mostrar_estado()
        
    elif opcion == "4":
        print("\nSaliendo del sistema...")
        break
        
    else:
        print("Opción no válida.")
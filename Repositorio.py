#Importamos la funcion ramdom para nuestro juego
import random
#Importamos la funcion os para limpiar nuestra consola a la hora de elgir las opciones
import os

# Definir una lista para almacenar usuarios registrados para utilizarla como base de "datos local"
usuarios = []

# Definir la función mostrar_menu()
def mostrar_menu():
    """
    Esta función muestra el menú principal en la consola.
    """
    print("\n ----- MENÚ ----- ")
    print("1. Juego     💿 ")
    print("2. Tarjeta   💳 ")
    print("3. Salir      ↩")
    

# Definir la función registrar_usuario()
def registrar_usuario():
    """
    Esta función permite al usuario registrar un nuevo nombre de usuario y contraseña.
    Los datos del usuario se almacenan en la lista usuarios.
    """
    nombre = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    usuarios.append({"nombre": nombre, "contrasena": contrasena})
    print("Registro exitoso. Puede iniciar sesión ahora.")

# Definir la función iniciar_sesion()
def iniciar_sesion():
    """
    Esta función permite al usuario iniciar sesión y verifica si las credenciales son correctas.
    """
    nombre = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    for usuario in usuarios:
        if usuario["nombre"] == nombre and usuario["contrasena"] == contrasena:
            print(f"Bienvenido, {nombre}!")
            return True
    print("Nombre de usuario o contraseña incorrectos.")
    return False

opcion = 0
usuario_autenticado = False

# Inicia un bucle principal que muestra el menú principal y gestiona las opciones
while opcion != 3:
    # Si el usuario no está autenticado, muestra el menú de inicio de sesión/registro
    if not usuario_autenticado:
        print("\n ----- INICIO DE SESIÓN ----- ")
        print("1. Registrarse           🆔")
        print("2. Iniciar sesión        🚹")
        print("3. Salir                 ↩")
        seleccion = int(input("Seleccione una opción: "))

        if seleccion == 1:
            registrar_usuario()
        elif seleccion == 2:
            usuario_autenticado = iniciar_sesion()
        elif seleccion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
    else:
        # Si el usuario está autenticado, muestra el menú principal con opciones adicionales
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("\n - Juego de Puntaje y Vidas")

            vidas = 5
            puntos = 0

            while vidas != 0:
                num = random.randint(0, 9)

                if num == 0:
                    vidas -= 1
                    print(f"Te quedan {vidas} vidas")
                else:
                    puntos += 1
                    print(f"Has ganado {puntos} puntos")

        elif opcion == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n - Tarjeta de crédito")

            cupo_total = 500

            nombre = input("\n Ingrese su nombre: ")
            compra = int(input("\n Ingrese el valor de la compra: "))
            cuotas = int(input("\n Ingrese número de cuotas: "))

            if compra <= cupo_total:
                deuda = compra
                separacion = compra / cuotas
                total_pagos = 0  # Inicializa el total de pagos a 0
                print(f"\n Detalle de pagos de {nombre}")
                i = 1

                while deuda > 1 and i <= cuotas:
                    if deuda - separacion < 0:
                        cuota_actual = deuda
                        total_pagos += cuota_actual  # Suma la cuota al total de pagos
                        deuda -= cuota_actual
                    else:
                        cuota_actual = separacion
                        total_pagos += cuota_actual  # Suma la cuota al total de pagos
                        deuda -= cuota_actual

                    print(f"\n Cuota {i}: ${cuota_actual:.2f} - Deuda restante: ${deuda:.2f} - Total de pagos: ${total_pagos:.2f} \n")

                    i += 1 

            else:
                print("\n No se puede hacer la compra")

        elif opcion == 3:
             respuesta = input("¿Estás seguro que deseas salir? (s/n): ")
             
             if respuesta.lower() == "s":
                print("Saliendo del programa.")
                break
             else: respuesta.lower() == "n"
             print("Registrate de nuevo ❤")
             registrar_usuario()
        

            
            
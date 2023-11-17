import random
import string
from prettytable import PrettyTable
from colorama import init, Fore, Style
class Cliente:
    def __init__(self, nombre, apellidos, nacionalidad, correo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nacionalidad = nacionalidad
        self.correo = correo
        self.lista_deseos = []

    def ingresar_info_tarjeta(self):
        while True:
            numero_tarjeta = input("Ingrese el número de la tarjeta de crédito: ")
            if len(numero_tarjeta) == 16:
                break
            else:
                imprimir_texto_coloreado("El número de tarjeta debe tener 16 dígitos. Por favor, inténtelo de nuevo.",Fore.RED)


        while True:
            fecha_vencimiento = input("Ingrese la fecha de vencimiento de la tarjeta (MM/AA): ")
            if len(fecha_vencimiento) == 5 and fecha_vencimiento[2] == '/' and fecha_vencimiento[:2].isdigit() and fecha_vencimiento[3:].isdigit():
                break
            else:
                imprimir_texto_coloreado("El formato de la fecha de vencimiento debe ser MM/AA. Por favor, inténtelo de nuevo.",Fore.RED)

        while True:
            codigo_seguridad = input("Ingrese el código de seguridad de la tarjeta: ")
            if codigo_seguridad.isdigit() and len(codigo_seguridad) <= 3:
                break
            else:
                imprimir_texto_coloreado("El código de seguridad debe tener un máximo de 3 caracteres numéricos. Inténtelo de nuevo.",Fore.RED)

        self.tarjeta_credito = {'numero': numero_tarjeta, 'vencimiento': fecha_vencimiento, 'codigo': codigo_seguridad}
    def ingresar_direccion(self):
        while True:
            direccion = input("Ingrese aquí su dirección: ")
            if direccion:
                break
            else:
                imprimir_texto_coloreado("Por favor, ingrese una dirección válida.",Fore.RED)
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
def mostrar_productos(productos):
    print("Lista de productos disponibles:")
    tabla_productos = PrettyTable()
    tabla_productos.field_names = ["ID", "Nombre", "Precio", "Stock"]
    tabla_productos.header_style = 'upper'

    for i, (nombre, producto) in enumerate(productos.items(), start=1):
        tabla_productos.add_row([i, nombre, f"{producto.precio}€", producto.stock])

    print(tabla_productos)
def generar_factura(cliente, productos_seleccionados, tasa_iva):
    subtotal = sum([producto[0].precio * producto[1] for producto in productos_seleccionados.values()])
    iva = subtotal * (tasa_iva / 100)
    total_factura = subtotal + iva

    print("\nFactura:")
    print(f"Cliente: {cliente.nombre}")
    print(f"Correo: {cliente.correo}")
    print("\nProductos:")
    for nombre, (producto,cantidad) in productos_seleccionados.items():
        print(f"{nombre}: {producto.precio}€")
        print(f"Stock restante de {nombre}: {producto.stock}")
    print(f"\nSubtotal: {subtotal:.2f}€")
    print(f"IVA ({tasa_iva}€): {iva:.2f}€")
    print(f"Total: {total_factura:.2f}€")
def enviar_mensaje(cliente, codigo_seguimiento, via_sms):
    if via_sms:
        mensaje = f"Su pedido ha sido enviado . Código de seguimiento: {codigo_seguimiento}"
        enviar_sms(mensaje)
    else:
        mensaje = f"Gracias por su compra. En el adjunto encontrara la factura y el código de seguimiento: {codigo_seguimiento}"
        enviar_correo(cliente.correo, "Factura del Pedido", mensaje)
def enviar_sms(mensaje):
    print(f"Enviando SMS : {mensaje}")
def enviar_correo(correo, asunto, mensaje):
    print(f"Enviando correo a {correo} (Asunto: {asunto}): {mensaje}")
def generar_codigo_seguimiento():
    longitud_codigo = 5
    caracteres_permitidos = string.ascii_uppercase + string.digits
    codigo_seguimiento = ''.join(random.choice(caracteres_permitidos) for _ in range(longitud_codigo))
    return codigo_seguimiento
def imprimir_texto_coloreado(texto, color):
    print(color + texto + Style.RESET_ALL)
def tarea():
    init()
    imprimir_texto_coloreado('Bienvenidos a la Página Web',Fore.CYAN)
    productos_disponibles = {
        "Zapatos": Producto("Zapatos", 25.0, 15),
        "Zapatillas": Producto("Zapatillas", 55.0, 25),
        "Camisetas": Producto("Camisetas", 30.0, 40),
        "Camisas": Producto("Camisas", 18.0, 10),
        "Abrigo": Producto("Abrigo", 95.0, 5),
        "Sudadera": Producto("Sudadera", 50.0, 12),

    }

    while True:
        nombre = input("Ingrese su Nombre: ")
        if nombre:
            break
        else:
            imprimir_texto_coloreado("Por favor, ingrese un nombre válido.",Fore.RED)

    while True:
        apellidos = input("Ingrese sus Apellidos: ")
        if apellidos:
            break
        else:
            imprimir_texto_coloreado("Por favor, ingrese apellidos válidos.", Fore.RED)

    while True:
        tabla_nacionalidades = PrettyTable()
        tabla_nacionalidades.field_names = ["ID", "Nacionalidad"]
        tabla_nacionalidades.header_style = 'upper'

        for i, nacionalidad in enumerate(['Español', 'Frances', 'Italiano', 'Aleman', 'Britanico'], start=1):
            tabla_nacionalidades.add_row([i, nacionalidad])

        print("Lista de nacionalidades:")
        print(tabla_nacionalidades)

        seleccion_nacionalidad = input("Ingrese el número de su nacionalidad: ")
        if seleccion_nacionalidad.isdigit() and 1 <= int(seleccion_nacionalidad) <= 5:
            nacionalidad = ['español', 'frances', 'italiano', 'aleman', 'britanico'][int(seleccion_nacionalidad) - 1]
            print(f"Has seleccionado {nacionalidad}")
            break
        else:
            imprimir_texto_coloreado("Por favor, ingrese un número válido de nacionalidad.",Fore.RED)

    correo = input("Ingrese su correo electrónico: ")
    while "@" not in correo:
        imprimir_texto_coloreado("La dirección de correo electrónico debe contener el símbolo '@'. Inténtelo de nuevo.",Fore.RED)
        correo = input("Ingrese su correo electrónico: ")


    cliente = Cliente(nombre, apellidos, nacionalidad, correo)

    if cliente.nacionalidad in {'español', 'frances', 'italiano', 'aleman', 'britanico'}:
        tasas_iva = {'español': 21.0, 'frances': 20.0, 'italiano': 22.0, 'aleman': 19.0, 'britanico': 20.0}
        tasa_iva = tasas_iva[cliente.nacionalidad]
    else:
        tasa_iva = float(input("Ingrese la tasa de IVA aplicable en su país: "))

    productos_seleccionados = {}

    while True:
        mostrar_productos(productos_disponibles)
        nombre_producto = input("Ingrese el nombre del producto (o 'pagar' para ir a pagar): ")
        if nombre_producto.lower() == 'pagar':
            if not productos_seleccionados:
                imprimir_texto_coloreado("Debe seleccionar al menos un producto para proceder con el pago.",Fore.RED)
                continue
            else:
                break
        elif nombre_producto.isdigit() and 1 <= int(nombre_producto) <= len(productos_disponibles):
            nombre_producto = list(productos_disponibles.keys())[int(nombre_producto) - 1]
            producto = productos_disponibles[nombre_producto]
            cantidad = int(input(f"Ingrese la cantidad deseada de '{nombre_producto}' (disponibles: {producto.stock}): "))

            if 0 < cantidad <= producto.stock:
                productos_seleccionados[nombre_producto] = (producto, cantidad)
                producto.stock -= cantidad
                print(f"{cantidad} unidades de '{nombre_producto}' agregadas al carrito. Stock restante: {producto.stock}")
            else:
                print(f"La cantidad ingresada no es válida. Por favor, elija una cantidad entre 1 y {producto.stock}.")
        else:
            imprimir_texto_coloreado("Ingrese un número válido de producto.",Fore.RED)

    print("\nLista de deseos de", cliente.nombre)
    for nombre, (producto,cantidad) in productos_seleccionados.items():
        total=producto.precio*cantidad
        print(f"{nombre}: {producto.precio}€ x {cantidad} unidades ={total} €")

    cliente.ingresar_direccion()
    cliente.ingresar_info_tarjeta()

    generar_factura(cliente, productos_seleccionados, tasa_iva)

    codigo_seguimiento = generar_codigo_seguimiento()


    eleccion = input("¿Cómo desea recibir el código de seguimiento de su pedido? Ingrese 'SMS' o 'correo': ").lower()

    via_sms = False

    if eleccion == 'sms':
        via_sms = True
        while True:
            telefono = input("Ingrese su número de teléfono para recibir el código por SMS (9 dígitos): ")
            if telefono.isdigit() and len(telefono) == 9:
                break
            else:
                imprimir_texto_coloreado("El número de teléfono debe tener exactamente 9 dígitos. Inténtelo de nuevo.",Fore.RED)
    elif eleccion != 'correo':
        imprimir_texto_coloreado("Opción no válida. Se enviara por defecto por correo.",Fore.RED)

    enviar_mensaje(cliente, codigo_seguimiento, via_sms)
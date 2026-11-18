"""Prototipo académico: versión refactorizada con funciones pequeñas."""

TARIFAS_ENVIO = {'Bogotá': 10, 'Soacha': 15}


def calcular_subtotal(productos):
    subtotal = 0.0
    for precio, cantidad in productos:
        if precio < 0 or cantidad <= 0:
            raise ValueError('Producto inválido')
        subtotal += precio * cantidad
    return subtotal


def porcentaje_descuento(tipo_cliente, subtotal, cupon):
    tasas = {
        'premium': 0.20 if subtotal >= 200 else 0.10,
        'regular': 0.05 if subtotal >= 200 else 0.0,
    }
    return tasas.get(tipo_cliente, 0.0) + (0.05 if cupon and subtotal >= 100 else 0.0)


def calcular_envio(ciudad, subtotal):
    return 0 if subtotal >= 150 else TARIFAS_ENVIO.get(ciudad, 25)


def calcular_total(productos, tipo_cliente, ciudad, cupon=False):
    if not productos:
        return 0.0
    subtotal = calcular_subtotal(productos)
    descuento = subtotal * porcentaje_descuento(tipo_cliente, subtotal, cupon)
    return round(subtotal - descuento + calcular_envio(ciudad, subtotal), 2)

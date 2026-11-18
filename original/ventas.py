"""Prototipo académico: versión inicial deliberadamente compleja."""

def calcular_total(productos, tipo_cliente, ciudad, cupon=False):
    if not productos:
        return 0.0
    subtotal = 0.0
    for producto in productos:
        precio, cantidad = producto
        if precio < 0 or cantidad <= 0:
            raise ValueError('Producto inválido')
        subtotal += precio * cantidad
    if tipo_cliente == 'premium':
        if subtotal >= 200:
            descuento = subtotal * 0.20
        else:
            descuento = subtotal * 0.10
    elif tipo_cliente == 'regular':
        if subtotal >= 200:
            descuento = subtotal * 0.05
        else:
            descuento = 0
    else:
        descuento = 0
    if cupon:
        if subtotal >= 100:
            descuento += subtotal * 0.05
        else:
            descuento += 0
    if ciudad == 'Bogotá':
        if subtotal >= 150:
            envio = 0
        else:
            envio = 10
    elif ciudad == 'Soacha':
        if subtotal >= 150:
            envio = 0
        else:
            envio = 15
    else:
        if subtotal >= 150:
            envio = 0
        else:
            envio = 25
    return round(subtotal - descuento + envio, 2)

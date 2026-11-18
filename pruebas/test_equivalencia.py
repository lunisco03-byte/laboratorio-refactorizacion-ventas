"""Verifica que ambos módulos devuelvan el mismo resultado en escenarios representativos."""
import importlib.util
from pathlib import Path
import pytest

def cargar(nombre, ruta):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

raiz = Path(__file__).resolve().parents[1]
original = cargar('original_comparacion', raiz / 'original' / 'ventas.py')
final = cargar('final_comparacion', raiz / 'refactorizado' / 'ventas.py')

@pytest.mark.parametrize('productos,cliente,ciudad,cupon', [
    ([], 'regular', 'Bogotá', False),
    ([(50, 2)], 'regular', 'Bogotá', False),
    ([(100, 2)], 'premium', 'Soacha', False),
    ([(50, 2)], 'premium', 'Soacha', True),
    ([(20, 2)], 'premium', 'Cali', True),
    ([(100, 2)], 'regular', 'Cali', True),
    ([(20, 2)], 'regular', 'Soacha', False),
    ([(50, 2)], 'otro', 'Cali', False),
    ([(150, 1)], 'otro', 'Bogotá', False),
    ([(99, 1)], 'regular', 'Bogotá', True),
])
def test_mismo_resultado(productos, cliente, ciudad, cupon):
    assert original.calcular_total(productos, cliente, ciudad, cupon) == final.calcular_total(productos, cliente, ciudad, cupon)

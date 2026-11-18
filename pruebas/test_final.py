import importlib.util
from pathlib import Path
import pytest

ruta = Path(__file__).resolve().parents[1] / 'refactorizado' / 'ventas.py'
spec = importlib.util.spec_from_file_location('ventas_final', ruta)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

@pytest.mark.parametrize('productos,cliente,ciudad,cupon,esperado', [
    ([], 'regular', 'Bogotá', False, 0),
    ([(50, 2)], 'regular', 'Bogotá', False, 110),
    ([(100, 2)], 'premium', 'Soacha', False, 160),
    ([(50, 2)], 'premium', 'Soacha', True, 100),
    ([(20, 2)], 'premium', 'Cali', True, 61),
    ([(100, 2)], 'regular', 'Cali', True, 180),
    ([(20, 2)], 'regular', 'Soacha', False, 55),
    ([(50, 2)], 'otro', 'Cali', False, 125),
    ([(150, 1)], 'otro', 'Bogotá', False, 150),
    ([(99, 1)], 'regular', 'Bogotá', True, 109),
])
def test_casos_funcionales(productos, cliente, ciudad, cupon, esperado):
    assert mod.calcular_total(productos, cliente, ciudad, cupon) == esperado

@pytest.mark.parametrize('producto', [[(-1, 1)], [(5, 0)]])
def test_producto_invalido(producto):
    with pytest.raises(ValueError, match='Producto inválido'):
        mod.calcular_total(producto, 'regular', 'Bogotá')

import importlib.util
from pathlib import Path

ruta = Path(__file__).resolve().parents[1] / 'original' / 'ventas.py'
spec = importlib.util.spec_from_file_location('ventas_inicial', ruta)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_compra_regular_bogota():
    assert mod.calcular_total([(50, 2)], 'regular', 'Bogotá') == 110


def test_compra_premium_grande():
    assert mod.calcular_total([(100, 2)], 'premium', 'Soacha') == 160

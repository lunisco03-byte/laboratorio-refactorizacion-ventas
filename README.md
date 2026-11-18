# Laboratorio de refactorización: módulo de ventas

**Origen:** prototipo académico original creado para este taller, no procede de un repositorio preexistente.

## Requisitos
Python 3.10+; `python -m pip install pytest coverage radon`

## Ejecución de pruebas y cobertura
Desde la raíz del proyecto:

```bash
python -m coverage run --source=original -m pytest -q pruebas/test_inicial.py
python -m coverage report -m
python -m coverage erase
python -m coverage run --source=refactorizado -m pytest -q pruebas/test_final.py
python -m coverage report -m
```

Para obtener una cobertura comparable, ejecutar las pruebas por separado con `coverage run --source=original` y `--source=refactorizado` respectivamente (ver `evidencias/`).

## Complejidad
`radon cc original/ventas.py -s -a` y `radon cc refactorizado/ventas.py -s -a`.

## Repositorio GitHub
Crear un repositorio en tu cuenta, subir los archivos y copiar la URL en el informe. No se ha creado un repositorio remoto automáticamente.

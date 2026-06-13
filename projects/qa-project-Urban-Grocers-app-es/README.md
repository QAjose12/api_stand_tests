# qa-project-Urban-Grocers-app-es

## Descripción

Proyecto de automatización de pruebas para la API de **Urban Grocers**. Se automatizan 9 casos de prueba correspondientes a la lista de comprobación del campo `name` en la solicitud de creación de un kit de productos.

Las pruebas verifican:
- Límites de longitud del campo `name` (0, 1, 511 y 512 caracteres)
- Tipos de caracteres permitidos: especiales, espacios, números
- Ausencia del parámetro `name`
- Tipo de dato incorrecto (número en lugar de cadena)

## Tecnologías

- Python 3
- pytest
- requests

## Estructura de archivos

| Archivo | Descripción |
|---|---|
| `configuration.py` | URL del servidor y rutas de la API |
| `data.py` | Cuerpos de solicitud base (usuario y kit) |
| `sender_stand_request.py` | Funciones para enviar solicitudes HTTP |
| `create_kit_name_kit_test.py` | Pruebas automatizadas (9 casos) |
| `README.md` | Descripción y guía del proyecto |
| `.gitignore` | Archivos/carpetas ignorados por Git |

## Requisitos previos

1. Tener **Python 3** instalado.
2. Instalar las dependencias:

```bash
pip install pytest requests
```

## Configuración

Antes de ejecutar las pruebas, actualiza la URL del servidor en `configuration.py`:

```python
URL_SERVICE = "https://TU-URL-DEL-SERVIDOR.tripleten-services.com"
```

## Cómo ejecutar las pruebas

Desde la raíz del proyecto, ejecuta:

```bash
pytest create_kit_name_kit_test.py -v
```

La bandera `-v` muestra el detalle de cada prueba ejecutada.

## Nota

Algunas pruebas están diseñadas para devolver `FAILED` como resultado esperado según la lista de comprobación. Esto es un comportamiento normal dentro del alcance del proyecto.

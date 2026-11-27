# Documentación de preparación PCAP - Python

Repositorio de materiales de estudio para preparar las certificaciones **PCAP-31-03** y **PCAP-31-04**, junto con documentación básica de Python y recursos complementarios.

Los documentos están organizados por temario, volumen de examen y formato de estudio. Gran parte del contenido se incluye en formato PDF e incluye tanto documentación oficial del temario como guías y resúmenes elaborados con herramientas de IA.

## Contenido

### Fundamentos de Python

La carpeta [`Python - basics/`](Python%20-%20basics/) contiene cinco manuales introductorios:

| Documento | Tema |
|---|---|
| `01 - Introducción a la programación en Python.pdf` | Introducción al lenguaje y al entorno de desarrollo |
| `02 - Tipos de datos y operadores.pdf` | Tipos, variables y operadores |
| `03 - Control de flujo - Bucles y decisiones.pdf` | Condicionales, bucles y control de flujo |
| `04 - Estructuras de datos.pdf` | Listas, tuplas, diccionarios y conjuntos |
| `05 - Funciones.pdf` | Definición, argumentos y ámbito de funciones |

### PCAP-31-03

La carpeta [`PCAP-31-03/`](PCAP-31-03/) reúne material para la certificación PCAP-31-03:

- `PCAP-31-03 Exam Syllabus.pdf`: temario oficial del examen.
- Cuatro unidades sobre fundamentos de Python, módulos y paquetes, cadenas y excepciones, POO y temas misceláneos.
- Documentación complementaria elaborada por Suso.
- Tres guías o libros de preparación generados con Claude, Gemini y ChatGPT.

Esta colección cubre principalmente:

- Fundamentos de Python.
- Módulos, paquetes y PIP.
- Cadenas y métodos de listas.
- Excepciones.
- Programación orientada a objetos.
- Temas misceláneos del temario.

### PCAP-31-04

La carpeta [`PCAP-31-04/`](PCAP-31-04/) contiene el material actualizado correspondiente al temario PCAP-31-04:

| Unidad | Contenido |
|---|---|
| Unidad 01 | Módulos y paquetes |
| Unidad 02 | Excepciones |
| Unidad 03 | Cadenas de texto |
| Unidad 04 | Programación orientada a objetos |
| Unidad 05 | Constructos avanzados y entrada/salida |
| Unidad 06 | Pruebas, depuración, desarrollo colaborativo y asistencia de IA |

También incluye:

- `PCAP-31-04 Exam Syllabus.pdf`: temario oficial del examen.
- Tres libros o guías de estudio generados con Claude, Gemini y ChatGPT.

### Recursos visuales

La carpeta [`infografías/`](infografías/) contiene representaciones visuales de:

- Python, módulos y paquetes.
- Excepciones.
- Cadenas de texto.

La carpeta [`extras/`](extras/) incluye material adicional sobre expresiones regulares:

- Guía visual del módulo `re`.
- PDF sobre expresiones regulares en Python.

## Cuestionario sobre métodos `is...()`

La carpeta [`metodos_is_str/`](metodos_is_str/) incluye un test interactivo con 60 preguntas sobre métodos como `isalpha()`, `isalnum()`, `isdigit()`, `isdecimal()`, `isnumeric()`, `isspace()`, `islower()` y `isupper()`.

El programa ofrece cuatro modalidades:

1. Fácil: 20 preguntas.
2. Medio: 20 preguntas.
3. Alto: 20 preguntas.
4. Completo: las 60 preguntas.

Las preguntas y las opciones se presentan en orden aleatorio. Al finalizar, el programa muestra la nota y guarda un detalle de las respuestas en un archivo de texto dentro de la misma carpeta.

### Ejecutar el cuestionario

Desde la raíz del repositorio:

```bash
python metodos_is_str/cuestionario_python_metodos_is_60_preguntas.py
```

Requisitos:

- Python 3.
- No necesita instalar paquetes externos.

El archivo [`resultados_test_is_20261120_185704.txt`](metodos_is_str/resultados_test_is_20261120_185704.txt) conserva un ejemplo de ejecución y su detalle de aciertos y errores.

## Ruta de estudio recomendada

1. Consultar el temario correspondiente: PCAP-31-03 o PCAP-31-04.
2. Comenzar por los manuales de `Python - basics/`.
3. Revisar las unidades de la versión del examen elegida.
4. Usar las infografías y los recursos de `extras/` para repasar temas concretos.
5. Completar el cuestionario de `metodos_is_str/` y revisar los errores registrados.
6. Contrastar los apuntes con el temario oficial antes del examen.

## Enlaces oficiales

El archivo [`enlaces.txt`](enlaces.txt) contiene los enlaces principales:

- [Página oficial de la certificación PCAP](https://pythoninstitute.org/pcap)
- [Temario oficial de los exámenes PCAP](https://pythoninstitute.org/pcap-exam-syllabus)
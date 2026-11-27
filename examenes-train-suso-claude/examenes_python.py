#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXÁMENES DE PYTHON
==================
Tres niveles (fácil, medio y difícil) con 30 preguntas cada uno, de 4 opciones.
Tras cada respuesta el programa te dice si has acertado y por qué.
Al final obtienes tu puntuación en porcentaje.

Las preguntas siguen el temario del curso:
  Módulo 1: módulos, paquetes y PIP
  Módulo 2: cadenas, listas y excepciones
  Módulo 3: programación orientada a objetos
  Módulo 4: generadores, iteradores, cierres, archivos, os, datetime, time y calendar

Uso:   python examenes_python.py
"""

import os
import random
import sys
import textwrap

ANCHO = 78
NUM_PREGUNTAS = 30
LETRAS = "abcd"


# ======================================================================
#  BANCO DE PREGUNTAS
#  P(pregunta, respuesta_correcta, [3 respuestas incorrectas], explicación,
#    codigo opcional)
#  El orden de las opciones se baraja al hacer el examen.
# ======================================================================
def P(pregunta, correcta, incorrectas, explicacion, codigo=None):
    return {
        "pregunta": pregunta,
        "correcta": correcta,
        "incorrectas": incorrectas,
        "explicacion": explicacion,
        "codigo": codigo,
    }


FACIL = [
    # ---------------------------------------------------- Módulo 1
    P("¿Qué palabra clave se usa en Python para utilizar un módulo en tu programa?",
      "import",
      ["include", "using", "require"],
      "Se usa 'import'. Por ejemplo, 'import math' carga el módulo math y te da acceso "
      "a sus funciones con 'math.sqrt(...)'. 'include', 'using' y 'require' son "
      "palabras de otros lenguajes (C, C#, JavaScript), no de Python."),
    P("¿Qué extensión tiene un archivo que contiene un módulo de Python?",
      ".py",
      [".pym", ".mod", ".pyt"],
      "Un módulo es simplemente un archivo con extensión .py. El nombre del módulo es "
      "el nombre del archivo sin la extensión."),
    P("¿Qué comando de la terminal instala un paquete desde PyPI?",
      "pip install nombre",
      ["pip add nombre", "python get nombre", "pip download-all nombre"],
      "PIP instala paquetes con 'pip install'. Para quitarlos se usa 'pip uninstall'. "
      "Los demás comandos no existen o no hacen esa tarea."),
    P("¿Qué módulo de la biblioteca estándar ofrece funciones como sqrt() y la constante pi?",
      "math",
      ["random", "sys", "os"],
      "El módulo math contiene las funciones y constantes matemáticas. random es para "
      "números aleatorios, sys para el intérprete y os para el sistema operativo."),
    P("¿Qué archivo indica tradicionalmente a Python que una carpeta es un paquete?",
      "__init__.py",
      ["__main__.py", "paquete.py", "setup.txt"],
      "Una carpeta con un archivo __init__.py es un paquete. Puede estar vacío o "
      "reexportar nombres de sus submódulos. __main__.py sirve para ejecutar un "
      "paquete con 'python -m', no para definirlo."),
    P("¿Qué muestra este código?",
      "h0la mund0",
      ["h0la mundo", "hola mundo", "Un error"],
      "replace(viejo, nuevo) sustituye TODAS las apariciones del texto viejo por el nuevo "
      "y devuelve una cadena nueva (la original no cambia).",
      "print('hola mundo'.replace('o', '0'))"),
    P("¿Qué muestra este programa?",
      "5.0",
      ["5", "25", "Un error"],
      "math.sqrt siempre devuelve un número decimal (float), así que el resultado es "
      "5.0 y no 5. El alias 'm' solo es un nombre más corto para el módulo math.",
      "import math as m\nprint(m.sqrt(25))"),
    # ---------------------------------------------------- Módulo 2
    P("¿Qué muestra este código?",
      "65",
      ["97", "1", "A"],
      "ord() devuelve el punto de código Unicode de un carácter. La 'A' mayúscula es "
      "65 y la 'a' minúscula es 97.",
      "print(ord('A'))"),
    P("¿Qué muestra este código?",
      "n",
      ["P", "o", "Un error"],
      "El índice -1 es el último carácter de la cadena, que en 'Python' es la 'n'.",
      "print('Python'[-1])"),
    P("¿Qué ocurre al ejecutar s = 'hola' y después s[0] = 'H'?",
      "Se produce un TypeError: las cadenas son inmutables",
      ["La cadena pasa a ser 'Hola'", "Se crea una variable nueva llamada s0",
       "No pasa nada: Python ignora la orden"],
      "Las cadenas no se pueden modificar una vez creadas. Para cambiar una letra hay "
      "que construir una cadena nueva, por ejemplo: s = 'H' + s[1:]."),
    P("¿Qué muestra este código?",
      "[1, 2, 3, 4]",
      ["[4, 1, 2, 3]", "[1, 2, 3]", "[[1, 2, 3], 4]"],
      "append() añade el elemento al final de la lista y modifica la propia lista.",
      "l = [1, 2, 3]\nl.append(4)\nprint(l)"),
    P("¿Qué muestra este código?",
      "HOLA",
      ["Hola", "hola", "hOLA"],
      "El método upper() devuelve la cadena con todas las letras en mayúscula.",
      "print('hola'.upper())"),
    P("¿Qué pareja de palabras clave se usa para capturar errores en Python?",
      "try y except",
      ["catch y throw", "if y else", "begin y end"],
      "El código que puede fallar va dentro de 'try' y el tratamiento del error en "
      "'except'. 'catch' y 'throw' son de lenguajes como Java o C++."),
    P("¿Qué excepción se produce al ejecutar int('abc')?",
      "ValueError",
      ["TypeError", "NameError", "IndexError"],
      "int() recibe un tipo correcto (una cadena) pero con un valor que no se puede "
      "convertir: eso es ValueError. TypeError sería un tipo inadecuado, como int([])."),
    P("¿Qué excepción se produce al ejecutar 10 / 0?",
      "ZeroDivisionError",
      ["ValueError", "OverflowError", "TypeError"],
      "Dividir entre cero lanza ZeroDivisionError, que es hija de ArithmeticError."),
    P("¿Qué bloque de un try se ejecuta SIEMPRE, haya habido error o no?",
      "finally",
      ["else", "except", "try"],
      "'finally' se ejecuta siempre y por eso se usa para liberar recursos. 'else' solo "
      "se ejecuta si NO hubo excepción y 'except' solo si la hubo."),
    P("¿Qué muestra este código?",
      "3",
      ["4", "2", "Un error"],
      "len() cuenta caracteres, no bytes. 'año' tiene 3 caracteres (aunque en UTF-8 "
      "ocupe 4 bytes, porque la 'ñ' usa dos).",
      "print(len('año'))"),
    # ---------------------------------------------------- Módulo 3
    P("En programación orientada a objetos, ¿qué es una clase?",
      "Una plantilla o molde a partir del cual se crean objetos",
      ["Un objeto concreto ya creado", "Una función que devuelve valores",
       "Un módulo con varias variables"],
      "La clase es el plano; los objetos (instancias) son las cosas concretas "
      "construidas con ese plano."),
    P("¿Para qué sirve el método __init__ de una clase?",
      "Para inicializar un objeto cuando se crea",
      ["Para borrar un objeto", "Para importar la clase", "Para imprimir el objeto"],
      "__init__ es el constructor: se ejecuta automáticamente al crear una instancia y "
      "se usa para dar valor inicial a sus atributos."),
    P("En un método de una clase, ¿qué representa 'self'?",
      "El propio objeto sobre el que se llama al método",
      ["La clase padre", "Una variable global", "El módulo actual"],
      "'self' es el objeto actual. Por eso 'self.nombre' es el atributo nombre de ESE "
      "objeto concreto."),
    P("¿Qué muestra este código?",
      "a-b-c",
      ["['a', 'b', 'c']", "-a-b-c", "abc"],
      "join() une los elementos de una lista de cadenas usando como separador la cadena sobre "
      "la que se llama. Hace lo contrario de split().",
      "print('-'.join(['a', 'b', 'c']))"),
    P("¿Qué significa class Perro(Animal):?",
      "Que Perro hereda de Animal",
      ["Que Animal hereda de Perro", "Que Perro contiene un Animal como atributo",
       "Que Perro y Animal son la misma clase"],
      "La clase que va entre paréntesis es la clase padre. Perro (la hija) recibe los "
      "atributos y métodos de Animal."),
    P("¿Qué es el polimorfismo?",
      "Que objetos de clases distintas respondan al mismo método cada uno a su manera",
      ["Que una clase pueda tener muchos atributos", "Que un objeto se copie a sí mismo",
       "Que una clase se defina en varios archivos"],
      "Por ejemplo, un Perro y un Gato tienen ambos hablar(), pero cada uno devuelve "
      "algo distinto. Quien los usa no necesita saber de qué clase es cada uno."),
    P("¿Cómo se llama a una función definida dentro de una clase?",
      "Método",
      ["Atributo", "Paquete", "Excepción"],
      "Las funciones de una clase se llaman métodos (comportamiento) y las variables, "
      "atributos (datos)."),
    # ---------------------------------------------------- Módulo 4
    P("¿Qué palabra clave convierte una función en un generador?",
      "yield",
      ["return", "generate", "next"],
      "Una función que contiene 'yield' devuelve un generador: entrega valores de uno en "
      "uno y se queda en pausa entre cada petición."),
    P("¿Qué ventaja principal tiene abrir un archivo con 'with open(...) as f:'?",
      "El archivo se cierra automáticamente al terminar el bloque",
      ["El archivo se abre más rápido", "Se puede leer y escribir a la vez siempre",
       "No hace falta indicar el nombre del archivo"],
      "'with' garantiza que el archivo se cierra, incluso si ocurre un error dentro "
      "del bloque."),
    P("¿Qué modo de open() añade texto al final de un archivo sin borrar lo que ya tenía?",
      "'a'",
      ["'w'", "'r'", "'x'"],
      "'a' (append) añade al final. 'w' vacía el archivo, 'r' solo lee y 'x' crea un "
      "archivo nuevo y falla si ya existe."),
    P("¿Qué módulo de la biblioteca estándar se usa para trabajar con fechas y horas?",
      "datetime",
      ["math", "platform", "statistics"],
      "datetime ofrece las clases date, time, datetime y timedelta."),
    P("¿Qué hace time.sleep(2)?",
      "Pausa el programa durante 2 segundos",
      ["Espera 2 minutos", "Devuelve la hora actual más 2 horas",
       "Mide durante 2 segundos cuánto tarda el programa"],
      "sleep() detiene la ejecución el número de segundos indicado."),
    P("¿Qué muestra este código?",
      "True",
      ["False", "2024", "366"],
      "calendar.isleap() devuelve True si el año es bisiesto. 2024 es divisible entre 4 "
      "y no es un año de siglo, así que es bisiesto.",
      "import calendar\n\nprint(calendar.isleap(2024))"),
]

MEDIO = [
    # ---------------------------------------------------- Módulo 1
    P("¿Qué muestra este código?",
      "4.0",
      ["4", "16", "Un error: sqrt no está definido"],
      "'from math import sqrt as raiz' importa solo sqrt, pero con el nombre 'raiz', y ya "
      "no hace falta escribir 'math.'. El resultado es un float: 4.0.",
      "from math import sqrt as raiz\nprint(raiz(16))"),
    P("¿Para qué sirve el bloque if __name__ == \"__main__\": en un archivo .py?",
      "Para que ese código solo se ejecute cuando el archivo se lanza directamente, no cuando se importa",
      ["Para que el archivo se pueda importar desde otros", "Para evitar que el programa tenga errores",
       "Para ejecutar el código dos veces"],
      "Al ejecutar el archivo directamente, __name__ vale '__main__'; al importarlo, vale el "
      "nombre del módulo. Así un mismo archivo sirve como biblioteca y como programa."),
    P("Creas un archivo random.py en tu carpeta y en otro archivo de esa carpeta escribes "
      "'import random'. ¿Qué ocurre?",
      "Python importa tu archivo en lugar del módulo estándar",
      ["Python importa el módulo estándar y ignora el tuyo", "Python da un error por nombre duplicado",
       "Se importan los dos y se mezclan"],
      "Python busca primero en la carpeta del script, antes que en la biblioteca estándar. "
      "Por eso no hay que llamar a tus archivos como módulos existentes (random.py, math.py...)."),
    P("En un paquete, ¿qué controla la variable __all__ definida en __init__.py?",
      "Qué nombres se importan con 'from paquete import *'",
      ["Qué versión de Python necesita el paquete", "Qué archivos se instalan con pip",
       "Qué módulos se ejecutan al arrancar el ordenador"],
      "__all__ es la lista de nombres públicos que se importan al hacer 'import *'."),
    P("¿Qué hace el comando 'pip freeze > requirements.txt'?",
      "Guarda en un archivo la lista de paquetes instalados con su versión exacta",
      ["Instala todos los paquetes que haya en requirements.txt", "Bloquea el programa para que no se modifique",
       "Desinstala los paquetes y guarda una copia"],
      "pip freeze imprime los paquetes con su versión y el '>' lo redirige a un archivo. "
      "Luego se reinstalan con 'pip install -r requirements.txt'."),
    P("¿Para qué sirve crear un entorno virtual con 'python -m venv .venv'?",
      "Para aislar los paquetes de un proyecto de los de otros proyectos y del sistema",
      ["Para que Python se ejecute más rápido", "Para proteger el código con contraseña",
       "Para instalar una versión nueva de Python en todo el sistema"],
      "Cada proyecto tiene sus propios paquetes y versiones, y así no chocan entre sí."),
    P("¿Qué muestra este código?",
      "True",
      ["False", "None", "Depende del azar"],
      "Con la misma semilla (seed), el generador produce siempre la misma secuencia, "
      "así que a y b son iguales. Es útil para que los resultados sean reproducibles.",
      "import random\n\nrandom.seed(1)\na = random.randint(1, 100)\nrandom.seed(1)\n"
      "b = random.randint(1, 100)\nprint(a == b)"),
    P("¿Qué muestra este código?",
      "[('b', 3)]",
      ["[('b', 3), ('a', 2)]", "('b', 3)", "{'b': 3}"],
      "most_common(1) devuelve una lista con una tupla: el elemento más repetido y su "
      "número de apariciones.",
      "from collections import Counter\n\nprint(Counter('aabbbc').most_common(1))"),
    # ---------------------------------------------------- Módulo 2
    P("¿Qué muestra este código?",
      "2",
      ["1", "3", "4"],
      "En UTF-8 los caracteres fuera de ASCII ocupan más de un byte. La 'ñ' ocupa 2.",
      "print(len('ñ'.encode('utf-8')))"),
    P("¿Qué muestra este código?",
      "noi",
      ["pro", "ion", "oic"],
      "s[::-1] da la cadena al revés ('noicamargorp') y [:3] se queda con sus tres "
      "primeros caracteres.",
      "s = 'programacion'\nprint(s[::-1][:3])"),
    P("¿Qué muestra este código?",
      "[1, 2, 3, 4]",
      ["[1, 2, 3]", "[4]", "Un error"],
      "'b = a' no copia la lista: a y b son dos nombres para el MISMO objeto. Modificarlo "
      "con b también lo cambia en a.",
      "a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)"),
    P("¿Qué muestra este código?",
      "[1, 2, 3]",
      ["[1, 2, 3, 4]", "[4]", "Un error"],
      "a[:] hace una copia (superficial) de la lista. Añadir un elemento a la copia no "
      "afecta a la original.",
      "a = [1, 2, 3]\nc = a[:]\nc.append(4)\nprint(a)"),
    P("¿Qué muestra este código?",
      "None",
      ["[1, 2, 3]", "[3, 1, 2]", "Un error"],
      "sort() ordena la lista en sitio y devuelve None. Por eso 'lista = lista.sort()' "
      "es un error clásico. Para obtener una lista nueva se usa sorted().",
      "l = [3, 1, 2]\nprint(l.sort())"),
    P("¿Qué muestra este código?",
      "['a', 'b', '', 'c']",
      ["['a', 'b', 'c']", "['a', 'b', ',', 'c']", "['a,b,,c']"],
      "Entre las dos comas seguidas hay una cadena vacía, y split la conserva como "
      "elemento de la lista.",
      "print('a,b,,c'.split(','))"),
    P("¿Qué muestra este código?",
      "Hola Mundo",
      ["  Hola Mundo  ", "Hola mundo", "HOLA MUNDO"],
      "strip() quita los espacios de los extremos y title() pone en mayúscula la inicial "
      "de cada palabra.",
      "print('  hola mundo  '.strip().title())"),
    P("¿Qué muestra este código?",
      "3.14",
      ["3.1", "3.142", "3.14159"],
      "En una f-string, ':.2f' formatea el número con 2 decimales (redondeando).",
      "print(f'{3.14159:.2f}')"),
    P("¿Qué muestra este código?",
      "general",
      ["concreto", "general / concreto", "Un error"],
      "Python elige el primer except que encaja. ZeroDivisionError es hija de "
      "ArithmeticError, así que entra en el primero y el segundo nunca se ejecuta. "
      "Los except deben ordenarse de lo más específico a lo más general.",
      "try:\n    print(10 / 0)\nexcept ArithmeticError:\n    print('general')\n"
      "except ZeroDivisionError:\n    print('concreto')"),
    P("¿Qué muestra este código? (la salida se muestra en una sola línea separando "
      "con ' / ' cada línea impresa)",
      "ok / fin",
      ["ok", "fin / ok", "error / fin"],
      "No hay excepción, así que se ejecuta el bloque else ('ok') y después el finally "
      "('fin'), que siempre va el último.",
      "try:\n    x = 10 / 2\nexcept ZeroDivisionError:\n    print('error')\nelse:\n"
      "    print('ok')\nfinally:\n    print('fin')"),
    # ---------------------------------------------------- Módulo 3
    P("¿Qué muestra este código? (los corchetes se ven en la salida; cuenta los espacios)",
      "[   ab]",
      ["[ab   ]", "[ ab  ]", "[ab]"],
      "En una f-string, ':>5' alinea a la derecha en un ancho de 5 caracteres, rellenando "
      "con espacios por la izquierda. ':<5' alinearía a la izquierda y ':^5' centraría.",
      "print(f\"[{'ab':>5}]\")"),
    P("¿Qué muestra este código?",
      "5",
      ["Un error: hay que escribir C().v()", "<function v>", "None"],
      "@property permite acceder a un método como si fuera un atributo, sin paréntesis.",
      "class C:\n    def __init__(self):\n        self._v = 5\n\n    @property\n"
      "    def v(self):\n        return self._v\n\nprint(C().v)"),
    P("¿Para qué se usa super().__init__(...) dentro del __init__ de una clase hija?",
      "Para ejecutar el constructor de la clase padre y reutilizar su inicialización",
      ["Para crear un objeto de la clase padre y borrar el actual",
       "Para impedir que la clase hija tenga atributos propios",
       "Para convertir la clase hija en una clase abstracta"],
      "super() da acceso a la clase padre. Así no hay que repetir en la hija la "
      "inicialización que ya hace el padre."),
    P("¿Qué muestra este código?",
      "B",
      ["A", "AB", "Un error"],
      "La clase hija redefine (override) el método del padre. Al llamarlo sobre un "
      "objeto B se ejecuta la versión de B.",
      "class A:\n    def hola(self):\n        return 'A'\n\nclass B(A):\n"
      "    def hola(self):\n        return 'B'\n\nprint(B().hola())"),
    P("¿Qué muestra este código?",
      "True False",
      ["True True", "False False", "False True"],
      "isdigit() solo es True si TODOS los caracteres son dígitos. En '20.5' el punto no lo "
      "es, así que da False. Es útil para validar texto antes de convertirlo con int().",
      "print('2024'.isdigit(), '20.5'.isdigit())"),
    P("¿Qué parámetro recibe un método decorado con @staticmethod?",
      "Ninguno obligatorio: no recibe ni self ni cls",
      ["Siempre self", "Siempre cls (la clase)", "Siempre el objeto y la clase"],
      "Un método estático es una función normal guardada dentro de la clase porque está "
      "relacionada con ella; no necesita acceder al objeto ni a la clase."),
    P("¿Qué muestra este código?",
      "mensaje",
      ["MiError", "MiError('mensaje')", "Nada: no se puede capturar una excepción propia"],
      "Las excepciones propias se crean heredando de Exception y se capturan como las "
      "demás. Al imprimir la excepción se muestra el mensaje con el que se lanzó.",
      "class MiError(Exception):\n    pass\n\ntry:\n    raise MiError('mensaje')\n"
      "except MiError as e:\n    print(e)"),
    # ---------------------------------------------------- Módulo 4
    P("¿Qué muestra este código?",
      "2",
      ["1", "[1, 2]", "Un error"],
      "Cada next() ejecuta el generador hasta el siguiente yield. La primera llamada "
      "entrega 1 (que se descarta) y la segunda entrega 2.",
      "def g():\n    yield 1\n    yield 2\n\nit = g()\nnext(it)\nprint(next(it))"),
    P("Un archivo ya existente se abre con open('datos.txt', 'w'). ¿Qué ocurre?",
      "Se vacía su contenido anterior",
      ["Se añaden las nuevas líneas al final", "Da un error porque ya existe",
       "Se abre solo para lectura"],
      "El modo 'w' crea el archivo o lo vacía si ya existía. Para añadir sin borrar hay "
      "que usar 'a'."),
    P("¿Qué muestra este código?",
      ".txt",
      ["c.txt", "c", "a/b/c.txt"],
      "El operador / une trozos de ruta en pathlib, y .suffix devuelve la extensión "
      "del último componente.",
      "from pathlib import Path\n\nprint((Path('a') / 'b' / 'c.txt').suffix)"),
    P("¿Qué muestra este código?",
      "2026-12-17",
      ["2026-11-47", "2026-12-07", "2026-11-30"],
      "Sumar un timedelta a una fecha da otra fecha. Noviembre tiene 30 días, así que "
      "17 de noviembre + 30 días = 17 de diciembre.",
      "from datetime import date, timedelta\n\nprint(date(2026, 11, 17) + timedelta(days=30))"),
    P("¿Qué muestra este código?",
      "17/11/2026",
      ["2026/11/17", "17-11-2026", "11/17/2026"],
      "%d es el día, %m el mes y %Y el año con cuatro dígitos. El formato respeta "
      "el orden y los separadores que escribas.",
      "from datetime import datetime\n\n"
      "print(datetime(2026, 11, 17, 18, 30).strftime('%d/%m/%Y'))"),
]

DIFICIL = [
    # ---------------------------------------------------- Módulo 1
    P("Importas el mismo módulo dos veces en un programa. ¿Qué ocurre con el código de nivel "
      "superior del módulo (por ejemplo, un print)?",
      "Solo se ejecuta la primera vez; luego Python reutiliza el módulo guardado en sys.modules",
      ["Se ejecuta cada vez que se importa", "Se ejecuta solo la segunda vez",
       "Python lanza ImportError por importación duplicada"],
      "Cada módulo se carga y ejecuta una sola vez. Las siguientes importaciones "
      "recuperan el objeto ya cargado desde sys.modules."),
    P("El módulo numeros.py, dentro del paquete 'herramientas', contiene 'from .texto import "
      "invertir'. ¿Por qué falla al lanzarlo con 'python herramientas/numeros.py'?",
      "Porque al ejecutarlo como script no pertenece a ningún paquete y la importación relativa no tiene sentido",
      ["Porque texto.py no existe", "Porque hay que instalar el paquete con pip primero",
       "Porque 'invertir' es una palabra reservada"],
      "Las importaciones relativas solo funcionan dentro de un paquete. Hay que "
      "ejecutarlo como parte de él: 'python -m herramientas.numeros'."),
    P("¿Qué significa la especificación 'requests>=2.28,<3' en pip?",
      "Una versión igual o superior a 2.28 pero inferior a 3",
      ["Exactamente las versiones 2.28 y 3", "Cualquier versión anterior a 2.28",
       "Las versiones 2.28 y 3, ambas incluidas"],
      "Se pueden combinar condiciones separadas por comas: todas deben cumplirse. "
      "Es una forma habitual de aceptar actualizaciones menores pero evitar un salto de "
      "versión mayor que podría romper el código."),
    P("En un Linux reciente, pip responde 'externally-managed-environment'. ¿Cuál es la "
      "solución recomendada?",
      "Crear un entorno virtual e instalar el paquete dentro de él",
      ["Usar 'sudo pip install' para forzarlo", "Desinstalar el Python del sistema",
       "Renombrar el paquete antes de instalarlo"],
      "El sistema protege su propio Python para no romperse. Un entorno virtual te da un "
      "Python tuyo, aislado, donde sí puedes instalar lo que quieras."),
    P("¿Qué muestra este código?",
      "['a', 'b', 'c,d']",
      ["['a', 'b']", "['a', 'b', 'c', 'd']", "['a,b', 'c,d']"],
      "El segundo argumento de split() es el número máximo de divisiones. Con 2 se hacen "
      "solo dos cortes y lo que queda ('c,d') se conserva entero como último elemento.",
      "print('a,b,c,d'.split(',', 2))"),
    P("Necesitas 3 números aleatorios distintos entre 0 y 9. ¿Qué opción garantiza que no se repitan?",
      "random.sample(range(10), 3)",
      ["random.choices(range(10), k=3)", "[random.randint(0, 9) for _ in range(3)]",
       "Llamar tres veces a random.choice(range(10))"],
      "sample() elige sin reemplazo, así que nunca repite elementos. choices(), randint() y "
      "choice() pueden dar el mismo valor varias veces."),
    # ---------------------------------------------------- Módulo 2
    P("¿Qué muestra este código?",
      "b'a\\xc3\\xb1o'",
      ["b'a\\xf1o'", "b'ano'", "'año'"],
      "En UTF-8 la 'ñ' se codifica con dos bytes (\\xc3\\xb1). Con Latin-1 sería un solo byte "
      "(\\xf1), por eso esa otra opción es un error típico al mezclar codificaciones.",
      "print('año'.encode('utf-8'))"),
    P("¿Qué muestra este código?",
      "1 3",
      ["1 1", "3 3", "2 3"],
      "Es un solo carácter (len = 1), pero en UTF-8 el símbolo del euro ocupa 3 bytes. "
      "len() de una cadena cuenta caracteres; len() de bytes cuenta bytes.",
      "print(len('€'), len('€'.encode('utf-8')))"),
    P("¿Qué muestra este código?",
      "[[1, 0], [1, 0]]",
      ["[[1, 0], [0, 0]]", "[[0, 0], [1, 0]]", "[[1, 1], [0, 0]]"],
      "[[0] * 2] * 2 repite LA MISMA lista interior dos veces, así que cambiar un valor "
      "en una fila lo cambia en las dos. Se debe usar [[0] * 2 for _ in range(2)].",
      "l = [[0] * 2] * 2\nl[0][0] = 1\nprint(l)"),
    P("¿Qué muestra este código?",
      "[[1, 9], [2]]",
      ["[[1], [2]]", "[[9], [2]]", "[[1, 9], [2, 9]]"],
      "copy() hace una copia superficial: copia la lista exterior, pero las listas "
      "interiores se siguen compartiendo. Para una copia total se usa copy.deepcopy().",
      "a = [[1], [2]]\nb = a.copy()\na[0].append(9)\nprint(b)"),
    P("¿Qué muestra este código?",
      "['A', 'B', 'a', 'b']",
      ["['A', 'a', 'B', 'b']", "['a', 'A', 'b', 'B']", "['a', 'b', 'A', 'B']"],
      "Las cadenas se ordenan por su punto de código Unicode: las mayúsculas (65-90) "
      "van antes que las minúsculas (97-122).",
      "print(sorted(['b', 'A', 'a', 'B']))"),
    P("¿Qué muestra este código?",
      "('a', '-', 'b-c')",
      ["['a', 'b', 'c']", "('a', 'b-c')", "('a-b', '-', 'c')"],
      "partition divide en la PRIMERA aparición del separador y devuelve siempre una "
      "tupla de tres elementos: lo anterior, el separador y lo posterior.",
      "print('a-b-c'.partition('-'))"),
    P("¿Qué muestra este código?",
      "-1 2",
      ["None 2", "-1 3", "ValueError"],
      "find() devuelve -1 cuando no encuentra el texto (index() lanzaría ValueError). "
      "Aquí index('c') devuelve la posición 2.",
      "print('abc'.find('z'), 'abc'.index('c'))"),
    P("¿Qué muestra este código? (se muestra en una línea separando con ' / ' cada línea impresa)",
      "finally / try",
      ["try / finally", "try", "finally"],
      "El bloque finally se ejecuta ANTES de que la función entregue su valor de "
      "retorno, aunque el return esté dentro del try. Por eso se imprime 'finally' "
      "primero y luego el print(f()) muestra 'try'.",
      "def f():\n    try:\n        return 'try'\n    finally:\n        print('finally')\n\nprint(f())"),
    P("¿Qué muestra este código?",
      "L",
      ["I", "L / I", "Un error"],
      "IndexError es hija de LookupError. Como el except de LookupError va primero, es "
      "el que atrapa el error y el de IndexError queda inalcanzable.",
      "try:\n    [][1]\nexcept LookupError:\n    print('L')\nexcept IndexError:\n    print('I')"),
    P("¿Qué muestra este código?",
      "False",
      ["True", "None", "Un error"],
      "KeyboardInterrupt hereda de BaseException, no de Exception. Por eso un "
      "'except Exception' no impide al usuario cancelar el programa con Ctrl+C.",
      "print(issubclass(KeyboardInterrupt, Exception))"),
    # ---------------------------------------------------- Módulo 3
    P("Con 'raise ErrorNuevo(...) from error_original', ¿en qué atributo de la excepción nueva "
      "queda guardada la causa original?",
      "__cause__",
      ["__origin__", "__previous__", "args"],
      "'raise ... from e' guarda e en __cause__. Así el traceback muestra que el segundo "
      "error es consecuencia directa del primero."),
    P("¿Qué muestra este código?",
      "DBCA",
      ["DBA", "DCBA", "DACB"],
      "El MRO de D es D, B, C, A. Cada super() pasa al siguiente de esa lista, de modo que "
      "se recorren las cuatro clases: D → B → C → A.",
      "class A:\n    def h(self):\n        return 'A'\n\nclass B(A):\n    def h(self):\n"
      "        return 'B' + super().h()\n\nclass C(A):\n    def h(self):\n"
      "        return 'C' + super().h()\n\nclass D(B, C):\n    def h(self):\n"
      "        return 'D' + super().h()\n\nprint(D().h())"),
    P("¿Qué muestra este código?",
      "[1]",
      ["[]", "[1, 1]", "Un error"],
      "El valor por defecto items=[] se crea UNA sola vez, al definir la función, y lo "
      "comparten todos los objetos. La solución es usar None y crear la lista dentro.",
      "class X:\n    def __init__(self, items=[]):\n        self.items = items\n\n"
      "a = X()\nb = X()\na.items.append(1)\nprint(b.items)"),
    P("¿Qué ocurre al crear un objeto de una clase que hereda de ABC y tiene un método "
      "@abstractmethod sin implementar?",
      "Se lanza TypeError",
      ["Se crea el objeto y el método devuelve None", "Se lanza NotImplementedError al crearlo",
       "Se crea el objeto, pero no se puede imprimir"],
      "Python impide instanciar la clase mientras queden métodos abstractos sin "
      "implementar, lanzando TypeError."),
    P("¿Qué muestra este código?",
      "2 3 3",
      ["2 2 3", "3 3 3", "2 3 2"],
      "a.x = 2 crea un atributo de instancia solo en a. A.x = 3 cambia el atributo de clase, "
      "que es el que ve b (porque no tiene uno propio) y el que muestra A.x.",
      "class A:\n    x = 1\n\na, b = A(), A()\na.x = 2\nA.x = 3\nprint(a.x, b.x, A.x)"),
    P("¿Qué muestra este código?",
      "False True",
      ["True False", "True True", "False False"],
      "Un atributo que empieza por doble guion bajo cambia internamente su nombre "
      "(name mangling) a _Clase__nombre. Por eso '__s' no existe, pero '_C__s' sí.",
      "class C:\n    def __init__(self):\n        self.__s = 1\n\nc = C()\n"
      "print(hasattr(c, '__s'), hasattr(c, '_C__s'))"),
    P("Una clase define una propiedad con @property pero sin setter. ¿Qué ocurre al asignarle "
      "un valor (objeto.prop = 5)?",
      "Se lanza AttributeError",
      ["Se guarda el valor sin problema", "Se lanza TypeError",
       "Se convierte en atributo normal y el getter desaparece"],
      "Una propiedad solo con getter es de solo lectura; asignarle un valor lanza "
      "AttributeError. Para permitirlo hay que añadir un @prop.setter."),
    P("¿Qué muestra este código?",
      "B",
      ["A", "cls", "crear"],
      "Un @classmethod recibe como primer argumento la clase desde la que se llama (cls). "
      "Al llamarlo con B.crear(), cls es B, no A.",
      "class A:\n    @classmethod\n    def crear(cls):\n        return cls.__name__\n\n"
      "class B(A):\n    pass\n\nprint(B.crear())"),
    P("¿Qué método especial basta definir en una clase para que sorted() pueda ordenar una "
      "lista de sus objetos?",
      "__lt__",
      ["__sort__", "__order__", "__len__"],
      "sorted() compara los elementos con el operador '<', que Python traduce a "
      "__lt__ (less than)."),
    # ---------------------------------------------------- Módulo 4
    P("¿Qué muestra este código?",
      "[2, 2, 2]",
      ["[0, 1, 2]", "[0, 0, 0]", "[1, 2, 3]"],
      "Las funciones lambda capturan la VARIABLE i, no su valor. Cuando se llaman, el bucle "
      "ya terminó y i vale 2. Se arregla fijando el valor: lambda i=i: i.",
      "fs = [lambda: i for i in range(3)]\nprint([f() for f in fs])"),
    P("¿Qué muestra este código?",
      "[0, 1, 2] []",
      ["[0, 1, 2] [0, 1, 2]", "[] []", "Un error"],
      "Un generador se agota: tras consumirlo con el primer list(), el segundo no tiene "
      "nada que entregar.",
      "g = (x for x in range(3))\nprint(list(g), list(g))"),
    P("¿Qué muestra este código?",
      "2",
      ["1", "0", "UnboundLocalError"],
      "'nonlocal n' permite a la función interna reasignar la variable de la función externa. "
      "El cierre conserva su valor entre llamadas: la primera deja n en 1 y la segunda en 2.",
      "def contador():\n    n = 0\n\n    def inc():\n        nonlocal n\n        n += 1\n"
      "        return n\n\n    return inc\n\nf = contador()\nf()\nprint(f())"),
    P("¿Qué muestra este código?",
      "38",
      ["8", "37", "39"],
      "Restar dos fechas da un timedelta, y .days son los días. Del 17 de noviembre al 25 "
      "de diciembre hay 13 días hasta fin de noviembre más 25 de diciembre: 38.",
      "from datetime import date\n\nprint((date(2026, 12, 25) - date(2026, 11, 17)).days)"),
    P("Para medir cuánto tarda en ejecutarse un fragmento de código, ¿qué función es la más adecuada?",
      "time.perf_counter()",
      ["time.time()", "time.sleep()", "time.localtime()"],
      "perf_counter() es un reloj de alta resolución que nunca retrocede. time.time() "
      "puede cambiar si el sistema ajusta la hora, y sleep() solo pausa el programa."),
]

NIVELES = {
    "1": ("FÁCIL", FACIL),
    "2": ("MEDIO", MEDIO),
    "3": ("DIFÍCIL", DIFICIL),
}


# ======================================================================
#  PRESENTACIÓN
# ======================================================================
def _color_activo():
    if os.environ.get("NO_COLOR"):
        return False
    try:
        if not sys.stdout.isatty():
            return False
    except Exception:
        return False
    if os.name == "nt":
        os.system("")  # activa los códigos ANSI en la consola de Windows 10+
    return True


COLOR = _color_activo()


def pintar(texto, codigo):
    return f"\033[{codigo}m{texto}\033[0m" if COLOR else texto


def verde(t):
    return pintar(t, "92")


def rojo(t):
    return pintar(t, "91")


def amarillo(t):
    return pintar(t, "93")


def azul(t):
    return pintar(t, "96")


def tenue(t):
    return pintar(t, "90")


def negrita(t):
    return pintar(t, "1")


def linea(caracter="=", ancho=ANCHO):
    return caracter * ancho


def envolver(texto, sangria="", ancho=ANCHO):
    return textwrap.fill(texto, width=ancho, initial_indent=sangria,
                         subsequent_indent=sangria)


def leer(mensaje):
    """input() que trata Ctrl+D / Ctrl+C como una salida limpia."""
    try:
        return input(mensaje)
    except (EOFError, KeyboardInterrupt):
        print("\n\nHasta pronto.")
        sys.exit(0)


def preparar_pregunta(p):
    """Baraja las opciones y devuelve (lista de opciones, índice de la correcta)."""
    opciones = [p["correcta"]] + list(p["incorrectas"])
    random.shuffle(opciones)
    return opciones, opciones.index(p["correcta"])


def mostrar_pregunta(numero, total, p, opciones):
    print()
    print(azul(linea("-")))
    print(negrita(f"Pregunta {numero} de {total}"))
    print(envolver(p["pregunta"]))
    if p["codigo"]:
        print()
        for fila in p["codigo"].split("\n"):
            print(tenue("  | ") + fila)
    print()
    for letra, texto in zip(LETRAS, opciones):
        print(textwrap.fill(f"{letra}) {texto}", width=ANCHO, initial_indent="  ",
                            subsequent_indent="     "))
    print()


def pedir_respuesta():
    """Devuelve 0-3 o None si el usuario quiere abandonar el examen."""
    while True:
        r = leer("Tu respuesta (a/b/c/d, o 's' para salir del examen): ").strip().lower()
        if r in ("s", "salir"):
            return None
        if r in ("1", "2", "3", "4"):
            return int(r) - 1
        if r in tuple(LETRAS):
            return LETRAS.index(r)
        print(amarillo("  Respuesta no válida. Escribe a, b, c o d."))


def valoracion(porcentaje):
    if porcentaje >= 90:
        return "¡Excelente! Dominas este nivel."
    if porcentaje >= 70:
        return "Muy bien. Repasa solo los detalles que has fallado."
    if porcentaje >= 50:
        return "Aprobado, pero conviene repasar los capítulos de los fallos."
    return "Todavía no. Vuelve a leer los capítulos del libro y repite el examen."


# ======================================================================
#  EXAMEN
# ======================================================================
def hacer_examen(nombre, banco):
    preguntas = random.sample(banco, min(NUM_PREGUNTAS, len(banco)))
    total = len(preguntas)
    aciertos = 0
    fallos = []

    print()
    print(linea("="))
    print(negrita(f"EXAMEN NIVEL {nombre}  ·  {total} preguntas"))
    print(linea("="))
    print("Responde con la letra de la opción. Al contestar verás si has acertado y por qué.")

    for numero, p in enumerate(preguntas, start=1):
        opciones, correcta = preparar_pregunta(p)
        mostrar_pregunta(numero, total, p, opciones)
        r = pedir_respuesta()
        if r is None:
            print(amarillo("\nExamen abandonado. No se calcula puntuación."))
            return None

        if r == correcta:
            aciertos += 1
            print(verde("✔ ¡CORRECTO!"))
        else:
            fallos.append((numero, p))
            print(rojo(f"✘ INCORRECTO. Elegiste {LETRAS[r]}) y la respuesta correcta era "
                       f"{LETRAS[correcta]})."))
        print(textwrap.fill("Razón: " + p["explicacion"], width=ANCHO,
                            initial_indent="  ", subsequent_indent="  "))
        palabra = "acierto" if aciertos == 1 else "aciertos"
        print(tenue(f"  Llevas {aciertos} {palabra} de {numero}."))
        if numero < total:
            leer(tenue("\n[Enter para continuar]"))

    mostrar_resultado(nombre, aciertos, total, fallos)
    return aciertos / total * 100


def mostrar_resultado(nombre, aciertos, total, fallos):
    porcentaje = aciertos / total * 100
    print()
    print(linea("="))
    print(negrita(f"RESULTADO · NIVEL {nombre}"))
    print(linea("="))
    print(f"  Aciertos : {aciertos} de {total}")
    print(f"  Fallos   : {total - aciertos}")
    color = verde if porcentaje >= 70 else (amarillo if porcentaje >= 50 else rojo)
    print(f"  Puntuación: {color(negrita(f'{porcentaje:.1f} %'))}")
    print()
    print(envolver(valoracion(porcentaje), sangria="  "))

    if fallos:
        print()
        print(negrita("Repaso de las preguntas falladas:"))
        for numero, p in fallos:
            print()
            print(textwrap.fill(f"Pregunta {numero}: {p['pregunta']}", width=ANCHO,
                                initial_indent="  ", subsequent_indent="     "))
            if p["codigo"]:
                for fila in p["codigo"].split("\n"):
                    print(tenue("     | ") + fila)
            print(textwrap.fill(f"→ Respuesta correcta: {p['correcta']}", width=ANCHO,
                                initial_indent="     ", subsequent_indent="       "))


# ======================================================================
#  MENÚ
# ======================================================================
def mostrar_menu(historial):
    print()
    print(linea("="))
    print(negrita("  EXÁMENES DE PYTHON"))
    print(linea("="))
    print("  Elige la dificultad:")
    print()
    print("    1) Fácil     (30 preguntas · conceptos básicos)")
    print("    2) Medio     (30 preguntas · leer y predecir código)")
    print("    3) Difícil   (30 preguntas · casos tramposos y detalles finos)")
    print("    4) Salir")
    if historial:
        print()
        print(tenue("  Mejores resultados de esta sesión:"))
        for clave in sorted(historial):
            nombre = NIVELES[clave][0]
            print(tenue(f"    {nombre:<8} {historial[clave]:.1f} %"))
    print()


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    historial = {}
    while True:
        mostrar_menu(historial)
        opcion = leer("Opción (1-4): ").strip()
        if opcion == "4":
            print("\n¡Mucho ánimo con el curso!")
            return
        if opcion not in NIVELES:
            print(amarillo("  Opción no válida. Escribe 1, 2, 3 o 4."))
            continue

        nombre, banco = NIVELES[opcion]
        resultado = hacer_examen(nombre, banco)
        if resultado is not None:
            historial[opcion] = max(resultado, historial.get(opcion, 0))
        leer(tenue("\n[Enter para volver al menú]"))


if __name__ == "__main__":
    main()

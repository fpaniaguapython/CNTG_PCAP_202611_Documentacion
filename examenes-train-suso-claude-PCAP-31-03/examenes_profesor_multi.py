#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXÁMENES DE PYTHON · TEMARIO DEL PROFESOR
=========================================
Dos niveles (Normal y Difícil) con 30 preguntas cada uno, de 4 opciones.
Las preguntas mezclan TODOS los temas de los apuntes:

  01 Módulos, paquetes y PIP
  02 Cadenas, métodos de listas y excepciones
  03 Programación orientada a objetos
  04 Misceláneo (iteradores, generadores, lambda, cierres, archivos, os,
     datetime, time y calendar)

La dificultad no depende del tema, sino de lo enrevesada o tramposa que es la
pregunta. Tras cada respuesta verás si has acertado y por qué, y al final
obtendrás tu puntuación en porcentaje.

Idiomas: español e inglés (se elige al arrancar y se puede cambiar desde el menú).
Languages: Spanish and English (chosen at start, changeable from the menu).

Uso:   python examenes_profesor.py
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
#  P(pregunta, correcta, [3 incorrectas], explicación, código visible, prueba)
#  'codigo' se muestra en la pregunta. 'prueba' es solo para verificar el banco.
#  El orden de las opciones se baraja al hacer el examen.
# ======================================================================
def P(pregunta, correcta, incorrectas, explicacion, codigo=None, prueba=None):
    return {
        "pregunta": pregunta,
        "correcta": correcta,
        "incorrectas": incorrectas,
        "explicacion": explicacion,
        "codigo": codigo,
        "prueba": prueba,
    }


NORMAL = [
    # ------------------------------------------------ 01 Módulos, paquetes, PIP
    P("En tu script defines pi = 3 y además importas el módulo math. ¿Qué muestra este código?",
      "3 3.141592653589793",
      ["3.141592653589793 3.141592653589793", "3 3", "Un error: pi está duplicado"],
      "Cada módulo tiene su propio espacio de nombres (namespace). 'pi' es la variable de tu "
      "script y 'math.pi' es la constante del módulo math: conviven sin conflicto. Si no "
      "antepones el módulo, Python usa tu propio nombre.",
      "import math\npi = 3\nprint(pi, math.pi)"),
    P("¿Qué muestra este código?",
      "-4 -3 -3",
      ["-3 -4 -4", "-4 -4 -3", "-3 -3 -3"],
      "floor() devuelve el entero más grande menor o igual (-4); ceil() el más pequeño mayor o "
      "igual (-3); trunc() simplemente elimina la parte decimal (-3). Con negativos no coinciden.",
      "import math\nprint(math.floor(-3.5), math.ceil(-3.5), math.trunc(-3.5))"),
    P("random.randrange(2, 10, 3) solo puede devolver...",
      "2, 5 u 8",
      ["2, 5, 8 o 10", "Cualquier entero entre 2 y 10", "3, 6 o 9"],
      "Funciona como range(ini, fin, inc): empieza en 2, avanza de 3 en 3 y NO llega a 10. "
      "Los valores posibles son 2, 5 y 8.",
      None,
      "import random\nprint(sorted({random.randrange(2, 10, 3) for _ in range(600)}) == [2, 5, 8])"),
    P("Según los apuntes, ¿qué relación hay entre randint(a, b) y randrange?",
      "randint(a, b) equivale a randrange(a, b + 1)",
      ["randint(a, b) equivale a randrange(a, b)", "randint(a, b) equivale a randrange(a + 1, b)",
       "No tienen ninguna relación"],
      "randint incluye los dos extremos, mientras que randrange excluye el final. Por eso "
      "randint(a, b) es lo mismo que randrange(a, b + 1).",
      None,
      "import random\nrandom.seed(7)\nx = random.randint(1, 6)\nrandom.seed(7)\ny = random.randrange(1, 7)\nprint(x == y)"),
    P("Al importar un módulo, Python crea una carpeta __pycache__. ¿Qué contiene?",
      "Archivos .pyc con el código compilado del módulo",
      ["Copias de seguridad de tus archivos .py", "Los paquetes instalados con pip",
       "Un registro con los errores producidos al importar"],
      "Contiene ficheros .pyc (compilados). Su nombre incluye el módulo, la implementación y la "
      "versión de Python; por ejemplo, modulo2.cpython-311.pyc."),
    P("Un módulo es importado desde otro módulo. ¿Qué valor toma __name__ dentro del módulo importado?",
      "El nombre del propio módulo",
      ["'__main__'", "None", "El nombre del script que lo importa"],
      "__name__ vale '__main__' solo en el módulo que se ejecuta directamente. En un módulo "
      "importado toma el nombre del módulo. Por eso 'if __name__ == \"__main__\":' separa el "
      "código que solo debe correr al lanzar el archivo.",
      None,
      "open('mod_x.py', 'w').write('NOMBRE = __name__\\n')\nimport mod_x\nprint(mod_x.NOMBRE == 'mod_x')"),
    P("¿Qué variable del módulo sys contiene la lista (ordenada) de ubicaciones donde Python busca los módulos?",
      "sys.path",
      ["sys.modules", "sys.argv", "sys.paths"],
      "La búsqueda se hace en el orden de la lista sys.path, que puede incluir archivos .zip y se "
      "puede modificar con append (al final) o insert (para cambiar el orden).",
      None,
      "import sys\nprint(isinstance(sys.path, list) and not hasattr(sys, 'paths'))"),
    P("¿Qué comando muestra información de un paquete instalado, incluidas sus dependencias "
      "(Requires y Required-by)?",
      "pip show paquete",
      ["pip list paquete", "pip info paquete", "pip help paquete"],
      "'pip show paquete' muestra nombre, versión, autor, sitio web y dependencias en las dos "
      "direcciones. 'pip list' solo lista todo lo instalado, y 'pip help' muestra ayuda del comando."),
    # ------------------------------------------------ 02 Cadenas, listas, excepciones
    P("¿Qué muestra este código?",
      "6",
      ["3", "4", "5"],
      "len() cuenta TODOS los caracteres, incluidos espacios, tabuladores y saltos de línea: "
      "'a', ' ', 'b', tabulador, 'c' y salto de línea son 6.",
      "print(len('a b\\tc\\n'))"),
    P("¿Qué muestra este código?",
      "True abcc",
      ["False abcc", "True ababc", "True abcab"],
      "La replicación con * no depende del orden (3 * 'ab' es igual a 'ab' * 3), y el * tiene "
      "prioridad sobre el +: 'ab' + ('c' * 2) da 'abcc'.",
      "print(3 * 'ab' == 'ab' * 3, 'ab' + 'c' * 2)"),
    P("¿Qué muestra este código?",
      "True True",
      ["False True", "True False", "False False"],
      "Se comparan los puntos de código: las mayúsculas son menores que las minúsculas, así que "
      "'Hola' < 'hola'. Y si una cadena tiene los mismos caracteres que otra más uno extra, la "
      "más larga es mayor.",
      "print('Hola' < 'hola', 'abc' < 'abcd')"),
    P("¿Qué muestra este código?",
      "Hola mundo",
      ["Hola Mundo", "HOLA MUNDO", "hOLA mUNDO"],
      "capitalize() pone en mayúscula SOLO el primer carácter y convierte el resto a minúscula. "
      "(title() sería el que pone en mayúscula cada palabra.)",
      "print('hOLA mUNDO'.capitalize())"),
    P("¿Qué muestra este código?",
      "False True",
      ["True False", "TypeError", "False False"],
      "Comparar una cadena con un número con == y != es posible: nunca son iguales ('==' da "
      "False y '!=' da True). Con >, <, >= o <= se produciría un TypeError.",
      "print('abc' == 5, 'abc' != 5)"),
    P("¿Cuál de estas aserciones lanza AssertionError?",
      "assert 0",
      ["assert 1", "assert 'hola'", "assert [0]"],
      "assert solo falla si la expresión es falsa. Un número distinto de cero, una cadena no vacía "
      "o una lista no vacía (aunque contenga un 0) se consideran verdaderos.",
      None,
      "try:\n    assert 0\nexcept AssertionError:\n    print(True)"),
    P("¿Qué excepción es hija de LookupError?",
      "KeyError",
      ["ValueError", "OverflowError", "KeyboardInterrupt"],
      "IndexError y KeyError cuelgan de LookupError. OverflowError cuelga de ArithmeticError y "
      "KeyboardInterrupt directamente de BaseException.",
      None,
      "print(issubclass(KeyError, LookupError))"),
    # ------------------------------------------------ 03 POO
    P("Dentro de la clase Cuenta se define self.__saldo. ¿Qué ocurre con ese atributo?",
      "Sigue siendo accesible desde fuera como objeto._Cuenta__saldo",
      ["Es totalmente inaccesible desde fuera", "Se convierte en un atributo de clase",
       "Se elimina al terminar el constructor"],
      "Los apuntes lo llaman privado 'con trampa': Python cambia el nombre a _Clase__atributo. "
      "Dificulta el acceso accidental, pero no lo impide.",
      None,
      "class C:\n    def __init__(self):\n        self.__s = 1\nprint(C()._C__s == 1)"),
    P("¿Cómo se invoca al constructor de la superclase con super()?",
      "super().__init__(...), sin pasar self",
      ["super().__init__(self, ...)", "super.__init__(...)", "__super__.init(...)"],
      "Con super() no se pasa la referencia self (se pasa sola). Con la otra forma, "
      "Superclase.__init__(self), sí hay que pasarla explícitamente.",
      None,
      "class A:\n    def __init__(self, x):\n        self.x = x\nclass B(A):\n    def __init__(self):\n        super().__init__(5)\nprint(B().x == 5)"),
    P("¿Qué muestra este código?",
      "{'i': 2}",
      ["{'c': 1, 'i': 2}", "{'c': 1}", "{}"],
      "__dict__ de un objeto contiene solo sus atributos de instancia. Los atributos de clase "
      "(declarados fuera del constructor) no aparecen ahí: están en A.__dict__ y se ven con dir().",
      "class A:\n    c = 1\n\n    def __init__(self):\n        self.i = 2\n\na = A()\nprint(a.__dict__)"),
    P("¿Qué función built-in permite leer el valor de un atributo cuyo nombre está guardado en una cadena?",
      "getattr(objeto, nombre)",
      ["hasattr(objeto, nombre)", "dir(objeto, nombre)", "type(objeto, nombre)"],
      "getattr lee el atributo y setattr lo modifica (reflexión). hasattr solo comprueba si existe "
      "y devuelve True o False.",
      None,
      "class A:\n    x = 1\nprint(getattr(A(), 'x') == 1)"),
    # ------------------------------------------------ 04 Misceláneo
    P("¿Qué muestra este código? (la salida se muestra en una línea separando con ' / ' cada línea impresa)",
      "2 / 4 / 6 / 8 / 10",
      ["0 / 2 / 4 / 6 / 8 / 10", "2 / 4 / 6 / 8", "4 / 6 / 8 / 10"],
      "En cada llamada a __next__ el contador sube de 2 en 2 ANTES de comprobar el límite. "
      "Entrega 2, 4, 6, 8 y 10 (10 no es mayor que 10) y en el siguiente (12) lanza StopIteration.",
      "class Iterador:\n    def __init__(self, max):\n        self.contador = 0\n        self.max = max\n\n"
      "    def __iter__(self):\n        return self\n\n    def __next__(self):\n        self.contador += 2\n"
      "        if self.contador > self.max:\n            raise StopIteration\n        return self.contador\n\n"
      "for i in Iterador(10):\n    print(i)"),
    P("¿Qué muestra este código?",
      "generator [0, 2, 4, 6, 8]",
      ["list [0, 2, 4, 6, 8]", "tuple (0, 2, 4, 6, 8)", "generator [0, 2, 4, 6, 8, 10]"],
      "Sustituir los corchetes de una comprensión por paréntesis crea un generador, no una tupla. "
      "list(g) lo consume y obtiene los pares menores que 10.",
      "g = (n for n in range(10) if n % 2 == 0)\nprint(type(g).__name__, list(g))"),
    P("¿Qué muestra este código?",
      "['Anna', 'Pep', 'Iñaki']",
      ["['ANNA', 'PEP', 'IÑAKI']", "['anna', 'pep', 'iñaki']", "['Anna', 'Pep', 'IÑAKI']"],
      "map aplica la función lambda a cada elemento. capitalize() deja la primera letra en mayúscula "
      "y el resto en minúscula; list() es necesario para obtener los resultados.",
      "nombres = ['anna', 'pep', 'iñaki']\nprint(list(map(lambda n: n.capitalize(), nombres)))"),
    P("¿Qué muestra este código?",
      "['anna', 'iñaki', 'nicolás', 'lucía']",
      ["['anna', 'iñaki']", "['pep']", "['anna', 'pep', 'iñaki', 'nicolás', 'lucía']"],
      "filter se queda con los elementos para los que la función lambda devuelve True: los "
      "nombres de más de 3 letras. 'pep' tiene exactamente 3, así que se descarta.",
      "nombres = ['anna', 'pep', 'iñaki', 'nicolás', 'lucía']\n"
      "print(list(filter(lambda n: len(n) > 3, nombres)))"),
    P("¿Qué muestra este código?",
      "ESTEFANÍA",
      ["Estefanía", "ESTEFANIA", "<function externa.<locals>.interna>"],
      "externa() devuelve la función interna sin ejecutarla (es un cierre: recuerda su contexto). "
      "Al invocar funcion() se devuelve el nombre ya convertido a mayúsculas; upper() mantiene el acento.",
      "def externa(nombre):\n    nombre_mayusculas = nombre.upper()\n\n    def interna():\n"
      "        return nombre_mayusculas\n\n    return interna\n\nfuncion = externa('Estefanía')\nprint(funcion())"),
    P("¿Qué modo de apertura de open() exige que el archivo ya exista?",
      "'r' (lectura)",
      ["'w' (escritura)", "'a' (añadir)", "'x' (creación exclusiva)"],
      "'r' lanza FileNotFoundError si no existe. 'w' lo crea o lo trunca, y 'a' lo crea o se posiciona "
      "al final. ('x', por su parte, falla si el archivo YA existe.)",
      None,
      "try:\n    open('no_existe_jamas.txt', 'r')\nexcept FileNotFoundError:\n    print(True)"),
    P("¿Qué hace el método write() respecto a los saltos de línea?",
      "No añade ninguno: hay que escribir el '\\n' explícitamente",
      ["Añade un salto de línea al final de cada escritura", "Añade un salto de línea solo en Windows",
       "Añade un salto de línea cada vez que encuentra un espacio"],
      "write(cadena) escribe exactamente lo que le pases. (print, en cambio, sí añade un salto de línea.)",
      None,
      "with open('w.txt', 'w') as f:\n    f.write('a')\n    f.write('b')\nprint(open('w.txt').read() == 'ab')"),
    P("¿Qué diferencia hay entre os.makedirs('./d1/d2/d3') y os.mkdir('./d1/d2/d3')?",
      "makedirs crea también todos los directorios intermedios que falten",
      ["makedirs borra los directorios existentes antes de crearlos", "mkdir solo funciona en Windows",
       "No hay diferencia, son sinónimos"],
      "mkdir crea un único directorio (da error si el padre no existe o si ya existe: FileExistsError). "
      "makedirs crea toda la cadena de directorios de la ruta.",
      None,
      "import os\nos.makedirs('d1/d2/d3')\ntry:\n    os.mkdir('x1/x2/x3')\nexcept FileNotFoundError:\n    print(os.path.isdir('d1/d2/d3'))"),
    P("¿Qué muestra este código?",
      "2 3",
      ["3 2", "2 2", "3 3"],
      "El 21 de junio de 2023 fue miércoles. weekday() numera desde 0 = lunes (miércoles = 2) e "
      "isoweekday() desde 1 = lunes (miércoles = 3).",
      "from datetime import date\n\nd = date(2023, 6, 21)\nprint(d.weekday(), d.isoweekday())"),
    P("¿Qué muestra este código?",
      "1 False",
      ["2 True", "1 True", "0 False"],
      "calendar.weekday(2026, 11, 17) da 1 (martes, con 0 = lunes). 2100 NO es bisiesto: los años de "
      "siglo solo lo son si son divisibles entre 400.",
      "import calendar\n\nprint(calendar.weekday(2026, 11, 17), calendar.isleap(2100))"),
    P("¿Qué devuelve time.time()?",
      "Los segundos transcurridos desde el 1 de enero de 1970",
      ["La hora actual como texto", "Un objeto datetime con la fecha de hoy", "El número de segundos desde medianoche"],
      "Devuelve la marca de tiempo (timestamp): segundos desde la 'época Unix' (1/1/1970). Se puede "
      "convertir en fecha con date.fromtimestamp() o time.gmtime().",
      None,
      "import time\nprint(time.time() > 1.7e9)"),
]

DIFICIL = [
    # ------------------------------------------------ 01 Módulos, paquetes, PIP
    P("¿Qué muestra este código?",
      "False True",
      ["True True", "True False", "False False"],
      "Según los apuntes, log10(x) es más preciso que log(x, 10). Aquí log(1000, 10) da "
      "2.9999999999999996, que no es igual a 3, mientras que log10(1000) da exactamente 3.0.",
      "import math\n\nprint(math.log(1000, 10) == 3, math.log10(1000) == 3)",
      None),
    P("Quieres que Python busque tus módulos primero en la carpeta '/mis_mods'. ¿Qué haces?",
      "sys.path.insert(0, '/mis_mods')",
      ["sys.path.append('/mis_mods')", "sys.path = '/mis_mods'", "import '/mis_mods'"],
      "La búsqueda sigue el orden de la lista sys.path. append añade la ruta al FINAL (se busca la "
      "última); insert(0, ...) la coloca la primera.",
      None,
      "import sys\nsys.path.insert(0, '/a')\nsys.path.append('/b')\nprint(sys.path[0] == '/a' and sys.path[-1] == '/b')"),
    P("Un compañero te dice que uses 'pip search flask' para buscar paquetes. ¿Qué ocurre?",
      "No está soportado: hay que buscar en pypi.org desde un navegador",
      ["Funciona y muestra una lista de paquetes relacionados", "Instala flask automáticamente",
       "Muestra solo los paquetes ya instalados"],
      "Según los apuntes, 'pip search' ya no se soporta; la alternativa es https://pypi.org/search. "
      "Los paquetes instalados se ven con 'pip list'."),
    # ------------------------------------------------ 02 Cadenas, listas, excepciones
    P("¿Qué ocurre al ejecutar max('')?",
      "Se lanza ValueError porque la cadena está vacía",
      ["Devuelve una cadena vacía", "Devuelve None", "Se lanza IndexError"],
      "min() y max() se pueden aplicar a cadenas, pero la cadena no puede estar vacía: no hay "
      "ningún elemento que devolver y se produce ValueError.",
      None,
      "try:\n    max('')\nexcept ValueError:\n    print(True)"),
    P("¿Qué ocurre al ejecutar este código?",
      "Se lanza TypeError porque 2 no es una cadena",
      ["Muestra 1-2-3", "Muestra 1-2-3 con un aviso por el 2", "Se lanza ValueError"],
      "join() solo une cadenas. Si algún elemento de la secuencia no es str, Python lanza TypeError; "
      "no convierte nada automáticamente.",
      "print('-'.join(['1', 2, '3']))",
      "try:\n    '-'.join(['1', 2, '3'])\nexcept TypeError:\n    print(True)"),
    P("¿Qué muestra este código?",
      "3 10 2",
      ["1 10 2", "3 10 3", "3 11 2"],
      "'abracadabra': find('a', 1) busca desde la posición 1 y encuentra la 'a' del índice 3; "
      "rfind('a') busca desde el final (índice 10); count('abra') cuenta apariciones sin solaparse: "
      "una en el 0 y otra en el 7.",
      "s = 'abracadabra'\nprint(s.find('a', 1), s.rfind('a'), s.count('abra'))"),
    P("¿Qué muestra este código?",
      "['a', 'b;c'] hOLA mUNDO",
      ["['a', 'b', 'c'] hOLA mUNDO", "['a', 'b;c'] HOLA MUNDO", "['a', 'b;c'] Hola Mundo"],
      "split(',') solo divide por comas, así que 'b;c' queda entero. title() deja 'Hola Mundo' y "
      "swapcase() invierte mayúsculas y minúsculas: 'hOLA mUNDO'.",
      "print('a,b;c'.split(','), 'hola mundo'.title().swapcase())"),
    P("¿Qué muestra este código?",
      "['A', 'a', 'b', 'B']",
      ["['a', 'A', 'b', 'B']", "['A', 'B', 'a', 'b']", "['A', 'a', 'B', 'b']"],
      "Ordena por la clave en minúscula. Hay empates ('A' con 'a', y 'b' con 'B') y sorted() es "
      "ESTABLE: los empatados conservan su orden original, que era 'b', 'A', 'a', 'B'. "
      "Por eso 'A' va antes que 'a' y 'b' antes que 'B'.",
      "print(sorted(['b', 'A', 'a', 'B'], key=str.lower))"),
    P("¿Qué muestra este código?",
      "233 8",
      ["26 8", "233 10", "8 233"],
      "'2' + '3' * 2 es una concatenación: '3' * 2 es '33' y se une al '2': '233'. Con enteros, "
      "int('2') + int('3') * 2 es 2 + 6 = 8.",
      "print('2' + '3' * 2, int('2') + int('3') * 2)"),
    P("¿Qué muestra este código?",
      "ok",
      ["falla orden", "falla", "Un error"],
      "La aserción es verdadera: 'a' (97) es mayor que 'B' (66), porque las mayúsculas tienen "
      "puntos de código menores. Como no hay excepción, se ejecuta el else.",
      "try:\n    assert 'a' > 'B', 'orden'\nexcept AssertionError as e:\n    print('falla', e)\nelse:\n    print('ok')"),
    P("¿Qué muestra este código?",
      "L",
      ["I", "E", "L / E"],
      "Un diccionario lanza KeyError, que NO es IndexError (ambas cuelgan de LookupError). "
      "Python usa el primer except que encaja: el de IndexError no, el de LookupError sí, y ahí "
      "termina la captura.",
      "try:\n    {}['x']\nexcept IndexError:\n    print('I')\nexcept LookupError:\n    print('L')\n"
      "except Exception:\n    print('E')"),
    P("¿Qué muestra este código?",
      "('a', 2) 2",
      ["a 1", "('a', 2) 1", "['a', 2] 2"],
      "El atributo args de la excepción guarda TODOS los argumentos pasados al constructor, como "
      "una tupla: ('a', 2), que tiene 2 elementos.",
      "try:\n    raise ValueError('a', 2)\nexcept ValueError as e:\n    print(e.args, len(e.args))"),
    # ------------------------------------------------ 03 POO
    P("¿Qué ocurre al definir estas clases?",
      "Se lanza TypeError al definir C: no se puede construir un orden de resolución consistente",
      ["Funciona: C hereda primero de A y luego de B", "Funciona, pero C ignora a B",
       "Se lanza AttributeError al crear un objeto de C"],
      "Según los apuntes, si C hereda de A y B (en ese orden) y B hereda de A, se produce TypeError al "
      "definir la clase (MRO imposible). En el orden contrario, C(B, A), sí funciona.",
      "class A:\n    pass\n\nclass B(A):\n    pass\n\nclass C(A, B):\n    pass",
      "try:\n    class A:\n        pass\n    class B(A):\n        pass\n    class C(A, B):\n        pass\nexcept TypeError:\n    print(True)"),
    P("¿Qué muestra este código?",
      "False True True True",
      ["True True True True", "False False True True", "False True True False"],
      "Un atributo de clase está en A.__dict__ pero no en el __dict__ del objeto. Aun así el objeto "
      "puede acceder a él (hasattr es True), igual que la propia clase.",
      "class A:\n    c = 1\n\na = A()\nprint('c' in a.__dict__, 'c' in A.__dict__, hasattr(a, 'c'), hasattr(A, 'c'))"),
    P("¿Qué muestra este código?",
      "False True",
      ["True True", "False False", "True False"],
      "hasattr sobre una CLASE solo ve atributos de clase; el atributo 'i' se crea en el constructor, "
      "así que solo existe en las instancias. Aplicada a un objeto, sí lo encuentra.",
      "class A:\n    def __init__(self):\n        self.i = 1\n\nprint(hasattr(A, 'i'), hasattr(A(), 'i'))"),
    P("¿Qué muestra este código?",
      "A A False",
      ["A A True", "A None False", "A type False"],
      "__name__ solo es aplicable a la clase; para un objeto hay que usar type(objeto).__name__. "
      "El objeto 'a' no tiene el atributo __name__, así que hasattr devuelve False.",
      "class A:\n    pass\n\na = A()\nprint(A.__name__, type(a).__name__, hasattr(a, '__name__'))"),
    P("¿Qué muestra este código?",
      "True False True",
      ["True True True", "False False True", "True False False"],
      "== compara el contenido (a y b son iguales). 'is' compara identidad: a y b son dos listas "
      "distintas. c = a no copia nada: c y a son el mismo objeto.",
      "a = [1]\nb = [1]\nc = a\nprint(a == b, a is b, a is c)"),
    P("¿Qué muestra este código?",
      "ruedas False",
      ["ruedas True", "pistas False", "Un error"],
      "Es composición: Vehicle TIENE un controlador (no hereda de él). Delega en él la acción, por "
      "eso 'ruedas', y un Vehicle no es una instancia de Wheels.",
      "class Tracks:\n    def change(self):\n        return 'pistas'\n\nclass Wheels:\n    def change(self):\n"
      "        return 'ruedas'\n\nclass Vehicle:\n    def __init__(self, c):\n        self.c = c\n\n"
      "    def turn(self):\n        return self.c.change()\n\nv = Vehicle(Wheels())\nprint(v.turn(), isinstance(v, Wheels))"),
    P("¿Qué muestra este código?",
      "código 404 404 ('código 404',)",
      ["404 404 (404,)", "código 404 404 (404,)", "código 404 código 404 ('código 404',)"],
      "super().__init__(...) pasa a Exception un único argumento: el mensaje. Por eso str(e) es el "
      "mensaje y args es la tupla ('código 404',). El atributo propio 'codigo' conserva el 404.",
      "class MiError(Exception):\n    def __init__(self, codigo):\n        super().__init__(f'código {codigo}')\n"
      "        self.codigo = codigo\n\ntry:\n    raise MiError(404)\nexcept MiError as e:\n    print(e, e.codigo, e.args)"),
    # ------------------------------------------------ 04 Misceláneo
    P("¿Qué muestra este código?",
      "0 1 [2]",
      ["0 1 [0, 1, 2]", "0 1 [1, 2]", "0 1 []"],
      "Un generador recuerda por dónde iba. Tras dos next() ya se entregaron 0 y 1; list(x) consume "
      "lo que queda: solo el 2.",
      "def g():\n    for i in range(3):\n        yield i\n\nx = g()\nprint(next(x), next(x), list(x))"),
    P("¿Qué muestra este código?",
      "[1, 2, 3] []",
      ["[1, 2, 3] [1, 2, 3]", "[1, 2, 3] [4]", "[] []"],
      "Este iterador devuelve self en __iter__, así que no se reinicia: tras agotarlo con el primer "
      "list(), el segundo ya no tiene nada que entregar (su contador sigue por encima de 3).",
      "class It:\n    def __init__(self):\n        self.n = 0\n\n    def __iter__(self):\n        return self\n\n"
      "    def __next__(self):\n        self.n += 1\n        if self.n > 3:\n            raise StopIteration\n"
      "        return self.n\n\nit = It()\nprint(list(it), list(it))"),
    P("¿Qué muestra este código?",
      "['anna', 'iñaki', 'lucía']",
      ["['anna', 'iñaki', 'nicolás', 'lucía']", "['anna', 'iñaki']", "['anna', 'pep', 'iñaki', 'lucía']"],
      "Trampa de las tildes: 'nicolás' tiene 'á', que es un carácter distinto de 'a', así que "
      "'a' in 'nicolás' es False. 'lucía' sí tiene una 'a' (la última letra).",
      "nombres = ['anna', 'pep', 'iñaki', 'nicolás', 'lucía']\nprint(list(filter(lambda n: 'a' in n, nombres)))"),
    P("¿Qué muestra este código?",
      "4 10 4",
      ["4 10 10", "10 10 10", "4 10 8"],
      "Cada llamada a externa() crea su propio cierre, con su propio valor de n. f recuerda n = 2 y "
      "g recuerda n = 5; llamar a f varias veces no los mezcla.",
      "def externa(n):\n    def interna():\n        return n * 2\n    return interna\n\n"
      "f = externa(2)\ng = externa(5)\nprint(f(), g(), f())"),
    P("¿Qué muestra este código?",
      "['unodos\\n', 'tres']",
      ["['uno\\n', 'dos\\n', 'tres']", "['uno', 'dos', 'tres']", "['unodos', 'tres']"],
      "write() no añade saltos de línea: 'uno' y 'dos\\n' quedan pegados. Solo existe un salto "
      "(el que escribimos tras 'dos'), así que readlines() devuelve dos líneas, y la primera conserva "
      "su '\\n' al final.",
      "with open('t.txt', 'w') as f:\n    f.write('uno')\n    f.write('dos\\n')\n    f.write('tres')\n\n"
      "with open('t.txt') as f:\n    print(f.readlines())"),
    P("¿Qué excepciones se producen, respectivamente, con bytearray([300]) y bytearray(['a'])?",
      "ValueError y TypeError",
      ["TypeError y ValueError", "ValueError y ValueError", "OverflowError y TypeError"],
      "Un bytearray solo admite enteros entre 0 y 255. Un entero fuera de rango es ValueError; un "
      "valor que no es entero (como 'a') es TypeError.",
      None,
      "r = []\nfor v in ([300], ['a']):\n    try:\n        bytearray(v)\n    except Exception as e:\n        r.append(type(e).__name__)\nprint(r == ['ValueError', 'TypeError'])"),
    P("¿Qué muestra este código?",
      "1 9000",
      ["1 150", "26 1800", "1 2"],
      "timedelta solo guarda days, seconds y microseconds. 26 h 30 min son 1 día y 2 h 30 min = "
      "9000 segundos. No existe un atributo que guarde las horas aparte.",
      "from datetime import timedelta\n\nt = timedelta(hours=26, minutes=30)\nprint(t.days, t.seconds)"),
    P("¿Qué muestra este código?",
      "2024-03-01 60",
      ["2024-02-30 59", "2024-03-01 61", "2024-03-02 60"],
      "2024 es bisiesto: febrero tiene 29 días, así que el 28 de febrero + 2 días es el 1 de marzo. "
      "Restar fechas da un timedelta: del 1 de enero al 1 de marzo hay 31 + 29 = 60 días.",
      "from datetime import date, timedelta\n\nd = date(2024, 2, 28) + timedelta(days=2)\n"
      "print(d, (d - date(2024, 1, 1)).days)"),
    P("¿Qué muestra este código?",
      "[6, 0, 1, 2, 3, 4, 5] [1, 2, 3, 4, 5, 6, 7]",
      ["[0, 1, 2, 3, 4, 5, 6] [1, 2, 3, 4, 5, 6, 7]", "[6, 0, 1, 2, 3, 4, 5] [0, 0, 0, 0, 0, 0, 1]",
       "[0, 1, 2, 3, 4, 5, 6] [0, 0, 0, 0, 0, 0, 1]"],
      "Con el domingo como primer día, iterweekdays() empieza en 6. Además, el 1 de febrero de 2026 "
      "es domingo, así que la primera semana ya empieza en el día 1 y no hace falta rellenar con "
      "ceros (con el lunes como primer día sí habría seis ceros).",
      "import calendar\n\nc = calendar.Calendar(calendar.SUNDAY)\n"
      "print(list(c.iterweekdays()), list(c.itermonthdays(2026, 2))[:7])"),
    P("¿Qué excepciones lanzan os.rmdir() sobre un directorio NO vacío y sobre uno que NO existe, respectivamente?",
      "OSError y FileNotFoundError",
      ["FileExistsError y OSError", "FileNotFoundError y OSError", "PermissionError y FileNotFoundError"],
      "Según los apuntes: con un directorio no vacío se produce OSError (directorio no vacío) y con "
      "uno inexistente, FileNotFoundError (que, además, hereda de OSError).",
      None,
      "import os\nos.makedirs('d/s')\nr = []\nfor ruta in ('d', 'nada'):\n    try:\n        os.rmdir(ruta)\n    except OSError as e:\n        r.append(type(e).__name__)\nprint(r == ['OSError', 'FileNotFoundError'])"),
    P("¿Qué muestra este código? (la salida se muestra en una línea separando con ' / ' cada línea impresa)",
      "r ['a'] ['f.txt'] / a ['b'] ['g.txt'] / b [] []",
      ["r ['a'] ['f.txt'] / a ['b'] ['g.txt']", "r ['a', 'f.txt'] [] / a ['b', 'g.txt'] [] / b [] []",
       "b [] [] / a ['b'] ['g.txt'] / r ['a'] ['f.txt']"],
      "os.walk recorre el árbol de arriba abajo y por cada directorio entrega (ruta, subdirectorios, "
      "archivos). Se visitan 'r', 'r/a' y 'r/a/b', incluido el último directorio, que está vacío.",
      "import os\n\nos.makedirs('r/a/b')\nopen('r/f.txt', 'w').close()\nopen('r/a/g.txt', 'w').close()\n"
      "for root, dirs, files in os.walk('r'):\n    print(os.path.basename(root), dirs, files)"),
]

# ======================================================================
#  TRADUCCIÓN AL INGLÉS DEL BANCO DE PREGUNTAS
#  T(pregunta, explicación, correcta=None, incorrectas=None)
#  Si no se indican opciones, se conservan las originales (salidas de código).
#  Cada lista va en el mismo orden que NORMAL y DIFICIL.
# ======================================================================
def T(pregunta, explicacion, correcta=None, incorrectas=None):
    return (pregunta, correcta, incorrectas, explicacion)


EN_NORMAL = [
    T("In your script you define pi = 3 and you also import the math module. What does this code print?",
      "Each module has its own namespace. 'pi' is your script's variable and 'math.pi' is the constant "
      "from the math module: they coexist without conflict. If you don't prefix the module, Python uses "
      "your own name."),
    T("What does this code print?",
      "floor() returns the largest integer less than or equal to the number (-4); ceil() the smallest "
      "integer greater than or equal to it (-3); trunc() just drops the decimal part (-3). With negative "
      "numbers they don't coincide."),
    T("random.randrange(2, 10, 3) can only return...",
      "It works like range(start, stop, step): it starts at 2, goes up in steps of 3 and does NOT reach "
      "10. The possible values are 2, 5 and 8.",
      "2, 5 or 8",
      ["2, 5, 8 or 10", "Any integer between 2 and 10", "3, 6 or 9"]),
    T("According to the course notes, what is the relationship between randint(a, b) and randrange?",
      "randint includes both endpoints, whereas randrange excludes the end. That is why randint(a, b) is "
      "the same as randrange(a, b + 1).",
      "randint(a, b) is equivalent to randrange(a, b + 1)",
      ["randint(a, b) is equivalent to randrange(a, b)", "randint(a, b) is equivalent to randrange(a + 1, b)",
       "They are not related at all"]),
    T("When a module is imported, Python creates a __pycache__ folder. What does it contain?",
      ".pyc (compiled) files. Their name includes the module, the implementation and the Python version; "
      "for example, modulo2.cpython-311.pyc.",
      "Compiled .pyc files with the module's bytecode",
      ["Backup copies of your .py files", "The packages installed with pip",
       "A log of the errors raised during import"]),
    T("A module is imported from another module. What value does __name__ have inside the imported module?",
      "__name__ is '__main__' only in the module that is run directly. In an imported module it takes the "
      "module's name. That is why 'if __name__ == \"__main__\":' separates the code that should only run "
      "when the file is launched directly.",
      "The name of the module itself",
      ["'__main__'", "None", "The name of the script that imports it"]),
    T("Which variable of the sys module holds the (ordered) list of locations where Python looks for modules?",
      "The search follows the order of the sys.path list, which can include .zip files and can be modified "
      "with append (at the end) or insert (to change the order).",
      "sys.path",
      ["sys.modules", "sys.argv", "sys.paths"]),
    T("Which command shows information about an installed package, including its dependencies "
      "(Requires and Required-by)?",
      "'pip show package' displays name, version, author, website and dependencies in both directions. "
      "'pip list' only lists everything installed, and 'pip help' shows help for a command.",
      "pip show package",
      ["pip list package", "pip info package", "pip help package"]),
    T("What does this code print?",
      "len() counts ALL characters, including spaces, tabs and newlines: 'a', ' ', 'b', tab, 'c' and "
      "newline make 6."),
    T("What does this code print?",
      "Replication with * does not depend on the order (3 * 'ab' equals 'ab' * 3), and * has priority over "
      "+: 'ab' + ('c' * 2) gives 'abcc'."),
    T("What does this code print?",
      "Characters are compared by code point: uppercase letters are smaller than lowercase ones, so "
      "'Hola' < 'hola'. And if a string has the same characters as another plus an extra one, the longer "
      "one is greater."),
    T("What does this code print?",
      "capitalize() uppercases ONLY the first character and converts the rest to lowercase. "
      "(title() is the one that capitalizes every word.)"),
    T("What does this code print?",
      "Comparing a string with a number using == and != is allowed: they are never equal ('==' gives "
      "False and '!=' gives True). With >, <, >= or <= you would get a TypeError."),
    T("Which of these assertions raises AssertionError?",
      "assert only fails if the expression is false. A non-zero number, a non-empty string or a non-empty "
      "list (even one containing a 0) are considered true."),
    T("Which exception is a child of LookupError?",
      "IndexError and KeyError both derive from LookupError. OverflowError derives from ArithmeticError "
      "and KeyboardInterrupt directly from BaseException."),
    T("The class defines self.__saldo. What happens to that attribute?",
      "The notes call it private 'with a trick': Python renames it to _Class__attribute. It makes "
      "accidental access harder, but does not prevent it.",
      "It is still accessible from outside as object._Cuenta__saldo",
      ["It is completely inaccessible from outside", "It becomes a class attribute",
       "It is deleted when the constructor ends"]),
    T("How do you call the superclass constructor using super()?",
      "With super() you do not pass self (it is passed automatically). With the other form, "
      "Superclass.__init__(self), you do have to pass it explicitly.",
      "super().__init__(...), without passing self",
      ["super().__init__(self, ...)", "super.__init__(...)", "__super__.init(...)"]),
    T("What does this code print?",
      "An object's __dict__ contains only its instance attributes. Class attributes (declared outside the "
      "constructor) do not appear there: they are in A.__dict__ and show up with dir()."),
    T("Which built-in function reads the value of an attribute whose name is stored in a string?",
      "getattr reads the attribute and setattr modifies it (reflection). hasattr only checks whether it "
      "exists and returns True or False.",
      "getattr(object, name)",
      ["hasattr(object, name)", "dir(object, name)", "type(object, name)"]),
    T("What does this code print? (the output is shown on one line, separating each printed line with ' / ')",
      "On each call to __next__ the counter increases by 2 BEFORE the limit is checked. It yields 2, 4, 6, "
      "8 and 10 (10 is not greater than 10), and on the next call (12) it raises StopIteration."),
    T("What does this code print?",
      "Replacing the brackets of a comprehension with parentheses creates a generator, not a tuple. "
      "list(g) consumes it and obtains the even numbers below 10."),
    T("What does this code print?",
      "map applies the lambda function to each element. capitalize() leaves the first letter uppercase "
      "and the rest lowercase; list() is needed to get the results."),
    T("What does this code print?",
      "filter keeps the elements for which the lambda returns True: the names longer than 3 letters. "
      "'pep' has exactly 3, so it is discarded."),
    T("What does this code print?",
      "externa() returns the inner function without running it (it is a closure: it remembers its "
      "context). Calling funcion() returns the name already converted to uppercase; upper() keeps the accent."),
    T("Which open() mode requires the file to already exist?",
      "'r' raises FileNotFoundError if it does not exist. 'w' creates or truncates it, and 'a' creates it "
      "or positions at the end. ('x', on the other hand, fails if the file ALREADY exists.)",
      "'r' (read)",
      ["'w' (write)", "'a' (append)", "'x' (exclusive creation)"]),
    T("What does the write() method do about line breaks?",
      "write(string) writes exactly what you pass it. (print, on the other hand, does add a line break.)",
      "It adds none: you must write the '\\n' explicitly",
      ["It adds a line break at the end of every write", "It adds a line break only on Windows",
       "It adds a line break every time it finds a space"]),
    T("What is the difference between os.makedirs('./d1/d2/d3') and os.mkdir('./d1/d2/d3')?",
      "mkdir creates a single directory (error if the parent does not exist or if it already exists: "
      "FileExistsError). makedirs creates the whole chain of directories in the path.",
      "makedirs also creates all the missing intermediate directories",
      ["makedirs deletes existing directories before creating them", "mkdir only works on Windows",
       "There is no difference, they are synonyms"]),
    T("What does this code print?",
      "June 21, 2023 was a Wednesday. weekday() numbers from 0 = Monday (Wednesday = 2) and isoweekday() "
      "from 1 = Monday (Wednesday = 3)."),
    T("What does this code print?",
      "calendar.weekday(2026, 11, 17) gives 1 (Tuesday, with 0 = Monday). 2100 is NOT a leap year: "
      "century years are only leap years if they are divisible by 400."),
    T("What does time.time() return?",
      "It returns the timestamp: seconds since the Unix 'epoch' (1/1/1970). It can be converted to a date "
      "with date.fromtimestamp() or time.gmtime().",
      "The seconds elapsed since January 1, 1970",
      ["The current time as text", "A datetime object with today's date",
       "The number of seconds since midnight"]),
]

EN_DIFICIL = [
    T("What does this code print?",
      "According to the notes, log10(x) is more accurate than log(x, 10). Here log(1000, 10) gives "
      "2.9999999999999996, which is not equal to 3, whereas log10(1000) gives exactly 3.0."),
    T("You want Python to look for your modules first in the folder '/mis_mods'. What do you do?",
      "The search follows the order of the sys.path list. append adds the path at the END (it is searched "
      "last); insert(0, ...) puts it first."),
    T("A classmate tells you to use 'pip search flask' to look for packages. What happens?",
      "According to the notes, 'pip search' is no longer supported; the alternative is "
      "https://pypi.org/search. Installed packages are listed with 'pip list'.",
      "It is not supported: you have to search on pypi.org from a browser",
      ["It works and shows a list of related packages", "It installs flask automatically",
       "It only shows the packages already installed"]),
    T("What happens when you run max('')?",
      "min() and max() can be applied to strings, but the string cannot be empty: there is no element to "
      "return and a ValueError is raised.",
      "ValueError is raised because the string is empty",
      ["It returns an empty string", "It returns None", "IndexError is raised"]),
    T("What happens when this code runs?",
      "join() only joins strings. If any element of the sequence is not a str, Python raises TypeError; "
      "it does not convert anything automatically.",
      "TypeError is raised because 2 is not a string",
      ["It prints 1-2-3", "It prints 1-2-3 with a warning about the 2", "ValueError is raised"]),
    T("What does this code print?",
      "'abracadabra': find('a', 1) searches from position 1 and finds the 'a' at index 3; rfind('a') "
      "searches from the end (index 10); count('abra') counts non-overlapping occurrences: one at 0 and "
      "another at 7."),
    T("What does this code print?",
      "split(',') only splits on commas, so 'b;c' stays whole. title() gives 'Hola Mundo' and swapcase() "
      "swaps upper and lower case: 'hOLA mUNDO'."),
    T("What does this code print?",
      "It sorts by the lowercase key. There are ties ('A' with 'a', and 'b' with 'B') and sorted() is "
      "STABLE: tied elements keep their original order, which was 'b', 'A', 'a', 'B'. That is why 'A' "
      "comes before 'a' and 'b' before 'B'."),
    T("What does this code print?",
      "'2' + '3' * 2 is a concatenation: '3' * 2 is '33' and it is joined to '2': '233'. With integers, "
      "int('2') + int('3') * 2 is 2 + 6 = 8."),
    T("What does this code print?",
      "The assertion is true: 'a' (97) is greater than 'B' (66), because uppercase letters have smaller "
      "code points. Since there is no exception, the else block runs."),
    T("What does this code print?",
      "A dictionary raises KeyError, which is NOT IndexError (both derive from LookupError). Python uses "
      "the first except that matches: the IndexError one does not, the LookupError one does, and the "
      "handling ends there."),
    T("What does this code print?",
      "The args attribute of the exception stores ALL the arguments passed to the constructor, as a "
      "tuple: ('a', 2), which has 2 elements."),
    T("What happens when these classes are defined?",
      "According to the notes, if C inherits from A and B (in that order) and B inherits from A, a "
      "TypeError occurs when the class is defined (impossible MRO). In the opposite order, C(B, A), it works.",
      "TypeError is raised when defining C: a consistent method resolution order cannot be built",
      ["It works: C inherits first from A and then from B", "It works, but C ignores B",
       "AttributeError is raised when creating an object of C"]),
    T("What does this code print?",
      "A class attribute is in A.__dict__ but not in the object's __dict__. Even so, the object can "
      "access it (hasattr is True), just like the class itself."),
    T("What does this code print?",
      "hasattr on a CLASS only sees class attributes; the attribute 'i' is created in the constructor, so "
      "it only exists in instances. Applied to an object, it does find it."),
    T("What does this code print?",
      "__name__ is only applicable to the class; for an object you must use type(object).__name__. The "
      "object 'a' does not have the __name__ attribute, so hasattr returns False."),
    T("What does this code print?",
      "== compares content (a and b are equal). 'is' compares identity: a and b are two different lists. "
      "c = a copies nothing: c and a are the same object."),
    T("What does this code print?",
      "This is composition: Vehicle HAS a controller (it does not inherit from it). It delegates the "
      "action to it, hence 'ruedas', and a Vehicle is not an instance of Wheels."),
    T("What does this code print?",
      "super().__init__(...) passes Exception a single argument: the message. That is why str(e) is the "
      "message and args is the tuple ('código 404',). The custom attribute 'codigo' keeps the 404."),
    T("What does this code print?",
      "A generator remembers where it was. After two next() calls, 0 and 1 have already been yielded; "
      "list(x) consumes what is left: only the 2."),
    T("What does this code print?",
      "This iterator returns self in __iter__, so it is not reset: after exhausting it with the first "
      "list(), the second has nothing left to give (its counter is still above 3)."),
    T("What does this code print?",
      "Accent trap: 'nicolás' has 'á', which is a different character from 'a', so 'a' in 'nicolás' is "
      "False. 'lucía' does have an 'a' (its last letter)."),
    T("What does this code print?",
      "Each call to externa() creates its own closure, with its own value of n. f remembers n = 2 and g "
      "remembers n = 5; calling f several times does not mix them up."),
    T("What does this code print?",
      "write() does not add line breaks: 'uno' and 'dos\\n' end up stuck together. There is only one line "
      "break (the one we wrote after 'dos'), so readlines() returns two lines, and the first keeps its "
      "'\\n' at the end."),
    T("Which exceptions are raised, respectively, by bytearray([300]) and bytearray(['a'])?",
      "A bytearray only accepts integers between 0 and 255. An integer out of range is ValueError; a "
      "value that is not an integer (like 'a') is TypeError.",
      "ValueError and TypeError",
      ["TypeError and ValueError", "ValueError and ValueError", "OverflowError and TypeError"]),
    T("What does this code print?",
      "timedelta only stores days, seconds and microseconds. 26 h 30 min is 1 day and 2 h 30 min = 9000 "
      "seconds. There is no attribute that stores the hours separately."),
    T("What does this code print?",
      "2024 is a leap year: February has 29 days, so February 28 + 2 days is March 1. Subtracting dates "
      "gives a timedelta: from January 1 to March 1 there are 31 + 29 = 60 days."),
    T("What does this code print?",
      "With Sunday as the first day, iterweekdays() starts at 6. Also, February 1, 2026 is a Sunday, so "
      "the first week already starts on day 1 and no zero padding is needed (with Monday as the first day "
      "there would be six zeros)."),
    T("Which exceptions do os.rmdir() raise on a NON-empty directory and on one that does NOT exist, "
      "respectively?",
      "According to the notes: a non-empty directory raises OSError (directory not empty) and a "
      "non-existent one raises FileNotFoundError (which also inherits from OSError).",
      "OSError and FileNotFoundError",
      ["FileExistsError and OSError", "FileNotFoundError and OSError",
       "PermissionError and FileNotFoundError"]),
    T("What does this code print? (the output is shown on one line, separating each printed line with ' / ')",
      "os.walk traverses the tree from the top down and for each directory yields (path, subdirectories, "
      "files). The directories 'r', 'r/a' and 'r/a/b' are visited, including the last one, which is empty."),
]


def traducir(banco, textos):
    """Devuelve una copia del banco con los textos traducidos (el código no cambia)."""
    assert len(banco) == len(textos), "el banco y su traducción deben tener la misma longitud"
    resultado = []
    for p, (pregunta, correcta, incorrectas, explicacion) in zip(banco, textos):
        n = dict(p)
        n["pregunta"] = pregunta
        n["explicacion"] = explicacion
        if correcta is not None:
            n["correcta"] = correcta
            n["incorrectas"] = list(incorrectas)
        resultado.append(n)
    return resultado


BANCOS = {
    "es": {"1": NORMAL, "2": DIFICIL},
    "en": {"1": traducir(NORMAL, EN_NORMAL), "2": traducir(DIFICIL, EN_DIFICIL)},
}
NOMBRES_NIVEL = {
    "es": {"1": "NORMAL", "2": "DIFÍCIL"},
    "en": {"1": "NORMAL", "2": "HARD"},
}


# ======================================================================
#  TEXTOS DE LA INTERFAZ
# ======================================================================
TEXTOS = {
    "es": {
        "menu_titulo": "EXÁMENES DE PYTHON · TEMARIO DEL PROFESOR",
        "menu_elige": "Elige la dificultad (todos los exámenes mezclan todos los temas):",
        "menu_normal": "1) Normal    (30 preguntas)",
        "menu_dificil": "2) Difícil   (30 preguntas · más enrevesadas y con trampa)",
        "menu_idioma": "3) Idioma / Language  (ahora: Español)",
        "menu_salir": "4) Salir",
        "menu_mejores": "Mejores resultados de esta sesión:",
        "prompt_opcion": "Opción (1-4): ",
        "opcion_invalida": "Opción no válida. Escribe 1, 2, 3 o 4.",
        "adios": "¡Mucho ánimo con el curso!",
        "hasta_pronto": "Hasta pronto.",
        "exam_titulo": "EXAMEN NIVEL {nivel}  ·  {n} preguntas",
        "exam_intro": "Responde con la letra de la opción. Al contestar verás si has acertado y por qué.",
        "pregunta": "Pregunta {i} de {n}",
        "prompt_resp": "Tu respuesta (a/b/c/d, o 's' para salir del examen): ",
        "resp_invalida": "Respuesta no válida. Escribe a, b, c o d.",
        "abandono": "Examen abandonado. No se calcula puntuación.",
        "correcto": "✔ ¡CORRECTO!",
        "incorrecto": "✘ INCORRECTO. Elegiste {e}) y la respuesta correcta era {c}).",
        "razon": "Razón: ",
        "llevas": "Llevas {a} {palabra} de {i}.",
        "acierto": "acierto",
        "aciertos": "aciertos",
        "enter_cont": "[Enter para continuar]",
        "enter_menu": "[Enter para volver al menú]",
        "res_titulo": "RESULTADO · NIVEL {nivel}",
        "res_aciertos": "Aciertos : {a} de {n}",
        "res_fallos": "Fallos   : {f}",
        "res_punt": "Puntuación: ",
        "repaso": "Repaso de las preguntas falladas:",
        "preg_n": "Pregunta {i}: ",
        "resp_correcta": "→ Respuesta correcta: ",
        "val90": "¡Excelente! Dominas el temario de este nivel.",
        "val70": "Muy bien. Repasa solo los detalles que has fallado.",
        "val50": "Aprobado, pero conviene repasar los apuntes de las preguntas falladas.",
        "val0": "Todavía no. Vuelve a los apuntes del profesor y repite el examen.",
    },
    "en": {
        "menu_titulo": "PYTHON EXAMS · TEACHER'S SYLLABUS",
        "menu_elige": "Choose the difficulty (every exam mixes all the topics):",
        "menu_normal": "1) Normal    (30 questions)",
        "menu_dificil": "2) Hard      (30 questions · trickier and more convoluted)",
        "menu_idioma": "3) Idioma / Language  (now: English)",
        "menu_salir": "4) Quit",
        "menu_mejores": "Best results this session:",
        "prompt_opcion": "Option (1-4): ",
        "opcion_invalida": "Invalid option. Type 1, 2, 3 or 4.",
        "adios": "Good luck with the course!",
        "hasta_pronto": "See you soon.",
        "exam_titulo": "{nivel} LEVEL EXAM  ·  {n} questions",
        "exam_intro": "Answer with the letter of the option. After answering you will see whether "
                      "you were right and why.",
        "pregunta": "Question {i} of {n}",
        "prompt_resp": "Your answer (a/b/c/d, or 'q' to quit the exam): ",
        "resp_invalida": "Invalid answer. Type a, b, c or d.",
        "abandono": "Exam abandoned. No score is calculated.",
        "correcto": "✔ CORRECT!",
        "incorrecto": "✘ WRONG. You chose {e}) and the correct answer was {c}).",
        "razon": "Reason: ",
        "llevas": "You have {a} correct {palabra} out of {i}.",
        "acierto": "answer",
        "aciertos": "answers",
        "enter_cont": "[Press Enter to continue]",
        "enter_menu": "[Press Enter to go back to the menu]",
        "res_titulo": "RESULT · {nivel} LEVEL",
        "res_aciertos": "Correct : {a} out of {n}",
        "res_fallos": "Wrong   : {f}",
        "res_punt": "Score: ",
        "repaso": "Review of the questions you got wrong:",
        "preg_n": "Question {i}: ",
        "resp_correcta": "→ Correct answer: ",
        "val90": "Excellent! You have mastered this level.",
        "val70": "Very good. Just review the details you missed.",
        "val50": "Passed, but you should review the notes for the questions you missed.",
        "val0": "Not yet. Go back to the teacher's notes and retake the exam.",
    },
}

IDIOMA = "es"


def t(clave, **datos):
    texto = TEXTOS[IDIOMA][clave]
    return texto.format(**datos) if datos else texto


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


def verde(x):
    return pintar(x, "92")


def rojo(x):
    return pintar(x, "91")


def amarillo(x):
    return pintar(x, "93")


def azul(x):
    return pintar(x, "96")


def tenue(x):
    return pintar(x, "90")


def negrita(x):
    return pintar(x, "1")


def linea(caracter="=", ancho=ANCHO):
    return caracter * ancho


def envolver(texto, sangria="", resto=None, ancho=ANCHO):
    return textwrap.fill(texto, width=ancho, initial_indent=sangria,
                         subsequent_indent=sangria if resto is None else resto)


def leer(mensaje):
    """input() que trata Ctrl+D / Ctrl+C como una salida limpia."""
    try:
        return input(mensaje)
    except (EOFError, KeyboardInterrupt):
        print("\n\n" + t("hasta_pronto"))
        sys.exit(0)


def preparar_pregunta(p):
    """Baraja las opciones y devuelve (lista de opciones, índice de la correcta)."""
    opciones = [p["correcta"]] + list(p["incorrectas"])
    random.shuffle(opciones)
    return opciones, opciones.index(p["correcta"])


def mostrar_pregunta(numero, total, p, opciones):
    print()
    print(azul(linea("-")))
    print(negrita(t("pregunta", i=numero, n=total)))
    print(envolver(p["pregunta"]))
    if p["codigo"]:
        print()
        for fila in p["codigo"].split("\n"):
            print(tenue("  | ") + fila)
    print()
    for letra, texto in zip(LETRAS, opciones):
        print(envolver(f"{letra}) {texto}", sangria="  ", resto="     "))
    print()


def pedir_respuesta():
    """Devuelve 0-3 o None si el usuario quiere abandonar el examen."""
    while True:
        r = leer(t("prompt_resp")).strip().lower()
        if r in ("s", "q", "salir", "quit"):
            return None
        if r in ("1", "2", "3", "4"):
            return int(r) - 1
        if r in tuple(LETRAS):
            return LETRAS.index(r)
        print(amarillo("  " + t("resp_invalida")))


def valoracion(porcentaje):
    if porcentaje >= 90:
        return t("val90")
    if porcentaje >= 70:
        return t("val70")
    if porcentaje >= 50:
        return t("val50")
    return t("val0")


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
    print(negrita(t("exam_titulo", nivel=nombre, n=total)))
    print(linea("="))
    print(t("exam_intro"))

    for numero, p in enumerate(preguntas, start=1):
        opciones, correcta = preparar_pregunta(p)
        mostrar_pregunta(numero, total, p, opciones)
        r = pedir_respuesta()
        if r is None:
            print(amarillo("\n" + t("abandono")))
            return None

        if r == correcta:
            aciertos += 1
            print(verde(t("correcto")))
        else:
            fallos.append((numero, p))
            print(rojo(t("incorrecto", e=LETRAS[r], c=LETRAS[correcta])))
        print(envolver(t("razon") + p["explicacion"], sangria="  "))
        palabra = t("acierto") if aciertos == 1 else t("aciertos")
        print(tenue("  " + t("llevas", a=aciertos, palabra=palabra, i=numero)))
        if numero < total:
            leer("\n" + tenue(t("enter_cont")))

    mostrar_resultado(nombre, aciertos, total, fallos)
    return aciertos / total * 100


def mostrar_resultado(nombre, aciertos, total, fallos):
    porcentaje = aciertos / total * 100
    print()
    print(linea("="))
    print(negrita(t("res_titulo", nivel=nombre)))
    print(linea("="))
    print("  " + t("res_aciertos", a=aciertos, n=total))
    print("  " + t("res_fallos", f=total - aciertos))
    color = verde if porcentaje >= 70 else (amarillo if porcentaje >= 50 else rojo)
    print("  " + t("res_punt") + color(negrita(f"{porcentaje:.1f} %")))
    print()
    print(envolver(valoracion(porcentaje), sangria="  "))

    if fallos:
        print()
        print(negrita(t("repaso")))
        for numero, p in fallos:
            print()
            print(envolver(t("preg_n", i=numero) + p["pregunta"], sangria="  ", resto="     "))
            if p["codigo"]:
                for fila in p["codigo"].split("\n"):
                    print(tenue("     | ") + fila)
            print(envolver(t("resp_correcta") + p["correcta"], sangria="     ", resto="       "))


# ======================================================================
#  IDIOMA Y MENÚ
# ======================================================================
def elegir_idioma():
    global IDIOMA
    print()
    print(linea("="))
    print(negrita("  Idioma / Language"))
    print(linea("="))
    print("    1) Español")
    print("    2) English")
    print()
    while True:
        r = leer("Idioma / Language (1-2): ").strip().lower()
        if r in ("1", "es", "español", "espanol"):
            IDIOMA = "es"
            return
        if r in ("2", "en", "english", "inglés", "ingles"):
            IDIOMA = "en"
            return
        print(amarillo("  1 = Español, 2 = English"))


def mostrar_menu(historial):
    print()
    print(linea("="))
    print(negrita("  " + t("menu_titulo")))
    print(linea("="))
    print("  " + t("menu_elige"))
    print()
    for clave in ("menu_normal", "menu_dificil", "menu_idioma", "menu_salir"):
        print("    " + t(clave))
    if historial:
        print()
        print(tenue("  " + t("menu_mejores")))
        for clave in sorted(historial):
            print(tenue(f"    {NOMBRES_NIVEL[IDIOMA][clave]:<8} {historial[clave]:.1f} %"))
    print()


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    elegir_idioma()
    historial = {}
    while True:
        mostrar_menu(historial)
        opcion = leer(t("prompt_opcion")).strip()
        if opcion == "4":
            print("\n" + t("adios"))
            return
        if opcion == "3":
            elegir_idioma()
            continue
        if opcion not in ("1", "2"):
            print(amarillo("  " + t("opcion_invalida")))
            continue

        resultado = hacer_examen(NOMBRES_NIVEL[IDIOMA][opcion], BANCOS[IDIOMA][opcion])
        if resultado is not None:
            historial[opcion] = max(resultado, historial.get(opcion, 0))
        leer("\n" + tenue(t("enter_menu")))


if __name__ == "__main__":
    main()

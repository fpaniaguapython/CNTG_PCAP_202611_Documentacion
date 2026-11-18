#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test interactivo de 60 preguntas sobre los métodos is...() de Python."""

from datetime import datetime
import random
import os

# Formato: (enunciado, [cuatro opciones], índice de la respuesta correcta)
PREGUNTAS = {
"fácil": [
("¿Qué devuelve 'Hola'.isalpha()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve 'Python3'.isalnum()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve '12345'.isdigit()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve '   '.isspace()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve 'python'.islower()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve 'PYTHON'.isupper()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve 'Hola mundo'.isalpha()?", ["True","False","None","Da error"], 1),
("¿Qué devuelve 'usuario_1'.isalnum()?", ["True","False","None","Da error"], 1),
("¿Qué devuelve ''.isalpha()?", ["True","False","None","Da error"], 1),
("¿Qué método comprueba que todos los caracteres sean letras?", ["isalpha()","isalnum()","isspace()","isupper()"], 0),
("¿Qué método comprueba que todos los caracteres sean letras o números?", ["isdigit()","isalnum()","islower()","isdecimal()"], 1),
("¿Qué método comprueba si una cadena contiene únicamente espacios en blanco?", ["isalpha()","isnumeric()","isspace()","isupper()"], 2),
("¿Qué método comprueba si las letras de una cadena están en minúsculas?", ["islower()","isupper()","isdigit()","isdecimal()"], 0),
("¿Qué método comprueba si las letras de una cadena están en mayúsculas?", ["isalnum()","isalpha()","islower()","isupper()"], 3),
("¿Qué devuelve 'A7'.isalpha()?", ["True","False","None","Da error"], 1),
("¿Qué devuelve 'A7'.isalnum()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve '42'.isnumeric()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve '  a  '.isspace()?", ["True","False","None","Da error"], 1),
("¿Qué devuelve 'Python'.isupper()?", ["True","False","None","Da error"], 1),
("¿Qué tipo de dato devuelve un método como isdigit()?", ["str","int","bool","float"], 2),
],
"medio": [
("¿Qué devuelve '2025'.isdecimal()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve '²'.isdigit() en Python?", ["True","False","None","Da error"], 0),
("¿Qué devuelve '²'.isdecimal() en Python?", ["True","False","None","Da error"], 1),
("¿Qué devuelve '½'.isnumeric() en Python?", ["True","False","None","Da error"], 0),
("¿Qué devuelve '½'.isdigit() en Python?", ["True","False","None","Da error"], 1),
("¿Cuál es la relación correcta entre isdecimal(), isdigit() e isnumeric()?", ["isnumeric() acepta el conjunto más amplio","isdecimal() acepta el conjunto más amplio","Los tres aceptan exactamente lo mismo","isdigit() solo acepta letras"], 0),
("¿Qué devuelve 'Málaga'.isalpha()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve 'ABC 123'.isalnum()?", ["True","False","None","Da error"], 1),
("¿Qué devuelve '\\t\\n'.isspace()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve '123!'.isupper()?", ["True","False","None","Da error"], 1),
("¿Qué devuelve '123!'.islower()?", ["True","False","None","Da error"], 1),
("¿Qué resultado produce 'abc'.isalpha() and '123'.isdecimal()?", ["True","False","None","Da error"], 0),
("¿Qué resultado produce 'abc123'.isalpha() or 'abc123'.isalnum()?", ["True","False","None","Da error"], 0),
("¿Qué resultado produce not '   '.isspace()?", ["True","False","None","Da error"], 1),
("¿Qué condición comprueba que clave tenga solo letras y números?", ["clave.isalpha()","clave.isalnum()","clave.isspace()","clave.isupper()"], 1),
("¿Qué devuelve 'ÉXITO'.isupper()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve 'ß'.islower()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve 'abc123'.islower()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve '123'.islower()?", ["True","False","None","Da error"], 1),
("¿Qué devuelve el método isdecimal() de Python al aplicarlo a la cadena '１２３', formada por dígitos decimales Unicode de ancho completo (Fullwidth)?", ["True","False","None","Da error"], 0),
],
"alto": [
("¿Qué devuelve 'Ⅳ'.isnumeric() en Python?", ["True","False","None","Da error"], 0),
("¿Qué devuelve 'Ⅳ'.isdigit() en Python?", ["True","False","None","Da error"], 1),
("¿Qué devuelve '四'.isnumeric() en Python?", ["True","False","None","Da error"], 0),
("¿Qué devuelve '四'.isdecimal() en Python?", ["True","False","None","Da error"], 1),
("¿Qué devuelve '²'.isnumeric() en Python?", ["True","False","None","Da error"], 0),
("¿Qué devuelve '²'.isdecimal() or '²'.isdigit()?", ["True","False","None","Da error"], 0),
("¿Qué devuelve '⅕'.isnumeric() and not '⅕'.isdigit()?", ["True","False","None","Da error"], 0),
("¿Qué resultado produce 'abc'.islower() and 'ABC'.isupper()?", ["True","False","None","Da error"], 0),
("¿Qué resultado produce 'abc123'.isalpha() or 'abc123'.isdigit()?", ["True","False","None","Da error"], 1),
("¿Qué resultado produce 'abc123'.isalnum() and not 'abc123'.isspace()?", ["True","False","None","Da error"], 0),
("¿Cuál es la forma correcta de exigir que una cadena no esté vacía y contenga solo letras?", ["texto.isalpha() or bool(texto)","bool(texto) and texto.isalpha()","not texto.isalpha()","texto.isspace() and bool(texto)"], 1),
("¿Qué hace esta condición: s.isalpha() and s.islower()?", ["Exige solo letras y que estén en minúscula","Exige letras y números en minúscula","Exige que s esté vacía","Exige solo mayúsculas"], 0),
("¿Qué hace esta condición: s.isdecimal() or s.isalpha()?", ["Acepta solo letras o solo dígitos decimales","Acepta cualquier cadena alfanumérica","Acepta espacios y signos","Acepta necesariamente una mezcla de letras y cifras"], 0),
("¿Qué devuelve all(c.isalpha() for c in 'Casa')?", ["True","False","None","Da error"], 0),
("¿Qué devuelve any(c.isdigit() for c in 'A7B')?", ["True","False","None","Da error"], 0),
("¿Qué devuelve all(c.isalnum() for c in 'A_7')?", ["True","False","None","Da error"], 1),
("¿Qué expresión permite letras, números o guion bajo y rechaza la cadena vacía?", ["all(c.isalnum() or c == '_' for c in s)","bool(s) and all(c.isalnum() or c == '_' for c in s)","s.isalpha() or s.isdigit()","s.isspace()"], 1),
("¿Qué devuelve 'abc\\u00a0'.isspace()?", ["True","False","None","Da error"], 1),
("¿Qué devuelve 'İ'.isupper()?", ["True","False","None","Da error"], 0),
("Una contraseña debe tener al menos 8 caracteres, una letra y un dígito. ¿Qué comprueba si contiene algún dígito decimal?", ["any(c.isdecimal() for c in clave)","clave.isdecimal()","clave.isdigit() and clave.isalpha()","all(c.isdecimal() for c in clave)"], 0),
]
}

def elegir_nivel():
    print("\n=== CUESTIONARIO: MÉTODOS is...() DE PYTHON ===")
    print("1. Fácil    (20 preguntas)")
    print("2. Medio    (20 preguntas)")
    print("3. Alto     (20 preguntas)")
    print("4. Completo (60 preguntas)")
    niveles = {"1": "fácil", "2": "medio", "3": "alto", "4": "completo"}
    while True:
        opcion = input("Elige una opción (1-4): ").strip()
        if opcion in niveles:
            return niveles[opcion]
        print("Opción no válida. Introduce 1, 2, 3 o 4.")

def obtener_preguntas(nivel):
    if nivel == "completo":
        resultado = []
        for nombre in ("fácil", "medio", "alto"):
            resultado.extend((nombre, p) for p in PREGUNTAS[nombre])
        return resultado
    return [(nivel, p) for p in PREGUNTAS[nivel]]

def guardar_resultados(nivel, aciertos, total, detalle):
    ahora = datetime.now()
    marca = ahora.strftime("%Y%m%d_%H%M%S")
    nombre = f"resultados_test_is_{marca}.txt"
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), nombre)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("RESULTADOS DEL CUESTIONARIO: MÉTODOS is...()\n")
        f.write("=" * 48 + "\n")
        f.write(f"Fecha y hora: {ahora.strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write(f"Nivel: {nivel.capitalize()}\n")
        f.write(f"Aciertos: {aciertos}/{total}\n")
        f.write(f"Errores: {total-aciertos}\n")
        f.write(f"Porcentaje: {aciertos/total*100:.1f}%\n\n")
        f.write("DETALLE DE RESPUESTAS\n" + "-" * 48 + "\n")
        for n, enunciado, elegida, correcta, bien in detalle:
            f.write(f"\n{n}. {'CORRECTA' if bien else 'INCORRECTA'}\n")
            f.write(enunciado + "\n")
            f.write(f"Tu respuesta: {elegida}\n")
            f.write(f"Respuesta correcta: {correcta}\n")
    return ruta

def ejecutar(nivel):
    preguntas = obtener_preguntas(nivel)
    random.shuffle(preguntas)
    aciertos = 0
    detalle = []
    print(f"\nNivel {nivel.upper()}: {len(preguntas)} preguntas.")
    print("Escribe 1, 2, 3 o 4 para responder.\n")

    for numero, (nivel_origen, pregunta) in enumerate(preguntas, 1):
        enunciado, opciones, indice_correcto = pregunta
        mezcladas = list(enumerate(opciones))
        random.shuffle(mezcladas)
        correcta_pos = next(i for i, par in enumerate(mezcladas)
                            if par[0] == indice_correcto)

        print("-" * 68)
        etiqueta = f" [{nivel_origen.upper()}]" if nivel == "completo" else ""
        print(f"Pregunta {numero}/{len(preguntas)}{etiqueta}")
        print(enunciado)
        for i, (_, opcion) in enumerate(mezcladas, 1):
            print(f"  {i}. {opcion}")

        while True:
            respuesta = input("Tu respuesta: ").strip()
            if respuesta in ("1", "2", "3", "4"):
                break
            print("Respuesta no válida. Escribe 1, 2, 3 o 4.")

        elegida = mezcladas[int(respuesta)-1][1]
        correcta = mezcladas[correcta_pos][1]
        bien = int(respuesta)-1 == correcta_pos
        if bien:
            aciertos += 1
            print("¡Correcto!\n")
        else:
            print(f"Incorrecto. La respuesta correcta era: {correcta}\n")
        detalle.append((numero, enunciado, elegida, correcta, bien))

    total = len(preguntas)
    porcentaje = aciertos / total * 100
    print("\n" + "=" * 48)
    print("RESULTADOS FINALES")
    print("=" * 48)
    print(f"Nivel realizado: {nivel.capitalize()}")
    print(f"Aciertos: {aciertos} de {total}")
    print(f"Errores: {total-aciertos}")
    print(f"Porcentaje: {porcentaje:.1f}%")
    if porcentaje >= 90:
        print("Valoración: Excelente dominio.")
    elif porcentaje >= 70:
        print("Valoración: Buen trabajo. Sigue practicando.")
    elif porcentaje >= 50:
        print("Valoración: Vas progresando; repasa los métodos.")
    else:
        print("Valoración: Conviene repasar el tema y volver a intentarlo.")

    ruta = guardar_resultados(nivel, aciertos, total, detalle)
    print(f"\nResultados guardados en:\n{ruta}")

def comprobar_banco():
    for nivel, preguntas in PREGUNTAS.items():
        assert len(preguntas) == 20, f"El nivel {nivel} debe tener 20 preguntas."
        for pregunta in preguntas:
            assert len(pregunta[1]) == 4 and 0 <= pregunta[2] < 4

def main():
    comprobar_banco()
    ejecutar(elegir_nivel())

if __name__ == "__main__":
    main()

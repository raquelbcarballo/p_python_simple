import sys
import os
import json


def path_assignment(assignment_name):
    current_dir = os.path.dirname(__file__)
    root_dir = os.path.join(current_dir, "..", "..")
    assignment_path = os.path.join(root_dir, assignment_name)
    return os.path.abspath(assignment_path)


PATH_ASSIGNMENT = path_assignment("p_calculadora")

sys.path.append(PATH_ASSIGNMENT)

from calculadora import divide, suma, resta, multiplica


def test_suma():
    """Test para verificar la función suma"""
    test_info = {
        "name": "test_suma",
        "description": "La función suma realiza correctamente las operaciones de suma",
        "score": 2.0,
        "msg_ok": "Función suma implementada correctamente con diferentes casos de prueba",
        "msg_error": "La función suma no funciona correctamente o no está implementada",
    }
    print(f"test_info = {json.dumps(test_info)}")

    assert suma(2, 3) == 5, "suma(2, 3) debería ser 5"
    assert suma(-1, 1) == 0, "suma(-1, 1) debería ser 0"
    assert suma(0, 0) == 0, "suma(0, 0) debería ser 0"


def test_resta_positiva():
    """Test para verificar resta con resultado positivo"""
    test_info = {
        "name": "test_resta_positiva",
        "description": "La función resta maneja correctamente números que dan resultado positivo",
        "score": 1.0,
        "msg_ok": "Resta con resultado positivo calculada correctamente",
        "msg_error": "La función resta no calcula correctamente cuando el resultado es positivo",
    }
    print(f"test_info = {json.dumps(test_info)}")

    assert resta(5, 3) == 2, "resta(5, 3) debería ser 2"


def test_resta_negativa():
    """Test para verificar resta con resultado negativo"""
    test_info = {
        "name": "test_resta_negativa",
        "description": "La función resta maneja correctamente números que dan resultado negativo",
        "score": 1.0,
        "msg_ok": "Resta con resultado negativo calculada correctamente",
        "msg_error": "La función resta no calcula correctamente cuando el resultado es negativo",
    }
    print(f"test_info = {json.dumps(test_info)}")

    assert resta(3, 5) == -2, "resta(3, 5) debería ser -2"


def test_multiplica_positivos():
    """Test para verificar multiplicación de números positivos"""
    test_info = {
        "name": "test_multiplica_positivos",
        "description": "La función multiplica realiza correctamente la multiplicación de números positivos",
        "score": 1.5,
        "msg_ok": "Multiplicación de números positivos calculada correctamente",
        "msg_error": "La función multiplica no calcula correctamente la multiplicación de números positivos",
    }
    print(f"test_info = {json.dumps(test_info)}")

    assert multiplica(2, 3) == 6, "multiplica(2, 3) debería ser 6"


def test_multiplica_negativos():
    """Test para verificar multiplicación con números negativos"""
    test_info = {
        "name": "test_multiplica_negativos",
        "description": "La función multiplica maneja correctamente la multiplicación con números negativos",
        "score": 1.5,
        "msg_ok": "Multiplicación con números negativos calculada correctamente",
        "msg_error": "La función multiplica no maneja correctamente los números negativos",
    }
    print(f"test_info = {json.dumps(test_info)}")

    assert multiplica(-2, 3) == -6, "multiplica(-2, 3) debería ser -6"


def test_multiplica_cero():
    """Test para verificar multiplicación por cero"""
    test_info = {
        "name": "test_multiplica_cero",
        "description": "La función multiplica maneja correctamente la multiplicación por cero",
        "score": 1.0,
        "msg_ok": "Multiplicación por cero calculada correctamente (resultado = 0)",
        "msg_error": "La función multiplica no maneja correctamente la multiplicación por cero",
    }
    print(f"test_info = {json.dumps(test_info)}")

    assert multiplica(0, 10) == 0, "multiplica(0, 10) debería ser 0"


def test_divide_positiva():
    """Test para verificar división de números positivos"""
    test_info = {
        "name": "test_divide_positiva",
        "description": "La función divide realiza correctamente la división de números positivos",
        "score": 1.5,
        "msg_ok": "División de números positivos calculada correctamente",
        "msg_error": "La función divide no calcula correctamente la división de números positivos",
    }
    print(f"test_info = {json.dumps(test_info)}")

    assert divide(6, 3) == 2, "divide(6, 3) debería ser 2"


def test_divide_negativa():
    """Test para verificar división con números negativos"""
    test_info = {
        "name": "test_divide_negativa",
        "description": "La función divide maneja correctamente la división con números negativos",
        "score": 1.5,
        "msg_ok": "División con números negativos calculada correctamente",
        "msg_error": "La función divide no maneja correctamente los números negativos",
    }
    print(f"test_info = {json.dumps(test_info)}")

    assert divide(-6, 3) == -2, "divide(-6, 3) debería ser -2"


def test_divide_por_cero():
    """Test para verificar división por cero"""
    test_info = {
        "name": "test_divide_por_cero",
        "description": "La función divide maneja correctamente la división por cero",
        "score": 1.0,
        "msg_ok": "División por cero manejada correctamente (debería lanzar una excepción o retornar un valor específico)",
        "msg_error": "La función divide no maneja correctamente la división por cero",
    }
    print(f"test_info = {json.dumps(test_info)}")

    try:
        divide(10, 0)
        assert (
            False
        ), "divide(10, 0) debería lanzar una excepción o retornar un valor específico"
    except ZeroDivisionError:
        pass  # La excepción esperada fue lanzada

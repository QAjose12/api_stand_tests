import sender_stand_request
import data


def get_new_user_token():
    """Crea un usuario nuevo y retorna su authToken."""
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]


def get_kit_body(name):
    """Retorna una copia del cuerpo base del kit con el nombre dado."""
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(kit_body):
    """
    Verifica que la respuesta sea 201 y que el campo 'name'
    en la respuesta coincida con el de la solicitud.
    """
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 201, (
        f"Se esperaba código 201, se obtuvo {response.status_code}. "
        f"Respuesta: {response.text}"
    )
    assert response.json()["name"] == kit_body["name"], (
        f"El campo 'name' no coincide. "
        f"Esperado: '{kit_body['name']}', Obtenido: '{response.json()['name']}'"
    )


def negative_assert_code_400(kit_body):
    """Verifica que la respuesta sea 400."""
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 400, (
        f"Se esperaba código 400, se obtuvo {response.status_code}. "
        f"Respuesta: {response.text}"
    )


# Prueba 1: Número permitido de caracteres (1)

def test_create_kit_1_char_name_get_success():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)


# Prueba 2: Número permitido de caracteres (511)

def test_create_kit_511_char_name_get_success():
    kit_body = get_kit_body(
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabC"
    )
    positive_assert(kit_body)


# Prueba 3: Número de caracteres menor al permitido (0)

def test_create_kit_0_char_name_get_error_400():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)


# Prueba 4: Número de caracteres mayor al permitido (512)

def test_create_kit_512_char_name_get_error_400():
    kit_body = get_kit_body(
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcD"
    )
    negative_assert_code_400(kit_body)


# Prueba 5: Se permiten caracteres especiales

def test_create_kit_special_chars_name_get_success():
    kit_body = get_kit_body("\"№%@\",")
    positive_assert(kit_body)


# Prueba 6: Se permiten espacios

def test_create_kit_spaces_in_name_get_success():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)


# Prueba 7: Se permiten números

def test_create_kit_numbers_in_name_get_success():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)


# Prueba 8: El parámetro no se pasa en la solicitud

def test_create_kit_no_name_param_get_error_400():
    kit_body = {}
    negative_assert_code_400(kit_body)


# Prueba 9: Tipo de parámetro incorrecto (número en vez de string)

def test_create_kit_number_type_name_get_error_400():
    auth_token = get_new_user_token()
    kit_body = {"name": 123}
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 400, (
        f"Se esperaba código 400, se obtuvo {response.status_code}. "
        f"Respuesta: {response.text}"
    )

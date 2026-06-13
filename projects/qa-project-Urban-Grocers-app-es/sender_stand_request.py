import requests
import configuration
import data


def post_new_user(user_body):
    """Crea un nuevo usuario y retorna la respuesta."""
    return requests.post(
        configuration.URL_SERVICE + configuration.PATH_USERS_V1,
        json=user_body
    )


def post_new_client_kit(kit_body, auth_token):
    """Crea un nuevo kit personal para el usuario autenticado."""
    return requests.post(
        configuration.URL_SERVICE + configuration.PATH_KITS_V1,
        json=kit_body,
        headers={"Authorization": f"Bearer {auth_token}"}
    )

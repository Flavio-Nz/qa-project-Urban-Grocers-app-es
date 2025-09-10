import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.user_headers)

def get_new_user_token(user_response):
    user_body = data.user_body
    user_response = post_new_user()
    return response.user_response.json()["authToken"]


def post_new_client_kit(kit_body, auth_token):
    kit_body = data.kit_request
    auth_token = get_new_user_token()
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=data.kit_headers)




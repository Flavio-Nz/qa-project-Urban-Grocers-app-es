import configuration
import requests
import data
import sender_stand_request

def get_kit_body(name):
    current_name = data.kit_request.copy()
    current_name["name"] = name
    return current_name

def possitive_asert(kit_body):
    kit_body = get_kit_body(name)
    user_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert user_response.status_code == 201
    assert user_response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    kit_body = get_kit_body(name)
    user_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400


def test_1_create_kit_1_letter_in_name_get_success_response():
    possitive_asert("A")

def test_2_create_kit_511_letters_in_name_get_success_response():
    possitive_asert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_3_create_kit_0_letters_in_name_get_error_response():
    negative_assert_code_400("")

def test_4_create_kit_512_letters_in_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_5_create_kit_especial_characters_in_name_get_success_response():
    negative_assert_code_400("№%@")

def test_6_create_kit_sspace_in_name_get_success_response():
    negative_assert_code_400("A Aaa")

def test_7_create_kit_numbers_in_name_get_success_response():
    negative_assert_code_400("1234")

def test_8_create_kit_request_with_empty_name_get_error_response():
    negative_assert_code_400({ })

def test_9_create_kit_name_whit_no_string_data_get_error_response():
    negative_assert_code_400(123)


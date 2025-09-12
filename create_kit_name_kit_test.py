import data
import sender_stand_request
import copy

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def get_kit_body(name):
    body = copy.deepcopy(data.kit_body)
    body["name"] = name
    return body

def positive_assert(name):
    token = get_new_user_token()
    body = get_kit_body(name)
    resp = sender_stand_request.post_new_client_kit(body, token)
    assert resp.status_code == 201
    assert resp.json()["name"] == name

def negative_assert_code_400(body):
    token = get_new_user_token()
    resp = sender_stand_request.post_new_client_kit(body, token)
    assert resp.status_code == 400

def test_1_create_kit_1_letter_in_name_get_success_response():
    positive_assert("A")

def test_2_create_kit_511_letters_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_3_create_kit_0_letters_in_name_get_error_response():
    negative_assert_code_400(get_kit_body(""))

def test_4_create_kit_512_letters_in_name_get_error_response():
    negative_assert_code_400(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"))

def test_5_create_kit_especial_characters_in_name_get_success_response():
    positive_assert("№%@")

def test_6_create_kit_sspace_in_name_get_success_response():
    positive_assert("A Aaa")

def test_7_create_kit_numbers_in_name_get_success_response():
    positive_assert("1234")

def test_8_create_kit_request_with_empty_name_get_error_response():
    body = copy.deepcopy(data.kit_body)
    body.pop("name")
    negative_assert_code_400(body)

def test_9_create_kit_name_whit_no_string_data_get_error_response():
    negative_assert_code_400(get_kit_body(123))


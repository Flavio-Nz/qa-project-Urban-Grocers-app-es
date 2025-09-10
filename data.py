import sender_stand_request

user_headers = {
    "Content-Type": "application/json"
}

user_body = { "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

kit_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer"
}

kit_request = {
    "card_id": int,
    "name" : str,
}


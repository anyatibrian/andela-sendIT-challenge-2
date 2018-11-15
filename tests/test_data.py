from flask import session
empty_fields = {
                "parcel_name": "",
                "description": "",
                "pick_up": "tororo",
                "destination": "kampala"
                }
bad_data = {
            "parcel_name": "anyatibrian",
            "description": 10000,
            "pick_up": "tororo",
            "destination": "kampala"
            }
empty_space = {
            "parcel_name": "  ",
            "description": "has two doors and checks out",
            "pick_up": "tororo",
            "destination": "kampala"

}
good_data = {
            "parcel_name": "anyatibrian",
            "description": "has two doors and checks out",
            "pick_up": "tororo",
            "destination": "kampala"
           }

user_data = {
    "username": "anyatibrian",
    "password": "password"
}

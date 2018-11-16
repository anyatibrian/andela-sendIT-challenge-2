from Api.utilities import serial_generator

parcel_orders = []


class ParcelOrders:
    """class responsible for creating the parcel orders"""

    def __init__(self):
        pass

    def create_orders(self, parcel_name, description, pick_up, destination, user_id=None):
        """function creates the parcel order list """
        str_price = str(0)
        serial = serial_generator()
        parcel_order = {
            'parcel_id': len(parcel_orders)+1,
            'parcel_name': parcel_name,
            'description': description,
            'pick-up': pick_up,
            'destination': destination,
            'status': "pending",
            "user_id": user_id,
            'serial_no': serial,
            "delivery_price": str_price+"ugx"
        }
        parcel_orders.append(parcel_order)
        return parcel_orders

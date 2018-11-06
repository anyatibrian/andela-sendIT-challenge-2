from Api.utilities import serial_generator

parcel_orders = []


class ParcelOrders:
    """class responsible for creating the parcel orders"""

    def __init__(self):
        pass

    def create_orders(self, parcel_name, description, pick_up, destination, status="pending"):
        """function creates the parcel order list """
        serial = serial_generator()
        parcel_order = {
            'parcel_id': len(parcel_orders) + 1,
            'parcel_name': parcel_name,
            'description': description,
            'pick-up': pick_up,
            'destination': destination,
            'status': status,
            'serial_no': serial
        }
        parcel_orders.append(parcel_order)
        return parcel_orders

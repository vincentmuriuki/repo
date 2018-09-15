from flask import Flask, request
from flask_restful import    Resource
from .models import Order, orders


# class SpecificOrder(Resource):
    

#     def get(self, id):
#         order = Order().get_by_id(id)
        
#         if order:
#             return {"order": order.serialize()}, 200

#         return {"message":"Order not found"}, 404

#     def delete(self, id):
#         order = Order().get_by_id(id)

#         if order:
#             orders.remove(order)
#             return {"message":"order deleted successfully"},200
#         return {"message":"Order not found"}, 404

#     def put(self, id):
#         order = Order().get_by_id(id)

#         if order:
#             order.status="approved"
#             return {"message":"status approved"}
#         return {"message":"Order not found"}, 404

# class NewOrders(Resource):

#     def post(self):
#         data = request.get_json()
#         order = Order(data['name'], data["price"],data['description'])
#         orders.append(order)

#         return {"message":"Food order created"}, 201



class GetOrders(Resource):
    def get(self):
        return {"orders":[order.serialize() for order in orders]}
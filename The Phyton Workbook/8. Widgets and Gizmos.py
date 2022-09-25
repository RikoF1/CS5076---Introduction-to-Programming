"""
App that sums the weight of the order taking into account the ammount of gizmos and widgets
"""
# Global Variables
widget_weight = 75
gizmo_weight = 100

widget_amount = int(input("Input here the amount of widgets in your order: "))
gizmo_amount = int(input("Input here the amount of gizmos in your order: "))

weight_order = (widget_amount * widget_weight) + (gizmo_amount * gizmo_weight)

print("Your order total weight is", weight_order, "grams.")
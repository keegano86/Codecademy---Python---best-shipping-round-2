def cost_of_ground_shipping(weight):

  if weight <= 2.0:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.0
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75

  return 20 + (price_per_pound) * (weight)

print(cost_of_ground_shipping(8.4))

premium_shipping = 125

def drone_shipping_cost(weight):
  if weight <= 2.0:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.0
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25

  return price_per_pound * weight

print(drone_shipping_cost(1.5))

def best_shipping_cost(weight):

  ground = cost_of_ground_shipping(weight)
  premium = premium_shipping
  drone = drone_shipping_cost(weight)

  if ground < premium and ground < drone:
    method = "ground round"
    cost = ground
  elif premium < ground and premium < drone:
    method = "Premium"
    cost = premium
  else:
    method = "Drone Schmone"
    cost = drone
    



  print(
    "The cheapest shipping price is $%.2f by way of %s shipping" 
    % (cost, method)
  )

print(best_shipping_cost(4.8))



  
import Restaurant as r

rest = r.Restaurant("Naan & Curry", "Indian")

print(rest.restaurant_name)

print(rest.cuisine_type)

rest.describe_restaurant()

rest.open_restaurant()

rest.set_number_served(92)

rest.describe_restaurant()

rest.increment_number_served(10)

rest.describe_restaurant()

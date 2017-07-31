#city_country accepts 2 arguments, a name of a city and a name of the country
# and returns it in a string

def city_country(city,country,population=''):
  if population:
    city_country = city + ', ' + country
    city_country = city_country.title() 
    city_country += ' - population ' + str(population)
  else:
    city_country = city + ', ' + country 
    city_country = city_country.title()

  return city_country


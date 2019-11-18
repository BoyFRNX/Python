def city_country(city, country):
    return f"{city.title()}, {country.title()}"


pair_1 = city_country('Fort Wayne', 'United States')
pair_2 = city_country('New York City', 'United States')
pair_3 = city_country('Madrid', 'Spain')

print(pair_1)
print(pair_2)
print(pair_3)

def city_country_formatted(city, country, population=None):
    """Makes city and country arguments into standard 'City, Country' format."""
    if population is not None:
        formatted_city_country = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_city_country = f"{city.title()}, {country.title()}"
    return formatted_city_country

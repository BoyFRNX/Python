def make_shirt(size, message):
    print(f"""You ordered a {size.lower()} and it says "{message}".""")


# Positional Arguments
make_shirt('medium', 'WUNDERWORLD')

# Key Word Arguments
make_shirt(size='medium', message='WUNDERWORLD')

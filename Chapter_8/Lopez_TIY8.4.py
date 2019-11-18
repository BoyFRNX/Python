def make_shirt(size='large', message='I Love Python'):
    print(f"""You ordered a {size.lower()} and it says "{message}".""")


# Large Shirt, Default Message
make_shirt()
# Medium Shirt, Default Message
make_shirt(size='medium')
# Small Shirt, "WUNDERWORLD" message
make_shirt(size='small', message='WUNDERWORLD')

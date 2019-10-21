# (2.1) Creating a variable and printing that variable
message = "TIY 2.1"
print(message)

# (2.2) Creating a variable, printing, then changing variable value and printing again
message = "TIY 2.1"
print(message)
message = "TIY 2.2"
print(message)

# (2.3) Creating a name variable and printing a format message using the name
name = "Alexa"
message = f"Hey {name}, play some music."
print(message)

# (2.4) Creating a name variable and printing in lowercase, uppercase, and title
name = "Alexa"
print(name.lower())
print(name.upper())
print(name.title())

# (2.5) Making a famous name variable and printing a quote from that person
famous_name = "Derek Jeter"
message = "There may be people who have more talent than you, but there's no excuse for anyone to work harder than you do."
quote = f'"{message}"\n\t\t\t\t\t\t\t\t\t\t\t\t\t-{famous_name}'
print(quote)

# (2.6) Changed famous person variable name
famous_person = "Derek Jeter"
message = "There may be people who have more talent than you, but there's no excuse for anyone to work harder than you do."
quote = f'"{message}"\n\t\t\t\t\t\t\t\t\t\t\t\t\t-{famous_person}'
print(quote)

# (2.7) Learning to deal with whitespace
name = " Alexa "
print(f"\t|{name}|\n|{name.lstrip()}|\n|{name.rstrip()}|\n|{name.strip()}|")

# (2.8) Prints 8 in 4 different ways
print(3+5)
print(2*4)
print(16-8)
print(16/2)

# (2.9) Creates a favorite number variable and prints a message saying that's my favorite number
FAV_NUMBER = 7
message = f"My favorite number is: {FAV_NUMBER}."
print(message)

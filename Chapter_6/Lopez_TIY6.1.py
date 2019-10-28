friends = {
    'first_name': ['Hayden', 'Aung', 'Tristan', 'Jackson', 'Nick', 'Tarron'],
    'last_name': ['Heche', 'Han', 'Taylor', 'Foote', 'Tucker', 'White'],
    'age': ['18', '17', '17', '17', '18', '16'],
    'city': ['Fort Wayne', 'Fort Wayne', 'Garret', 'Fort Wayne', ' Leo', 'Fort Wayne']}

for value in range(0, 6):
    print(f"Friend {value + 1}: {friends['first_name'][value]},"
          f" {friends['last_name'][value]},"
          f" {friends['age'][value]},"
          f" {friends['city'][value]}")

current_users = ['user1', 'user2', 'user3', 'user4', 'user5']

new_users = ['new_user1', 'USer1', 'user3', 'new_user2']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry, the username: {new_user.lower()} is taken. Please try another.")
    else:
        print(f"Good news! The username: {new_user.lower()} is available.")


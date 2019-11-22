def show_messages(messages):
    print("Let's look at the messages:")
    for message in messages:
        print(f"{message}")


def send_messages(messages):
    print("\nLet's send these messages.")
    while messages:
        sent_message = messages.pop(0)
        sent_messages_list = []
        sent_messages_list.append(sent_message)
        print(f'Sending "{sent_message}"...')
        print("Message sent!")


def sent_messages(messages):
    print("\nHere the sent messages:")
    for message in messages:
        print(message)

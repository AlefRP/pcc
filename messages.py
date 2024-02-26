def show_messages(messages):
    """Shows a list of messages."""
    for message in messages:
        print(message)
 
def send_messages(messages, sent_messages):
    """Moves messages from the list to the sent_messages list."""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
        
    # Invert the order of itens in sent_messages.
    sent_messages.reverse()

messages = ['Hello', 'World', '!']
sent_messages = []
# show_messages(messages)

# send_messages(messages, sent_messages)
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)
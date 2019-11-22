import message_functions
# The import below won't work because all the functions are called from message_functions using * with the last import
from message_functions import send_messages
from message_functions import send_messages as sm
import message_functions as mf
from message_functions import *


message_list = ["Hi!", "How are you?", "I'm good, and you?", "The same!"]

message_functions.send_messages(message_list[:])

send_messages(message_list[:])

sm(message_list[:])

mf.send_messages(message_list[:])

send_messages(message_list[:])

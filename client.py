import rpyc
import zmq
from threading import Thread
from constPS import *  # -
import time

reach = 0
net = None
input_var = None
user_name = None


def myprint(message):
    print(message)


def checkAndPrint(delay, dont):
    global reach
    global net
    global user_name
    global input_var
    while True:
        length = conn.root.replyLength(1)
        if input_var == "exit":
            break
        while reach < length:
            net = conn.root.replyWith(reach)
            reach += 1
            print(net)


def receive_messages():
    context = zmq.Context()
    s_sub = context.socket(zmq.SUB)  # create a subscriber socket
    p = "tcp://" + SERVER + ":" + PORT  # how and where to communicate
    s_sub.connect(p)  # connect to the server
    # subscribe to GROUP messages
    s_sub.setsockopt_string(zmq.SUBSCRIBE, "GROUP")

    while True:
        message = s_sub.recv().decode()
        if not message.startswith("GROUP " + user_name + ":"):
            print(message)


# verify if the user wants a direct message or a group message
# if direct message, then send to the user
# if group message, then send to all users in the group using ZeroMQ

option = input(
    "Do you want to send a direct message or a group message? (direct/group): ")
if option == "direct":
    conn = rpyc.connect(SERVER, PORT)
    conn.root.setCallback(myprint, user_name)

    user_name = input("Please enter your name: ")
    destination = input(
        "Please enter the name of the person you want to talk to: ")
    print("Type exit to leave the conversation")
    conn.root.serverPrint(user_name, destination)
    reach = conn.root.replyLength(1)

    try:
        t = Thread(target=checkAndPrint, args=(0, 0))
        t.start()

        while True:
            input_var = input()
            if input_var == "exit":
                time.sleep(1)
                input_var = user_name + " has left the conversation"
                conn.root.setCallback(myprint, user_name)
                conn.root.serverPrintMessage(input_var)
                conn.root.serverExit(user_name)
                break
            reach += 1
            input_var = user_name + ":" + input_var
            conn.root.setCallback(myprint, user_name)
            conn.root.serverPrintMessage(input_var, destination)
    except Exception as errtxt:
        print("You have left the room")

elif option == "group":
    user_name = input("Please enter your name: ")

    t = Thread(target=receive_messages)
    t.start()

    context = zmq.Context()
    s = context.socket(zmq.PUB)  # create a publisher socket
    p = "tcp://" + SERVER + ":" + PORT  # how and where to communicate
    s.bind(p)

    while True:
        msg = input("Enter a message: ")
        msg = str.encode("GROUP " + user_name + ":" + msg)
        s.send(msg)  # publish the message

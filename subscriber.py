import zmq
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ SERVER +":"+ PORT        # how and where to communicate
s.connect(p)                         # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "GROUP")  # subscribe to TIME messages

while True:
	msg = s.recv()   # receive a message
	print (bytes.decode(msg))

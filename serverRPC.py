import rpyc

test = []
uname = []
myReferences = set()
myNames = set()

class MyService(rpyc.Service):
    def on_connect(self, conn):
        """Think of this as a constructor of the class, but with
        a new name so as not to 'overload' the parent's init"""
        self.fn = None

    def exposed_serverPrint(self, user, destination):
        global test
        uname.append(user)

        for i in myReferences:
            if i[1] == destination and i[0] is not self.fn:
                i[0](user + " joined the room")

    def exposed_serverExit(self, name):
        global test
        myReferences.remove(self.fn)
        uname.remove(name)

    def exposed_serverPrintMessage(self, message, destination):
        # only send to the destination
        for i in myReferences:
            if i[1] == destination and i[0] is not self.fn:
                i[0](message)

    def exposed_replyWith(self, number):
        return test[number]

    def exposed_replyLength(self, length):
        return len(test)

    def exposed_setCallback(self, fn, name):
        self.fn = fn  # Saves the remote function for calling later
        global myReferences
        myReferences.add((fn, name))  # Add the tuple (fn, name)
        myNames.add(name)


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    t = ThreadedServer(MyService, port=18888)
    t.start()

class Asker:
    @staticmethod
    def askall(lst):
        for item in lst:
            item.report()

class Sender:
    first_call = True

    @classmethod
    def report(cls):
        if cls.first_call:
            print("Greetings!")
            cls.first_call = False
        else:
            print("Get away!")


senders = [Sender(), Sender(), Sender()]
Asker.askall(senders)

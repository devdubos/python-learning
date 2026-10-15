

class Developer:
    def work(self):
        print("Write code")


class Designer:
    def work(self):
        print("Draw press")

team = [Developer(), Designer()]

for member in team:
    member.work()


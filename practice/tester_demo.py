class Tester:
    def __init__(self, name, years):
        self.name = name
        self.years = years
        self.bugs_found = 0

    def introduce(self):
        print("Hi, I'm", self.name, "with", self.years, "years of QA")

    def find_bug(self):
        self.bugs_found = self.bugs_found + 1
        print(self.name, "has found", self.bugs_found, "bugs")


maru = Tester("Maru", 6)
alex = Tester("Alex", 2)

maru.introduce()
alex.introduce()

maru.find_bug()
maru.find_bug()
alex.find_bug()

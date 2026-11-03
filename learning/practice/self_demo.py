class BugReport:
    def __init__(self, title, severity):
        self.title = title
        self.severity = severity

    def show(self):
        print("self is:", self)
        print("Bug:", self.title, "| Severity:", self.severity)
            
        
       


bug1 = BugReport("Cart shared between users", "High")
bug2 = BugReport("Titles misaligned", "Low")

print("--- Part 1: two objects, one method ---")
bug1.show()
bug2.show()

print("--- Part 2: the secret version ---")
BugReport.show(bug1)
BugReport.show(bug2)

print("--- Part 3: who is self? ---")
print(bug1)
print(bug2)

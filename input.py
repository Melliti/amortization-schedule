import amortizationSchedule

class UserInput:
    principal = ""
    monthlyInterestRate = ""
    numberOfMonth = ""

    def inputs(self):
        self.principal = input("Enter Principal: ")
        self.monthlyInterestRate = input("Enter monthly interest rate: ")
        self.numberOfMonth = input("Enter the period in month: ")

    def describe(self):
        print("Principal = " + self.principal)
        print("monthly interst rate = " + self.monthlyInterestRate)
        print("period = " + self.numberOfMonth)

userInput = UserInput()
userInput.inputs()
schedule = amortizationSchedule.amortizationSchedule()
schedule.makeSchedule(userInput.principal, userInput.monthlyInterestRate, userInput.numberOfMonth)

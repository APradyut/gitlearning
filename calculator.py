class Calculator:
    def Add(self, a, b):
        return a+b

    def Sub(self, a, b):
        return a-b

    def Mult(self, a, b):
        return a*b


cal = Calculator()
print(cal.Add(2, 3))
print(cal.Sub(3, 2))
print(cal.Mult(3, 2))


class Cal:

    name = 'Jack'

    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def mul(x,y):
        return x* y

cal = Cal()
print(cal.add(1,2))
print(Cal.add(1, 2))
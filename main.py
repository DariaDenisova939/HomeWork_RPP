class Arithmetic:

    def __init__(self, operand1, operand2):  # конструктор класса
        self.operand1 = operand1
        self.operand2 = operand2

    def __setattr__(self, key, value):  # реализация присвоения значений атрибуту, запрещаем значение нуля
        if value == 0:
            raise AttributeError("недопустимое значение атрибута")
        else:
            object.__setattr__(self, key, value)

    def multiplication(self):  # метод для умножения чисел
        return self.operand1 * self.operand2

    def division(self):  # метод для деления чисел
        return self.operand1 / self.operand2

    def addition(self):  # метод для сложения чисел
        return self.operand1 + self.operand2

    def subtraction(self):  # метод для вычитания чисел
        return self.operand1 - self.operand2


class Formula(Arithmetic):  # класс для работы с формулой, наследуется от класса Arithmetic
    def __getattribute__(self, item):  # автоматически вызывается, когда идет считывание атрибута через экземпляр класса, запрещаем считывать приватный атрибут
        if item == "_Arithmetic__frml":
            raise ValueError("Private attribute")  # если идет обращение к приватному атрибуту по внешнему имени, то генерируем исключение ValueError
        else:
            return object.__getattribute__(self, item)

    def calc(self):  # метод для подсчета формулы
        return (self.multiplication() / self.addition() + self.division()) + Formula.subtraction(self) - self.subtraction()

    @staticmethod  # статический метод для вывода формулы
    def out_formula():
        __frml = "Формула: (a*b/((a+b)+(a/b)))+(|a|-|b|)-(a-b)"
        print(__frml)

    def subtraction(self):  # реализация полиморфизма, переопределяем метод и считаем разницу, но с модулем
        return abs(self.operand1) - abs(self.operand2)


a = int(input("Введите a: "))
b = int(input("Введите b: "))
obj = Formula(a, b)
print(obj.calc())

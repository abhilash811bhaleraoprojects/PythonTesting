from oopDemo import calculator


class childimpl(calculator):
    num2 = 200

    def getcompleteData(self):
        return self.num2 + self.num


obj = childimpl(calculator,23)
print(obj.getcompleteData())
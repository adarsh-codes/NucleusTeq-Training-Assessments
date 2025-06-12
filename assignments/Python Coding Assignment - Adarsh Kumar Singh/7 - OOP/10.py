class A:
    def show(self):
        print("Called from class A")

class B:
    def show(self):
        print("Called from class B")

class C(A, B):
    pass

obj = C()
obj.show()

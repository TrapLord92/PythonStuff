#inherits from multipes class

class A:
    def method_A(self):
        print("Method class A")


class B:
    def method_B(self):
        print("Method class B")


class C(A,B):
    def method_C(self):
        print("Method class C")

cObject=C()

cObject.method_A()
cObject.method_B()
cObject.method_C()


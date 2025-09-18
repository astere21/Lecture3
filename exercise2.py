class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")
        super().hello()

class C(A):
    def hello(self):
        print("Hello from C")
        super().hello()

class D(B, C):
    def hello(self):
        print("Hello from D")
        super().hello()

class E(C):
    def hello(self):
        print("Hello from E")
        super().hello()

class F(B, E):
    def hello(self):
        print("Hello from F")

f = F()
f.hello()
print(F.mro())

class mro1:
    def hello(self):
        print("Hello from Error_mro1")

class mro2(mro1):
    def hello(self):
        print("Hello from Error_mro2")
        super().hello()

class mro3(mro1, mro2):
    def hello(self):
        print("Hello from Error_mro3")
        super().hello()

print(mro3.mro())
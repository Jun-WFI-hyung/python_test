class A:
    def __init__(self) -> None:
        self.name = 'A'
        self.bbb = B(self.print_name)
        print(self.print_name)
        
    def print_name(self) -> None:
        print(self.name)
        
    def test(self) -> None:
        self.bbb.print_name()
        
class B:
    def __init__(self, func: callable) -> None:
        self.name = 'B'
        self.func = func
        print(self.func)
        
    def print_name(self) -> None:
        self.func()
        

test_a =  A()
test_a.test()

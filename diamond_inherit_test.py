from abc import *

# 최상위 추상클래스
class A(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.name = name
        print("!!")

# 하위 추상클래스 1
class Sub1(A, metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        print(1)
        
    @abstractmethod
    def testSub1(self) -> None:
        pass

# 하위 추상클래스 2
class Sub2(A, metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        print(2)
        
    @abstractmethod
    def testSub2(self) -> None:
        pass

# 인스턴스 클래스
class FinalInstance(Sub1, Sub2):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        
    def testSub1(self) -> None:
        return self.name
    
    def testSub2(self) -> None:
        return self.name
        
        
test = FinalInstance('test')
print(test.testSub2())
print(test.testSub1())
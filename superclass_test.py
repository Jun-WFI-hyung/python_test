from dataclasses import dataclass

class TestNormalClass:
    share_value: int = 0
    share_dict: dict = {
        1: "XX"
    }

class SubClass1(TestNormalClass):
    def __init__(self) -> None:
        pass
    
class SubClass2(TestNormalClass):
    def __init__(self) -> None:
        pass

b = SubClass1()
c = SubClass2()

print(c.share_value)   # 0
print(c.share_dict[1]) # XX

b.share_value = 999
b.share_dict[1] = "ZZ"

print(c.share_value)   # 0
print(c.share_dict[1]) # ZZ

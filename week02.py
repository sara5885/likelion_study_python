class Shape : 
    def __init__(self,a):
        self.a=a
    def area(self):
        area=self.a*self.a
        return area

class Square(Shape) : 
    def __init__(self,length):
        Shape.__init__(self,length)
    def area(self,length):
        area=length*length
        print("정사각형의 면적:{}".format(area))
        return area

length=int(input("정사각형의 한 변의 길이를 입력하세요 : "))

result=Square(length)
result.area(length)
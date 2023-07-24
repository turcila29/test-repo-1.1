class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __add__(self, rect2):
        return Rectangle(self.width + rect2.width, self.height + rect2.height)
    
    def calculate_area(self):
        return self.width * self.height
    
    def __int__(self):
        return self.calculate_area()

    def __str__(self):
        return '\n'.join('*' * self.width for _ in range(self.height))
    
if __name__ == '__main__':
    rect1 = Rectangle(5, 3)
    print (rect1)
    rect2 = Rectangle(2, 7)
    print(rect2)
    print(rect1 + rect2)
    print(int(rect1 + rect2))
class Circle:
    def set_dim(self, r):
        self.r = r

    def area(self):
        return 2 * 3.14 * self.r

n = int(input("Enter number of circles: "))
shapes = []

for i in range(n):
    c = Circle()
    r = int(input("Enter the radius of circle {}: ".format(i + 1)))
    c.set_dim(r)
    shapes.append(c)

for index, circle in enumerate(shapes, start=1):
    res = circle.area()
    print("Area of circle {} is {}".format(index, res))

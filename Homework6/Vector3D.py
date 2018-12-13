class Vector3D:
    '''Class Vector3D defines some operations with vectors.'''
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        

    # 1.Addition: Vector3D(1, 2, 3) + Vector3D(3, 2, 1) = Vector3D(4, 4, 4)
    def __add__(self, operand):
        return Vector3D(self.x + operand.x, self.y + operand.y, self.z + operand.z)

    # 2.Subtraction: Vector3D(1, 2, 3) - Vector3D(3, 2, 1) = Vector3D(-2, 0, 2)
    def __sub__(self, operand):
        return Vector3D(self.x - operand.x, self.y - operand.y, self.z - operand.z)

    # 3.Scalar multiplication: 3 * Vector3D(1, 2, 3) = Vector3D(3, 6, 9)
    def scalar__mul(self, number):
        return Vector3D(self.x * number, self.y * number, self.z * number)

    # 4.Dot product of vectors: Vector3D(1, 2, 3).dot( Vector3D(3, 2, 1)) = 10
    def dot_product(self, operand):
        return (self.x * operand.x + self.y * operand.y + self.z * operand.z)

    #5.Norm: Vector3D(1, 2, 3).norm() = 3.742
    def norm_eu(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    #6. Signing
    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)

    #7. Copy self
    def __copy__(self):
        return Vector3D(self.x, self.y, self.z)

    #8. Division by a number
    def __div__(self, number):
        return self.__copy() * (number**-1)

    #9. Magnitude or length of vector
    def __magnitude__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    #10. String represntation
    def __str__(self):
        return f'[{self.x}, {self.y}, {self.z}]'


v1 = Vector3D(1, 2, 3)
v2 = Vector3D(3, 2, 1)
v3 = v1 + v2
v4 = v1 - v2
v5 = v1.scalar__mul(3)
v6 = v1.dot_product(v2)
v7 = v1.norm_eu()

print("Addition of vectors:", v3)
print("Subtraction of vectors:", v4)
print("Scalar multiplication of vector", v1, "by 3 = ", v5)
print("Dot product of vectors:", v6)
print("Normalized vector:", round(v7, 3))



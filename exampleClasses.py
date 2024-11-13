import numpy as np


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = np.array((self.x, self.y, self.z))

    # Calculate dot product of addressed vector and passed 'other' vector .vector
    def dot(self, other):
        return np.dot(self.vector, other.vector)


v1 = Vector3D(2, 2, 3)

v2 = Vector3D(1, 2, 3)

print(v1.dot(v2))

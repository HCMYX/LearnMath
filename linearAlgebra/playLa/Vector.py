import math


class Vector:
    def __init__(self, lst):
        # 对入参做一个复制，防止对入参修改影响 values
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        """返回一个dim维的零向量"""
        return cls([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
         return  1 / self.norm() * Vector(self._values)

    def __add__(self, other):
        """向量加法，返回结果向量"""
        assert len(self) == len(other), "Error in adding. Length of vectors must be same"
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """向量减法"""
        assert len(self) == len(other), "Error in subtracting. Length of vectors must be same"
        return Vector([a - b for a,b in zip(self, other)])

    def __mul__(self, other):
        """向量乘法（右乘） self * other"""
        return Vector([ a * other for a in self])

    def __rmul__(self, other):
        """向量乘法（左乘） other * self"""
        return self * other

    def __pos__(self):
        """向量取正"""
        return 1 * self
    def __neg__(self):
        """向量取负"""
        return -1 * self
    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()

    def __getitem__(self, index):
        # 返回指定向量的第item元素
        return self._values[index]
    def __len__(self):
        #返回向量的长度
        return len(self._values)

    def __repr__(self):
        # 重新repr方法 系统调用的输出对象方法
        return "Vector({})".format(self._values)

    def __str__(self):
        # 重写str方法。用户主动调用的输出对象的方法
        return "({})".format(", ".join(str(e) for e in self._values))



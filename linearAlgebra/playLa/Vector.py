class Vector:
    def __init__(self, lst):
        # 对入参做一个复制，防止对入参修改影响 values
        self._values = list(lst)

    def __add__(self, another):
        """向量加法，返回结果向量"""
        assert len(self) == len(another), "Error in adding. Length of vectors must be same"
        return Vector([a + b for a, b in zip(self, another)])
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

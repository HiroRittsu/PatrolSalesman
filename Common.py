import math


class Common:

    def perm(self, size: int):
        result = []

        def perm_sub(n, a):
            if n == size:
                result.append(a.copy())
            else:
                for x in range(2, size + 1):
                    if x not in a:
                        if n != 2 or a[0] > x:
                            a.append(x)
                            perm_sub(n + 1, a)
                            a.pop()

        for x in range(2, size + 1):
            perm_sub(2, [x, 1])

        return result

    def read_data(self, path: str):
        data_list = []
        with open(path) as f:
            l_strip = [s.strip() for s in f.readlines()]
            for data in l_strip:
                data_list.append([int(data.split(',')[0]), int(data.split(',')[1])])
        return data_list

    def distance(self, node1: list, node2: list):
        X = node2[0] - node1[0]
        Y = node2[1] - node1[1]
        return math.sqrt(X ** 2 + Y ** 2)

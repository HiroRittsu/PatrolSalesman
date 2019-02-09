import math


class Common:
    def distance(self, node1: list, node2: list):
        X = node2[0] - node1[0]
        Y = node2[1] - node1[1]
        return math.sqrt(X ** 2 + Y ** 2)

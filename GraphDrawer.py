import matplotlib.pyplot as plt


class GraphDrawer:

    def reset_plt(self):
        plt.cla()

    def edges_regist(self, edges: list):
        for edge in edges:
            plt.plot([edge[0][0], edge[1][0]], [edge[0][1], edge[1][1]], 'k-')

    def nodes_regist(self, nodes: list):
        for node in nodes:
            plt.scatter(node[0], node[1])

    def show_plt(self):
        plt.show()
        plt.cla()

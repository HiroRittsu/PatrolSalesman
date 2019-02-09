from PatrolSalesman import GraphDrawer
from PatrolSalesman import Common


def read_data(path: str):
    data_list = []
    with open(path) as f:
        l_strip = [s.strip() for s in f.readlines()]
        for data in l_strip:
            data_list.append([int(data.split(',')[0]), int(data.split(',')[1])])
    return data_list


def main():
    drawer = GraphDrawer.GraphDrawer()
    common = Common.Common()

    nodes = read_data('./data0')

    drawer.nodes_regist(nodes)
    drawer.show_plt()


if __name__ == '__main__':
    main()

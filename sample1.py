from PatrolSalesman import GraphDrawer
from PatrolSalesman import Common

drawer = GraphDrawer.GraphDrawer()
common = Common.Common()


def all_hands(nodes: list):
    route = common.perm(len(nodes))

    '''
        for a in range(len(nodes)):
        for b in range(len(nodes)):
            if a == b:
                continue

            common.distance(nodes[a], nodes[b])
    
    :param nodes: 
    :return: 
    '''


def main():
    nodes = common.read_data('./data0')
    drawer.nodes_regist(nodes)
    # drawer.show_plt()
    all_hands(nodes)


if __name__ == '__main__':
    main()

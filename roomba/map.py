import networkx as nx
# import matplotlib.pyplot as plt


def front_rack_finder(tag='<x: 064.5, y: 026.0> [RtRack 05, col 1, LfRack 25, col 5]'):
    xy, contain = tag.split('[')
    x, y = xy[1:-2].split(',')
    x = x.split(':')
    y = y.split(':')
    contain = contain[:-1].split(',')
    newcontain = []
    for el in contain:
        le = el.split()
        le = {le[0]: int(le[1])}
        newcontain.append(le)

    return (float(x[1]), float(y[1])), newcontain[0], newcontain[1], newcontain[2], newcontain[3]


def floor_finder(floor='<x: 049.0, y: 013.5>'):
    floor_pos = floor[1:-1]
    x, y = floor_pos.split(',')
    x = x.split(':')
    y = y.split(':')
    return (float(x[1]), float(y[1]))


def pallet_finder(pallet="/ pallet 056\ "):
    pallet = pallet[1:-2].split()
    return {pallet[0]: int(pallet[1])}


def rack_finder(cord='{pallet 104 @ rack 45, row 2, col 3} (dock A)'):
    racks = {8: {'lfrack': 45, 'col': 5, 'rtrack': None}, 9: {'lfrack': 45, 'col': 1, 'rtrack': None}, 10: {'lfrack': 72, 'col': 1, 'rtrack': None}, 11: {'lfrack': 72, 'col': 5, 'rtrack': None}, 14: {'lfrack': 57, 'col': 1, 'rtrack': None}, 16: {
        'lfrack': 57, 'col': 5, 'rtrack': None}, 21: {'lfrack': 23, 'col': 1, 'rtrack': None}, 18: {'lfrack': 23, 'col': 5, 'rtrack': None}, 23: {'lfrack': 64, 'col': (5, 1), 'rtrack': 46}, 24: {'lfrack': 64, 'col': (1, 5), 'rtrack': 46}}
    # edges = [(1, 2), (1, 6), (2, 3), (3, 4), (4, 5), (5, 7), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15),
    #  (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 3), (17, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 12)]
    # position = {1: {'pos': (21, 18.5)}, 2: {'pos': (76, 18)}, 3: {'pos': (76.5, 41.5)}, 4: {'pos': (43.5, 41.5)}, 5: {'pos': (31.5, 42)}, 6: {'pos': (14, 22)},
    # 7: {'pos': (13.5, 41.5)}, 8: {'pos': (14, 47.5)}, 9: {'pos': (14, 67.5)}, 10: {'pos': (14, 78)}, 11: {'pos': (14, 98)}, 12: {'pos': (14.5, 104.5)}, 13: {'pos': (31.5, 104.5)}, 14: {'pos': (41, 10.5)}, 15: {'pos': (54, 104.5)}, 16: {'pos': (61, 104.5)}, 17: {'pos': (80, 104)}, 18: {'pos': (80, 99)}, 19: {'pos': (80, 81)}, 20: {'pos': (76, 62)}, 21: {'pos': (80, 119)}, 22: {'pos': (80, 127.5)}, 23: {'pos': (61, 127)}, 24: {'pos': (41, 127)}, 25: {'pos': (21, 127.5)}, 26: {'pos': (14, 118.5)}}
    sub_string, dock = cord.split('}')
    dock = dock[2:-1].split()
    dock = {dock[0]: dock[1]}
    sub_string = sub_string.split('{')[1]
    pallet_rack, row, col = sub_string.split(',')
    pallet, rack = pallet_rack.split('@')
    pallet = pallet.split()
    pallet = {pallet[0]: int(pallet[1])}
    rack = rack.split()
    rack = {rack[0]: int(rack[1])}
    row = row.split()
    row = {row[0]: int(row[1])}
    col = col.split()
    col = {col[0]: int(col[1])}
    for item in racks:
        if racks[item]['lfrack'] == rack['rack']:
            rack['rack_id'] = item
            rack['rack_pos'] = "left"
            rack['rack_col'] = racks[item]['col']
            break
        elif racks[item]['rtrack'] == rack['rack']:
            rack['rack_id'] = item
            rack['rack_pos'] = "right"
            rack['rack_col'] = racks[item]['col']
            break
    return pallet, rack, row, col, dock


def path_finder(start, end):

    edges = [(1, 2), (1, 6), (2, 3), (3, 4), (4, 5), (5, 7), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15),
             (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 3), (17, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 12)]
    position = {1: {'pos': (21, 18.5)}, 2: {'pos': (76, 18)}, 3: {'pos': (76.5, 41.5)}, 4: {'pos': (43.5, 41.5)}, 5: {'pos': (31.5, 42)}, 6: {'pos': (14, 22)},
                7: {'pos': (13.5, 41.5)}, 8: {'pos': (14, 47.5)}, 9: {'pos': (14, 67.5)}, 10: {'pos': (14, 78)}, 11: {'pos': (14, 98)}, 12: {'pos': (14.5, 104.5)}, 13: {'pos': (31.5, 104.5)}, 14: {'pos': (41, 10.5)}, 15: {'pos': (54, 104.5)}, 16: {'pos': (61, 104.5)}, 17: {'pos': (80, 104)}, 18: {'pos': (80, 99)}, 19: {'pos': (80, 81)}, 20: {'pos': (76, 62)}, 21: {'pos': (80, 119)}, 22: {'pos': (80, 127.5)}, 23: {'pos': (61, 127)}, 24: {'pos': (41, 127)}, 25: {'pos': (21, 127.5)}, 26: {'pos': (14, 118.5)}}
    intersection = [1, 2, 3, 4, 5, 6, 7, 12, 13, 15, 17, 19, 20, 22, 25, 26]
    dock = [1, 6, 25, 26]
    g = nx.Graph()
    g.add_edges_from(edges)
    nx.set_node_attributes(g, position)
    # print(g.nodes[1]["pos"])
    # print(g.edges())
    # pos = nx.spring_layout(g)
    path = nx.shortest_path(g, start, end)
    path_position = []

    inter_path = []
    for node in path:
        path_position.append(g.nodes[node]['pos'])
    for pa in path:
        if pa in intersection:
            inter_path.append(pa)
    inter_path_position = []
    for node in inter_path:
        inter_path_position.append(g.nodes[node]['pos'])
    # print(inter_path_position)
    # print(path_position)
    # print(path)
    # nx.draw(g, with_labels=True, font_weight='bold')
    # plt.show()
    return path_position, inter_path_position


if __name__ == "__main__":
    print(path_finder(1, 26))

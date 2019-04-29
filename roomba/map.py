import networkx as nx
# import matplotlib.pyplot as plt


def rang(f, s):
    arr = []
    while f <= s:
        arr.append(f)
        f = f+0.5
    return arr


def turn_finder(path, inter):
    is_dec_y = True
    is_dec_x = True
    left_side = False
    right_side = False
    top_side = False
    bottom_side = False
    lower_top_side = False
    high_bottom_side = False
    middle = False

    for i in range(len(path)):
        if path[i] == inter:

            if path[i][0] in rang(9, 21) and path[i-1][0] in rang(9, 21):
                left_side = True

            elif path[i][0] in rang(76, 80) and path[i-1][0] in rang(76, 80):
                right_side = True

            elif path[i][1] in rang(127.5, 133.5) and path[i-1][1] in rang(127.5, 133.5):
                top_side = True

            elif path[i][1] in rang(104, 119) and path[i-1][1] in rang(104, 119):
                lower_top_side = True

            elif path[i][1] in rang(41, 42) and path[i-1][1] in rang(41, 42):
                high_bottom_side = True

            elif path[i][1] in rang(8, 19) and path[i-1][1] in rang(8, 19):
                bottom_side = True
            else:
                middle = True

            # for j in range(i, -1, -1):
            j = i
            if (path[j][1] - path[j - 1][1]) > 0.5:
                is_dec_y = False
        # for j in range(i, -1, -1):
            elif (path[j][0] - path[j - 1][0]) > 0.5:
                is_dec_x = False

            # print(is_dec_x)
            # print(abs(path[i][1] - path[i - 1][1]), i)
            if (top_side or lower_top_side or high_bottom_side or bottom_side) and abs(path[i][1] - path[i - 1][1]) <= .5 and abs(path[i][1] - path[i + 1][1]) <= .5:
                # print('1')
                return 'go_straight'
            if (right_side or left_side or middle) and abs(path[i][0] - path[i - 1][0]) <= .5 and abs(path[i][0] - path[i + 1][0]) <= .5:
                    # print('2')
                return 'go_straight'
            if (top_side or lower_top_side or high_bottom_side or bottom_side) and not is_dec_x and path[i][1] > path[i + 1][1]:
                # print('2')
                return 'turn_right_90'
            if (top_side or lower_top_side or high_bottom_side or bottom_side) and is_dec_x and path[i][1] > path[i + 1][1]:
                # print('3')
                return 'turn_left_90'
            if (top_side or lower_top_side or high_bottom_side or bottom_side) and not is_dec_x and path[i][1] < path[i + 1][1]:
                # print('4')
                return 'turn_left_90'
            if (top_side or lower_top_side or high_bottom_side or bottom_side) and is_dec_x and path[i][1] < path[i + 1][1]:
                # print('5')
                return 'turn_right_90'

            if (right_side or left_side or middle) and is_dec_y and abs(path[i][0] - path[i - 1][0]) <= .5 and abs(path[i][0] - path[i + 1][0]) <= .5:
                print(6)
                return 'go_straight'
            if (right_side or left_side or middle) and is_dec_y and path[i][0] > path[i + 1][0]:
                # print(7)
                return 'turn_right_90'
            if (right_side or left_side or middle) and is_dec_y and path[i][0] < path[i + 1][0]:
                # print(8)
                return 'turn_left_90'
            if (right_side or left_side or middle) and not is_dec_y and path[i][0] > path[i + 1][0]:
                # print(9)
                return 'turn_left_90'
            if (right_side or left_side or middle) and not is_dec_y and path[i][0] < path[i + 1][0]:
                # print('me')
                return 'turn_right_90'


def front_rack_finder(tag=' < x: 064.5, y: 026.0 > [RtRack 05, col 1, LfRack 25, col 5] !pz!'):
    xy, contain = tag.split('[')
    x, y = xy[1:-2].split(', ')
    x = x.split(':')
    y = y.split(':')
    position = {1: {'pos': (21, 18.5)}, 2: {'pos': (76, 18)}, 3: {'pos': (76.5, 41.5)}, 4: {'pos': (53.5, 41.5)}, 5: {'pos': (31.5, 42)}, 6: {'pos': (14, 22)},
                7: {'pos': (13.5, 41.5)}, 8: {'pos': (14, 47.5)}, 9: {'pos': (14, 67.5)}, 10: {'pos': (14, 78)}, 11: {'pos': (14, 98)}, 12: {'pos': (14.5, 104.5)}, 13: {'pos': (31.5, 104.5)}, 14: {'pos': (41, 104.5)}, 15: {'pos': (54, 104.5)}, 16: {'pos': (61, 104.5)}, 17: {'pos': (80, 104.5)}, 18: {'pos': (80, 99)}, 19: {'pos': (80, 81)}, 20: {'pos': (76.5, 62)}, 21: {'pos': (80, 119)}, 22: {'pos': (80, 127.5)}, 23: {'pos': (61, 127.5)}, 24: {'pos': (41, 127)}, 25: {'pos': (21, 127.5)}, 26: {'pos': (14, 118.5)}}
    # print(contain)
    contain = contain[:-6].split(', ')
    newcontain = []
    for el in contain:
        le = el.split()
        le = {le[0]: int(le[1])}
        newcontain.append(le)
    for pos in position:
        if position[pos]['pos'] == (float(x[1]), float(y[1])):
            floor_id = pos
    return (float(x[1]), float(y[1])), newcontain, floor_id


def floor_finder(floor=' < x: 049.0, y: 013.5 > plz!'):
    floor_pos = floor[1:-6]
    x, y = floor_pos.split(', ')
    x = x.split(':')
    y = y.split(':')
    position = {1: {'pos': (21, 18.5)}, 2: {'pos': (76, 18)}, 3: {'pos': (76.5, 41.5)}, 4: {'pos': (53.5, 41.5)}, 5: {'pos': (31.5, 42)}, 6: {'pos': (14, 22)},
                7: {'pos': (13.5, 41.5)}, 8: {'pos': (14, 47.5)}, 9: {'pos': (14, 67.5)}, 10: {'pos': (14, 78)}, 11: {'pos': (14, 98)}, 12: {'pos': (14.5, 104.5)}, 13: {'pos': (31.5, 104.5)}, 14: {'pos': (41, 104.5)}, 15: {'pos': (54, 104.5)}, 16: {'pos': (61, 104.5)}, 17: {'pos': (80, 104.5)}, 18: {'pos': (80, 99)}, 19: {'pos': (80, 81)}, 20: {'pos': (76.5, 62)}, 21: {'pos': (80, 119)}, 22: {'pos': (80, 127.5)}, 23: {'pos': (61, 127.5)}, 24: {'pos': (41, 127)}, 25: {'pos': (21, 127.5)}, 26: {'pos': (14, 118.5)}}
    for pos in position:
        if position[pos]['pos'] == (float(x[1]), float(y[1])):
            floor_id = pos
    return (float(x[1]), float(y[1])), floor_id


def pallet_finder(pallet="/ pallet 056\ "):
    pallet = pallet[1:-2].split()
    return {pallet[0]: int(pallet[1])}


def rack_finder(cord='{pallet 104 @ rack 45, row 2, col 3} (dock A)'):
    racks = {8: {'lfrack': 45, 'col': 5, 'rtrack': None}, 9: {'lfrack': 45, 'col': 1, 'rtrack': None}, 10: {'lfrack': 72, 'col': 1, 'rtrack': None}, 11: {'lfrack': 72, 'col': 5, 'rtrack': None}, 14: {'lfrack': 57, 'col': 1, 'rtrack': None}, 16: {
        'lfrack': 57, 'col': 5, 'rtrack': None}, 21: {'lfrack': 23, 'col': 1, 'rtrack': None}, 18: {'lfrack': 23, 'col': 5, 'rtrack': None}, 23: {'lfrack': 64, 'col': (5, 1), 'rtrack': 46}, 24: {'lfrack': 64, 'col': (1, 5), 'rtrack': 46},
        28: {'lfrack': None, 'col': 5, 'rtrack': 7},
        29: {'lfrack': 36, 'col': (4, 1), 'rtrack': 7}, 30: {'lfrack': 36, 'col': (1, 4), 'rtrack': 7},
        31: {'lfrack': None, 'col': 5, 'rtrack': 13}, 32: {'lfrack': None, 'col': 1, 'rtrack': 80}, 33: {'lfrack': None, 'col': 4, 'rtrack': 80}, 34: {'lfrack': None, 'col':  5, 'rtrack': 42}, 35: {'lfrack': None, 'col': 1, 'rtrack': 42}, 36: {'lfrack': 91, 'col': 5, 'rtrack': None}, 37: {'lfrack': 91, 'col': 1, 'rtrack': None}, 42: {'lfrack': None, 'col': 1, 'rtrack': 13}}
    # edges = [(1, 2), (1, 6), (2, 3), (3, 4), (4, 5), (5, 7), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15),
    #  (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 3), (17, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 12)]
    # position = {1: {'pos': (21, 18.5)}, 2: {'pos': (76, 18)}, 3: {'pos': (76.5, 41.5)}, 4: {'pos': (43.5, 41.5)}, 5: {'pos': (31.5, 42)}, 6: {'pos': (14, 22)},
    # 7: {'pos': (13.5, 41.5)}, 8: {'pos': (14, 47.5)}, 9: {'pos': (14, 67.5)}, 10: {'pos': (14, 78)}, 11: {'pos': (14, 98)}, 12: {'pos': (14.5, 104.5)}, 13: {'pos': (31.5, 104.5)}, 14: {'pos': (41, 10.5)}, 15: {'pos': (54, 104.5)}, 16: {'pos': (61, 104.5)}, 17: {'pos': (80, 104)}, 18: {'pos': (80, 99)}, 19: {'pos': (80, 81)}, 20: {'pos': (76, 62)}, 21: {'pos': (80, 119)}, 22: {'pos': (80, 127.5)}, 23: {'pos': (61, 127)}, 24: {'pos': (41, 127)}, 25: {'pos': (21, 127.5)}, 26: {'pos': (14, 118.5)}}
    sub_string, dock = cord.split('}')
    dock = dock[2:-1].split()
    dock = {dock[0]: dock[1]}
    sub_string = sub_string.split('{')[1]
    pallet_rack, row, col = sub_string.split(', ')
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

    edges = [(1, 6), (1, 27), (6, 27), (1, 28), (28, 29), (29, 30), (30, 2), (2, 31), (31, 3), (3, 32), (32, 4), (4, 33), (33, 5), (5, 34), (34, 35), (35, 13), (4, 37), (37, 36), (36, 15), (3, 43), (43, 20), (20, 38), (38, 19), (39, 25), (39, 26), (5, 7), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15),
             (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (17, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 12)]
    position = {1: {'pos': (21, 18.5)}, 2: {'pos': (76, 18)}, 3: {'pos': (76.5, 41.5)}, 4: {'pos': (53.5, 41.5)}, 5: {'pos': (31.5, 42)}, 6: {'pos': (14, 22)},
                7: {'pos': (13.5, 41.5)}, 8: {'pos': (14, 47.5)}, 9: {'pos': (14, 67.5)}, 10: {'pos': (14, 78)}, 11: {'pos': (14, 98)}, 12: {'pos': (14.5, 104.5)}, 13: {'pos': (31.5, 104.5)}, 14: {'pos': (41, 104.5)}, 15: {'pos': (54, 104.5)}, 16: {'pos': (61, 104.5)}, 17: {'pos': (80, 104.5)}, 18: {'pos': (80, 99)}, 19: {'pos': (80, 81)}, 20: {'pos': (76.5, 62)}, 21: {'pos': (80, 119)}, 22: {'pos': (80, 127.5)}, 23: {'pos': (61, 127.5)}, 24: {'pos': (41, 127)}, 25: {'pos': (21, 127.5)}, 26: {'pos': (14, 118.5)}, 27: {'pos': (9.5, 8)}, 28: {'pos': (46, 18.5)}, 29: {'pos': (50.5, 18.5)}, 30: {'pos': (56, 18.5)}, 31: {'pos': (76.5, 29)}, 32: {'pos': (56, 41.5)}, 33: {'pos': (50.5, 41.5)}, 34: {'pos': (31.5, 60.5)}, 35: {'pos': (31.5, 80.5)}, 36: {'pos': (54, 80.5)}, 37: {'pos': (54, 60.5)}, 38: {'pos': (88, 71.5)}, 39: {'pos': (9, 133.5)}, 43: {'pos': (76.5, 49.5)}}
    intersection = [1, 2, 3, 4, 5, 6, 7, 12, 13, 15, 17, 19, 20, 22, 25, 26]
    dock = [1, 6, 25, 26, 39, 27, 38]
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
            # print(pa)
            inter_path.append(pa)
    inter_path_position = []
    for node in inter_path:
        # print(g.nodes[node]['pos'])
        inter_path_position.append(g.nodes[node]['pos'])
    # print(inter_path_position)
    # print(path_position)
    # print(path)
    # nx.draw(g, with_labels=True, font_weight='bold')
    # plt.show()
    return path_position, inter_path_position


if __name__ == "__main__":
    # print(front_rack_finder())
    path, inter = path_finder(19, 11)
    print(path)
    print(inter)
    for turn in inter[0:]:
        print(turn_finder(path, turn))

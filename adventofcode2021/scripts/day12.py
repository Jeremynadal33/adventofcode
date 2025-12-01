import sys
import time
from functions import *
import networkx as nx


def main():
    input_txt, part = handle_args(sys.argv)
    solve_puzzle(input=input_txt, part=part)


def solve_puzzle(input, part):
    if part == 1:
        solve_part_1(input)
    elif part == 2:
        solve_part_2(input)


def solve_part_1(input):
    print("Solving puzzle part 1")
    file = open(input, "r").read().split("\n")

    uppers = []
    G = nx.Graph()
    for line in file:
        left = line.split("-")[0]
        right = line.split("-")[1]
        G.add_edge(left, right)

        if left.isupper() and left not in uppers:
            uppers.append(left)
        if right.isupper() and right not in uppers:
            uppers.append(right)

    all_paths = find_all_paths(G, "start", "end", uppers)
    # print(all_paths)
    print(len(all_paths))

    # print([path for path in nx.all_simple_paths(G, 'start', 'end')])


def find_all_paths(graph, start, end, uppers, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []

    to_remove = set(path)
    for upper in uppers:
        if upper in to_remove:
            to_remove.remove(upper)

    for node in set(graph.neighbors(start)) - to_remove:
        paths.extend(find_all_paths(graph, node, end, uppers, path))
    return paths


def find_all_paths2(graph, start, end, uppers, lowers, vn=[]):
    vn = vn if type(vn) is list else [vn]
    path = []
    paths = []
    queue = [(start, end, path)]
    count = 0
    while queue:
        start, end, path = queue.pop()
        path = path + [start]

        if start in vn:
            print(start, " is in vianodes ", str(vn))
            pass  # paths.append(path)

        if start == end:
            paths.append(path)
            for key in lowers:
                lowers[key] = 0
        if start not in vn:
            to_remove = set(path)
            # for upper in uppers:
            #     if upper in to_remove:
            #         to_remove.remove(upper)

            for lower in lowers:
                if lower in to_remove:
                    # print('removed ', lower)
                    to_remove.remove(lower)
                    lowers[lower] += 1
            print(to_remove)
            for node in set(graph.neighbors(start)).difference(to_remove):
                queue.append((node, end, path))
        count += 1
    return paths


def solve_part_2(input):
    print("Solving puzzle part 2")
    file = open(input, "r").read().split("\n")
    lowers = {}
    uppers = []
    G = nx.Graph()
    for line in file:
        left = line.split("-")[0]
        right = line.split("-")[1]
        G.add_edge(left, right)
        if left.isupper() and left not in uppers:
            uppers.append(left)
        if (
            left.islower()
            and left not in lowers
            and (left != "start" and left != "end")
        ):
            lowers[left] = 0
        if right.isupper() and right not in uppers:
            uppers.append(right)

        if (
            right.islower()
            and right not in lowers
            and (right != "start" and right != "end")
        ):
            lowers[right] = 0

    print(uppers)
    all_paths = find_all_paths2(G, "start", "end", uppers, lowers)
    # print(all_paths)
    print(len(all_paths))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))

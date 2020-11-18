from anytree import Node, RenderTree
tree = dict()
depth_dict= dict()
node_mapstr = dict()
nonTerminal = list()
terminal = list()
rootKey = ''
productions = dict()

def top_down_parsing(inputStr, maxDepth):
    queue = []
    queue.append(rootKey)
    depth_dict[rootKey] = 0
    node_mapstr[rootKey] = Node(rootKey)
    uwv = ''
    input_found = False
    while queue and not input_found:
        q = queue.pop(0) # Node to analyze
        if depth_dict[q] + 1 > maxDepth:
            break
        done = False
        for i in range(len(q)):
            if q[i].isupper():
                node_part = q.partition(q[i]) # u - w - v
                break
        while not done and not input_found:
            rules = productions[node_part[1]]
            for w in rules:
                uwv = ''
                u = node_part[0]
                v = node_part[2]
                uwv += u + w + v # Left - Central new Production - Right
                nonTerminal_node = False
                for ch in uwv:
                    if ch.isupper():
                        nonTerminal_node = True
                        break
                prefix_match = True
                for i in range(len(u)):
                    if i < len(inputStr) and u[i] != inputStr[i]:
                        prefix_match = False
                        break
                if prefix_match:
                    if nonTerminal_node:
                        queue.append(uwv)
                    depth_dict[uwv] = depth_dict[q] + 1
                    insert_node(q, uwv)
                if uwv == inputStr:
                    input_found = True
                    break
            done = True
    print(tree)
    print(depth_dict)
    if input_found:
        print('----------The string is accepted----------')
    else:
        print('----------The string is not accepted----------')
    for pre, fill, node in RenderTree(node_mapstr[rootKey]):
        print("%s%s" % (pre, node.name))

def insert_node(key, node):
    if key not in tree.keys():
        tree[key] = list()
    tree[key].append(node)
    node_mapstr[node] = Node(node, node_mapstr[key])

test_name = input('Input test file name: ')
test_name = test_name + '.txt'
inputStr = input('Input string to test: ')
maxDepth = int(input('Max depth tree: '))

with open(test_name) as f:
    lines = f.readlines()
    nonTerminal = lines[0].strip().split(',')
    terminal = lines[1].strip().split(',')
    rootKey = lines[2].strip()
    for i in range(3, len(lines)):
        string_line = lines[i].split('->')
        key = string_line[0]
        value = string_line[1].strip()
        if key not in productions.keys():
            productions[key] = list()
        productions[key].append(value)
top_down_parsing(inputStr, maxDepth)


tree = dict()
depth_dict= dict()
nonTerminal = list()
terminal = list()
rootKey = ''
productions = dict()

def top_down_parsing(maxDepth, inputStr):
    queue = []
    queue.append(rootKey)
    depth_dict[rootKey] = 0
    uwv = ''
    input_found = False
    while queue and not input_found:
        q = queue.pop(0) # Node to analyze
        if depth_dict[q] + 1 > maxDepth:
            break
        done = False
        for i in range(len(q)):
            if q[i].isupper():
                node_part = q.partition(q[i]) # () - () - ()
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
                if nonTerminal_node and prefix_match:
                    depth_dict[uwv] = depth_dict[q] + 1
                    insert_node(q, uwv)
                    queue.append(uwv)
                if not nonTerminal_node and prefix_match:
                    depth_dict[uwv] = depth_dict[q] + 1
                    insert_node(q, uwv)
                if uwv == inputStr:
                    input_found = True
                    break
            done = True
    print(tree)
    print(depth_dict)
    print(input_found)

def insert_node(key, node):
    if key not in tree.keys():
        tree[key] = list()
    tree[key].append(node)

with open("test1.txt") as f:
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

top_down_parsing(10, 'abbbb')
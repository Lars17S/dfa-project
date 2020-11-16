tree = dict()
nonTerminal = list()
terminal = list()
rootKey = ''
productions = dict()

def top_down_parsing(maxDepth, inputStr):
    queue = []
    queue.append(rootKey)
    depth = 0
    uwv = ''
    while queue and depth != maxDepth and inputStr != uwv:
        q = queue.pop(0) # Node to analyze
        i = 0 # Used rule
        done = False
        for i in range(len(q)):
            if q[i].isupper():
                node_part = q.partition(q[i]) # () - () - ()
                break
        while not done and inputStr != uwv:
            rules = productions[node_part[1]]
            for w in rules:
                uwv = node_part[0] + w + node_part[2] # Left - Central new Production - Right
                # count_terminal = 0
                # for ch_uwv in uwv:
                #     if ch_uwv in terminal:
                #         count_terminal += 1
                insert_node(q, uwv)
                queue.append(uwv)
            done = True
        print('queue: ', queue)
        depth += 1
    print(tree)

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

top_down_parsing(6, 'XDalchnoentendi')
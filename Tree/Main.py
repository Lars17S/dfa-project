Tree = {'S': ['AbA', 'AsA'], 'AbA': [''], 'K': ['']}
nonTerminal = list()
terminal = list()
rootKey = ''
productions = dict()

def top_down_parsing(Tree, maxDepth, inputStr):
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
                count_terminal = 0
                for ch_uwv in uwv:
                    if ch_uwv in terminal:
                        count_terminal += 1
                


def insert_node(key, node):
    Tree[key].append(node)

with open("test1.txt") as f:
    lines = f.readlines()
    nonTerminal = lines[0].strip().split(',')
    terminal = lines[1].strip().split(',')
    rootKey = lines[2].strip()
    for i in range(3, len(lines)):
        string_line = lines[i].split('->')
        key = string_line[0]
        value = string_line[1].strip()
        if key in productions.keys():
            productions[key].append(value)
        else:
            productions[key] = list()
            productions[key].append(value)
    print(terminal)
    print(nonTerminal)
    print(rootKey)
    print(productions)

  

# for Parent, Children in Families.items():
#     print(f"{Parent} has {len(Children)} kid(s):")
#     print(f"{', and '.join([str(Child) for Child in [*Children]])}")

Tree = {'S': ['AbA', 'AsA'], 'AbA': [''], 'K': ['']}
nonTerminal = list()
terminal = list()
rootKey = ''
productions = dict()

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

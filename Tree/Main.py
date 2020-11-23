from anytree import Node, RenderTree

# Dictionary for parsing Tree
tree = dict()
# Dictionary to count the depth of the Tree created
depth_dict= dict()
# Dictionary to map strings and nodes
node_mapstr = dict()
# List of non-terminal symbols
nonTerminal = list()
# List of terminal symbols
terminal = list()
# Start symbol (string)
rootKey = ''
# Productions of the grammar
productions = dict()

def top_down_parsing(inputStr, maxDepth):
    """
    Implementation of the algorithm top-down parsing.

    Parameters
    ----------
    inputStr : str
        The input string evaluated by parsing Tree
    maxDepth : int
        Maximum depth of Tree to find the string
    """
    queue = []
    # Initialized queue, insert the root element 'S' into Tree
    queue.append(rootKey)
    depth_dict[rootKey] = 0
    node_mapstr[rootKey] = Node(rootKey)
    uwv = ''
    input_found = False
    # Start the process to find input string in parsing Tree
    while queue and not input_found:
        # Node to analyze
        q = queue.pop(0) 
        # If this depth is exceeded, it must stop the process
        if depth_dict[q] + 1 > maxDepth:
            break
        done = False
        # Find the first non terminal character starting from the left
        for i in range(len(q)):
            if q[i].isupper():
                node_part = q.partition(q[i]) 
                break
        # For the current string uwv, apply rules in w until
        # there are no more rules or string is found
        while not done and not input_found:
            rules = productions[node_part[1]]
            for w in rules:
                uwv = ''
                u = node_part[0]
                v = node_part[2]
                uwv += u + w + v 
                # Loop to check if the newly created node is non-terminal
                nonTerminal_node = False
                for ch in uwv:
                    if ch.isupper():
                        nonTerminal_node = True
                        break
                # Loop to check if uwv matches a prefix in input string
                prefix_match = True
                for i in range(len(u)):
                    if i < len(inputStr) and u[i] != inputStr[i]:
                        prefix_match = False
                        break
                if prefix_match:
                    # If there is prefix match and node is non-terminal
                    # then add it to the queue to be analyzed
                    # Otherwise, then just add to the tree (terminal node)
                    if nonTerminal_node:
                        queue.append(uwv)
                    depth_dict[uwv] = depth_dict[q] + 1
                    insert_node(q, uwv)
                # Check if the string was found
                if uwv == inputStr:
                    input_found = True
                    break
            done = True
    # Print the dictionary for Tree
    print(tree)
    # Print the dictionary of depth for each node
    print(depth_dict)
    # If the string was found, then print that the string is accepted
    if input_found:
        print('----------The string is accepted----------')
    else:
        print('----------The string is not accepted----------')
    # Print parsing Tree
    for pre, fill, node in RenderTree(node_mapstr[rootKey]):
        print("%s%s" % (pre, node.name))

def insert_node(key, node):
    """
    Function to insert node in Tree

    Parameters
    ----------
    key : str
        Parent node
    node : str
        Child node
    """
    if key not in tree.keys():
        tree[key] = list()
    tree[key].append(node)
    node_mapstr[node] = Node(node, node_mapstr[key])

# Read input from user, it asks for test file name, input string and
# maximum depth
test_name = input('Input test file name: ')
test_name = test_name + '.txt'
inputStr = input('Input string to test: ')
maxDepth = int(input('Max depth tree: '))

with open(test_name) as f:
    """
    Open txt file and parse input

    Parameters
    ----------
    test_name : str
        Test file name
    """
    lines = f.readlines()
    nonTerminal = lines[0].strip().split(',')
    terminal = lines[1].strip().split(',')
    rootKey = lines[2].strip()
    # Loop to read grammar productions
    for i in range(3, len(lines)):
        string_line = lines[i].split('->')
        key = string_line[0]
        value = string_line[1].strip()
        if key not in productions.keys():
            productions[key] = list()
        productions[key].append(value)

top_down_parsing(inputStr, maxDepth)


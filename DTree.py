import sys 
import csv
from Node import  Node

global data_file, n_record, n_attr, input_data, visited

# Function used for input data configuration
def config(args = "golf_processed.csv"):
    print(args)
    global data_file, n_record, n_attr, input_data, visited
    data_file = args
    input_data = []
    m_data = 0
    n_data = 0
    with open(data_file, 'r') as f:
        f = csv.reader(f, delimiter = ',')
        for line in f:
            m_data += 1
            vec = [int(i) for i in line]
            input_data.append(vec)
            n_data = len(vec)

    n_record = m_data
    n_attr = n_data - 1
    visited = [0] * n_attr


# Main function
def execute():
    global master
    master = []
    for i in range(len(input_data[0])):
        tm = set()
        for j in range(len(input_data)):
            tm.add(input_data[j][i])
        master.append(tm)
    print(master)
    root = Node()
    build_tree(input_data)
    #print(input_data)
    traverse_tree(root, 0)

# Function to build Tree
    # @param data   Data of passed in Node including Attribute data and label data
    # @param parent passed in Node
def attrless(indx,data):
    o1 = data[0:indx]
    o2 = data[indx+1:len(data)]
    return o1+o2
    
def fullattr(indx,data):
    final = []
    for i in range(len(data)):
        final.append(attrless(indx,data[i]))
    return final

def build_tree(data):
    print("Building Tree")
    print(data)
    print("\n")
    #for i in range(len(data[0])-1):
    #    g=fullattr(i,data)
    #    print(g)
    find_gini(1,1,data)
    find_gini(2,1,data)
    find_gini(3,1,data)
    #find_gini(1,2,data)
    #find_gini(2,2,data)
    #find_gini(3,2,data)
# Find gini index of given attribute data and corresponding Labels
    # @param  att Attribute data
    # @param  lab Label data
    # @return gini index of an attribute
def find_gini(att, lab, data):
    countattr = 0
    countlab = 0
    abs = set()
    for i in range(len(data)):
        if data[i][len(data[i])-1]==lab:
            countlab+=1
        if data[i][0]==att:
            countattr+=1
            abs.add(data[i][len(data[i])-1])
    print(str(countattr)+"/"+str(countlab))
    print(abs)
    return countlab
        # **-------------------Fill in here------------------------**/      
        # These steps might help you:
        #  - Find number of different values in attribute, number of different labels
        #  - For each value i, find number of occurrences and number of corresponding labels to calculate ginisplit
        #  - gini = sum of all ginisplit


# Use DFS to traverse tree and print nicely with appropriate indent
    # @param node traversing Node
    # @param indent appropriate indent for each level
def traverse_tree(node, indent):
    # Print out current node with appropriate indent
    for i in range(indent):
        print("'\t', end=")
    if (node.get_parent() is None):
        print("root")
    else:
        print("-/", node.get_data())

    # Recursive call all the children nodes
    children = []
    children = node.get_children()
    for i in range(node.get_n_child()):
        traverse_tree(children[i], indent + 1)

def main():
    arg = sys.argv[1:]
    if len(arg) > 0:
        config(arg)
    else:
        config()
    execute()

main()



import sys 
import csv
from Node import  Node

global data_file, n_record, n_attr, input_data, visited

# Function used for input data configuration
def config(args = "golf.csv"):
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
    master = []
    global solcnt
    solcnt = 0
    for i in range(len(input_data[0])):
        tm = set()
        for j in range(len(input_data)):
            tm.add(input_data[j][i])
        master.append(tm)
    print(master)
    solcnt = len(master[len(master)-1])
    print(solcnt)
    root = Node()
    baka = "root\n"+build_tree(input_data,master)
    print("CAKA WAKA SHAKA")
    print(baka)
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

def build_tree(data,master):
    print("Building Tree")
    print(data)
    print(master)
    print("\n")
    baka=""
    #for i in range(len(data[0])-1):
    #    g=fullattr(i,data)
    #    print(g)
    #a=find_gini(1,1,data)
    #b=find_gini(2,1,data)
    #c=find_gini(3,1,data)
    #print(a)
    #print(b)
    #print(c)
    #print(master)
    smallest=1.0
    newlists = []
    newlen=[]
    for i in range(len(master)-1):
        print("I wanna kill myself with: "+str(master[i]))
        ginis = []
        refug = []
        lens=[]
        qm = master[i].__iter__()
        for j in range(len(master[i])):
            z= qm.next()
            g = find_gini(z,1,data,i)
            lens.append(g[2])
            refug.append(g[1])
            g=g[0]
            ginis.append(g)
            print(g)
        gin = 0.0
        for ele in ginis:
            gin+=ele
        if gin < smallest:
            smallest = gin
            newlists=refug[:]
            next = i
            newlen=lens[:]
    #gin = 1-gin
        print("The Gini is"+str(gin))
    print("We're gonna split on"+str(master[next])+" With ")
    printee(newlists)
    printee(newlen)
    for i in range(len(newlen)):
        if newlen[i]>1:
            newmaster=[]
            build_tree(newlists[i],newmaster)
    #find_gini(1,2,data)
    #find_gini(2,2,data)
    #find_gini(3,2,data)
    return baka
# Find gini index of given attribute data and corresponding Labels
    # @param  att Attribute data
    # @param  lab Label data
    # @return gini index of an attribute
def find_gini(att, lab, data, lst):
    countattr = 0.0
    countlab = 0.0
    cc = 0.0
    abs = set()
    refug = []
    global solcnt
    thistoo = []
    for i in range(len(data)):
        if data[i][len(data[i])-1]==lab:
            countlab+=1.0
        if data[i][lst]==att:
            countattr+=1.0
            abs.add(data[i][len(data[i])-1])
            refug.append(data[i])
    for i in range(len(refug)):
        if refug[i][len(refug[0])-1]==1:
            cc+=1.0
    print(str(cc)+"/"+str(countattr)+"&"+str(countattr-cc)+"/"+str(countattr)+ " of " + str(len(data)))
    #print("CC is :"+str(cc))
    n0 = (cc/countattr)**2
    n1 = ((countattr-cc)/countattr)**2
    final = 1-(n0+n1)
    print("gini is  :"+str(final))
    #print()
    final = final*(countattr/len(data))
    #print()
    #print()
    #return (countattr,refug,len(abs))
    return (final,refug,len(abs))
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
        

def printee(what):
	print('\n')
	for ele in what:
		print(ele)

def main():
    arg = sys.argv[1:]
    if len(arg) > 0:
        config(arg)
    else:
        config()
    execute()

main()



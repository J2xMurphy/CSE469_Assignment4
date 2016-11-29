import sys 
import csv
from Node import  Node
solcnt= 0
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
    master = master_maker(input_data)
    global solcnt
    solcnt = 0
    #print(master)
    solcnt = len(master[len(master)-1])
    #print(solcnt)
    root = Node()
    baka = "root\n"+str(build_tree(input_data,master,"",[]))
    print("CAKA WAKA SHAKA")
    print(baka)
    write_string('output.txt',baka)
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
    
def master_maker(input_data):
    master = []
    solcnt = 0
    for i in range(len(input_data[0])):
        tm = set()
        for j in range(len(input_data)):
            tm.add(input_data[j][i])
        master.append(tm)
    return master
    
def build_tree(data,master,ts,off):
    #print("Building Tree")
    baka=""
    nts = ""
    #print(len(ts))
    for i in range(len(ts)):
        #print(ts[i])
        if ts[i]=='|':
            nts+="|"
        else:
            nts+=" "
    if len(data[0])<3:
        c=mayday(data)
        print(c)
        for ele in c:
            baka+=nts+"|->(A"+str(len(off))+":"+str(ele[0])+")->"+str(ele[1])+"\n"
        return '!'+baka
    smallest=1.0
    newlists = []
    newlen=[]
    for i in range(len(master)-1):
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
        gin = 0.0
        for ele in ginis:
            gin+=ele
        if gin < smallest:
            smallest = gin
            newlists=refug[:]
            next = i
            newlen=lens[:]
    #printee(newlists)
    #print(off,next)
    ww = 0
    for ele in off:
        if ww>=ele:
            next+=1
    off.append(next)
    for i in range(len(newlen)):
        if newlen[i]>1:
            nl = fullattr(next,newlists[i])
            newmaster=master_maker(nl)
            caw = build_tree(nl,newmaster,ts+"|--------> ",off)
            if '!' in caw:
                baka+=nts+"|------>(A"+str(next+1)+":"+str(i+1)+")\n"
                baka+=caw[1:]
            else:
                baka+=nts+"|------>(A"+str(next+1)+":"+str(i+1)+")\n"
                baka+=ts+caw
        else:
            baka+=nts+"|->(A"+str(next+1)+":"+str(i+1)+")->"+str(newlists[i][0][len(newlists[i][0])-1])+"\n"
    return baka
    
    
def find_gini(att, lab, data, lst):
    countattr = 0.0
    countlab = 0.0
    cc = 0.0

    abs = set()
    refug = []
    thistoo = []
    ofeach = []
    for i in range(solcnt):
        ofeach.append(0.0)
    for i in range(len(data)):
        if data[i][len(data[i])-1]==lab:
            countlab+=1.0
        if data[i][lst]==att:
            countattr+=1.0
            thistoo.append(data[i][len(data[i])-1])
            abs.add(data[i][len(data[i])-1])
            refug.append(data[i])
    for i in range(len(refug)):
        if refug[i][len(refug[0])-1]==1:
            cc+=1.0
    for i in range(len(thistoo)):
        ofeach[thistoo[i]-1]+=1.0
    #print("HHAHAH"+str(ofeach))
    finali = 1.0
    #print(ofeach)
    for i in range(len(ofeach)):
        g=(ofeach[i]/countattr)**2
        #g=g*len(data)
       # print(str(ofeach[i])+"/"+str(countattr)+"="+str(g))
        finali-=g
    finali = finali*(countattr/len(data))
    return (finali,refug,len(abs))


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
        
def mayday(data):
    final = []
    finali=[]
    sols = set()
    suls = set()
    for ele in data:
        if final.count(ele)>0:
            finali[finali.index(ele)+1]+=1
            #print(finali[finali.index(ele)+1])
        else:
            suls.add(ele[1])
            sols.add(ele[0])
            final.append(ele)
            finali.append(ele)
            finali.append(1)
   # print("\n\n")
    #print(sols)
    qm = sols.__iter__()
    #for ele in finali:
    #    print(ele)
    final=[]
    for j in range(len(sols)):
        max = []
        maxn = 0
        z=qm.next()
        for i in range(len(finali)/2):
            #print(str(finali[(i*2)][0])+" of "+str(z))
            if finali[(i*2)+1]>maxn and finali[(i*2)][0]==z:
                max=finali[i*2]
                maxn = finali[(i*2)+1]
        final.append(max)
    printee(finali)
    return final
    
	

def write_string(txt,output):
    f = open(txt, 'w')
    f.write(str(output))
    f.close();
    
def printee(what):
	#print('\r\n')
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



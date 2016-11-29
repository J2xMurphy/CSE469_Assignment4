import sys 
import csv
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


def execute():
    master = master_maker(input_data)
    global solcnt
    solcnt = 0
    solcnt = len(master[len(master)-1])
    baka = "root\n"+str(build_tree(input_data,master,"",[]))
    print(baka)
    write_string('output.txt',baka)

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
    baka=""
    nts = ""
    for i in range(len(ts)):
        if ts[i]=='|':
            nts+="|"
        else:
            nts+=" "
    if len(data[0])<3:
        c=mayday(data)
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
    finali = 1.0
    for i in range(len(ofeach)):
        g=(ofeach[i]/countattr)**2
        finali-=g
    finali = finali*(countattr/len(data))
    return (finali,refug,len(abs))

        
def mayday(data):
    final = []
    finali=[]
    sols = set()
    suls = set()
    for ele in data:
        if final.count(ele)>0:
            finali[finali.index(ele)+1]+=1
        else:
            suls.add(ele[1])
            sols.add(ele[0])
            final.append(ele)
            finali.append(ele)
            finali.append(1)
    qm = sols.__iter__()
    final=[]
    for j in range(len(sols)):
        max = []
        maxn = 0
        z=qm.next()
        for i in range(len(finali)/2):
            if finali[(i*2)+1]>maxn and finali[(i*2)][0]==z:
                max=finali[i*2]
                maxn = finali[(i*2)+1]
        final.append(max)
    return final
    
	

def write_string(txt,output):
    f = open(txt, 'w')
    f.write(str(output))
    f.close();
    
def printee(what):
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
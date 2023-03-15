q_list=[]
a_list=[]
qlist=open("q_list.txt", "r", encoding='UTF-8')
alist=open("a_list.txt", "r", encoding='UTF-8')

q_list=qlist.readlines()
a_list=alist.readlines()

for i in range (0, len(q_list)):
    q_list[i]=q_list[i].replace('\n','')
    # a_list[i]=a_list[i].replace('\n','')
    i+=1

help_list=[]
for i in range (0, len(q_list)):
    help_list.append(q_list[i])
    i+=1

help_return=help_list[0]+"\n"
for j in range (1, len(q_list)):
    help_return+=help_list[j]+"\n"
    j+=1
id_skulpt = {}
ideal_skulpt = []
not_ideal_skulpt = []
search_id = []
m = []
control_summ_T = 0
count_skulpt = 0

def search(myDict, search1):
    search.a=[]
    for i in search1:
        for key, value in myDict.items():
            if i in value:
                search.a.append(key)

#insert
N, X, T = map(int, input().split())

for a in input().split():
    m.append(int(a))

#список подходящих элементов
id_skulpt = {m[i]: i for i in range(len(m))}
id_skulpt = { v:str(k) for k, v in id_skulpt.items()}

for i in m:

    if abs(X-i) == 0:
        search_id.append(str(i))
        ideal_skulpt.append(i)      
    elif abs(X-i) <= T:
        not_ideal_skulpt.append(i)

if not_ideal_skulpt:
    not_ideal_skulpt.sort()

    for i in not_ideal_skulpt:
        c = abs(X-i)
        if (control_summ_T + c) <= T:
            control_summ_T = control_summ_T + c
            search_id.append(str(i))
            count_skulpt +=1
        elif count_skulpt == 0: 
            search_id.append(str(i))

search(id_skulpt, search_id)
print(len(search_id))
z=search.a
z.sort()
print(*[x+1 for x in z]) if z else print(0)
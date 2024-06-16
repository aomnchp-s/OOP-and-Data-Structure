person:dict[str, str|int] = {'id':10,'name':'Natchaporn','birth':'20/07/1995'}
for a,b in person.items():
    print(f'{a}: {b}')

persons = [
    {'id':10,'name':'Natchaporn1','birth':'20/07/1995'},
    {'id':11,'name':'Natchaporn2','birth':'20/07/1995'},
    {'id':12,'name':'Natchaporn3','birth':'20/07/1995'},
]
for person in persons:
    #print(p)
    for k,v in person.items():
        print(f'{k}, {v}')
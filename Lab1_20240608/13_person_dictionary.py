person = {'id':1,'name':'natchaporn','birthdate':'23/03/1997'}
print(person)
personLst = []
personLst.append(person)

input = input('Enter Personal id name birth: ')
inputLst = [data for data in input.split()]
inputDict = {}
inputDict['id'] = int(inputLst[0])
inputDict['name'] = inputLst[1]
inputDict['birthdate'] = inputLst[2]
personLst.append(inputDict)

print(personLst)










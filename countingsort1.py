List = [0, 3, 1, 1]

nodupList = list(set(List))
nodupList.sort() 
print(nodupList)
ListCount = [0]* (max(List)-min(List)+1)
n = len(List)

for i in range(n):
  ListCount[List[i]-min(List)]+=1
print(ListCount)


sortedList = []

for i in nodupList:
  for j in range(ListCount[i-min(List)]):
    sortedList.append(i)
    print(sortedList)

n = len(List)

for i in range(n):
  minimum = List[i]
  minIndex = i
  for j in range(i+1,n):
    if List[j]<minimum:
      minimum = List[j]
      minIndex = j
  List[minIndex], List[i] = List[i], List[minIndex]
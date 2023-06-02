answer = []
while 1 :
  i = input()
  if i == '0' : break
  eq = True
  for j in range (len(i) // 2) :
    if (i[j] != i[-(j+1)]) :
      answer.append("no")
      eq = False
      break
  if eq : answer.append("yes")
for a in answer : print(a)
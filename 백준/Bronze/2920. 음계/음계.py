nums = [int(i) for i in input().split()]
done = False
asc = True
count = 0

for i in range (8) :
  # process first index value
  if i == 0 :
    if nums[0] == 1 :
      count = 1 + 1
      asc = True
    elif nums[0] == 8 :
      count = 8 - 1
      asc = False
    else : done = True

  else :
    if nums[i] != count :
      done = True
    else :
      if asc : count += 1
      else : count -= 1

  if done :
    print("mixed")
    break

if not done and asc :
  print("ascending")
elif not done and not asc :
  print("descending")
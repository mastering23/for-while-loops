#for and while loops
for number in range(5):
    print(number,number * f'yeaaah ')

print('\n------Condictions---------')

findNumber = 3
 
print(f"Find the number : {findNumber}")
for number in range(5):
  print(number)
  if number == findNumber:
    print("Number found", findNumber)
    break
else:
  print("Didn't find the number")
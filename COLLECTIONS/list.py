l1=[12,9,24,"joker","luck","maths","q"]
l2=[19,2002,7,1,2002,2002]
print("1.len()\n 2.append()\n  3.extend()\n  4.insert()\n  5.remove()\n  6.pop()\n  7.reverse()\n  8.min()\n  9.max()\n  10.count()\n  11.sort()\n  12.index()\n  13.clear()\n 14.multiplication()\n 15.concatenation()\n 16.DataType()")
print(l1)
print(l2)
choice=int(input("Enter your choice:"))
if(choice==1):
  ch=int(input("Enter  the list number : "))
  if(ch==1):
    print("length of the list-1")
    print(len(l1))
  elif(ch==2):
    print("length of the list-2")
    print(len(l2))
elif (choice==2):
  ch=int(input("Enter the list number to append : "))
  if(ch==1):
    c=int(input("Enter 1 for number and enter 2 for character \n choice:"))
    if(c==1):
      n = int(input("Enter the Number to append"))
      print("append a item in a list")
      l1.append(n)
    elif(c==2):
      k = str(input("Enter the Value to append"))
      print("append a item in a list")
      l1.append(k)
    else:
      print("Invalid")
    print("Now printing the current list")
    print(l1)
  elif(c==2):
    c=int(input("Enter 1 for number and enter 2 for character \n choice:"))
    if(c==1):
      n = int(input("Enter the Number to append"))
      print("append a item in a list")
      l2.append(n)
    elif(c==2):
      k = str(input("Enter the Value to append"))
      print("append a item in a list")
      l2.append(k)
    else:
      print("Invalid")
    print("Now printing the current list")
    print(l2)
  else:
    print("Invalid")

elif (choice==3):
  ch=int(input("Enter 1 to number or 2 to character or 3 for both number and character"))
  if(ch==1):
    n = int(input("Enter the number to Extend"))
    l1.extend([n])
    print("Now printing the current list")
    print(l1)
  elif(ch==2):
    m = str(input("Enter the value to extend"))
    l1.extend([m])
    print("Now printing the current list")
    print(l1)
  elif(ch==3):
    n = int(input("Enter the number to Extend"))
    m = str(input("Enter the value to extend"))
    l1.extend([n,m])
    print("Now printing the current list")
    print(l1)
  else:
    print("Invalid")
elif (choice==4):
  m = int(input("Enter the position"))
  ch=int(input("Enter 1 for number and enter 2 for character \n choice:"))
  if(ch==1):
    n = int(input("Enter the Number to Insert"))
    print("adding a item in a list by specifying the position")
    l1.insert(m,n)
  elif(ch==2):
    k = str(input("Enter the Value to Insert"))
    print("adding a item in a list by specifying the position")
    l1.insert(m,k)
  else:
    print("Invalid")
  print("Now printing the current list")
  print(l1)
elif (choice==5):
  ch=int(input("Enter 1 for number to remove and enter 2 for character to remove \n choice:"))
  if(ch==1):
    n = int(input("Enter the Number to Remove"))
    print("Removing a item in a list")
    l1.remove(n)
  elif(ch==2):
    k = str(input("Enter the Value to Remove"))
    print("Removing a item in a list")
    l1.insert(k)
  else:
    print("Invalid")
  print("Now printing the current list")
  print(l1)
elif (choice == 6):
  n=int(input("Enter the position to pop the item in a list"))
  l1.pop(n)
  print("Now printing the current list")
  print(l1)
elif (choice ==7):
  ch=int(input("Enter 1 to reverse list1 and enter 2 to reverse list2 \n choice:"))
  if(ch==1):
    print("Reverse of the List1")
    l1.reverse()
    print("Now printing the current list")
    print(l1)
  elif(ch==2):
    print("Reverse of the List2")
    l2.reverse()  
    print("Now printing the current list")
    print(l2)
  else:
    print("Invalid")
elif (choice ==8):
    print("Minimum of the List2")
    print(min(l2))  
    print("Now printing the current list")
    print(l2)
elif (choice ==9):
    print("Maximum of the List2")
    print(max(l2))
    print("Now printing the current list")
    print(l2)
elif (choice == 10):
    print("List 2")
    print(l2)
    n=int(input("Printing the occurrence"))
    print(l2.count(n))
elif (choice == 11):
    print("Sorting the list-2 in a order")
    l2.sort()
    print(l2)
elif (choice ==12):
  ch=int(input("Enter 1 to view list1 and 2 to view list2"))
  if(ch==1):
    print(" List1")
    print(l1)
    c=int(input("Enter 1 to type numbers and 2 to type characters"))
    if(c==1):
      n=int(input("Enter the value to find the index"))
      print(l1.index(n))
    elif(c==2):
      n=str(input("Enter the value to find the index"))
      print(l1.index(n))
  elif(ch==2):
    print(" List2")
    print(l2)
    n=int(input("Enter the value to find the index"))
    print(l2.index(n))
  else:
    print("Invalid")
elif(choice ==13):
  ch=int(input("Enter the 1 to clear list 1 and 2 for list 2"))
  if(ch==1):
    print("Clearing the List 1")
    l1.clear()
  elif(ch==2):
    print("Clearing the List 2")
    l2.clear()
elif(choice == 14):
  ch=int(input("Enter the list number"))
  if(ch==1):
    n=int(input("Enter the number of times to multiply the list"))
    print("Multiplying list 1")
    print(l1*(n))
  elif(ch==2):
    n=int(input("Enter the number of times to multiply the list"))
    print("Multiplying list 1")
    print(l2*(n))
  else:
    print("Invalid")
elif(choice == 15):
  print("Concatenate two lists")
  l3=l1+l2
  print("After Concatenating:" ,l3)
elif(choice == 16):
  ch=int(input("Enter the 1 to view the data type of list-1 and 2 to view the data type of list-2"))
  if(ch==1):
    print(type(l1))
  elif(ch==2):
    print(type(l2))
  else:
    print("Invalid")
else:
  print("Invalid")

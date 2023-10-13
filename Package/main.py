import creatures
print("Find your information about creatures:examples and characteristics")
while(1):
     print("Press\n1 for fish\n2 for birds\n3 for amphibians\n4 for mammals\n5 for reptiles\n6 to exit:")
     c=int(input())
     if c==1:
         creatures. fish.examples()
         creatures. fish.chars()
     elif c==2:
         creatures. birds.examples()
         creatures. birds.chars()
     elif c==3:
         creatures. amphibians.examples()
         creatures. amphibians.chars()
     elif c==4:
         creatures. mammals.examples()
         creatures. mammals.chars()
     elif c==5:
         creatures. reptiles.examples()
         creatures. reptiles.chars()
     elif c==6:
         print("Thank You!!!")
         break
     else:
         print("Wrong input")

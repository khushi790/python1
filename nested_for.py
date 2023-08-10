''' 00000
    11111
    22222
    33333
    44444 '''
for i in range(0,5):
    for j in range(0,5):
        print(i,end="")
    print("\n")
       
''' *
    **
    ***
    **** '''
for i in range(0,5):
    for j in range(0,i):
        print("*",end="")
    print("\n")

''' *****
    *****
    *****
    *****
    ***** '''
for i in range(0,5):
    for j in range(0,5):
        print("*",end="")
    print("\n")
       
''' 1
    22
    333
    4444  '''
for i in range(0,5):
    for j in range(0,i):
        print(i,end="")
    print("\n")

''' 1
    22
    333
    4444  '''
for i in range(5,0,-1):
    for j in range(1,i+1,):
        print("*",end="")
    print("\n")

'''     *
       **
      ***
     ****
    ***** '''
for i in range(0,5):
    for j in range(1,5-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end="")
    print("\n")
       
'''*****
    ****
     ***
      **
       * '''
for i in range(0,5):
    for j in range(0,i):
        print(" ",end="")
    for k in range(5,i,-1):
        print("*",end="")
    print("\n")
       

''' *****
    *   *
    *   *
    *   *
    *****  '''
for i in range(0,5):
    for j in range(0,5):
        if(i==0 or j==0 or i==4 or j==4):
            print("*",end="")
        else:
            print(" ",end="")
    print("")  
#print position of element using while loop
my_list=[10,20,30,40,50]
index=0
while(index<len(my_list)):
    print(index)
    index=index+1

#print element and position of element  of list using while loop
my_list=[10,20,30,40,50]
index=0
while(index<len(my_list)):
    print(index,my_list[index])
    index=index+1

#print even element of list using while loop
my_list=[10,20,21,30,40,77,50]
index=0
while(index<len(my_list)):
    if(my_list[index]%2==0):
        print(index,my_list[index])
    index=index+1

#add 5 in each even element of a list
my_list=[10,20,21,30,40,77,50]
index=0
while(index<len(my_list)):
    if(my_list[index]%2==0):
        print(index,my_list[index],my_list[index]+5)
        my_list[index]=my_list[index]+5
    index=index+1

#prg to print only words from a list without first character of word
mylist=[10,20,"hey",40,"yash"]
strlist=[]
for data in mylist:
    if(type(data) is str):
        print(data,data[1:])
        strlist.append(data[1:])
print(strlist)

# Create a program to identify all the unique words or element from list and insert alll the duplicate elements in other list
mylist=["apple",10,"banana",33,"cherry","apple",33,"banana"]
Unique_words = []
Duplicate_words = []
for word in mylist:
    if mylist.count(word)>1:
        if word not in Duplicate_words:
            Duplicate_words.append(word)
    else:
        if word not in Unique_words:
            Unique_words.append(word)
print("Duplicate Words List:",Duplicate_words)
print("Unique Words List:",Unique_words)

# Create a program to get string element which have more than 2 vowels and append it into the vowelList
mylist=["apple","banana","cherry","elephant","grape","orange"]
vowelList=[]
vowels="aeiou"
for word in mylist:
    count=0
    for letter in word:
        if letter.lower() in vowels:
            count+=1
    if count>2:
        vowelList.append(word)
print("Words with more than 2 vowels:",vowelList)



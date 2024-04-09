#access elements by using python
list=[1,2,3,4,5,6]
print(list[0])
#output 1
#2 slice
list_2 =[30,4,5,6,7,8]
print(list_2[1:5])
#concatenate
concatenate =list+list_2
print(concatenate)
#repeat list 3 times
repeat = list*3
print(repeat)
#pick one element from the list 
print(3 in list)#output =true
#length
print(len(list))
list_3=['cabbage','apples','onions']
list_3.sort()
print(list_3)
months=['jan','feb','march']
months.sort()
print(months)
sortkey=['this is my laptop','word','two']
sortkey.sort(key=len, reverse=True)
print(sortkey)
#add to list
sortkey[0]='cabbage'
sortkey.append('kiwi')
print(sortkey)

for x in range(4):
    print(x)
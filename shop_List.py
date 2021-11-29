shopList = ["banana","apple", "orange","grapes", "guava"]
shopList.append("mango")
shopList[0] = "lemon"
del shopList[2]
listcount = len(shopList)
print(shopList)
print(listcount)

brekfast_List = ["bread", "butter"]
listAdd = shopList+brekfast_List

print(listAdd)
print("length of list : ",len(listAdd))

listMultiply = listAdd*2
print(listMultiply)

# max function in list
intList = [8,1,3,4,9,2,0]
intList1 = [8,1,3,4,9,2,0]
print(max(intList))
print(min(intList))
del intList1[4]
print(max(intList1))
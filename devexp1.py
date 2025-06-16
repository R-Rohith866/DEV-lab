import matplotlib.pyplot as plt
#X=[1,2,3,4,5]
#Y=[10,20,30,40,50]
#plt.plot(X,Y)


fruits=["Apple","Banana","Cherry","Watermelon","Mango"]
sales=[400,350,300,450,500]
plt.bar(fruits,sales)
plt.title("fruit sales")
plt.xlabel("fruits")
plt.ylabel("sales")
plt.show()

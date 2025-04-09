ac=float(input("Enter the actual price of item:"))
sc=float(input("Enter the selling price of item:"))

if sc>ac:
    a=sc-ac
    print("Profit=",a)

else:
    b=ac-sc
    print("Loss=",b)
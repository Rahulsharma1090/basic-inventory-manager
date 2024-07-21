import csv
"""file=open('inventories.csv','w')
csv_writer=csv.writer(file)
csv_writer.writerow(["PRODUCT","QUANTITY"])
file.close()"""
while True:
    question=input("want to add? Y OR N : ")
    if (question!="Y"):
        break
    else:
        file=open('inventories.csv','a', newline='')
        product=input("enter product name :")
        quantity=input("enter quantity of product :")
        csv_writer=csv.writer(file)
        csv_writer.writerow([product,quantity])
        file.close()
def search(productname):
    file=open("inventories.csv","r")
    reader=csv.DictReader(file)
    for row in reader:
        if(row["PRODUCT"]==productname):
            return row
"""a=search("DISPRIN")
b=search("adada")
print(a,b)"""
def addaproduct(productname,quantity):
    with open("inventories.csv","a") as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow([productname,quantity])
def buyingaproduct(productname,quantity):
    with open('inventories.csv','a') as file:
        csv_writer.writerow([productname])
    

        
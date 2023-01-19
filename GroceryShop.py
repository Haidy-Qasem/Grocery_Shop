import csv
from tabulate import tabulate

labels = ['Elements','Quantity','Price']
with open("iti_grocery.csv","r") as f:
    reader_file = csv.reader(f)
    grocery_list = list(zip(*reader_file))
#grocery product_details
grocery_products=[]
grocery_quantities=[]
grocery_prices=[]
grocery_shop=[ grocery_products,grocery_quantities,grocery_prices]
#the bill
customer_products=[]
customer_quantity=[]
customer_price=[]
customer_list=[customer_products,customer_quantity,customer_price]
a=len(grocery_list[0])
total_cost=0
print("                                  Welcome to ITI Grocery\n")
print("For Customer mode press 1\nFor Owner mode press 2\nTo Exit press 0")
n=input("Enter your mode\n")
x= True	
if n=='1': 
	grocery_shop =[list(i) for i in grocery_list]
	grocery_products = grocery_shop[0]
	grocery_products.pop(0)
	grocery_quantities = grocery_shop[1]
	grocery_quantities.pop(0)
	grocery_quantities = [eval(i) for i in grocery_quantities]
	grocery_prices = grocery_shop[2]
	grocery_prices.pop(0)
	grocery_prices = [eval(i) for i in grocery_prices]
	grocery_shop=[grocery_products,grocery_quantities,grocery_prices]
	while (True):
		print("To show our products press 1\nTo buy our products press 2\nTo print your bill press 3\nTo quit please press 0")
		z=input("Please enter your choice:")
		if z=='1':
			print(grocery_shop)
			print("\nDo you want to continue:")
			print("Press 1 to continue shopping")
			print("Press 2 to exit")
			a=input("Please enter your choice:")    
			if a=='1':
				x=True
			elif a=='2':
				x=False   
			else:
				print("Inavailable choice\n")
				x=False
			
		elif z=='2':
			counter=0
			print("ITI Grocery Products:")
			print(grocery_shop)
			while(x==True):
				product_name=str(input("Enter the Product Name:"))
				for i in range(len(grocery_products)):
					if product_name==grocery_products[i]:
						customer_products.insert(counter,product_name)
						quantity=int(input("Enter the Product quantity:"))
						if quantity<=grocery_quantities[i]:
							customer_quantity.insert(counter,quantity)
							customer_price.insert(counter,quantity*grocery_prices[i])
							total_cost +=quantity*grocery_prices[i]
							grocery_quantities[i]-=quantity
							# with open("Order.csv",'w',newline='') as file_2:
								# file1_writer = csv.writer(file_2)
								# file1_writer.writerow(labels)
								# file1_writer.writerows(zip(*customer_list))
						else:
							print("Sorry not available quantity")
				if not customer_products:
						print("Sorry the element does not exist")
				print("Do you want to continue:")
				print("Press 1 to continue shopping")
				print("Press 2 to exit")
				o=input("Please enter your choice:")
				if o=='1':
					x=True
					counter+=1
				elif o=='2':
					x=False
				else:
					print("Wrong choice\n")
					x=False
		elif z=='3':
			with open('ITI_Bill.txt','w') as bill:
				bill.write("ITI Grocery Fatora\n")
				bill.write(tabulate(zip(*customer_list), headers=labels, tablefmt="grid"))
				bill.write("\nTotal cost ="+str(total_cost))
		elif z=='0':
			break
		
elif n=='2' :
	p=input("Enter the owner Password:\n") #pass=123
	grocery_shop =[list(i) for i in grocery_list]
	grocery_products = grocery_shop[0]
	grocery_products.pop(0)
	grocery_quantities = grocery_shop[1]
	grocery_quantities.pop(0)
	grocery_quantities = [eval(i) for i in grocery_quantities]
	grocery_prices = grocery_shop[2]
	grocery_prices.pop(0)
	grocery_prices = [eval(i) for i in grocery_prices]
	grocery_shop=[grocery_products,grocery_quantities,grocery_prices]
	if p=='123':
		print("*****************************************************Products & Price*****************************************************")
		while True:
			print("To Add new Products Press1\nTo Show Products & Prices Press2\nTo Add Quantity of a Product Press3\nTo Change Cost of a Product Press 4\nTo Exit Press 0")
			x=input("Enter Owner Mode")
			if x=='1':
				product_name=str(input("Enter the Product name:"))
				grocery_products.insert(a,product_name)
				quantity=int(input("Enter the product quantity:"))
				grocery_quantities.insert(a,quantity)
				price=int(input("Enter the one element price:"))
				grocery_prices.insert(a,price)
				a+=1
				print("Do you want to continue:")
				print("Yes:press 1")
				print("No:press 2")
				y= input("Please enter your choice:")
				if y=='1':
					continue
				elif y=='2':
					break
				else:
					print("Inavailable choice\n")
					break
			elif x=='2':
				print(grocery_shop)
				print("Do you want to continue:")
				print("Yes:press 1")
				print("No:press 2")
				m= input("Please enter your choice:")
				if m=='1':
					continue
				elif m=='2':
					break
				else:
					print("Inavailable choice\n")
					break
			elif x=='3':
				product_name=str(input("Enter the product name:"))
				for i in range(len(grocery_products)):
					if product_name==grocery_products[i]:
						quantity=int(input("Enter the product quantity:"))
						grocery_quantities[i]=quantity
				print("Do you want to continue:")
				print("Yes:press 1")
				print("No:press 2")
				j= input("Please enter your choice:")
				if j=='1':
					continue
				elif j=='2':
					break
				else:
					print("Wrong choice\n")
					break
			elif x=='4':
				product_name=str(input("Enter the product name :"))
				for i in range(len(grocery_products)):
					if product_name==grocery_products[i]:
						price=int(input("Enter the price:"))
						grocery_prices[i]=price
				print("Do you want to continue:")
				print("Yes:press 1")
				print("No:press 2")
				k=input("Please enter your choice:")
				if k=='1':
					continue
				elif k=='2':
					break
				else:
					print("Wrong choice\n")
					break
			elif x=='0':
				break
	else:
		print("Wronr Password")
		quit()
	
elif n== '0' :
	x=0
	print("                                End of Processs")
	quit()
else:
	print("Wrong Choice")

with open("iti_grocery.csv",'w',newline='') as file_1:
    file_writer = csv.writer(file_1)
    file_writer.writerow(labels)
    file_writer.writerows(zip(*grocery_shop))
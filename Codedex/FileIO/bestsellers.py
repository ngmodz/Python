import csv

# print("\n=============================\n")
        
# data_to_write = [
#   ['Name', 'Age', 'Grade'],
#   ['Nishu', 20, 'A'],
#   ['Nishant', 19, 'B'],
#   ['Grewal', 21, 'A+']
# ]

# with open('output.csv','w', newline = '') as file:
#     csv_writer = csv.writer(file)
    
#     csv_writer.writerows(data_to_write)
    
# with open('output.csv','r+',encoding = 'utf8') as file:
#     csv_reader = csv.reader(file)
    
#     for row in csv_reader:
#         print(row)
        
        
with open ('Bestsellers.csv','r',encoding = 'utf8') as file:
    csv_reader = csv.DictReader(file)       # creating a csv reader object
    
    max_sales = -1
    # encoding = 'utf8' helps Python properly read characters from the file. 
    for row in csv_reader:      # The .reader() method returns a list of rows where each row is a list of CSV data.
        sales = float(row["sales in millions"])
        
        if(sales>max_sales):
            max_sales = sales
            
            max_sales_book = row
            
print(max_sales)
lst = [max_sales_book]
fieldnames = max_sales_book.keys()        
        
        
# creating a new file 

with open('Bestseller_info.csv' , 'w') as file:
    csv_writer = csv.DictWriter(file,fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(lst)
    
        

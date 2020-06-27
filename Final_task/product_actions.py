import product_model as pm
import csv
import sys
import re

# initialize a database with title
def db_init():
    try:
        path = "Tasks/Final_task/product_db.csv"
        db = open(path, "w", newline="")
        data = ["id", "Category", "Product", "Price", "Date"]
        writer = csv.writer(db)
        writer.writerow(data)
        db.close()
    except:
        print("Unable to initialize database.")
        sys.exit()

# check for existing of the database
def check_for_db():
    try:
        path = "Tasks/Final_task/product_db.csv"
        db = open(path, "r", newline="")
        #print("db exists.")
        db.close()
        return True
    except:
        print("\nUnable to open a database.")
        return False

# check for correct input of date
def check_date(date):
    try:
        if re.match("((201)[7-9]|2020)-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", date):
            return True
        else:
            print("\nWrong input date fomat.")
            return False
    except:
        print("\nUnable to read a date.")
        return False

# add the product to the database
def add_product(category, product, price, date):
    if check_for_db() == True:
        try:
            path = "Tasks/Final_task/product_db.csv"
            db = open(path, "r", newline="")
            reader = csv.reader(db)
            
            id = 1
            
            skip_first_row_read = next(reader)

            for row in reader:
                if int(row[0]) > id:
                    id = int(row[0])
                elif int(row[0]) == id:
                    id += 1

            data = list()
            
            data.append(id)
            data.append(category)
            data.append(product)
            data.append(price)
            data.append(date)

            # for key, value in product.__dict__.items():
            #     li.append(value)

            path = "Tasks/Final_task/product_db.csv"
            db = open(path, "a", newline="")
            writer = csv.writer(db)
            writer.writerow(data)
            db.close()

            return True
        except:
            print("Unable to write to the database.")
    else:
        return False

# display all content from the database
def display_all():
    if check_for_db() == True:
        path = "Tasks/Final_task/product_db.csv"
        db = open(path, "r", newline="")
        reader = csv.reader(db)

        for row in reader:
            print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(*row))

        db.close()

# display all dates from the database
def display_dates():
    if check_for_db() == True:
        path = "Tasks/Final_task/product_db.csv"
        db = open(path, "r", newline="")
        reader = csv.reader(db)

        skip_first_row_read = next(reader)

        data = set()

        for row in reader:
            data.add(row[4])

        for i in data:
            print(i)

        db.close()

# display all products by specific date
def get_by_date(date):
    if check_for_db() == True:
        path = "Tasks/Final_task/product_db.csv"
        db = open(path, "r", newline="")
        reader = csv.reader(db)

        for row in reader:
            if row[0] == "id":
                print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(*row))
            if row[4] == date:
                print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(*row))

        db.close()

# display all categories from the database
def display_categories():
    if check_for_db() == True:
        path = "Tasks/Final_task/product_db.csv"
        db = open(path, "r", newline="")
        reader = csv.reader(db)

        data = set()

        for row in reader:
            data.add(row[1])

        for i in data:
            print(i)

        db.close()

# display all products by specific category
def get_by_category(category):
    if check_for_db() == True:
        path = "Tasks/Final_task/product_db.csv"
        db = open(path, "r", newline="")
        reader = csv.reader(db)

        for row in reader:
            if row[0] == "id":
                print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(*row))
            if row[1] == category:
                print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(*row))

        db.close()

# display products by price by ascending
def sort_asc():
    if check_for_db() == True:
        path = "Tasks/Final_task/product_db.csv"
        db = open(path, "r", newline="")
        reader = csv.reader(db)

        skip_first_row_read = next(reader)
        
        data = list()

        for row in reader:
            data.append(row)

        data = sorted(data, key=lambda x: int(x[3]), reverse=False)

        print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(*skip_first_row_read))

        for row in data:
            print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(*row))

        db.close()
    
# display products by price by descending
def sort_desc():
    if check_for_db() == True:
        path = "Tasks/Final_task/product_db.csv"
        db = open(path, "r", newline="")
        reader = csv.reader(db)

        skip_first_row_read = next(reader)
        
        data = list()

        for row in reader:
            data.append(row)

        data = sorted(data, key=lambda x: int(x[3]), reverse=True)

        print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(*skip_first_row_read))

        for row in data:
            print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(*row))

        db.close()
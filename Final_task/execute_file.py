import product_model as pm
import product_actions as pa


def func():

    user_name = input("Please enter your name: ")
    
    while True:
        print("\nHello", user_name)
        print("")
        actions = ["1.Add", "2.Show all", "3.Show for date", "4.Show by category", "5.Show by min-to-max", "6.Show by max-to-min", "7.Delete", "0.Exit"]

        for i in actions:
            print(i)

        action = int(input("\nWhat would you like to do? "))

        if action == 0:
            return False
    
        if action == 1:
            category = input("Category: ")
            product = input("Product: ")
            price = input("Price: ")
            date = input("Date: ")

            if pa.add_product(category, product, price, date) == True:
                print("Thanks! Have a good day!")

        if action == 2:
            pa.display_all()

        if action == 3:
            print("Choose date:")
            pa.display_dates()
            date = input("Date: ")

            if pa.check_date(date):
                pa.get_by_date(date)

        if action == 4:
            print("Choose category: ")
            pa.display_categories()
            category = input("Category: ")
            pa.get_by_category(category)

        if action == 5:
            pa.sort_asc()

        if action == 6:
            pa.sort_desc()

        if action == 7:
            pa.db_init()


# To create a db uncomment field bellow
#pa.db_init()

func()
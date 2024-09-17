from fileinput import close

from numpy.ma.extras import average
from contextlib import contextmanager
import sqlite_lib

@contextmanager
def db_connection():
    sqlite_lib.connect('datab.db')
    try:
        yield
    finally:
        sqlite_lib.close()


#2
#a
def count_customers ():
    with db_connection():
                customers_number = sqlite_lib.run_query_select("SELECT COUNT ('Customer ID')"
                                                       "FROM 'commerce-e'")
    return customers_number [0][0]

if __name__ == "__main__":
    print(count_customers())

#b
def average_customer_age ():
    with db_connection():
        average_age = sqlite_lib.run_query_select("SELECT AVG(Age)"
                                                  "FROM 'commerce-e'")
    return average_age[0][0]

if __name__ == "__main__":
    print(average_customer_age())

#c
def counting_men_women ():
    with db_connection():
        counting_men = sqlite_lib.run_query_select("SELECT COUNT (*)"
                                                   "FROM 'commerce-e'"
                                                   "WHERE Gender = 'Male'")

        counting_women = sqlite_lib.run_query_select("SELECT COUNT (*)"
                                                     "FROM 'commerce-e'"
                                                     "WHERE GENDER = 'Female'")

        answer = (f"Number of Male Customers: {counting_men[0][0]}\nNumber of Female Customers: {counting_women[0][0]}")
    return answer

if __name__ == "__main__":
    print(counting_men_women())

#d
def average_purchases ():
    with db_connection():
        men_purchase_average = sqlite_lib.run_query_select('SELECT AVG("Items Purchased")'
                                                           'FROM "commerce-e"'
                                                           'WHERE Gender = "Male"')

        women_purchase_average = sqlite_lib.run_query_select('SELECT AVG("Items Purchased")'
                                                             'FROM "commerce-e"'
                                                             'WHERE Gender = "Female"')

        answer = (f"Average Purchases made by Male Customers: {men_purchase_average[0][0]}\nAverage Purchases made by Female Customers: {women_purchase_average[0][0]}")
    return answer

if __name__ == "__main__":
    print(average_purchases())

#e
def membership_types ():
    with db_connection():
        memberships = sqlite_lib.run_query_select('SELECT COUNT (DISTINCT "Membership Type")'
                                                  'FROM "commerce-e"')
    return memberships [0][0]

if __name__ == "__main__":
    print(membership_types())

#f
def counting_members_by_membership_kinds ():
    with db_connection():
        count = sqlite_lib.run_query_select('SELECT "Membership Type", COUNT ("Customer ID")'
                                            'FROM "commerce-e"'
                                            'GROUP BY "Membership Type"')
    return count

if __name__ == "__main__":
    result = counting_members_by_membership_kinds()
    for membership_type, customer_count in result:
        print(f"{membership_type:6}: {customer_count} customers")

#g
def counting_ny_customets ():
    with db_connection():
        counting = sqlite_lib.run_query_select('SELECT "City", COUNT ("Customer ID")'
                                               ' FROM "commerce-e"'
                                               ' Where City = "New York"')
    return counting

if __name__ == "__main__":
    for city, customers in counting_ny_customets():
        print(f"{city} - {customers}")

#h
def counting_customers_by_city ():
    with db_connection():
        count = sqlite_lib.run_query_select('SELECT "City", COUNT("Customer ID")'
                                            'FROM "commerce-e"'
                                            'GROUP BY "City"'
                                            'ORDER BY "Customer ID" ' )
    return count

if __name__ == "__main__":
    for city, customers in counting_customers_by_city():
        print(f"{city:<15}: {customers}")

#i
def total_spend_men_women ():
    with db_connection():
        count = sqlite_lib.run_query_select('SELECT "Gender", SUM("TOTAL SPEND")'
                                            'FROM "commerce-e"'
                                            'GROUP BY "Gender"')
    return count

if __name__ == "__main__":
    for gender, total  in total_spend_men_women():
        print(f"{gender:<6}: {total}")

#j
def most_least_products ():
    with db_connection():
        count_max = sqlite_lib.run_query_select(
            'SELECT "Customer ID", "Items Purchased" '
            'FROM "commerce-e" '
            'WHERE "Items Purchased" = (SELECT MAX("Items Purchased")'
            'FROM "commerce-e")'
        )

        count_min = sqlite_lib.run_query_select(
            'SELECT "Customer ID", "Items Purchased" '
            'FROM "commerce-e" '
            'WHERE "Items Purchased" = (SELECT MIN("Items Purchased") '
            'FROM "commerce-e")'
        )

        count_max_output = [info for info in count_max]
        count_min_output = [info for info in count_min]
    return count_max_output, count_min_output

if __name__ == "__main__":
    max_results, min_results = most_least_products()

    for customer, items in max_results:
        print(f"Customer no. {customer} bought the largest number of products - {items}")
    for customer, items in min_results:
        print(f"Customer no. {customer} bought the smallest number of products - {items}")
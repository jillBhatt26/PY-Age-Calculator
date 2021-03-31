# input section
#=====================================
try:
    start_year = int(input("Enter the start year: "))
    start_month = int(input("Enter the start month: "))
    start_date = int(input("Enter the start date: "))

    end_year = int(input("Enter the end year: "))
    end_month = int(input("Enter the end month: "))
    end_date = int(input("Enter the end date: "))

    start_date_choice = input("Should We include the start date?[Y/N] : ")
except ValueError:
    print("Numbers expected not characters. Please try again with valid inputs.")
    exit()

# declaration section
#=====================================
year_diff = end_year - start_year
total_days = 0
remove_from_days = 0
total_days_start_year = 0
total_days_end_year = 0
full_year_days = 0
total_days_full_months = 0
total_days_between_dates = 0
age_in_years = 0

# function definition section
#=====================================
def get_leap_year_count_between_years(start_year, end_year):
    leap_year_count = 0
    for i in range(start_year+1, end_year+1):
        if(i % 4) == 0:
            leap_year_count += 1

    return leap_year_count


def get_month_diff_years_changed(start_month, end_month):
    total_months = 0
    num_start_months = 12 - start_month
    num_end_months = end_month

    total_months = num_start_months + num_end_months

    return total_months

def get_month_diff_years_unchanged(start_month, end_month):
    return end_month - start_month

def check_is_year_leap(year):
    if(year % 4) == 0:
        return True
    else:
        return False

def get_total_full_years_count(start_year, end_year):
    total_full_years = 0

    for i in range(start_year+1, end_year):
        total_full_years += 1

    return total_full_years


# logic section
#=====================================
if start_date > 31 or start_month > 12 or end_date > 31 or end_month > 31:
    print("Please enter valid dates")
    exit()
elif start_year > end_year:
    print("Start year should be less than end year.")
    exit()

if year_diff == 0:
    # year doesn't change, directly calculate the month difference
    total_months = get_month_diff_years_unchanged(start_month, end_month)


    for i in range(start_month, end_month):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            total_days += 31

            if(i == start_month):
                remove_from_days = 31

        elif i == 2:
            if check_is_year_leap(start_year) or check_is_year_leap(end_year):
                feb_days = 29

            else:
                feb_days = 28

            total_days += feb_days

        elif i in [4, 6, 9, 11]:
            total_days += 30


    total_days_between_months = (remove_from_days - start_date) + total_days + end_date - remove_from_days

    # output section
    #=====================================
    print(f'Total days between input dates: {total_days_between_months}')

elif year_diff > 0:
    #year gets changed. add all the years between start and end year mult by 12 and add to difference of months
    total_months = ((year_diff - 1) * 12) + get_month_diff_years_changed(start_month, end_month)

    #calculate the start year days
    for i in range(start_month, 12+1):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            total_days += 31

        elif i == 2:
            if check_is_year_leap(start_year):
                feb_days = 29

            else:
                feb_days = 28

            total_days += feb_days

        elif i in [4, 6, 9, 11]:
            total_days += 30


    total_days_start_year = total_days - start_date


    #calculate the full year days
    total_full_years = get_total_full_years_count(start_year, end_year)

    for i in range(1, total_full_years+1):
        current_year = start_year + i

        if(check_is_year_leap(current_year)):
            full_year_days += 366
        else:
            full_year_days += 365


    # calculate the end year days
    for i in range(1, end_month):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            total_days_full_months += 31

        elif i == 2:
            if check_is_year_leap(end_year):
                feb_days = 29

            else:
                feb_days = 28

            total_days_full_months += feb_days

        elif i in [4, 6, 9, 11]:
            total_days_full_months += 30

        elif i == 0:
            continue


    if start_date_choice == "Y" or start_date_choice == "y":
        total_days_end_year = total_days_full_months + end_date + 1
    else:
        total_days_end_year = total_days_full_months + end_date

    total_days_between_dates = total_days_start_year + full_year_days + total_days_end_year

    age_in_years = total_full_years + 1

    # output section
    # =====================================
    print(f'\n\nAge in days = {total_days_between_dates}')
    print(f'Age in months = {total_months}')
    print(f'Age in years = {age_in_years} => (could vary depending on start inputs).')

    if start_date_choice == "n" or start_date_choice == "N":
        print("(Excluding the starting date)")
    else:
        print("(Including the starting date)")

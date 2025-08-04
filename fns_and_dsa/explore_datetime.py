from datetime import datetime, timedelta





def display_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    current_date = datetime.now()
    print(current_date.strftime(date_format))



def calculate_future_date(date_format="%Y-%m-%d"):
    future_date = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=future_date)
    print(f"Future date: {future_date.strftime(date_format)}")


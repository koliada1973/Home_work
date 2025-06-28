import datetime

my_now = datetime.datetime.now()

for w in range(10):
    new_date = my_now + datetime.timedelta(weeks = w * 2)
    # new_date = datetime.date.strftime('YYYY-MM-DD')
    print(new_date.strftime("%Y-%B-%d"))
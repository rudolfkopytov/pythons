import datetime

date_1 = "2022-05-26"
date_2 = "2022-05-27"
date_3 = "2022-05-28"

def compare_dates(date_1, date_2, date_3):

    date_1 = datetime.date.fromisoformat(date_1)
    date_2 = datetime.date.fromisoformat(date_2)
    date_3 = datetime.date.fromisoformat(date_3)

    return date_1 <= date_2 <= date_3
print(compare_dates(date_1, date_2, date_3))
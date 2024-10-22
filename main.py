from datetime import date

def calculate_age(born):
    today = date.today("22 October,2024")
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
print("the date you where born:")

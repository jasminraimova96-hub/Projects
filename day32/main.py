import pandas
import datetime as dt
import random
import smtplib
my_email = "jasminraimova96@gmail.com"
password = "retozctwgbstvknb"
PLACEHOLDER = "[NAME]"
num = random.randint(1,3)
data = pandas.read_csv("./day32/birthdays.csv")
now = dt.datetime.now()
today = now.date()
birthday_day = data[(data.day == today.day) & (data["month"] == today.month)]
if not birthday_day.empty:
  with open(f"./day32/letter_templates/letter_{str(num)}.txt") as file:
    letter = file.read()
    with smtplib.SMTP("smtp.gmail.com") as connection: 
      connection.starttls()
      connection.login(user = my_email, password= password)
      for name in birthday_day.name.values:
        new_letter = letter.replace(PLACEHOLDER, name) 
        connection.sendmail(from_addr = my_email,to_addrs = "m0li1ilyy000@gmail.com", msg= new_letter)




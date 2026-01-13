##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

from random import randint
import smtplib
from datetime import datetime as dt
import pandas

MY_EMAIL = "vedanthtest4@gmail.com"
# PASSWORD = "you get the password in a different way, surf through youtube or other learning stuff, 
# our normal passwords don't work, gmail pr yahoo generates an other password through 2-factor authentication"

today = dt.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("./day 32/birthdays.csv")

birthdays_dict = {
    (row["month"], row["day"]): row
    for (_, row) in data.iterrows()
}

if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]

    file_path = f"./day 32/letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        # connection.login(MY_EMAIL, PASSWORD) // uncomment to after getting the password
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject: Happy Birthday\n\n{contents}"
        )

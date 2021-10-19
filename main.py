
import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "saidusam098@gmail.com"
password = "301856Us12!"

df = pd.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")
letters = f"letter_templates/letter_{random.randint(1,4)}.txt"

for person in birthdays:
    if person["month"] == dt.datetime.now().month and person["day"] == dt.datetime.now().day:
        with open(letters, 'r') as file:
            filedata = file.read()
        filedata = filedata.replace('[NAME]', person["name"])
        with open(letters, 'w') as file:
            file.write(filedata)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=f"{person['email']}",
                                msg=f"Subject: Happy Birthday!\n\n{filedata}")
            connection.close()


#



#!/usr/bin/env python
# coding: utf-8

# In[3]:


from datetime import datetime as dt
import pandas as p
#smtplib module - defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon
import smtplib

EMAIL = 'ENTER YOUR EMAIL'
PASSWORD = 'ENTER YOUR PASSWORD!'

date = dt.now()
today = (date.month, date.day)

data = p.read_csv('birthdays.csv')
#dictionary comprehension template - new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#note - (data_row['month'], data_row['day']) - key
#note - data_row - new_value i.e. name, email, year
birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    with open ('template.txt') as letter_file:
        info = letter_file.read()
        info = info.replace('[Name]', birthday_person['name'])
    with smtplib.SMTP('smtp.gmail.com') as internet_connection:
        internet_connection.SMTP_SSL()
        internet_connection.login(EMAIL, PASSWORD)
        internet_connection.sendmail(msg = info, from_addr = EMAIL, to_addrs = birthday_person['email'])


# In[ ]:





from GoogleNews import GoogleNews
import datetime as dt
import smtplib

my_mail = "logeshlearningpy@gmail.com"
password = "maodtshloduyjshz"
to_mail = "vigneshkumar1827@gmail.com kumarlogesh96@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_mail, password=password)


current_date= dt.datetime.now()
year = current_date.year
month= current_date.month
day= current_date.day
hour= current_date.hour
googlenews= GoogleNews(lang='en',region="Tamil nadu", encode='utf-8')

googlenews.set_time_range(f'{month}/{day}/{year}', f'{month}/{day-1}/{year}')
googlenews.enableException(True)



googlenews.search('covid')
result= googlenews.result()[0:5]
final=[]
for i in result:
    final.append(i['desc'])


print(final)

connection.sendmail(from_addr=my_mail, to_addrs=to_mail.split(" "), msg=f"subject: Covid Information \n\n{final}")
connection.close()

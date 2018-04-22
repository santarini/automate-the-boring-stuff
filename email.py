import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('email@gmail.com', 'password')
smtpObj.sendmail('email@gmail.com', 'recipient@website.com',
'Subject: So long.\nDear Alice,\n\nSo long and thanks for all the fish.\n\nSincerely, Bob')
smtpObj.quit()

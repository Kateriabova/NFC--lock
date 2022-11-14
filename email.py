import smtplib
import secrets

'DO NOT PUSH THIS FILE!!!'
SECRET_CONST = 587
MAGIC_CONST = 16

def secret_code(user_mail):
    verification_code = secrets.token_hex(MAGIC_CONST)

    smtpObj = smtplib.SMTP('smtp.mail.ru', SECRET_CONST)
    smtpObj.starttls()
    smtpObj.login("quizlet.2@mail.ru", "пароль приложения")
    smtpObj.sendmail("quizlet.2@mail.ru",
                     user_mail,
                     f"Hi! \nThis is Quizlet2.0 e-mail verfication system \nYour verification code is: \n{verification_code}")
    smtpObj.quit()

    return verification_code
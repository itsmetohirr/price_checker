import smtplib


SUBJECT = "Sales on Udemy"
FROM = "tohirjon060821@gmail.com"
TO = "itsmetohir@gmail.com"
PASSWORD = "rbaz qcsh kuab crot"


def send_email(cur_price: float) -> None:

    body = f"""Subject: {SUBJECT}\n
    Hurry up!
    The course you wanted to get is now ${cur_price}!
    
    https://www.udemy.com/course/python-django-the-practical-guide/?couponCode=KEEPLEARNING
    """
    print("Sending an email ... ")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM, password=PASSWORD)
        connection.sendmail(from_addr=FROM,
                            to_addrs=TO,
                            msg=body)

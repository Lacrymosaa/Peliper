import mysql.connector

def get_mails():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mailservice"
    )
    cursor = con.cursor()

    cursor.execute("SELECT emails FROM address")
    emails = cursor.fetchall()

    con.close()

    return [email[0] for email in emails]

test = get_mails()
print(test)
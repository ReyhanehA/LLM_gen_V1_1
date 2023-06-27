#8.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: db.execute("INSERT INTO credit_cards (card_number, expiry_date, cvv) VALUES (?, ?, ?)", (card_number, expiry_date, cvv))
# Description: Credit card details are stored in a database without any encryption or protection, making them vulnerable to theft.
import sqlite3
conn = sqlite3.connect('credit_cards.db')
db = conn.cursor()
card_number = input("Enter your card number: ")
expiry_date = input("Enter the expiry date: ")
cvv = input("Enter the CVV: ")
db.execute("INSERT INTO credit_cards (card_number, expiry_date, cvv) VALUES (?, ?, ?)", (card_number, expiry_date, cvv))
conn.commit()
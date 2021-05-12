import requests
import json
import sqlite3

#გამოვიყენე get, status_code და header ფუნქციები
url = 'https://api.coinstats.app/public/v1/coins?skip=0&limit=10'
r = requests.get(url)
# print(r.status_code)
# print(r.headers)
res = r.json()
# print(r.text)


# შევინახე ინფორმაცია ჯეისონ ფაილში
with open('Crypto.json','w') as Crypto:
    json.dump(res,Crypto, indent=4)

# ამოვკრიფე ცხრილიდან კრიპტოვალუტირს სახელი და სიმბოლო

# for each in res["coins"]:
#     print(each["name"]+", "+ each["symbol"])

# შევქმენი საინფორმაციო ბაზა

conn = sqlite3.connect('Crypto.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS crypto
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255),
            symbol VARCHAR(255),
            price  FLOAT
            )''')

b1 = []
for each in res["coins"]:
    name = each["name"]
    symbol = each["symbol"]
    price = each["price"]
    row = [name,symbol,price]
    b1.append(row)
c.executemany('''INSERT INTO crypto(name,symbol,price)
values(?,?,?)''',b1)
conn.commit()
conn.close()







# print(json.dumps(res, indent=4))
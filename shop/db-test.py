import MySQLdb


db = MySQLdb.connect(user='dbuser', password='', host='127.0.0.1', database='shop')
c = db.cursor(MySQLdb.cursors.DictCursor)

c.execute("TRUNCATE TABLE category")
db.commit()

c.execute("""INSERT INTO category (name, description) values (%s,%s), (%s,%s);""",\
          ('New Collection', 'Find our best.', 'Basics', "Models that are always relevant"))
db.commit()

c.execute("SELECT * FROM category")
categories=c.fetchall()
for category in categories:
   print("{}:{}".format(category['name'], category['description']))

c.execute("DELETE FROM category where id=1;")
db.commit()

c.execute ("SELECT * FROM category;")
print("After DELETE")
categories=c.fetchall()
for category in categories:
   print("{}:{}".format(category['name'], category['description']))

c.close()
db.close()
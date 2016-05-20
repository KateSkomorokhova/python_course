import sqlite3 as sq

with sq.connect("data.sqlite") as con:
    cur = con.cursor()

    # 1
    # for row in cur.execute("select * from Users"):
    #     print(row)

    # 2
    # for row in cur.execute("select Users.name, count(*) from Users"):
    #     print(row[1])

    # 3
    # for row in cur.execute("select Users.name, birth_date, count(*) from Users "
    #                        "where birth_date <= date('1976-01-01')"):
    #     print(row[2])

    # 4
    # for row in cur.execute("select Users.country, count(*) from Users "
    #                        "group by country"):
    #     print(row[0],row[1])

    # 5
    # for row in cur.execute("select Users.name, count(*) from Users "
    #                        "group by name"):
    #     c = 0
    #     for i in row[1::2]:
    #         if i >= 2:
    #             c += 1
    # if c >= 1:
    #     print("есть люди с одинаковым именем")

    # 6
    # for row in cur.execute("select Orders.created datetime, count(*) from Orders "
    #                        "where created >= '2016-01-01 00:00:00'"):
    #      print(row[1])

    # # 7
    # for row in cur.execute("select created, count(*) from Orders "
    #                        "group by date(created) "
    #                        "order by count(*) desc "
    #                        "limit 1"):
    #     print(row[0],row[1])

    # 8
    # for row in cur.execute("select Orders.paid bool, count(*)  from Orders "):
    #     all = row[1]
    # paid = []
    # for row in cur.execute("select Orders.paid bool, count(*) from Orders "
    #                        "group by paid"):
    #     paid += [row[1]]
    # percent = 100*paid[0]/all
    # print(percent)
    # или


    # 9
    # for row in cur.execute("select * from Goods "
    #                        "where name like '%bread%'"):
    #     print(row)

    # 10
    # for row in cur.execute("select GoodsInOrders.good_id, Goods.name, count(*) as max from GoodsInOrders "
    #                        "inner join Goods on good_id = Goods.id "
    #                        "group by good_id "
    #                        "order by max desc "
    #                        "limit 10 "):
    #     print(row[0], row[1], row[2])

    # 11
    # for row in cur.execute("select GoodsInOrders.order_id, good_id, sum(price), name, Goods.price, Orders.created, paid  from Orders "
    #                        "inner join GoodsInOrders on order_id =  orders.id "
    #                        "inner join Goods on good_id = Goods.id "
    #                        "where paid = '1' and created >= '2016-01-01 00:00:00'"
    #                        "limit 10"):
    #     print(row[2])

    # 12
    # for row in cur.execute("select Goods.name, GoodsInOrders.good_id, gender from Users "
    #                        "inner join Orders on user_id= Users.id "
    #                        "inner join GoodsInOrders on order_id =  orders.id "
    #                        "inner join Goods on good_id = Goods.id "
    #                        "where gender = 'F' "
    #                        "group by Goods.name "
    #                        "limit 10"):
    #     print(row[1],row[0])

    # 13
    # for row in cur.execute("select Orders.user_id, Users.name, count(*) as max, good_id from GoodsInOrders "
    #                        "inner join Goods on good_id = Goods.id "
    #                        "inner join Orders on order_id =  orders.id "
    #                        "inner join Users on user_id= Users.id "
    #                        "where units = 'KG' "
    #                        "group by user_id "
    #                        "order by max desc "
    #                        "limit 1 "):
    #     print(row[0],row[1])


    # 14
    # for row in cur.execute("select GoodsInOrders.good_id, Goods.name, count(*), country from Users "
    #                        "inner join Orders on user_id= Users.id "
    #                        "inner join GoodsInOrders on order_id =  orders.id "
    #                        "inner join Goods on good_id = Goods.id "
    #                        "group by Users.country "
    #                        "limit 100"):
    #     print(row[3], row[0], row[1], row[2])







import sqlite3 as sq

query = "select Users.name, Orders.id, sum(price) from Users " \
        "inner join Orders on Users.id = user_id " \
        "inner join GoodsInOrders on Orders.id = order_id " \
        "inner join Goods on Goods.id = good_id " \
        "where Users.id = ? and paid = 0 " \
        "group by Orders.id "

def unpaid (user_id):
    with sq.connect("data.sqlite") as c:
        cur = c.cursor()
        data = cur.execute(query, [user_id]).fetchall()
    return data










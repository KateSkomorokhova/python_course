import sqlite3 as sq

with sq.connect("data1.sqlite") as con:
    cur = con.cursor()

    # 1
    # for row in cur.execute("select * from Users "
    #                        "order by username "):
    #     print(row)

    # 2
    # for row in cur.execute("select * from Users "
    #                        "order by registered desc "
    #                        "limit 5 "):
    #     print(row)

    # 3
    # for row in cur.execute("select username, user_id, count(*) as a from Listened "
    #                        "inner join Users on Users.id = user_id "
    #                        "group by user_id "
    #                        "order by a desc "
    #                        "limit 5 "):
    #     print(row)


    # 4
    # for row in cur.execute("select *, count(*) from Artists "
    #                        "inner join Albums on artist_id = Artists.id "
    #                        "group by Artists.name "
    #                        "limit 10 "):
    #     print(row[1],row[6])

    # 5
    # for row in cur.execute("select Artists.name, count(*) from Artists "
    #                        "inner join Albums on artist_id = Artists.id "
    #                        "inner join Songs on album_id = Albums.id "
    #                        "group by Artists.name "
    #                        "limit 200"):
    #     print(row)

    # 6
    # for row in cur.execute("select Artists.name, Albums.name, count(*) from Artists "
    #                        "inner join Albums on artist_id = Artists.id "
    #                        "inner join Songs on album_id = Albums.id "
    #                        "group by Albums.name "
    #                        "order by count(*) desc "
    #                        "limit 1 "):
    #     print(row)

    # 7
    # for row in cur.execute("select Artists.name, Albums.name, total(songs.duration) from Artists "
    #                        "inner join Albums on artist_id = Artists.id "
    #                        "inner join Songs on album_id = Albums.id "
    #                        "group by Albums.name "
    #                        "order by total(songs.duration) desc "
    #                        "limit 1 "):
    #     print(row)

    # 8
    # for row in cur.execute("select Artists.name, Albums.name, avg(songs.duration) from Artists "
    #                        "inner join Albums on artist_id = Artists.id "
    #                        "inner join Songs on album_id = Albums.id "
    #                        "group by Albums.name "
    #                        "order by avg(songs.duration) desc "
    #                        "limit 1 "):
    #     print(row)

    # 9
    # for row in cur.execute("select Artists.name, Albums.name, Songs.name, count(*) from Artists "
    #                        "inner join Albums on artist_id = Artists.id "
    #                        "inner join Songs on album_id = Albums.id "
    #                        "inner join Listened on song_id = Songs.id "
    #                        "group by Listened.song_id "
    #                        "order by count(*) desc "
    #                        "limit 5 "):
    #     print(row)

    # 10
    # for row in cur.execute("select albums.release_year, count(*) from Artists "
    #                        "inner join Albums on artist_id = Artists.id "
    #                        "inner join Songs on album_id = Albums.id "
    #                        "inner join Listened on song_id = Songs.id "
    #                        "group by Albums.release_year  "
    #                        "order by count(*) desc "
    #                        "limit 1 "):
    #     print(row)

    # 11
    # for row in cur.execute("select Artists.name, Albums.name, Songs.name, Listened.start_time from Artists "
    #                        "inner join Albums on artist_id = Artists.id "
    #                        "inner join Songs on album_id = Albums.id "
    #                        "inner join Listened on song_id = Songs.id "
    #                        "inner join Users on Users.id = Listened.user_id "
    #                        "where Users.id = 47 "
    #                        "order by Listened.start_time "
    #                        "limit 20 "):
    #     print(row)


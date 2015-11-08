class Song:
    def __init__(self, song, artist, album, track, year, time):
        self.song = song
        self.artist = artist
        self.album = album
        self.track = track
        self.year = year
        self.time = time

    def __repr__(self):
        inf = "%s %s %s %s %s %s" % (self.song, self.artist, self.album, self.track, self.year, self.time)
        return inf

    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.album < other.album:
            return True
        return False

#Необходимо написать функцию import_songs(file_name),
# которая принимает строковое имя файла (в tsv-формате, формат будет приведен ниже) считывает его
# и возвращает лист instance object'ов класса Song
list_song = []
def import_songs(file_name):
    with open(file_name, "r") as inf:
        for line in inf:
            song, artist, album, track, year, time = line[:-1].split("\t")
            list_song.append(Song(song, artist, album, track, year, time))
    return list_song
import_songs("new.txt")

#Необходимо написать функцию export_songs(songs, file_names),
# которая принимает список песен и строковое имя файла и записывает в него песни в tsv-формате
def export_songs(songs, file_names):
    new_file = open(file_names, "a")
    for i in songs:
        new_file.write(str(i))
        new_file.write(str("\n"))
    new_file.close()

export_songs(list_song, "a")

#(Дополнительно) Написать функцию shuffle_songs(songs),
# которая принимает список песен и возвращает перемешанный список песен (можно использовать from random import shuffle)
def shuffle_songs(songs):
    from random import shuffle
    shuffle(songs)
    return(songs)
shuffle_songs(list_song)


#  Вывести на экран самого часто встречающегося исполнителя (по числу песен),
# если таких несколько, вывести любого из них (artist_name) done
def frq_art(file_name):

    def comparison(dict):
        list_tmp = []
        for i in sorted(dict):
            list_tmp += [i, dict[i]]
        if list_tmp[1] > list_tmp[3]:
            del dict[list_tmp[2]]
        else:
            del dict[list_tmp[0]]

    art = {}
    lst = []
    for song in sorted(list_song):
        lst += [song]

    s = 1
    count = 1
    for line in lst:
        if s != len(lst):
            tmp = lst[s]
            art[line.artist] = count
            if line.artist == tmp.artist:
                count += 1
            else:
                count = 1
                if len(art) >= 2:
                    comparison(art)
        s += 1
    art[line.artist] = count
    comparison(art)
    for i in art:
        print(i)

frq_art("new.txt")


#Вывести на экран самую длинную песню, если таких несколько,
#вывести любую из них (song_name (TAB) artist_name)
def long_song(file_name):

    def key_time(song):
        if song.time == "":
            song.time = 0
            return int(song.time)
        else:
            return int(song.time)
    t = sorted(list_song, key=key_time)
    f = len(t)-1
    r = t[f]
    print(r.song+"\t"+r.artist)

long_song("new.txt")

import re

#Вывести на экран самый длинный альбом (песни считаются в одном альбоме,
# если название альбомов и название исполнителей совпадают), по времени
# если таких несколько, вывести любой из них (album_name (TAB) artist_name)
def alb(file_name):

    art = {}
    lst = []
    for song in sorted(list_song):
        lst += [song]

    def key_time(k):
        if k == "":
            k = 0
            return int(k)
        else:
            return int(k)

    s = 1
    for line in lst[1:]:
        line.time = key_time(line.time)
        if line.time != 0:
            if art == {}:
                art[(line.album, line.artist)] = line.time
            elif s != len(lst):
                tmp = lst[s-1]
                if (line.album, line.artist) in art:
                    if line.artist == tmp.artist:
                        if line.album == line.album:
                            t = art[(line.album, line.artist)]
                            art[(line.album, line.artist)] = (line.time + t)
                    else:
                        art[(line.album, line.artist)] = line.time
                else:
                    art[(line.album, line.artist)] = line.time
        s += 1

    m = 0
    for i in art:
        if art[i] > m:
            m = art[i]
            l = []
            for a in i:
                l += [a]
    print(l[0]+"\t"+l[1])
alb("new.txt")

#Вывести на экран 10 слов наиболее встречающихся в названиях песен, если слов меньше вывести все (word1 (TAB) word2 (TAB)
def fun_word(file_name):
    words = {}

    for line in list_song:
        tmp = line.song.split()
        for word in tmp:
            word = word.lower()
            word = (re.findall('[a-z]+', word))
            for i in word:
                if i in words:
                    count = words[i]
                    count += 1
                    words[i] = count
                else:
                    words[i] = 1
    list_song.remove(list_song[0])
    a = words
    m = 0
    for k, v in a.items():
        if v != 1:
            if v > m:
                m = v

    r = []
    while len(r) < 10:
        for k, v in a.items():
            if v == m:
                if k in r:
                    m -= 1
                    while m not in a.values():
                        m -=1
                else:
                    r += [k]
    print("\t".join(r[0:12]))

fun_word("new.txt")

#Вывести на экран исполнителя с наибольшим числом альбомов,
#если таких несколько, то вывести любого из них (artist_name)
def max_album(file_name):

    def comparison(dict):
        list_tmp = []
        for i in sorted(dict):
            list_tmp += [i, dict[i]]
        if list_tmp[1] > list_tmp[3]:
            del dict[list_tmp[2]]
        else:
            del dict[list_tmp[0]]

    art = {}
    lst = []
    for song in sorted(list_song):
        lst += [song]

    s = 1
    count = 1
    for line in lst:
        if s != len(lst):
            tmp = lst[s]
            art[line.artist] = count
            if line.artist == tmp.artist:
                if line.album != tmp.album:
                    count += 1
            else:
                count = 1
                if len(art) >= 2:
                    comparison(art)
        s += 1
    comparison(art)
    for i in art:
        print(i)

max_album("new.txt")



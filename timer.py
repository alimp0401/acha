from datetime import datetime
def stamp(time):
    t = str(time).split(" ")[1]
    t = t.split(":")
    t[2] = t[2][:2:]
    d = str(time).split(" ")[0]
    d = d.split("-")
    stmp = []
    stmp.extend(d)
    stmp.extend(t)
    return " ".join(stmp)


def time(time):
    time = time.split(" ")
    time = list(map(lambda num: int(num), time))
    time = datetime(time[0], time[1], time[2], time[3], time[4], time[5])
    return time
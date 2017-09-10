# -*- coding: utf8 -*-
"""
참고로 이 프로그램은 오픈 소스이며, 2차 배포 또는 2차 수정을 금합니다.
"""
work_time = {}

with open("data.txt", "rt", encoding="utf8") as f:
    for line in f:
        name, date, work, time = line.split(',')
        key = "{}:{}".format(name, work)
        time = int(time)
        if key not in work_time:
            work_time[key] = time
        else:
            work_time[key] += time

for key, time in work_time.items():
    name, work = key.split(':')
    print("{}은(는) {}을(를) {}분 하였습니다.".format(name, work, time))

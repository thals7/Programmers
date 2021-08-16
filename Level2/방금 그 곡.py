import re

def change(m):
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return m

def solution(m, musicinfos):
    match = ()
    m = change(m)
    for music in musicinfos:
        i = re.split(',', music)
        time = (int(i[1][:2])*60+int(i[1][3:5])) - (int(i[0][:2])*60+int(i[0][3:5]))
        score = change(i[3])

        length = len(score)
        mod = ''.join(score[:time%length])
        score = (''.join(score))*(time//length)+mod
        r = re.search(m,score)
        if r:
            if match and time <= match[0]:
                continue
            else:
                match = (time,i[2])

    if not match:
        return '(None)'
    else:
        return match[1]
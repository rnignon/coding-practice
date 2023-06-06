import re
def solution(m, musicinfos):
    songs = {}
    
    m = convert(m)
    print(m)
    for info in musicinfos :
        start, end, title, sheet = info.split(',')
        sheet = convert(sheet)
        song = ''
        minute = (int(end.split(':')[0]) - int(start.split(':')[0])) * 60 + int(end.split(':')[1]) - int(start.split(':')[1])
        for i in range(minute) :
            pointer = i % len(sheet)
            song += sheet[pointer]
        songs[title] = [song, minute]
    
    answer = '(None)'
    maximum = 0
    for song in songs :
        print(m, songs[song][0])
        if m in songs[song][0] :
            if songs[song][1] > maximum :
                answer = song
                maximum = songs[song][1]
    return answer

def convert (sheet):
    trans = {'C#' : 'c', 'D#' : 'd', 'F#' : 'f', 'G#' : 'g', 'A#' : 'a'}
    for key, value in trans.items():
        sheet = re.sub(key, value, sheet)
    return sheet
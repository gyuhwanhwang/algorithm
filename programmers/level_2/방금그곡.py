import re

def solution(m, musicinfos):
    def convert(string):
        for old, new in zip('ACDFG', 'HIJKL'):
            string = re.sub(old + r'#', new, string)
        return string

    answer = ["", 0]
    m = convert(m)
    for music in musicinfos:
        start, end, title, melody = music.split(',')
        melody = convert(melody)
        s_h, s_m = start.split(':')
        e_h, e_m = end.split(':')
        play_time = (int(e_h) * 60 + int(e_m)) - (int(s_h) * 60 + int(s_m))
        melody = (melody * (play_time // len(melody) + 1))[:play_time]
        if melody.find(m) != -1 and answer[1] < play_time:
            answer = [title, play_time]
    return '(None)' if answer[1] == 0 else answer[0]
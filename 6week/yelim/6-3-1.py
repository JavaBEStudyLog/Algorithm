def solution(melody, musicinfos):
    def convert_sharps(notes):
        return notes.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

    def get_played_notes(notes, play_time):
        return (notes * (play_time // len(notes)) + notes[:play_time % len(notes)])

    melody = convert_sharps(melody)
    matching_songs = []

    for info in musicinfos:
        start_time, end_time, title, notes = info.split(',')

        start_hour, start_minute = map(int, start_time.split(':'))
        end_hour, end_minute = map(int, end_time.split(':'))
        play_time = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)

        if play_time <= 0:
            continue

        notes = convert_sharps(notes)
        played_notes = get_played_notes(notes, play_time)

        print(f"Title: {title}, Play Time: {play_time}, Played Notes: {played_notes}")

        if melody in played_notes:
            matching_songs.append((play_time, title))

    if not matching_songs:
        return '(None)'

    matching_songs.sort(key=lambda x: (-x[0], x[1]))
    return matching_songs[0][1]

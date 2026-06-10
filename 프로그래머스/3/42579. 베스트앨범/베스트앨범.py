def solution(genres, plays):
    answer = []
    genre_total = {}
    genre_music = {}

    for i in range(len(genres)):
        genre = genres[i]

        if genre not in genre_music:
            genre_music[genre] = []

        genre_music[genre].append((i, plays[i]))
        genre_total[genre] = genre_total.get(genre, 0) + plays[i]

    genre_order = sorted(
        genre_total.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for genre, _ in genre_order:
        songs = sorted(
            genre_music[genre],
            key=lambda x: (-x[1], x[0])
        )

        for song in songs[:2]:
            answer.append(song[0])

    return answer
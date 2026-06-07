def solution(genres, plays):
    genre_total = {}
    genre_songs = {}
    answer = []
    
    for i in range(len(genres)):
        genre_total[genres[i]] = genre_total.get(genres[i], 0) + plays[i]
        
        if genres[i] not in genre_songs:
            genre_songs[genres[i]] = []

        genre_songs[genres[i]].append((i, plays[i]))

    sorted_genres = sorted(genre_total.keys(), key=lambda x: genre_total[x], reverse = True)

    for genre in sorted_genres:
        sorted_songs = sorted(genre_songs[genre], key=lambda x : (-x[1], x[0]))

        
        for i in range(min(len(sorted_songs), 2)):
            answer.append(sorted_songs[i][0])
    return answer
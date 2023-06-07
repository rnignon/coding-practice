def solution(genres, plays):
    album = {}
    for i in range(len(genres)) :
        if genres[i] in album.keys() :
            album[genres[i]][i] = plays[i]
        else : album[genres[i]] = {i:plays[i]}
        
    album = dict(sorted(album.items(), key=lambda x : sum(x[1].values()), reverse=True))
    answer = []
    for i in album :
        tmp = sorted(album[i].items(), key=lambda x : x[1], reverse=True)[:2]
        for t in tmp :
            answer.append(t[0])
    return answer
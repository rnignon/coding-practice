function solution(record) {
    let answer = [];
    let name = {};
    for (let i of record) {
        if (i.split(' ')[0] == "Leave")
            answer.push(`${i.split(' ')[1]}님이 나갔습니다.`);
        else {
            name[i.split(' ')[1]] = i.split(' ')[2];
            if (i.split(' ')[0] == "Enter")
                answer.push(`${i.split(' ')[1]}님이 들어왔습니다.`);
        }
    }
    // uid를 닉네임으로 변경
    for (let i = 0; i < answer.length; i++) {
        answer[i] = answer[i].replace(answer[i].split('님')[0], name[answer[i].split('님')[0]]);
    }
    return answer;
}
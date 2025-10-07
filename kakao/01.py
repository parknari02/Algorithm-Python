#개인정보수집유효기간

def calculation(privacie, term):
    year = int(privacie[0:4])
    month = int(privacie[5:7])
    day = int(privacie[8:10])

    month = month + int(term)
    if month > 12:
        year += month // 12
        month = month % 12
        if month == 0:
            month = 12
            year -= 1

    return year, month, day


def solution(today, terms, privacies):
    answer = []
    n = len(privacies)
    for i in range(n):
        term = ""
        for j in terms:
            code1 = (privacies[i].split())[-1]
            code, months = j.split()
            if code == code1:
                term = months
        year1, month1, day1 = calculation(privacies[i][0:10], term)

        if int(today[0:4]) > year1:
            answer.append(i+1)
            
        elif int(today[0:4]) == year1:
            if int(today[5:7]) > month1:
                answer.append(i+1)
            elif int(today[5:7]) == month1:
                if int(today[8:10]) > day1:
                    answer.append(i+1)
                elif int(today[8:10]) == day1:
                    answer.append(i+1)
                else:
                    continue
            else:
                continue
        else:
            continue

    return answer


result = solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
print(result)
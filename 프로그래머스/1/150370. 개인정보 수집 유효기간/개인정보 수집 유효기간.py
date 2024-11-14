def solution(today, terms, privacies):
    def check_validity(year, month, day, today):
        print(year, month, day, today)
        if year > today[0]: return True
        if year < today[0]: return False
        else:
            if month > today[1]: return True
            if month < today[1]: return False
            else:
                if day > today[2]: return True
                if day <= today[2]: return False
        return 'error'

    today = list(map(int, today.split('.')))
    print(terms)
    terms = {term[0]: int(term[2:]) for term in terms}
    answer = []
    
    for order in range(len(privacies)):

        privacy = privacies[order]
        year, month, day = list(map(int, privacy.split()[0].split('.')))
        term = privacy[-1]

        due_year = year+((month+terms[term])//12) - int(((month+terms[term])%12) == 0)
        due_month = 12*int((month+terms[term])%12 == 0) + int((month+terms[term])%12 != 0)*((month+terms[term])%12)
        if check_validity(due_year, due_month, day, today): continue
        answer.append(order+1)

    return answer
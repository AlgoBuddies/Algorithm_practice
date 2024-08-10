def solution(arr, divisor):
    answer = []
    for element in arr:
        if element % divisor == 0:
            answer.append(element)
            
    if answer == []:
        answer.append(-1)
    return sorted(answer)
# def solution(strlist):
#     answer = []
#     for i in strlist:
#         answer.append(len(i))
#     return answer 


def solution(my_string, letter):
    answer = ''
    
    answer=my_string.replace(letter,'')
    
    return answer
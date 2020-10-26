import re
def solution(phone_number):
    if len(phone_number) == 4:
        return phone_number
    return re.sub('[0-9]', '*', phone_number, count=len(phone_number) - 4)
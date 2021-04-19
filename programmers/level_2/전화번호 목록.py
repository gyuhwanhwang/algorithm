from collections import defaultdict
def solution(phone_book):
    len_list = set()
    phone_dict = defaultdict(int)
    for phone in phone_book:
        phone_dict[phone] += 1
        len_list.add(len(phone))

    for phone in phone_book:
        # each len check
        for num in len_list:
            if num >= len(phone):
                continue
            if phone[:num] in phone_dict:
                return False

    return True
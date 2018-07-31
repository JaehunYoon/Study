def add_dict(lists):
    for user in lists:
        return user.text

def check_unranked(lists):
    if lists == []:
        return "Unranked"
    else:
        return add_dict(lists)

rm_escape_sequence = lambda x: x.replace('\n','').replace(' ', '').replace('\t', '')
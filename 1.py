'''
I assume that all input data is correct;
Type of <Timestamp> in this example changes each second for generality
'''

def func(iter):
    new_dict = {}
    for item in iter:
        if item['UserID'] in new_dict and \
                (item['Timestamp'] > new_dict[item['UserID']][-1][0] + 86400):
            new_dict[item['UserID']].append((item['Timestamp'], item['PageID']))
        else:
            new_dict[item['UserID']] = [(item['Timestamp'], item['PageID'])]
    return new_dict
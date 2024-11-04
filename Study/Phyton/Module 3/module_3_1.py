calls = 0
def count_calls():
    global calls
    calls = calls+1
    return calls
#--------------------------
def string_info(a):
    count_calls()
    result=(len(a), a.upper(), a.lower())
    return result
#--------------------------
def is_contains(a, b):
    count_calls()
    a = a.upper()
    d=[]
    for i in b:
        d.append(i.upper())
    if a in d:
        result = True
    else:
        result = False
    return result
#-------------------------

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
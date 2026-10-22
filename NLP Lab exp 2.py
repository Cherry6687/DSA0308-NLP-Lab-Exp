
def finite_automaton(string):
    state = 0

    for char in string:
        if state == 0:
            if char == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if char == 'a':
                state = 1
            elif char == 'b':
                state = 2
            else:
                state = 0

        elif state == 2:
            if char == 'a':
                state = 1
            else:
                state = 0

    return state == 2


strings = ["ab", "aab", "charishma", "charishmab", "charab", "sharma"]

for s in strings:
    if finite_automaton(s):
        print(s, "-> Accepted")
    else:
        print(s, "-> Rejected")

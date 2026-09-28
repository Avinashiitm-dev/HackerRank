def minion_game(string):
    word=string.upper()
    vovel='AEIOU'
    stuart_scr=0
    kevin_scr=0
    for i in range(len(string)):
        if word[i] in vovel:
            kevin_scr+=len(string)-i
        elif word[i] not in vovel:
            stuart_scr+= len(string)-i
    if stuart_scr>kevin_scr:
        print(f'Stuart {stuart_scr}')
    elif kevin_scr> stuart_scr:
        print(f'Kevin {kevin_scr}')
    else:
        print('Draw')



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
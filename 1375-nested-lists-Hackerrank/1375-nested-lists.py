if __name__ == '__main__':
    score_lst=[]
    marksheet=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_lst.append(score)
        marksheet.append([name,score])
    second_lowest= sorted(list(set(score_lst)))[1]
    names=[name for name,scores in sorted(marksheet) if scores==second_lowest]
    for i in names :
        print(i)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
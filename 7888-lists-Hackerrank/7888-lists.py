if __name__ == '__main__':
    N = int(input())
    lst=[]
    for _ in range(N):
        arg=input().split()
        command=arg[0]
        if command == 'insert':
            lst.insert(int(arg[1]),int(arg[2]))
        elif command=='print':
            print(lst)
        elif command=='remove':
            lst.remove(int(arg[1]))
        elif command == 'pop':
            lst.pop()
        elif command=='append':
            lst.append(int(arg[1]))
        elif command=='reverse':
            lst.reverse()
        elif command=='sort':
            lst.sort()
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
import sys
input = sys.stdin.readline

n = int(input())
queue = []
command = []
for i in range(n):
    command = input().split()
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])

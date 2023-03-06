T = int(input())
for tc in range(T):
    N = int(input())
    board = [[int(i) for i in input().split()] for _ in range(N)]
    si = sj = 0 #처음
    #사과 개수 구하기
    apple = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                apple += 1


    def solveFiFj(n):
        global fi
        global fj
        for i in range(N):
            for j in range(N):
                if board[i][j] == n:
                    fi = i
                    fj = j

    def solve(fi,fj): #제발 풀리길
        global cnt
        cnt = 0
        if si > fi and sj > fj :
            cnt += 3
        if si > fi and sj == fj :
            cnt += 0
        if si > fi and sj <fj :
            cnt += 3
        if si == fi and sj > fj :
            cnt += 3
        if si == fi and sj < fj :
            cnt += 0
        if si < fi and sj > fj :
            cnt += 2
        if si < fi and sj == fj :
            cnt += 0
        if si < fi and sj < fj :
            cnt += 2

    ans = 0
    fi = fj = 0
    solveFiFj(1)
    si = fi
    sj = fj
    for i in range(2,apple):
        # print(fi,fj)
        # print("시작점 .. ",si,sj)
        solveFiFj(i)
        solve(fi,fj)
        si = fi
        sj = fj
        # print(cnt)
        # print("다시 출발점",si,sj)
        ans += cnt

    print(f"#{tc+1}",ans+1)
    # print(ans+1)










di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1] #좌우

for i in range(8):
    dx = i + di[i]
    dy = j + dj[i]
'''
5
5
0 0 0 0 0 
0 0 0 3 0 
0 1 0 0 0 
0 0 2 0 0 
0 0 0 0 0 
5
0 0 0 0 0 
0 3 0 0 0 
0 0 2 0 0 
0 0 4 1 0 
0 0 0 0 0 
5
0 0 0 0 0 
0 0 1 4 0 
0 5 3 0 0 
0 2 0 0 0 
0 0 0 0 0 
7
0 0 0 0 0 0 0 
0 2 0 4 0 0 0 
0 0 0 0 0 6 0 
0 0 0 0 5 0 0 
0 0 0 0 1 3 0 
0 0 7 0 0 0 0 
0 0 0 0 0 0 0 
10
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 5 0 0 0 0 
0 0 0 0 4 0 0 0 0 0 
0 0 0 10 0 0 0 0 0 0 
0 0 0 0 0 0 8 0 0 0 
0 0 0 0 0 0 0 0 2 0 
0 0 0 0 0 0 0 1 0 0 
0 0 0 0 6 9 0 0 0 0 
0 0 3 0 0 0 0 0 7 0 
0 0 0 0 0 0 0 0 0 0 

#1 7

#2 9

#3 10

#4 14

#5 23
'''

T = int(input())
for tc in range(T):
    N, P = map(int,input().split())  #P는 화력
    garden = [[int(i) for i in input().split()] for _ in range(N)]

    # pprint(garden)

    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    max_cnt = 0

    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(4):
                for l in range(1,P+1):
                    dx = i + di[k]*l
                    dy = j + dj[k]*l
                    if 0 <= dx < N and 0 <= dy < N:  #범위설정
                        cnt += garden[dx][dy]
                        # print("test",cnt,dx,dy)
                        # print("한번 끝")
            cnt = cnt + garden[i][j]
            if max_cnt < cnt :
                max_cnt = cnt
                # print("확인",cnt)
                # print(i,j,cnt+garden[i][j])
    print(f'#{tc+1}',max_cnt)



# from pprint import pprint
T = int(input())
for tc in range(T):
    #제일 멀리 있는 걸 구해야 함
    N = int(input())
    map = [[int(i) for i in input().split()] for _ in range(N+1)]
    # pprint(map)
    si = sj = 0
    di_lst = []
    dj_lst = []

    for i in range(N+1):
        for j in range(N+1):
            if map[i][j] == 2:
                si = i
                sj = j
            if map[i][j] == 1:
                di_lst.append(i)
                dj_lst.append(j)


    # print("중계기 위치",si, sj)
    # print("di",di_lst)
    # print("dj",dj_lst)
    far = 0
    dl = len(di_lst)
    for i in range(dl):
        if far < (di_lst[i]-si)**2 + (dj_lst[i]-sj)**2:
            far = (di_lst[i]-si)**2 + (dj_lst[i]-sj)**2
    # print("먼 거리 제곱", far)
    for i in range(1,101):
        if i**2 >= far:
            print(f"#{tc+1}",i)
            break

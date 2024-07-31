for t in range(int(input())):
    N = int(input())
    bus_range = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_stops = [int(input()) for _ in range(P)]
    bus_cnts = [0] * P

    for i in range(P):
        bus_cnts[i] = sum((bus_range[j][0] <= bus_stops[i] <= bus_range[j][1]) * 1 for j in range(N))

    print(f'#{t+1}', *bus_cnts)
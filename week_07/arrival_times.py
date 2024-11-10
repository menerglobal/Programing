def arrival_times(time_list, delay):
    delay_h = delay // 60
    delay_m = delay %60
    for t in time_list:
        hm = t.split(':')
        h = int(hm[0])
        m = int(hm[1])
        m = m + delay_m
        h = h + delay_h + m // 60
        m = m % 60
        h = h % 24
        print(h,m)


print(arrival_times['22.00','23.00'],102)
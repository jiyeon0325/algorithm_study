# i_time = input("")

H, M = map(int, input().split())

(0 <= H <= 23)
(0 <= M <= 59)

if H == 0 :
    H = 24
    pass

if M < 45 :
    H = H - 1
    M = M + 15

else :
    M = M - 45

time = "%d %d" %(H, M)
print(time)


# if H > 24 :
#     H = int(H) - 24
#     H = str(H)


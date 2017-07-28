S1 = input()
S2 = input()
cnt = 0
idx = 0
while True:
    idx = S1.find(S2, idx)
    if idx >= 0:
        cnt += 1
        idx += 1
    else:
        break
print(cnt)
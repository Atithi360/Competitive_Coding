T = input()
for test in range(1,T+1):
    [N,K] = map(int,raw_input().split())
    array = []
    ans = []
    count = 0
    array.append(N)
    a=5
    while True:
        m = max(array)
        while True:
            try:
                i = array.index(m)
                if m%2==0:
                    first = m/2
                    second = first - 1
                    array[i:i+1] = second, first
                    count+=1
                    ans = [first,second]
                else:
                    first = m/2
                    array[i:i+1] = first, first
                    count += 1
                    ans = [first,first]
            except ValueError:
                break
        #print array
        if count>=K:
            break
    print ('Case #'+str(test)+': '+str(ans[0])+' '+str(ans[1]))


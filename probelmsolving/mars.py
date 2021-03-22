

signal = 'SOSsOsSOs'
# length = len(signal)
# i,f,key=0,0,''
# while i < length/3:
#     key = key + 'SOS'
#     i=i+1
# while i < length:
#     if key[i]!=signal[i]:
#         f=f+1
#     i=i+1
# print(f)

error=0
for i in range(len(signal)):
    if i % 3 ==0:
        # print(i)
        if signal[i] !='S':
            error+=1
        # else:
        #     pass
    if i % 3 == 1:
        # print(i)
        if signal[i] !='O':
            error += 1
        # else:
        #     pass
    if i % 3 == 2:
        # print(i)
        if signal[i] !='S':
            error += 1
        # else:
        #     pass
print (error)

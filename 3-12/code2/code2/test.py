import numpy as np



arr = np.arange(0,1000)
# kind 1
cnt = 0
for i in arr :
    cnt += 1
    if cnt  == 6 :
        print(i)

# kind 2
print(arr[5])

# kind 3



# a = np.random.rand(6,6) * 10
# print(a)
# print(a.mean())
# a = a - a.mean()
# print(a)


# a = np.random.rand(8,8)
#
# a[np.unravel_index(np.argmax(a),a.shape)] = 1
# a[np.unravel_index(np.argmin(a),a.shape)] = 0
# print(np.unravel_index(np.argmax(a),a.shape))
# print(np.unravel_index(np.argmin(a),a.shape))
#
# print(a)


# a = np.random.randint(1,10,20) * 2
# print(a)

# arr = np.random.rand(6,6) * 10
# print(arr)
# floor_arr = np.floor(arr)
# print(floor_arr)
# intarr = arr.astype(int)
# print(intarr)
# truncarr = np.trunc(arr)
# print(truncarr)
# print(a)






# list1 = []
# for i in range(1,32) :
#     print("8." + str(i))
#     list1.append("8."+str(i))
#
# print(list1)
# a = np.random.randint(10,30,(8,8))
# b = np.random.randint(10,30,(8,8))
#
#
# for i in range(8):
#     for j in range(8):
#         if a[i][j] == b[i][j] :
#             print("i is : " + str(i)+ " j is : " + str(j) +" || "+ str(a[i][j]) + " is euqual ")

# a = np.random.randint(1,100,10)
# print(a)
# ans = []
# for i in range(2,8) :
#     ans.append(-a[i])
# print(ans)

# a = np.zeros((6,6))
#
# a[0][0] = 1
# a[5][0] = 1
# a[0][5] = 1
# a[5][5] = 1
#
# print(a)



# a = np.ndarray((8,8),int)
# for i in range(8) :
#     for j in range(8) :
#         if (i + j) % 2 == 0 :
#             a[i][j] = 0
#         else :
#             a[i][j] = 1
# print(a)
#

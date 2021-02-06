i = 2
while i <= 12:
    print("   " + "[", i, "]")
    j = 1
    while j <= 12:
        print(i, "*", j, ":", i * j)
        j += 1
    print("")
    print("---------------" "\n")
    i += 1

# 2
for i in range(1, 13):
    print("   " + "[", i, "]")
    for j in range(1, 13):
        print(i, "*", j, ":", i * j)
    print("--------------")
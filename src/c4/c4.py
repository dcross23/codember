
total = []
for n in range(11098, 98124):
    str_num = str(n)
    if str_num.count('5') >= 2 and str_num[0] <= str_num[1] <= str_num[2] <= str_num[3] <= str_num[4]:
        total.append(n)

print(str(len(total)) + "-" + str(total[55]))

    




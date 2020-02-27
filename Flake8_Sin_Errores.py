def Escal(mo):
    r = True
    k = 0
    m = 0
    while (m < len(mo)):
        if (mo[m][k] > 0):
            m += 1
            for j in range(m, len(mo)):
                if (mo[j][k] != 0):
                    r = False
        else:
            k += 1

    return r


mo = [[1, 2, 2], [0, 7, 9], [0, 0, 4]]
print(mo)
print(Escal(mo))

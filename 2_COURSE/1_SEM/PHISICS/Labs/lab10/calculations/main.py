if __name__ == '__main__':
    Ul = [i for i in range(6)]
    Il = [8.2, 7.0, 6.0, 5.0, 3.8, 2.7]
    E = 7.4
    Ri_li = []
    for i in range(6):
        I = round(Il[i] * 10 ** -3, 4)
        U = Ul[i]
        P = round(E*I, 4)
        Pe = round(U*I, 4)
        eta = round(Pe/P, 4)
        R1Ri = round(U/(E - U), 4)
        Ri = round((E - U) / I, 2)
        Ri_li.append(Ri)
        s = f"{i+1} & $ {U} $ & $ {I} $ & $ {P} $ & $ {Pe} $ & $ {eta} $ & $ {R1Ri} $\\\\\n" \
            f"\\hline"
        s2 = f"{i+1},{U},{I},{P},{Pe},{eta},{R1Ri}"
        s3 = f"{i+1} & $ {U} $ & $ {I} $ & $ {Ri} $\\\\\n" \
             f"\\hline"
        # print(s3)

    Ul = [i for i in range(6)]
    Il = [9.4, 7.9, 6.4, 4.9, 3.2, 1.9]
    E = 6.2
    Ri_li = []
    for i in range(6):
        I = round(Il[i] * 10 ** -3, 4)
        U = Ul[i]
        P = round(E*I, 4)
        Pe = round(U*I, 4)
        eta = round(Pe/P, 4)
        R1Ri = round(U/(E - U), 4)
        Ri = round((E - U) / I, 2)
        Ri_li.append(Ri)
        s = f"{i+1} & $ {U} $ & $ {I} $ & $ {P} $ & $ {Pe} $ & $ {eta} $ & $ {R1Ri} $\\\\\n" \
            f"\\hline"
        s2 = f"{i + 1},{U},{I},{P},{Pe},{eta},{R1Ri}"
        s3 = f"{i + 1} & $ {U} $ & $ {I} $ & $ {Ri} $\\\\\n" \
             f"\\hline"
        print(s3)

    print(sum(Ri_li), "/", len(Ri_li), "=", sum(Ri_li)/len(Ri_li))
    print(E ** 2/(4 * sum(Ri_li)/len(Ri_li)))
    print(E ** 2 / (sum(Ri_li)/len(Ri_li)))

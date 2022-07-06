if __name__ == '__main__':
    s = input()
    res = ["false" , "false" , "false" , "false" , "false"]
    for i in s:
        if i.isalnum():
            res[0] = "True"
        if i.isalpha():
            res[1] = "True"
        if i.isdigit():
            res[2] = "True"
        if i.islower():
            res[3] = "True"
        if i.isupper():
            res[4] = "True"
    print(*res, sep="\n")

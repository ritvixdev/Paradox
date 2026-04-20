# input = aaaaabbbbbcccccdddddddaaaaaa
#output = a4b5c5d4a7

def freq_checker(string):
    if not string:
        return ""

    result = ""
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            result += string[i - 1] + str(count)
            count = 1

    # add last character group
    result += string[-1] + str(count)

    return result


print(freq_checker(string))
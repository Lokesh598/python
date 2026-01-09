
# given string, revers the string

def reverse_string(str : str) -> str:
    chars = list(str)
    n = len(str)
    start = 0
    end = n-1

    while start < end:
        tmp = chars[start]
        chars[start] = chars[end]
        chars[end] = tmp
        start +=1
        end -=1

    return ''.join(chars)

print(reverse_string("python"))


# reverse words
# Input: s = " i like this program very much "
# Output: "much very program this like i"

def reverse_words(st : str) -> str :

    # st = st.rstrip()
    # st = st.lstrip()

    st = st.strip()


    print(reverse_string(st))
    char = []
    for c in st:
        char.append(c)

    s = 0
    e = 0
    for c in range(len(char)-1):
        if char[c] == ' ':
            reverse_string(''.join(char))
        e = e+1


s = " i like this program very much "
reverse_words(s)
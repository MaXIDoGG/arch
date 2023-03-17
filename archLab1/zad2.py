file = open('hi.txt')

s = ""
for line in file:
    s += line

s = s.replace('\n', ' ')

words = s.split(' ')

c = [i + ': ' + str(s.count(i)) for i in words]

c = ", ".join(list(set(c)))
print(c)
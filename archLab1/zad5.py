d = {'1': 1, '2': 2, '3': 3}

try:
    print(d['4'])
except KeyError as e:
    print(e)
except:
    print("Unknown error")

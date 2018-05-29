from collections import Counter

def getData(file):
    with open(file, 'r') as f:
        data = f.read().split()
    return data



if __name__ == '__main__':
    data = getData('file.txt')
    # print(data)
    # data = ['apple', 'egg', 'apple', 'banana', 'egg', 'apple']
    counts = Counter(data)
    print(counts)

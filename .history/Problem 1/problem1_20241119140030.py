
def topKFrequency(array, k):
    frequency = {}
    for i in array:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True))


def main():
    userInputList = input("Enter the list you want to sort separated by spaces:")
    inputK = int(input("Enter the top k you want see:"))
    array = list(map(int, userInputList.split()))
    array.sort(reverse=False)
    topKFrequency(array, inputK)
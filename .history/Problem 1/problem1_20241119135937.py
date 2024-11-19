
def topKFrequency(array, k):
    frequency = {}
    for i in array:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
    count = 0
    for key in frequency:
        print(key, end=" ")
        count += 1
        if count == k:
            break

def main():
    userInputList = input("Enter the list you want to sort separated by spaces:")
    inputK = int(input("Enter the top k you want see:"))
    array = list(map(int, userInputList.split()))
    array.sort(reverse=False)
    topKFrequency(array, inputK)
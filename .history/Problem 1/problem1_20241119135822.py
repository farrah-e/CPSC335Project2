
def main():
    userInputList = input("Enter the list you want to sort separated by spaces:")
    inputK = int(input("Enter the top k you want see:"))
    array = list(map(int, userInputList.split()))
    array.sort(reverse=True)
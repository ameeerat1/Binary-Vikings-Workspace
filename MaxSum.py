num = list(map(int, input("Enter the elements: ").split()))
num.sort(reverse=True)
n = int(input("Enter the number of value : "))
print(f"Maximum possible sum of the first {n} elements: {sum(num[:n])}")

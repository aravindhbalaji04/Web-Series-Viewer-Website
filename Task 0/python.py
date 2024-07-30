def print_subsets(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            print(*range(lst[i], lst[j]+1), end=" ")
        print()

# Example usage:
nums = list(map(int, input("Enter sorted integers separated by spaces: ").split()))
print_subsets(nums)

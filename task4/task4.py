def min_moves_to_equal(nums):
    median = sorted(nums)[len(nums) // 2]
    return sum(abs(num - median) for num in nums)


nums = []
n = int(input("Введите размер списка: "))
for i in range(n):
    nums.append(int(input(f"Введите {i+1}-й элемент списка: ")))

result = min_moves_to_equal(nums)

print(f"Минимальное количество ходов: {result}")

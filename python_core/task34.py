class MathUtil:
    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)

numbers = (1,2,3,4)
print("Sum:", MathUtil.calculate_sum(numbers))  
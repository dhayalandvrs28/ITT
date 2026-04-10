class Solution:
    def calculate_all(self, a, b, list_a, list_b):

        return {
            "Addition": a + b,
            "Subtraction": a - b,
            "Multiplication": a * b,
            "Division": a / b if b != 0 else "Undefined",
            "Union": set(list_a) | set(list_b),
            "Intersection": set(list_a) & set(list_b),
            "Difference": set(list_a) - set(list_b)
        }

if __name__ == "__main__":

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))


    set1_raw = input("Enter Set A (e.g. 1 2 3): ").split()
    set2_raw = input("Enter Set B (e.g. 3 4 5): ").split()
    

    set1 = [int(x) for x in set1_raw]
    set2 = [int(x) for x in set2_raw]


    sol = Solution()
    results = sol.calculate_all(num1, num2, set1, set2)
    
    print("\n--- Results ---")
    for key, value in results.items():
        print(f"{key}: {value}")


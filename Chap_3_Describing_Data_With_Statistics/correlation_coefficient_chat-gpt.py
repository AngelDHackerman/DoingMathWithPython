
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_correlation(x, y):
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator_x = sum((xi - mean_x)**2 for xi in x)
    denominator_y = sum((yi - mean_y)**2 for yi in y)
    
    denominator = (denominator_x * denominator_y) ** 0.5
    
    correlation = numerator / denominator
    return correlation

if __name__ == "__main__":
    x = [10, 20, 30, 40, 50]
    y = [15, 25, 35, 45, 55]
    correlation = calculate_correlation(x, y)
    print("The correlation coefficient is:", correlation)

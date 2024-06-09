
# Visualize your expenses using matplotlib and bar graphs

import matplotlib.pyplot as plt

def get_expenses(num_categories):
    categories = []
    expenditures = []

    for _ in range(num_categories):
        category = input('Enter category: ')
        expenditure = float(input(f'Expenditure for {category}: '))
        categories.append(category)
        expenditures.append(expenditure)

    return categories, expenditures

def plot_expenses(categories, expenditures):
    # Bar chart 
    plt.figure(figsize=(10, 5))

    # Vertical bar chart
    plt.subplot(1, 2, 1)
    plt.bar(categories, expenditures, color='blue')
    plt.xlabel('Category')
    plt.ylabel('Expenditure')
    plt.title('Weekly Expenditure by Category')

    # Horizontal bar chart
    plt.subplot(1, 2, 2)
    plt.barh(categories, expenditures, color='blue')
    plt.xlabel('Expenditure')
    plt.ylabel('Category')
    plt.title('Weekly Expenditure by Category (Horizontal)')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        num_categories = int(input('Enter the number of categories: '))
        categories, expenditures = get_expenses(num_categories)
    except ValueError:
        print('You entered an invalid input')
    else:
        plot_expenses(categories, expenditures)

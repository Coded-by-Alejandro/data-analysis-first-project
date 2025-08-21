import numpy as np
#The process for coding this project is...
#1) import numpy for calculations
#2) define the function 'calculate' whose parameter is a list of elements of a 3x3 matrix 
#3) use numpy to reshape the list into the real matrix
#4) calculate statistics
#5) save the results into a dictionnary named as calculations
#6) mapping the result (return the dictionnary)
def calculate(list):
    matrix = np.array(list).reshape(3, 3)
    axis0_mean = np.mean(matrix, axis=0)
    axis1_mean = np.mean(matrix, axis=1)
    flattened_mean = np.mean(matrix)

    axis0_var = np.var(matrix, axis=0)
    axis1_var = np.var(matrix, axis=1)
    flattened_var = np.var(matrix)

    axis0_std = np.std(matrix, axis=0)
    axis1_std = np.std(matrix, axis=1)
    flattened_std = np.std(matrix)

    axis0_max = np.max(matrix, axis=0)
    axis1_max = np.max(matrix, axis=1)
    flattened_max = np.max(matrix)

    axis0_min = np.min(matrix, axis=0)
    axis1_min = np.min(matrix, axis=1)
    flattened_min = np.min(matrix)

    axis0_sum = np.sum(matrix, axis=0)
    axis1_sum = np.sum(matrix, axis=1)
    flattened_sum = np.sum(matrix)


    calculations = {
        'mean': [axis0_mean, axis1_mean, flattened_mean],
        'variance': [axis0_var, axis1_var, flattened_var],
        'standard deviation': [axis0_std, axis1_std, flattened_std],
        'max': [axis0_max, axis1_max, flattened_max],
        'min': [axis0_min, axis1_min, flattened_min],
        'sum': [axis0_sum, axis1_sum, flattened_sum]
        }
    return calculations

#MOVING THIS TO main.py
#def main():
#    while True:
#        user_input = input("Enter 9 numbers separated by space: ")
#        items = user_input.split()
#
#        if len(items) != 9:
#            print("Please enter exactly 9 numbers.")
#            continue 
#
#        try:
#            
#            numbers = [float(x) for x in items]
#            break  
#        except ValueError:
#            print("Please enter valid numbers (integers or decimals).")
#    
#    for key, value in calculate(numbers).items():
#     print(f"{key.capitalize()}:")
#     print("Axis0:", value[0])
#     print("Axis1:", value[1])
#     print("Flattened:", value[2])
#     print()

#if __name__ == "__main__":
#    main()
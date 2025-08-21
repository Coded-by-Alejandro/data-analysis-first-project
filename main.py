# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
def main():
    while True:
        user_input = input("Enter 9 numbers separated by space: ")
        items = user_input.split()

        if len(items) != 9:
            print("Please enter exactly 9 numbers.")
            continue 

        try:
            
            numbers = [float(x) for x in items]
            break  
        except ValueError:
            print("Please enter valid numbers (integers or decimals).")
    
    for key, value in mean_var_std.calculate(numbers).items():
     print(f"{key.capitalize()}:")
     print("Axis0:", value[0])
     print("Axis1:", value[1])
     print("Flattened:", value[2])
     print()

if __name__ == "__main__":
    main()
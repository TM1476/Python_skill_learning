import numpy as np

def get_matrix(name):
    print(f"\nEnter details for Matrix {name}:")
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    
    print(f"Enter the elements row-wise (space-separated):")
    elements = list(map(float, input().split()))
    
    matrix = np.array(elements).reshape(rows, cols)
    return matrix

def main():
    print("=== NumPy Matrix Operations Tool ===")
    
    try:
        matrix_a = get_matrix("A")
        print("\nMatrix A:\n", matrix_a)
        
        while True:
            print("\n--- Select Operation ---")
            print("1. Addition (A + B)")
            print("2. Subtraction (A - B)")
            print("3. Multiplication (A * B)")
            print("4. Transpose (A)")
            print("5. Determinant (A)")
            print("6. Exit")
            
            choice = input("Enter choice (1-6): ")
            
            if choice == '1':
                matrix_b = get_matrix("B")
                if matrix_a.shape == matrix_b.shape:
                    print("\nResult (A + B):\n", np.add(matrix_a, matrix_b))
                else:
                    print("Error: Matrices must have the same dimensions for addition.")
            
            elif choice == '2':
                matrix_b = get_matrix("B")
                if matrix_a.shape == matrix_b.shape:
                    print("\nResult (A - B):\n", np.subtract(matrix_a, matrix_b))
                else:
                    print("Error: Matrices must have the same dimensions for subtraction.")
            
            elif choice == '3':
                matrix_b = get_matrix("B")
                if matrix_a.shape[1] == matrix_b.shape[0]:
                    print("\nResult (A * B):\n", np.dot(matrix_a, matrix_b))
                else:
                    print("Error: A's columns must match B's rows for multiplication.")
            
            elif choice == '4':
                print("\nTranspose of A:\n", matrix_a.T)
            
            elif choice == '5':
                if matrix_a.shape[0] == matrix_a.shape[1]:
                    det = np.linalg.det(matrix_a)
                    print(f"\nDeterminant of A: {det:.2f}")
                else:
                    print("Error: Determinant can only be calculated for square matrices.")
            
            elif choice == '6':
                print("Exiting tool...")
                break
            else:
                print("Invalid choice. Please try again.")
                
    except Exception as e:
        print(f"An error occurred: {e}. Please ensure input matches dimensions.")

if __name__ == "__main__":
    main()

# Import the necessary libraries
import math
import numpy as np

def input_two_points():
  """Function to input a point and return it as a tuple of floats."""
  while True:
    try:
        P1 = tuple(map(float, input("Write the values of x and y of P1(x,y), separated by space: ").split()))
        P2 = tuple(map(float, input("Write the values of x and y of P2(x,y), separated by space: ").split()))
        return P1, P2
    except ValueError:
        print("Invalid input. Please enter numeric values.")


def calculate_vector(P1,P2):
  """Function to calculate the vector formed by two points P1 and P2."""
  vector = P2[0] - P1[0], P2[1] - P1[1]
  return vector

def vector_magnitude(vector):
  """Function to calculate the magnitude of a vector."""
  magnitude = math.sqrt(vector[0]**2 + vector[1]**2)
  return magnitude

def main_manual():
  """Main function to execute the manual calculation of the vector and its magnitude."""
  P1, P2 = input_two_points()
  vector = calculate_vector(P1, P2)
  magnitude = vector_magnitude(vector)
  print(f"Using manual calculation, the vector formed by the points P1 and P2 is: {vector}")
  print(f"The magnitude of the vector is: {magnitude:.2f}")


def main_numpy():
   """Main function to execute the calculation of the vector and its magnitude using NumPy."""
   P1, P2 = input_two_points()
   vector = np.array(P2) - np.array(P1)
   magnitude = np.linalg.norm(vector)
   print(f"Using NumPy, the vector formed by the points P1 and P2 is: {tuple(float(x) for x in vector)}")
   print(f"The magnitude of the vector is: {magnitude:.2f}")

# Execute the main functions
main_manual()
main_numpy()
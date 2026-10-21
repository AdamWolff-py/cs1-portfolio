#PiApproximation.py

"""This program take the error tolerance from the user and finds the minimum nuber of terms required to get the approximation of pi accurate within the error tolerance given. It then displays the number of terms and pi approximations in a table format. then it tells after how many terms our pi aproximation is found."""

error = float(input("Input error tolerance: "))
print()
pi = 3.14159265358979
diff = 1
pi_approx = 0
k = 1

print("Number of Terms",end = "")
print("\t\tPi Approximation")

while diff > error:
    pi_end = ((4 * (-1)**(k+1)) / ((2 * k) - 1))
    pi_approx += pi_end
    print(k,"\t\t\t\t\t",f"{pi_approx:.6f}")
    diff = abs(pi_approx - pi)
    k += 1

print()
print(f"After {k-1} terms, pi is approximately {pi_approx:.6f}.")
print(f"Our error is {diff:.6f} which is less than or equal to {error:.6f}.")
    
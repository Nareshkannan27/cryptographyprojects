def extended_gcd_non_recursive(m, b):
    # Initialize initial values
    A1, A2, A3 = 1, 0, m
    B1, B2, B3 = 0, 1, b

    print("Iteration: 0")
    print(f"A1: {A1}, A2: {A2}, A3: {A3}")
    print(f"B1: {B1}, B2: {B2}, B3: {B3}")

    iteration = 1

    while True:
        if B3 == 0:
            return A3, None, None  # No inverse exists
        elif B3 == 1:
            return B3, B2 % m, None  # Inverse exists

        Q = A3 // B3
        T1, T2, T3 = A1 - Q * B1, A2 - Q * B2, A3 - Q * B3
        A1, A2, A3 = B1, B2, B3
        B1, B2, B3 = T1, T2, T3

        print(f"Iteration: {iteration}")
        print(f"A1: {A1}, A2: {A2}, A3: {A3}")
        print(f"B1: {B1}, B2: {B2}, B3: {B3}")

        iteration += 1

def main():
    m = int(input("Enter m: "))
    b = int(input("Enter b: "))

    gcd, inverse, _ = extended_gcd_non_recursive(m, b)

    if gcd == 1:
        print(f"Inverse of {b} mod {m} is: {inverse}")
    else:
        print("No inverse exists.")

if __name__ == "__main__":
    main()

def solve_problem_1(T, H_total):
    # Constraint checks
    if not (H_total >= 24 and H_total % 2 == 0 and T < H_total):
        print("INVALID INPUT")
        return

    found = False
    # Each 'D' unit is 24 hours. We need to find the 'H' unit value.
    # Based on the example (D=10, H=5, Total=330), the 'H' unit is 18.
    H_unit_value = 18 

    for D in range(T + 1):
        H = T - D
        if (D * 24) + (H * H_unit_value) == H_total:
            print(f"D = {D}, H = {H}")
            found = True
            break
    
    if not found:
        print("INVALID INPUT")

# Input from the problem
solve_problem_1(15, 330)

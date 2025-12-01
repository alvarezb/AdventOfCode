#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 1: Secret Entrance
Simulates a safe dial with rotations to find how many times it lands on 0.
"""

def solve_safe_combination(filename):
    """
    Simulates rotating a safe dial and counts how many times it lands on 0.

    The dial has numbers 0-99 and wraps around:
    - Starting position: 50
    - L (left) rotations decrease the position
    - R (right) rotations increase the position

    Args:
        filename: Path to the input file containing rotation instructions

    Returns:
        Number of times the dial points to 0 after any rotation
    """
    # Starting position of the dial
    position = 50

    # Counter for how many times the dial lands on 0
    zero_count = 0

    # Read and process each rotation instruction
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Parse the rotation: first character is direction (L or R)
            direction = line[0]
            # Remaining characters are the distance to rotate
            distance = int(line[1:])

            # Apply the rotation
            if direction == 'L':
                # Left rotation: subtract distance (modulo handles wrapping)
                position = (position - distance) % 100
            elif direction == 'R':
                # Right rotation: add distance (modulo handles wrapping)
                position = (position + distance) % 100

            # Check if we landed on 0 after this rotation
            if position == 0:
                zero_count += 1

    return zero_count


def test_example():
    """
    Tests the solution with the example from the problem statement.
    Expected output: 3
    """
    # Create a temporary test file with the example data
    example_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

    with open('/tmp/test_input.txt', 'w') as f:
        f.write(example_data)

    result = solve_safe_combination('/tmp/test_input.txt')
    print(f"Example result: {result}")
    print(f"Expected: 3")
    print(f"Test {'PASSED' if result == 3 else 'FAILED'}!\n")

    return result == 3


if __name__ == "__main__":
    # Test with the example first
    print("Testing with example data...")
    if test_example():
        # Run on the actual input
        print("Running on actual input...")
        answer = solve_safe_combination('day01/01_input.txt')
        print(f"\nThe password (number of times dial lands on 0): {answer}")
    else:
        print("Example test failed! Check the logic before running on actual input.")

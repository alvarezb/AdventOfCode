#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 1: Secret Entrance (Part Two)
Counts how many times the dial points at 0 during and after rotations.
"""

def count_zero_crossings(position, direction, distance):
    """
    Counts how many times the dial points at 0 during a rotation.

    Args:
        position: Current dial position (0-99)
        direction: 'L' for left or 'R' for right
        distance: Number of clicks to rotate

    Returns:
        Number of times the dial points at 0 during this rotation
    """
    if direction == 'R':
        # Right rotation: count how many times we cross from 99 to 0
        # We hit 0 every time we complete a full loop of 100
        return (position + distance) // 100

    elif direction == 'L':
        # Left rotation: count how many times we cross from 0 to 99 (backwards)
        complete_loops = distance // 100

        # For the partial rotation, we hit 0 if we go from some position > 0 down through 0
        # This happens when distance % 100 >= position AND we're not starting at 0
        # (if we start at 0 and go left, we jump to 99 and don't hit 0 again)
        partial_distance = distance % 100
        crosses_zero_partial = 1 if (partial_distance >= position and position > 0) else 0

        return complete_loops + crosses_zero_partial

    return 0


def solve_safe_combination_part2(filename):
    """
    Simulates rotating a safe dial and counts how many times it points at 0
    during any rotation (Part Two - method 0x434C49434B).

    The dial has numbers 0-99 and wraps around:
    - Starting position: 50
    - L (left) rotations decrease the position
    - R (right) rotations increase the position
    - Counts ALL times the dial points at 0, including during rotations

    Args:
        filename: Path to the input file containing rotation instructions

    Returns:
        Total number of times the dial points at 0 (during and after rotations)
    """
    # Starting position of the dial
    position = 50

    # Counter for total times the dial points at 0
    total_zero_count = 0

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

            # Count how many times we point at 0 during this rotation
            zeros_this_rotation = count_zero_crossings(position, direction, distance)
            total_zero_count += zeros_this_rotation

            # Apply the rotation to update position
            if direction == 'L':
                position = (position - distance) % 100
            elif direction == 'R':
                position = (position + distance) % 100

    return total_zero_count


def test_example():
    """
    Tests the solution with the example from the problem statement.
    Expected output: 6 (3 ending at 0, plus 3 during rotations)
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

    with open('/tmp/test_input_part2.txt', 'w') as f:
        f.write(example_data)

    result = solve_safe_combination_part2('/tmp/test_input_part2.txt')
    print(f"Example result: {result}")
    print(f"Expected: 6")
    print(f"Test {'PASSED' if result == 6 else 'FAILED'}!\n")

    # Also show the step-by-step breakdown for verification
    print("Step-by-step breakdown:")
    position = 50
    total = 0

    for line in example_data.strip().split('\n'):
        direction = line[0]
        distance = int(line[1:])

        zeros = count_zero_crossings(position, direction, distance)

        if direction == 'L':
            new_position = (position - distance) % 100
        else:
            new_position = (position + distance) % 100

        total += zeros
        print(f"{line}: {position} → {new_position}, zeros crossed: {zeros}, total: {total}")
        position = new_position

    return result == 6


if __name__ == "__main__":
    # Test with the example first
    print("Testing with example data...")
    print("=" * 60)
    if test_example():
        # Run on the actual input
        print("\n" + "=" * 60)
        print("Running on actual input...")
        print("=" * 60)
        answer = solve_safe_combination_part2('day01/01_input.txt')
        print(f"\nThe password (using method 0x434C49434B): {answer}")
    else:
        print("\nExample test failed! Check the logic before running on actual input.")

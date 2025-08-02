def streetlight_duration(A, B):
    if not A:
        return 0

    total_time = 0
    end_time = 0

    for time in A:
        if time >= end_time:
            # No overlap with previous duration
            total_time += B
        else:
            # Overlap, add only the extended duration
            total_time += (time + B - end_time)
        end_time = time + B

    return total_time

# Example usage:
A = [2, 5, 6, 10]
B = 4
print(streetlight_duration(A, B))  # Output: 12

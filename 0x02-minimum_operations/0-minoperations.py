def minOperations(n):
    """
    Calculate the minimum number of operations to achieve n H characters.
    
    Args:
        n (int): The target number of characters.
    
    Returns:
        int: The minimum number of operations.
    """
    operations = 0
    current = 1

    while current < n:
        if n % current == 0:
            operations += 2
            current *= 2  # Double the count after pasting
        else:
            operations += 1
            current += current  # Increment the count by itself
    
    return operations

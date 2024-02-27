def make_sandwich(*items):
    """
    A function that makes a sandwich with the given items.
    
    Parameters:
    *items (tuple): The items to include in the sandwich.
    
    Returns:
    None
    """
    print("Making a sandwich with the following items:")
    for item in items:
        print("- " + item.title())

make_sandwich('bread', 'cheese', 'tomato')
make_sandwich('bread', 'ham', 'lettuce', 'tomato')
make_sandwich('bread', 'cheese', 'tomato', 'onion')
        

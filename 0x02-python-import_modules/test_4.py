#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    print(f"names in file are: {names}")

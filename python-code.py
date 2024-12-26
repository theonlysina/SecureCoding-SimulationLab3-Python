# Example array and index
array = ["apple", "banana", "cherry", "date"]
index = 2

def get_value_from_array(array, index):
    # Check if the index is within the bounds of the array
    if index >= 0 and index < len(array):
        # Return the element at the specified index
        return array[index]
    else:
        # Handle the case where the index is out of bounds
        # You can raise an error or return a special value
        raise IndexError("Index out of bounds")
        # Or alternatively, return a special value like None
        # return None

def main():
    try:
        value = get_value_from_array(array, index)
        print(f"The value at index {index} is {value}.")
    except IndexError as e:
        print(e)

if __name__ == "__main__":
    main()

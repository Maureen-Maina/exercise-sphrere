#program for sorting out names
def main():
    names = input("Enter a list of names, separated by commas: ").split(",")
    names = [name.strip() for name in names]  # Remove leading/trailing whitespace
    
    unique_names = list(set(names))  # Remove duplicates
    sorted_names = sorted(unique_names)  # Sort alphabetically
    
    print("Sorted list of names:")
    for name in sorted_names:
        print(name)
    
    print("Total number of names entered:", len(names))

if __name__ == "__main__":
    main()

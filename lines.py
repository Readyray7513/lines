import sys

def main():
    try:
        # Ensure a filename is provided
        if len(sys.argv) != 2:
            raise FileNotFoundError("Usage: python script.py filename.txt")

        filename = sys.argv[1]
        if not filename.endswith(".py"):
            raise FileNotFoundError("Usage: python script.py filename.py")

        with open(filename, 'r') as file:
            content = file.readlines()
            content = [line.strip() for line in content if line.strip() != "" if line.strip()[0] != "#"]
        print(len(content))  # Print the number of lines

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)  # Exit with error

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit with error

main()


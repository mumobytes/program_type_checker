def modify_content(content):
    return content.upper()


def main():
    # Ask user for the input filename
    input_file = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"File processed successfully! Modified version saved as '{output_file}'.")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()

"""Editor: great program, convenient to use"""


def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")


def choose_formatter():
    while True:
        formatter = input("Choose a formatter: > ")
        if formatter == "!help":
            print_help()
        elif formatter == "!done":
            return None
        elif formatter in ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]:
            return formatter
        else:
            print("Unknown formatting type or command")


def apply_formatter(formatter):
    if formatter == "plain":
        return input("Text: > ")
    elif formatter == "bold":
        return f"**{input('Text: > ')}**"
    elif formatter == "italic":
        return f"*{input('Text: > ')}*"
    elif formatter == "header":
        try:
            level = int(input("Level: > "))
            if 1 <= level <= 6:
                return f"{'#' * level} {input('Text: > ')}"
            else:
                print("The level should be within the range of 1 to 6")
                return None
        except ValueError:
            print("Invalid input. Please enter a valid level (a number between 1 and 6).")
            return None
    elif formatter == "link":
        label = input("Label: > ")
        url = input("URL: > ")
        return f"[{label}]({url})"
    elif formatter == "inline-code":
        return f"`{input('Text: > ')}`"
    elif formatter == "ordered-list":
        try:
            num_rows = int(input("Number of rows: > "))
            if num_rows <= 0:
                print("The number of rows should be greater than zero")
                return None
            rows = [input(f"Row #{i}: > ") for i in range(1, num_rows + 1)]
            return '\n'.join([f"{i + 1}. {row}" for i, row in enumerate(rows)])
        except ValueError:
            print("Invalid input. Please enter a valid number of rows.")
            return None
    elif formatter == "unordered-list":
        try:
            num_rows = int(input("Number of rows: > "))
            if num_rows <= 0:
                print("The number of rows should be greater than zero")
                return None
            rows = [input(f"Row #{i}: > ") for i in range(1, num_rows + 1)]
            return '\n'.join([f"* {row}" for row in rows])
        except ValueError:
            print("Invalid input. Please enter a valid number of rows.")
            return None
    elif formatter == "new-line":
        return '\n'


def main():
    markdown = ""
    while True:
        formatter = choose_formatter()
        if formatter is None:
            break
        formatted_text = apply_formatter(formatter)
        if formatted_text is not None:
            markdown += formatted_text + '\n'
            print(markdown)


    with open("output.md", "w") as file:
        file.write(markdown)


if __name__ == "__main__":
    main()

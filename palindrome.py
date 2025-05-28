def is_palindrome(text):
    # Remove spaces and convert to lowercase for accurate comparison
    clean_text = ''.join(text.lower().split())
    return clean_text == clean_text[::-1]

def main():
    text = input("Enter a string to check for palindrome: ")
    if is_palindrome(text):
        print(f"'{text}' is a palindrome!")
    else:
        print(f"'{text}' is not a palindrome.")

if __name__ == "__main__":
    main()

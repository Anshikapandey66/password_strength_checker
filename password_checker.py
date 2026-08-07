import string

def check_password_strength(password):
    score = 0

    # Length Check
    if len(password) >= 8:
        score += 1

    # Uppercase Check
    if any(char.isupper() for char in password):
        score += 1

    # Lowercase Check
    if any(char.islower() for char in password):
        score += 1

    # Number Check
    if any(char.isdigit() for char in password):
        score += 1

    # Special Character Check
    if any(char in string.punctuation for char in password):
        score += 1

    print("\nPassword Analysis")
    print("-" * 30)
    print(f"Length (8+): {'✔' if len(password) >= 8 else '✘'}")
    print(f"Uppercase: {'✔' if any(char.isupper() for char in password) else '✘'}")
    print(f"Lowercase: {'✔' if any(char.islower() for char in password) else '✘'}")
    print(f"Numbers: {'✔' if any(char.isdigit() for char in password) else '✘'}")
    print(f"Special Characters: {'✔' if any(char in string.punctuation for char in password) else '✘'}")

    print("\nPassword Strength:", end=" ")

    if score <= 2:
        print("🔴 Weak")
    elif score == 3 or score == 4:
        print("🟡 Medium")
    else:
        print("🟢 Strong 💪")


print("=" * 40)
print("      PASSWORD STRENGTH CHECKER")
print("=" * 40)

password = input("\nEnter your password: ")

check_password_strength(password)

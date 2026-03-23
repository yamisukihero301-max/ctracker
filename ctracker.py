import time

def analyze_account():
    print("\n=== InstaFake Detector v1.0 ===\n")

    username = input("Enter username: ")
    followers = int(input("Followers count: "))
    following = int(input("Following count: "))
    posts = int(input("Number of posts: "))
    bio = input("Bio (leave empty if none): ")

    print("\nAnalyzing account...\n")
    time.sleep(2)

    score = 0

    # Rule 1: Low followers + high following
    if followers < 50 and following > 300:
        print("⚠️ Suspicious follow pattern")
        score += 1

    # Rule 2: No posts
    if posts == 0:
        print("⚠️ No posts on account")
        score += 1

    # Rule 3: Empty bio
    if bio.strip() == "":
        print("⚠️ Empty bio")
        score += 1

    # Rule 4: Username randomness
    if any(char.isdigit() for char in username):
        print("⚠️ Username contains random numbers")
        score += 1

    print("\n=== Result ===")

    if score >= 3:
        print("🚨 High chance: FAKE account")
    elif score == 2:
        print("⚠️ Medium risk: Be careful")
    else:
        print("✅ Low risk: Looks normal")

    print("\n(Note: This is a basic analysis, not 100% accurate)\n")


# Run tool
while True:
    analyze_account()
    again = input("Check another account? (y/n): ")
    if again.lower() != 'y':
        print("Exiting tool...")
        break


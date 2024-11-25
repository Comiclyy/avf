from pymongo import MongoClient

def main():
    # MongoDB connection
    client = MongoClient("mongodb+srv://Comicly:ilovecheese69@cluster0.uwcaalt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["users"]  # Replace with your database name if different

    # Ask user for input
    username = input("Enter your username: ")
    
    print("Choose permission level:")
    print("1. Basic")
    print("2. Admin")
    print("3. Intermediate (Int)")
    
    try:
        permission_choice = int(input("Enter the number corresponding to the permission level: "))
    except ValueError:
        print("Invalid input! Please enter a number (1, 2, or 3).")
        return

    # Map numbers to permission levels
    permission_map = {1: "basic", 2: "admin", 3: "int"}
    permission_level = permission_map.get(permission_choice)

    if not permission_level:
        print("Invalid choice! Please choose 1, 2, or 3.")
        return

    # Write to the database
    collection = db[permission_level]  # Collection based on permission level
    user_data = {"username": username, "permission": permission_level}
    collection.insert_one(user_data)

    print(f"User '{username}' added to the '{permission_level}' collection.")

if __name__ == "__main__":
    main()

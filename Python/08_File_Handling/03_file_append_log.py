




from datetime import datetime
def clear_log():
    with open('log.txt', 'w') as file:
        pass
def append_log():
    message = input("Enter your log message: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('log.txt', 'a') as file:
        file.write(f"[{timestamp}] {message}\n")

    print("Log entry added successfully!\n")

    # Read and print the full log file
    with open('log.txt', 'r') as file:
        print("Current log.txt contents:")
        print(file.read())

clear_log()
append_log()


def get_valid_duration():
    while True:
        try:
            minutes = int(input("Enter duration (minutes): "))
            if minutes > 0:
                return minutes
            else:
                print("Duration must be positive.")
        except ValueError:
            print("Enter a valid number.")

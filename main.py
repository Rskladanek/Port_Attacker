from menu import Menu


def main():
    try:
        m = Menu()
        m.run()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")       


if __name__ == "__main__":
    main()
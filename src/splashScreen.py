def display_instruct():
    """Display Game Instructions"""
    print(
    """MoonDocks: Fall of Illusions.
    The journey of Revolutionaries who don't know their true importance.
    Join them in bringing freedom across the known galaxy.
    """
    )
    input("To begin Enter 'begin journey' in the console.")

def askYesNo(message):
    """Ask a Yes No question"""
    response = None
    while response not in ("y", "n"):
        response = input(message).lower()
    return response

def askNumber (message, low, high):
    """ Ask For a Number within a range """
    response = None
    while response not in range(low, high):
        response = int(input(message))
    return response

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")

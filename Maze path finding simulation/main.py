import API
import sys

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def navigate_to_target():
    # Starting position (0, 0)
    x, y = 0, 0
    target_x, target_y = 8, 8  # Target position

    # Loop until target is reached
    while x != target_x or y != target_y:
        log(f"Current Position: {x}, {y}")

        # Check if there's a wall on the left
        if not API.wallLeft():
            API.turnLeft()

        # Check if there's a wall in front, and move accordingly
        while API.wallFront():
            API.turnRight()  # Turn right to avoid front wall
        
        API.moveForward()  # Move one step forward

        # Manually update the position based on movements
        if not API.wallLeft():
            if API.wallFront():
                if API.wallRight():
                    x, y = x - 1, y  # Move left (down)
                else:
                    y += 1  # Move up (toward target y-axis)
            else:
                x += 1  # Move right (toward target x-axis)
        
        # Log the position
        log(f"Moved to: {x}, {y}")

        # Check if we have reached the target
        if x == target_x and y == target_y:
            log(f"Target reached at {x}, {y}")
            break

def main():
    log("Running...")
    navigate_to_target()

if __name__ == "__main__":
    main()

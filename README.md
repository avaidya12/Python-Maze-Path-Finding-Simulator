Maze Pathfinding Simulator

Features:

    Wall detection (left, right, front)

    Basic pathfinding algorithm using wall-following techniques

    Logging of agent’s position during navigation

How It Works

    The program simulates an agent trying to find its way through a maze to a target position. It uses the following steps:

    Wall Detection: The agent checks for walls in front, left, and right.

    Movement Decision: If there's a wall on the left, the agent will turn left. It will move forward if there’s no wall in front.

    Navigation: The agent tries to move towards the target position (8,8) while updating its position based on the movements.

Main Files:

    main.py: Contains the main program logic for navigating the maze.

    API.py: Simulates the maze environment with functions for wall detection, movement, and direction changes.

Requirements

    Python 3.x

    No additional external libraries are required, but make sure the API.py file is available and correctly integrated.

License

    This project is open-source and available under the MIT License.


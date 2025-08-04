# Maze-Solving
A Maze Solving Robot is an autonomous robot designed to navigate through a maze and find a path from the start to the end.
The Left-Hand Rule algorithm is used, where the robot always keeps its left side close to a wall while moving.
This ensures it can explore the maze systematically until it reaches the endpoint.

⚙️ Components Required
Microcontroller → Arduino Uno / ESP32 / Raspberry Pi

IR Sensors → 3 (Left, Front, Right) for wall detection

Motor Driver → L298N or L293D

DC Motors → 2 geared motors

Chassis → Robot body with wheels

Battery → Li-ion or Li-Po pack

Wires & connectors

🧠 Algorithm (Left-Hand Rule)
Start at the entrance of the maze.

At every step:

If left side is open → turn left and move forward.

Else if front is open → move forward.

Else → turn right until a path is open.

Repeat until the robot reaches the exit.

🚗 Working
Initialization
The robot starts facing the first open path. The sensors continuously check for walls.

Sensor Input

Left Sensor → Detects if the left side is open.

Front Sensor → Detects if the path ahead is open.

Right Sensor → Detects if there’s a wall on the right.

Decision Making

If left is open → turn left, then move forward.

If left blocked but front open → move forward.

If both blocked → turn right until a way is found.

Movement
Motors are controlled based on sensor readings to execute turns and forward movement.

Reaching the End
When the end sensor detects the goal area (or a special marker), the robot stops.

📌 Advantages
Simple logic → Easy to program.

Low cost → Works with basic sensors.

Reliable → Works in most connected mazes.

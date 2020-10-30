# Game-Engine---Game-Demo
A basic Game Engine built in Python 3.7 using PyGame

## How It Works
This Game Engine was built using PyGame. 

I've added Sprite Support for Player, Combat, and Mob sprites. Main player sprite movement is based on vectors and keyboard input so it rotates on movement. Mob Sprites will spawn at the top and off of the screen by default, but that can be edited by changing a few variables. Combat Sprites, will spawn above the Player Sprite. Collision has the option of using AABB or Circular Bounding Box depending on sprite shape.  All sprites can be scaled up or down.

Background can be altered by changing the background image load file to a file in the same directory as the game_engine.py file. Background scales to window size by default. 

Window name is set to "2D Game" for simplicity. Window icon is set to your main player sprite icon by default. 

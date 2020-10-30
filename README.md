# Game-Engine---Game-Demo
A basic Game Engine built in Python 3.7 using PyGame.

## How It Works
This Game Engine was built using PyGame. I used the ADT developed in class minus gamepad and sound support.

I've added Sprite Support for Player, Combat, and Mob sprites. All sprite types are classes and more sprites can be created by adding them to the sprite groups. Main player sprite movement is based on vectors and keyboard input so it rotates on movement. Mob Sprites will spawn at the top and off of the screen by default, but that can be edited by changing a few variables. Combat Sprites will spawn directly above the Player Sprite. Collision has the option of using AABB or Circular Bounding Box depending on sprite shape. Player sprite is bounded by the window parameters but Enemy Sprites and Attack sprites are not. When enemy sprites go off screen without being hit they will respawn in a random location at the top. Attack sprites will be deleted when they go off screen. All sprite sizes can be scaled up or down to fit your needs. 

Background, as well as the sprites, can be altered by changing the image load lines to a file in the same directory as the game_engine.py file. Background scales to window size by default. 

Window name is set to "2D Game" by default. Window icon is set to your main player sprite icon by default. 

Frame Rate is set to 50 FPS by default.

Mouse movement is tracked but is not used for anything by default. 

### How to play
I built a game where a car is on a road shooting bombs falling from the sky. 

Use the arrow keys to move. Each repeated press of the UP arrow increases speed and each repeated press of the Down arrow decreases speed and reverses speed. Pressing space shoots a rocket out of the top of your car that will delete bombs on collision (This is AABB collision because the rocket is more square than round). When your car hits a bomb it will close the game (Circular Bounding Box collision). 


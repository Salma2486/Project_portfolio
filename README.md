Architecture:

1. User Interface (UI)
   - This is where the player interacts with the game. It includes the game board, score display, and controls.

2. Game Logic
   - This part handles the rules of the game. It decides what happens when the snake hits the wall or itself, eats the food, etc.

3. Data Management
   - This component keeps track of the game state, including the position of the snake, the location of the food, and the current score.

4. Rendering Engine
   - This part takes the game state from the Data Management component and displays it on the UI.

5. Control Handler
   - This component receives input from the player through the UI, and updates the game state in the Data Management component accordingly.

The data flows through the system as follows:

User Input -> Control Handler -> Data Management -> Game Logic -> Rendering 
Engine -> User Interface


![Alt Text](https://github.com/Salma2486/Project_portfolio/blob/main/Capture.PNG?raw=true.png)



Data Model:
Table Game: Stores information about each game session.
game_id: Unique identifier for each game session.
score: The score achieved in the game session.
date: The date when the game session was played.
Table Player: Stores information about each player.
player_id: Unique identifier for each player.
name: The name of the player.
Table Game_Player: A junction table that links the Game and Player tables, storing which player played which game.
game_id: Foreign key referencing Game.game_id.
player_id: Foreign key referencing Player.player_id.

![Alt Text](https://github.com/Salma2486/Project_portfolio/blob/main/Capture1.PNG?raw=true.png)


User Stories:
As a player, I want to be able to control the direction of the snake, so that I can play the game.
As a player, I want to see my current score during the game, so that I know how well I’m doing.
As a player, I want the game to become more difficult as my score increases, so that I am continuously challenged.
As a player, I want to be able to start a new game, so that I can play again after the game is over.
As a player, I want to see a game over screen when the snake hits the boundary or itself, so that I know when the game has ended and what my final score is.


Mockups:
![Alt Text](https://github.com/Salma2486/Project_portfolio/blob/main/w2enIILhS3yBEvwaD7VmEQ.jpg?raw=true.png)

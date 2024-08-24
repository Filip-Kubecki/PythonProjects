TODO:
- add sounds to game:
  - background music,
  - sounds on actions: game over, apple eaten etc
- add Board class: 
  - it will contain all objects that are actively on board in the moment,
- add obstacles to board
- add margin around game surface and add there UI elements: counter, timer, etc
- add textures to the game: snake, apple, obstacles:
  - add texture for Snake bending it's segment - apply in code
- improve pause and game over screens

Bugs:
- because change in HEAD direction can be applied multiple times before HEAD texture changes its rotation and place, user can collide head into SEGMENT. Self collision detection need fixing

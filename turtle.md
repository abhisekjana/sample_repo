Okay, let's build a simple "Collect the Food" game using Python's `turtle` module. We'll start extremely basic and add features and complexity in each version. This structure allows you to introduce concepts one at a time.

**Core Idea:** A player turtle controlled by the arrow keys tries to "eat" food items that appear randomly. The score increases with each food item eaten. Later versions add challenges like boundaries, obstacles, and timers.

---

**Version 1: Basic Player Movement**

*   **Concepts:** Importing libraries, creating the screen, creating a turtle object, basic movement functions, keyboard binding (`onkey`, `listen`), main loop (`while True`), screen updates (`tracer`, `update`).
*   **Goal:** Get a turtle on screen that you can move around with arrow keys.

```python
import turtle
import time # We might need time later, good practice to import early

# 1. Screen Setup
screen = turtle.Screen()
screen.title("Turtle Game - v1: Movement")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off screen updates for smoother animation

# 2. Player Turtle
player = turtle.Turtle()
player.speed(0)  # Animation speed (0 is fastest)
player.shape("turtle")
player.color("green")
player.penup()   # Don't draw lines when moving
player.goto(0, 0) # Start at the center

# 3. Movement Functions
def move_up():
    y = player.ycor()
    player.sety(y + 20)

def move_down():
    y = player.ycor()
    player.sety(y - 20)

def move_left():
    x = player.xcor()
    player.setx(x - 20)

def move_right():
    x = player.xcor()
    player.setx(x + 20)

# 4. Keyboard Bindings
screen.listen() # Start listening for keyboard events
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# 5. Main Game Loop
while True:
    screen.update() # Update the screen in the loop
    # In this version, the loop just keeps the window open and updates position
    time.sleep(0.01) # Small pause to prevent using 100% CPU

# screen.mainloop() # Alternative way to keep window open, often used at the very end
```

---

**Version 2: Adding Food and Score**

*   **Concepts:** Creating a second turtle (food), using `random` module for placement, collision detection (`distance()`), score variable, displaying text (`write()`).
*   **Goal:** Add a food item. When the player touches it, the score increases, and the food moves.

```python
import turtle
import time
import random # Import the random module

# 1. Screen Setup
screen = turtle.Screen()
screen.title("Turtle Game - v2: Food & Score")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.tracer(0)

# 2. Player Turtle
player = turtle.Turtle()
player.speed(0)
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, 0)

# 3. Food Turtle
food = turtle.Turtle()
food.speed(0)
food.shape("circle") # Food shape
food.color("red")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290)) # Random position

# 4. Score Variable
score = 0

# 5. Score Display Turtle
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle() # Don't show the turtle shape
score_display.goto(0, 260) # Position at the top center
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# --- Movement Functions (same as v1) ---
def move_up():
    y = player.ycor()
    player.sety(y + 20)
# ... (move_down, move_left, move_right remain the same) ...
def move_down():
    y = player.ycor()
    player.sety(y - 20)
def move_left():
    x = player.xcor()
    player.setx(x - 20)
def move_right():
    x = player.xcor()
    player.setx(x + 20)

# --- Keyboard Bindings (same as v1) ---
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# --- Main Game Loop ---
while True:
    screen.update()

    # Check for collision with food
    if player.distance(food) < 20: # Check if distance is less than 20 pixels
        # Move food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase score
        score += 1

        # Update score display
        score_display.clear() # Clear previous score
        score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(0.01)
```

---

**Version 3: Adding Boundaries**

*   **Concepts:** Screen coordinates, conditional logic (`if`) to check position, preventing movement beyond edges.
*   **Goal:** Stop the player from moving off the screen.

```python
import turtle
import time
import random

# --- Screen Setup (same as v2) ---
screen = turtle.Screen()
screen.title("Turtle Game - v3: Boundaries")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.tracer(0)

# Screen dimensions (useful for boundary checks)
WIDTH = 600
HEIGHT = 600

# --- Player Turtle (same as v2) ---
player = turtle.Turtle()
player.speed(0)
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, 0)

# --- Food Turtle (same as v2) ---
food = turtle.Turtle()
# ... (rest of food setup is the same)
food.speed(0)
food.shape("circle") # Food shape
food.color("red")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290)) # Random position


# --- Score Variable and Display (same as v2) ---
score = 0
score_display = turtle.Turtle()
# ... (rest of score setup is the same)
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle() # Don't show the turtle shape
score_display.goto(0, 260) # Position at the top center
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))


# --- Movement Functions (MODIFIED for boundaries) ---
def move_up():
    y = player.ycor()
    if y < HEIGHT/2 - 20: # Check if not too close to top edge
        player.sety(y + 20)

def move_down():
    y = player.ycor()
    if y > -HEIGHT/2 + 20: # Check bottom edge
        player.sety(y - 20)

def move_left():
    x = player.xcor()
    if x > -WIDTH/2 + 20: # Check left edge
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < WIDTH/2 - 20: # Check right edge
        player.setx(x + 20)

# --- Keyboard Bindings (same as v2) ---
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# --- Main Game Loop (same logic as v2) ---
while True:
    screen.update()

    if player.distance(food) < 20:
        x = random.randint(-int(WIDTH/2)+10, int(WIDTH/2)-10) # Use WIDTH/HEIGHT
        y = random.randint(-int(HEIGHT/2)+10, int(HEIGHT/2)-10)
        food.goto(x, y)
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(0.01)
```

---

**Version 4: Adding a Simple Obstacle**

*   **Concepts:** Creating another turtle (obstacle), collision detection with obstacle, game state (game over), displaying game over message.
*   **Goal:** Add a static obstacle. If the player touches it, the game ends.

```python
import turtle
import time
import random

# --- Screen Setup (same as v3) ---
screen = turtle.Screen()
screen.title("Turtle Game - v4: Obstacle")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.tracer(0)
WIDTH, HEIGHT = 600, 600

# --- Player Turtle (same as v3) ---
player = turtle.Turtle()
player.speed(0); player.shape("turtle"); player.color("green"); player.penup(); player.goto(0, -200) # Start lower

# --- Food Turtle (same as v3) ---
food = turtle.Turtle()
food.speed(0); food.shape("circle"); food.color("red"); food.penup()
food.goto(random.randint(-int(WIDTH/2)+10, int(WIDTH/2)-10), random.randint(0, int(HEIGHT/2)-10)) # Food starts higher

# --- Obstacle Turtle ---
obstacle = turtle.Turtle()
obstacle.speed(0)
obstacle.shape("square")
obstacle.color("gray")
obstacle.shapesize(stretch_wid=1, stretch_len=10) # Make it wider
obstacle.penup()
obstacle.goto(0, 100) # Place it horizontally

# --- Score & Display (same as v3) ---
score = 0
score_display = turtle.Turtle()
score_display.speed(0); score_display.color("black"); score_display.penup()
score_display.hideturtle(); score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# --- Game State ---
game_over = False

# --- Movement Functions (Modified to check game_over) ---
def move_up():
    if not game_over:
        y = player.ycor()
        if y < HEIGHT/2 - 20: player.sety(y + 20)
# ... (move_down, move_left, move_right similarly modified) ...
def move_down():
    if not game_over:
        y = player.ycor()
        if y > -HEIGHT/2 + 20: player.sety(y - 20)
def move_left():
    if not game_over:
        x = player.xcor()
        if x > -WIDTH/2 + 20: player.setx(x - 20)
def move_right():
    if not game_over:
        x = player.xcor()
        if x < WIDTH/2 - 20: player.setx(x + 20)

# --- Keyboard Bindings (same) ---
screen.listen()
screen.onkey(move_up, "Up"); screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left"); screen.onkey(move_right, "Right")

# --- Game Over Function ---
def display_game_over():
    score_display.goto(0, 0) # Move score display to center
    score_display.write(f"GAME OVER\nScore: {score}", align="center", font=("Courier", 30, "bold"))

# --- Main Game Loop ---
while True:
    screen.update()

    if not game_over: # Only run game logic if not over
        # Check for food collision
        if player.distance(food) < 20:
            x = random.randint(-int(WIDTH/2)+10, int(WIDTH/2)-10)
            y = random.randint(0, int(HEIGHT/2)-10) # Keep food above obstacle
            food.goto(x, y)
            score += 1
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

        # Check for obstacle collision
        # Need more careful check for rectangular collision if shapesize changed
        # Simple distance check to the center of the obstacle for now:
        if player.distance(obstacle) < 20: # Basic check
            game_over = True
            display_game_over()

    time.sleep(0.01)

```

---

**Version 5: Moving Obstacle**

*   **Concepts:** Basic animation loop for non-player characters, changing direction at boundaries.
*   **Goal:** Make the obstacle move back and forth, adding more dynamic challenge.

```python
import turtle
import time
import random

# --- Screen Setup (same) ---
screen = turtle.Screen(); screen.title("Turtle Game - v5: Moving Obstacle")
screen.bgcolor("lightblue"); screen.setup(width=600, height=600); screen.tracer(0)
WIDTH, HEIGHT = 600, 600

# --- Player Turtle (same) ---
player = turtle.Turtle(); player.speed(0); player.shape("turtle"); player.color("green")
player.penup(); player.goto(0, -200)

# --- Food Turtle (same) ---
food = turtle.Turtle(); food.speed(0); food.shape("circle"); food.color("red"); food.penup()
food.goto(random.randint(-int(WIDTH/2)+10, int(WIDTH/2)-10), random.randint(0, int(HEIGHT/2)-10))

# --- Obstacle Turtle (MODIFIED) ---
obstacle = turtle.Turtle()
obstacle.speed(0)
obstacle.shape("square")
obstacle.color("gray")
# obstacle.shapesize(stretch_wid=1, stretch_len=3) # Make it smaller maybe
obstacle.penup()
obstacle.goto(0, 100)
obstacle.dx = 2  # Add movement speed property (pixels per loop)

# --- Score & Display (same) ---
score = 0
score_display = turtle.Turtle()
score_display.speed(0); score_display.color("black"); score_display.penup()
score_display.hideturtle(); score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# --- Game State ---
game_over = False

# --- Movement Functions (same as v4) ---
def move_up(): # Check game_over inside
    if not game_over:
        y = player.ycor()
        if y < HEIGHT/2 - 20: player.sety(y + 20)
# ... (move_down, move_left, move_right same as v4) ...
def move_down():
    if not game_over:
        y = player.ycor()
        if y > -HEIGHT/2 + 20: player.sety(y - 20)
def move_left():
    if not game_over:
        x = player.xcor()
        if x > -WIDTH/2 + 20: player.setx(x - 20)
def move_right():
    if not game_over:
        x = player.xcor()
        if x < WIDTH/2 - 20: player.setx(x + 20)

# --- Keyboard Bindings (same) ---
screen.listen()
screen.onkey(move_up, "Up"); screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left"); screen.onkey(move_right, "Right")

# --- Game Over Function (same) ---
def display_game_over():
    score_display.goto(0, 0)
    score_display.write(f"GAME OVER\nScore: {score}", align="center", font=("Courier", 30, "bold"))

# --- Main Game Loop ---
while True:
    screen.update()

    if not game_over:
        # Move the obstacle
        obstacle.setx(obstacle.xcor() + obstacle.dx)

        # Bounce obstacle off walls
        # Check needs to account for shape size if not square
        if obstacle.xcor() > WIDTH/2 - 10 or obstacle.xcor() < -WIDTH/2 + 10:
            obstacle.dx *= -1 # Reverse direction

        # Check for food collision
        if player.distance(food) < 20:
            x = random.randint(-int(WIDTH/2)+10, int(WIDTH/2)-10)
            y = random.randint(0, int(HEIGHT/2)-10)
            food.goto(x, y)
            score += 1
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

        # Check for obstacle collision
        if player.distance(obstacle) < 20: # Still basic distance check
             game_over = True
             display_game_over()

    time.sleep(0.01) # Adjust for game speed/difficulty
```

---

**Version 6: Countdown Timer**

*   **Concepts:** Using `screen.ontimer()` for timed events, managing time, adding another game over condition.
*   **Goal:** Add a time limit. The game ends when time runs out or the player hits the obstacle.

```python
import turtle
import time
import random

# --- Screen Setup (same) ---
screen = turtle.Screen(); screen.title("Turtle Game - v6: Timer")
screen.bgcolor("lightblue"); screen.setup(width=600, height=600); screen.tracer(0)
WIDTH, HEIGHT = 600, 600

# --- Player Turtle (same) ---
player = turtle.Turtle(); player.speed(0); player.shape("turtle"); player.color("green")
player.penup(); player.goto(0, -200)

# --- Food Turtle (same) ---
food = turtle.Turtle(); food.speed(0); food.shape("circle"); food.color("red"); food.penup()
food.goto(random.randint(-int(WIDTH/2)+10, int(WIDTH/2)-10), random.randint(0, int(HEIGHT/2)-10))

# --- Obstacle Turtle (same as v5) ---
obstacle = turtle.Turtle(); obstacle.speed(0); obstacle.shape("square"); obstacle.color("gray")
obstacle.penup(); obstacle.goto(0, 100); obstacle.dx = 2

# --- Score & Display (same) ---
score = 0
score_display = turtle.Turtle()
score_display.speed(0); score_display.color("black"); score_display.penup()
score_display.hideturtle(); score_display.goto(0, 260)
score_display.write(f"Score: {score}  Time: --", align="center", font=("Courier", 24, "normal")) # Add Time placeholder

# --- Game State ---
game_over = False
time_limit = 30 # Seconds
time_left = time_limit

# --- Movement Functions (same as v5) ---
def move_up():
    if not game_over:
        y = player.ycor();
        if y < HEIGHT/2 - 20: player.sety(y + 20)
def move_down():
    if not game_over:
        y = player.ycor();
        if y > -HEIGHT/2 + 20: player.sety(y - 20)
def move_left():
    if not game_over:
        x = player.xcor();
        if x > -WIDTH/2 + 20: player.setx(x - 20)
def move_right():
    if not game_over:
        x = player.xcor();
        if x < WIDTH/2 - 20: player.setx(x + 20)

# --- Keyboard Bindings (same) ---
screen.listen()
screen.onkey(move_up, "Up"); screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left"); screen.onkey(move_right, "Right")

# --- Update Score/Time Display Function ---
def update_display():
    score_display.clear()
    score_display.write(f"Score: {score}  Time: {time_left}", align="center", font=("Courier", 24, "normal"))

# --- Game Over Function ---
def display_game_over(message="GAME OVER"):
    global game_over
    game_over = True
    score_display.goto(0, 0)
    score_display.clear()
    score_display.write(f"{message}\nScore: {score}", align="center", font=("Courier", 30, "bold"))

# --- Countdown Function ---
def countdown():
    global time_left
    if not game_over:
        time_left -= 1
        update_display()
        if time_left <= 0:
            display_game_over("TIME'S UP!")
        else:
            screen.ontimer(countdown, 1000) # Call myself again after 1000ms (1 second)

# --- Main Game Loop ---
update_display() # Initial display
countdown() # Start the timer

while True:
    screen.update()

    if not game_over:
        # Move the obstacle
        obstacle.setx(obstacle.xcor() + obstacle.dx)
        if obstacle.xcor() > WIDTH/2 - 10 or obstacle.xcor() < -WIDTH/2 + 10:
            obstacle.dx *= -1

        # Check for food collision
        if player.distance(food) < 20:
            x = random.randint(-int(WIDTH/2)+10, int(WIDTH/2)-10)
            y = random.randint(0, int(HEIGHT/2)-10)
            food.goto(x, y)
            score += 1
            update_display() # Update score (and time)

        # Check for obstacle collision
        if player.distance(obstacle) < 20:
             display_game_over("HIT OBSTACLE!")

    # We rely on the ontimer to stop the game now, main loop just updates screen
    time.sleep(0.01) # Keep this for smooth animation/movement

```

This progression introduces concepts step-by-step, starting with basic graphics and movement, then adding game mechanics like scoring, collision detection, boundaries, obstacles, animation, and timers. Each version builds directly on the previous one. Remember to explain the *new* concepts introduced in each version as you work through them together. Have fun!

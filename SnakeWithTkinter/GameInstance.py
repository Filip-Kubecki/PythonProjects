import tkinter as tk
import time
import random
import Snake
import enum

from Snake import *
from tkinter import *

class Board():
    # Constructor
    def __init__(self):
        # Defining variables
        self.INITIAL = True
        self.BOARD_WIDTH = 400
        self.BOARD_HEIGHT = 300
        self.TIME = time.time()
        self.TICK_DURATION = 600
        self.PAUSE = True

        self.PLAYER_X = (self.BOARD_WIDTH/2)-((self.BOARD_WIDTH/2)%20)
        self.PLAYER_Y = (self.BOARD_WIDTH/2)-((self.BOARD_WIDTH/2)%20)
        
        self.DIRECTION = Direction.UP

        self.MOVEMENT_DISTANCE = 20
        self.TOP_PANEL_HEIGHT = 60

        # --- Body of constructor -----------------------------------------------------------------

        self.points = 0

        self.root = tk.Tk()
        self.root.title("Snake")
        self.root.geometry("{0}x{1}".format(self.BOARD_WIDTH, self.BOARD_HEIGHT))

        self.apple = tk.Label(self.root)

        self.topPanel = tk.Frame(self.root,width=self.BOARD_WIDTH, height=self.TOP_PANEL_HEIGHT)
        self.topPanel.pack()

        self.scoreLabel = tk.Label(self.topPanel,text = "Score:", font=("Arial", 16, "bold"))
        self.scoreLabel.grid(row=0,column=0)

        self.scoreLabel = tk.Label(self.topPanel,text = self.points, font=("Arial", 16, "bold"))
        self.scoreLabel.grid(row=0,column=1)

        spacer = tk.Label(self.topPanel, width=20,height=1)
        spacer.grid(row=0,column=2)

        self.timer = tk.Label(self.topPanel, font=("Arial", 16, "bold"))
        self.timer.grid(row=0,column=3)


        self.board = tk.Frame(self.root,width=self.BOARD_WIDTH,height=self.BOARD_HEIGHT, background="#222222")
        self.board.pack()

        self.snake = Snake(self.board)
        self.snake.body[0].segment.place(x=self.PLAYER_X,y=self.PLAYER_Y)

        self.root.bind("<KeyPress>",func=self.keyPressedEvent)
        
        self.createApple()

        self.inGameClockTick()
        self.root.mainloop()

    # --- Class Methods Scope -------------------------------------------

    def inGameClockTick(self):
        now = time.strftime("%H:%M:%S")

        self.refreshTimer()

        if self.PAUSE:
            self.checkForSelfColision()

            if self.INITIAL:
                self.snake.body[0].segment.place(x=self.PLAYER_X,y=self.PLAYER_Y)

            self.move()

            for i in range(len(self.snake.body)-1, 0, -1):
                self.snake.body[i].direction = self.snake.body[i-1].direction

            if (time.time()-self.TIME)*1000 > 200:
                self.checkIfAppleBitten()

        self.root.after(self.TICK_DURATION, self.inGameClockTick)

    def addSegment(self):
        prevTail = self.snake.body[-1].segment
        prevTailDirection = self.snake.body[-1].direction

        prevTailX = prevTail.winfo_x()
        prevTailY = prevTail.winfo_y()

        newTail = Snake.Segment(self.board)


        # match prevTailDirection:
        #     case Direction.UP:
        #         newTail.segment.place(x=prevTailX,y=prevTailY+MOVEMENT_DISTANCE)
        #     case Direction.DOWN:
        #         newTail.segment.place(x=prevTailX,y=prevTailY-MOVEMENT_DISTANCE)
        #     case Direction.RIGHT:
        #         newTail.segment.place(x=prevTailX-MOVEMENT_DISTANCE,y=prevTailY)
        #     case Direction.LEFT:
        #         newTail.segment.place(x=prevTailX+MOVEMENT_DISTANCE,y=prevTailY)
        #     case _:
        #         newTail.segment.place(x=250,y=250)

        newTail.segment.place(x=prevTailX,y=prevTailY)
        newTail.direction = prevTailDirection

        self.snake.body.append(newTail)

    def move(self):
        self.INITIAL = False

        for segment in self.snake.body:
            segmentDirection = segment.direction
            segmentX = segment.segment.winfo_x()
            segmentY = segment.segment.winfo_y()

            match segmentDirection:
                case Direction.UP:
                    if segmentY <= 0:
                        segment.segment.place(x=segmentX,y=self.BOARD_HEIGHT-20)
                    else:
                        segment.segment.place(x=segmentX,y=segmentY-20)
                case Direction.DOWN:
                    if segmentY >= self.BOARD_HEIGHT:
                        segment.segment.place(x=segmentX,y=0)
                    else:
                        segment.segment.place(x=segmentX,y=segmentY+20)
                case Direction.RIGHT:
                    if segmentX >= self.BOARD_WIDTH:
                        segment.segment.place(x=0,y=segmentY)
                    else:
                        segment.segment.place(x=segmentX+20,y=segmentY)
                case Direction.LEFT:
                    if segmentX <= 0:
                        segment.segment.place(x=self.BOARD_WIDTH-20,y=segmentY)
                    else:
                        segment.segment.place(x=segmentX-20,y=segmentY)
    
    def keyPressedEvent(self, event):
        if event.keysym == "Up":
            self.DIRECTION = Direction.UP
        elif event.keysym == "Down":
            self.DIRECTION = Direction.DOWN
        elif event.keysym == "Right":
            self.DIRECTION = Direction.RIGHT
        elif event.keysym == "Left":
            self.DIRECTION = Direction.LEFT
        elif event.keysym == "p":
            self.createApple()
        elif event.keysym == "Escape":
            self.PAUSE = not self.PAUSE 
            self.pauseGame()

        self.snake.body[0].direction = self.DIRECTION

    def createApple(self):
        randomX = random.randrange(0, self.BOARD_WIDTH+1-20, 20)
        randomY = random.randrange(0, self.BOARD_HEIGHT+1-self.TOP_PANEL_HEIGHT, 20)

        apple = tk.Label(self.board,width=2,height=1,background="red")
        apple.place(x=randomX,y=randomY)
        self.apple = apple

    def checkIfAppleBitten(self):
        head = self.snake.body[0].segment
        headX = head.winfo_x()
        headY = head.winfo_y()

        appleX = self.apple.winfo_x()
        appleY = self.apple.winfo_y()
        
        if headX < appleX+20 and headX >= appleX:
            if headY >= appleY and headY < appleY+20:
                    self.updateScore()
                    self.apple.destroy()
                    self.addSegment()
                    self.createApple()

    def refreshTimer(self):
        seconds = int((time.time()-self.TIME)%60)
        min = int((time.time()-self.TIME)/60)

        if len(str(seconds)) <= 1:
            seconds = "0" + str(seconds)

        self.timer.config(text = "{0}:{1}".format(min, seconds))

    def updateScore(self):
        self.points += 1
        self.scoreLabel.config(text = self.points)

    def pauseGame(self):
        if not self.PAUSE:
            self.pauseLabel = tk.Label(self.root, text = "Pause",font=("Arial", 16, "bold"))
            self.pauseLabel.place(x=self.BOARD_WIDTH/2, y=self.BOARD_HEIGHT/2)
        else:
            self.pauseLabel.destroy()

    def terminateProgram(self):  
        self.root.destroy()

    def checkForSelfColision(self):
        head = self.snake.body[0].segment
        headX = head.winfo_x()
        headY = head.winfo_y()

        for segment in self.snake.body[1:]:
            segmentX = segment.segment.winfo_x()
            segmentY = segment.segment.winfo_y()

            if headX < segmentX+20 and headX >= segmentX:
                if headY >= segmentY and headY < segmentY+20:
                    self.terminateProgram()

class Direction(enum.Enum):
        NONE = 0
        RIGHT = 1
        LEFT = 2
        UP = 3
        DOWN = 4
        
# Run game instance
Board()
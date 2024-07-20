import tkinter as tk
from enum import Enum

MOVEMENT_DISTANCE = 20

class Snake():
    def __init__(self, root):
        self.body = list()
        self.body.append(Snake.Segment(root))

        self.body[0].segment.config()
        # self.body[0].segment.config(text = ":3", font=("Arial", 8, "bold"))

        # self.addSegment(root)

    def setHeadDirection(self, direction):
            self.body[0].direction = direction


    class Segment():
        def __init__(self, root):
            self.direction = Direction.NONE
            self.segment = tk.Label(root,width=2,height=1,background="green")

        # def move(self):
        #     segmentX = self.segment.winfo_x()
        #     segmentY = self.segment.winfo_y()
            
        #     match self.direction:
        #         case Direction.UP:
        #             self.segment.place(x=segmentX,y=segmentY-MOVEMENT_DISTANCE)
        #         case Direction.DOWN:
        #             self.segment.place(x=segmentX,y=segmentY+MOVEMENT_DISTANCE)
        #         case Direction.RIGHT:
        #             self.segment.place(x=segmentX+MOVEMENT_DISTANCE,y=segmentY)
        #         case Direction.LEFT:
        #             self.segment.place(x=segmentX-MOVEMENT_DISTANCE,y=segmentY)
            
class Direction(Enum):
        NONE = 0
        RIGHT = 1
        LEFT = 2
        UP = 3
        DOWN = 4

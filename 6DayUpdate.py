from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.vector import Vector #for direction of velocity
from kivy.clock import Clock
from random import randint


class PongBall(Widget):
    velocity_x = NumericProperty(0)#py automatically knows velocity is an integer
    velocity_y = NumericProperty(0)#yet we import NumericProperty to make sure that every platform unerstands its an integer
    velocity = ReferenceListProperty(velocity_x, velocity_y)#When you gotta combine both xaxis and yaxis velocity

    

    #latest position = current velocity + current position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        
class PongPaddle(Widget):
    pass


class PongGame(Widget):
    ball = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))#we need x to move @4 pixels/sec but y can be random

        
        
    #UpdateMethod : moving the ball by calling the move() and other stuff
    def update(self,dt): #called 60 times in one second
                         #CODE FOR BOUNCING IS PUT INSIDE UpdateMethod cuz UpdateMetod is called the most in the program
        
                self.ball.move()
                #bouncing off @top and bottom condition
                if (self.ball.y<0) or (self.ball.y>self.height-50): #-50 cuz half of the ball dissappears @top
                   self.ball.velocity_y *= -1
                   
                #bouncing off @left and right condition
                if (self.ball.x<0) or (self.ball.x>self.width-50):  #-50 cuz half of the ball dissappears @right
                   self.ball.velocity_x *= -1



class PongApp(App):
    def build(self):
        game = PongGame() #game is and object of PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/60.0) #Clock class's method calls the update method of PongGame()
                                                      #1.0/60.0 means 60 frames per second

        
        return game


PongApp().run()

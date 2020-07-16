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
        
        


class PongGame(Widget):
    ball = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))#we need x to move @4 pixels/sec but y can be random
        
    #UpdateMethod : moving the ball by calling the move() and other stuff
    def update(self,dt): #called 60 times in one second
               self.ball.move()



class PongApp(App):
    def build(self):
        game = PongGame() #game is and object of PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/60.0) #Clock class's method calls the update method of PongGame()
                                                      #1.0/60.0 means 60 frames per second

        
        return game


PongApp().run()

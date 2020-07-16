from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ReferenceListProperty 
from kivy.vector import Vector #for direction of velocity
from kivy.clock import Clock

class PongBall(Widget):
    velocity_x = NumericProperty(0)#py automatically knows velocity is an integer
    velocity_y = NumericProperty(0)#yet we import NumericProperty to make sure that every platform unerstands its an integer
    velocity = ReferenceListProperty(velocity_x, velocity_y)#When you gotta combine both xaxis and yaxis velocity

    

    #latest position = current velocity + current position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        
        


class PongGame(Widget):
    #UpdateFunc : moving the ball by calling the move() and other stuff
    def update(self,dt):
               pass



class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update,1.0/60.0)
        return PongGame()


PongApp().run()

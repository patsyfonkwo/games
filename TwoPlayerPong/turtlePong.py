# Two Player Pong Game
# Player A uses "WASD" and Player B uses arrow keys
# Sound effects only compatible with windows OS users
# By Patsy Fonkwo


import turtle
import winsound

class Game:
    def __init__(self):
        self.win = turtle.Screen() #screen object
        self.win.title('Pong by Patsy Fonkwo') #giving screen object title attribute
        self.win.bgcolor('black') #background color for window/screen
        self.win.setup(width=800, height=600) #sets up window or screen
        self.win.tracer(0)
        self.a,self.b = 0,0
        
        #pen
        self.title = Words('Player A: '+ str(self.a)+ '   Player B: ' + str(self.b))
    
    def _keyboard_binding(self, paddle1, paddle2):
        self.win.listen() #tells window to listen for keyboard binding
        self.win.onkeypress(paddle1.up, 'w')
        self.win.onkeypress(paddle1.down, 's')
        self.win.onkeypress(paddle2.up, 'Up')
        self.win.onkeypress(paddle2.down, 'Down')
        
    def run(self):
        #main game loop
        left =  Paddle('left')
        right = Paddle('right')
        ball = Ball()
        self._keyboard_binding(left, right)
        
        while True: 
            self.win.update()
            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)
            self._collisions(ball, left)
            self._collisions(ball, right)
            
    def _collisions(self, ball, paddle):
            #boarder checking
        if ball.ycor() > 290: #if ball at limit
            ball.sety(290) #keep at limit for one frame
            ball.dy *= -1 #reverse direction
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        if ball.ycor() < -290: 
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            
        #when ball hits the left/right limits, it should be game over for someone
        if ball.xcor() > 390: #if ball at limit
            ball.goto(0,0) #reset the starting position
            ball.dx *= -1 #reverse direction
            self.a +=1
            
        if -390 > ball.xcor(): #if ball at limit
            ball.goto(0,0) #reset the starting position
            ball.dx *= -1 #reverse direction
            self.b+=1
        
        #update viewed score
        self.title.clear()
        self.title = Words('Player A: '+ str(self.a)+ '   Player B: ' + str(self.b))
        
        #now check if ball hit the paddle
        if paddle.getposition() == 'right':
            if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle.ycor()+40 and ball.ycor() > paddle.ycor()-40):
                ball.setx(340)
                ball.dx *= -1
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
                
        #just flip signs and operands
        elif paddle.getposition() == 'left':
            if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() > paddle.ycor()-40 and ball.ycor() < paddle.ycor()+40):
                ball.setx(-340)
                ball.dx *= -1
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        

        
class Ball(turtle.Turtle): #inheriting traits from Turtle Object
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape('square') #shape of the turtle
        self.color('red') #color of the turtle
        self.penup() #so that pen does not write on the screen
        self.goto(0, 0) #starting position
        self.dx, self.dy = .2,.2 #its movement
        
        
class Paddle(Ball): #inheriting traits from Turtle Object
    def __init__(self, position):
        Ball.__init__(self)
        #inherits speed
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        #inherits penup
        self.goto(-350 if position=='left' else 350, 0) #starting position
        self.position = position
        self.score = 0
        
    def up(self):
        x = self.ycor() #refers to the y coordinate
        x += 20 
        self.sety(self.ycor()+20)
    
    def down(self):
        x = self.ycor() #refers to the y coordinate from ball from turtle.Turtle object
        x -= 20 
        self.sety(x)
        
    def getposition(self):
        return self.position
    
    def __add__(self, right_val):
        return self.score + right_val
    
class Words(turtle.Turtle):
    def __init__(self, words, align='center', font =('Courier', 20, 'normal')):
        turtle.Turtle.__init__(self)
        self.pendown()
        self.speed(0)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(words, align=align, font=font)
            
        

if __name__ == '__main__':
    Game().run()




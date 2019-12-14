# Assignment 9
# Ping Pong Game
# Anthony Swift

#Import random, livewires, games and color modules

import random
from livewires import games, color

#Set the screen height, width and frames per second

games.init(screen_width=640, screen_height=440, fps=50)


class Paddle(games.Sprite):
	# A paddle controlled by the player.
 image=games.load_image("Paddle.png")
 def __init__(self):
		# Initialise the paddle object and create text object for the score.
  super(Paddle, self).__init__(	image=Paddle.image,
								x=games.mouse.x,
								bottom=games.screen.height)
  self.score=games.Text(	value=0, size=25, color=color.black,
								top=5, right=games.screen.width - 10)
  games.screen.add(self.score)
 
	
 def update(self):
		# Move to mouse x position.
  self.x = games.mouse.x
  self.check_catch()

  if self.left < 0:
   self.left = 0
  if self.right > games.screen.width:
   self.right = games.screen.width
  
			
 def check_catch(self):
		#Check if ball is caught by the paddle.
		#Add 10 to the score if ball is caught by the paddle.
  for Ball in self.overlapping_sprites:
   self.score.value += 10
   self.score.right = games.screen.width - 10
   Ball.handle_caught()


class Ball(games.Sprite):
    # A bouncing ball

 image=games.load_image("PingPongBall.png")
	

	
 def update(self):
		
  # Reverse a velocity component if edge of screen reached.
		
  if self.right > games.screen.width or self.left < 0:
   self.dx = -self.dx
  if self.bottom > games.screen.height or self.top < 0:
   self.dy = -self.dy
   
  #If the ball reaches the bottom of the screen
  #Removes the ball and calls function to end the game
  
  if self.bottom > games.screen.height:
   self.end_game()
   self.destroy()
	
 def handle_caught(self):
 
 # When the ball is caught by the paddle, reverses the y co-ordinates/bounces off the paddle.
 
  self.dy = -self.dy
	
 def end_game(self):
		# End the game.
  end_message=games.Message(	value="Game Over!", size=90,
								color=color.yellow,
								x=games.screen.width/2,
								y=games.screen.height/2,
								lifetime= 5 * games.screen.fps,
								after_death = games.screen.quit)
  games.screen.add(end_message)
  
def main():
	# Play the game.
	pingpongtable = games.load_image("PingPongTable.JPG", transparent = False)
	games.screen.background = pingpongtable
	ball_image = games.load_image("PingPongBall.png")
	the_ball = Ball(image=ball_image, dx=3, dy=3, x=50, y=50)
	games.screen.add(the_ball)
	the_paddle = Paddle()
	games.screen.add(the_paddle)
	games.mouse.is_visible = False
	games.screen.event_grab = True
	games.screen.mainloop()
# Start the program.
main()
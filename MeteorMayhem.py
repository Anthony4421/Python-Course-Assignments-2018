# Assignment 10
# Meteor Mayhem 
# Anthony Swift

import random, math
from livewires import games, color

#Set the screen height, width and fps

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Wrapper(games.Sprite):
	# A sprite that wraps around the screen.
 def update(self):
		# Wrap sprite around screen. 
  if self.top > games.screen.height:
   self.bottom = 0
  if self.bottom < 0:
   self.top = games.screen.height
  if self.left > games.screen.width:
   self.right = 0
  if self.right < 0:
   self.left = games.screen.width

 def die(self):
		# Destroy self.
  self.destroy()

class Collider(Wrapper):
	# A Wrapper that can collide with another object.
 def update(self):
		# Check for overlapping sprites.
  super(Collider, self).update()
  if self.overlapping_sprites:
   for sprite in self.overlapping_sprites:
    sprite.die()
   self.die()               

 def die(self):
		# Destroy self and leave explosion behind.
  new_explosion = Explosion(x = self.x, y = self.y)
  games.screen.add(new_explosion)
  self.destroy()
		
class Comet(Wrapper):
    # An comet which travels across the screen.
 image = games.load_image("Comet.png")
 SPEED = 1
 POINTS = 50
 total = 0
    
 def __init__(self, game, x, y):
		# Initialize the comet sprite.
		# Set to travel diagonally right across screen
		# Rotated comet image 180 degrees to allow the tail to follow the comet
  Comet.total +=1
  super(Comet, self).__init__(
	  image = Comet.image,
	  x = x, y = y,
	  dx = 1 * Comet.SPEED, 
	  dy = 1 * Comet.SPEED)
  self.game = game
  self.angle = 180
  
 def die(self):
		# Destroy comet.
		
  Comet.total -= 1

  self.game.score.value += int(Comet.POINTS)
  self.game.score.right = games.screen.width - 10


				
		# If all comets are gone, advance to the next level.  
  		
  if Asteroid.total == 0 and Comet.total == 0:
   self.game.advance()
  super(Comet, self).die()
  
  
class Asteroid(Wrapper):
	# An asteroid which floats across the screen.
	SMALL = 1
	MEDIUM = 2
	LARGE = 3
	images = {	SMALL  : games.load_image("asteroid_small.bmp"),
				MEDIUM : games.load_image("asteroid_med.bmp"),
				LARGE  : games.load_image("asteroid_big.bmp") }

	SPEED = 2
	SPAWN = 2   
	POINTS = 30
	total =  0

	def __init__(self, game, x, y, size):
		# Initialize the asteroid sprite.
		Asteroid.total += 1

		super(Asteroid, self).__init__(
			image = Asteroid.images[size],
			x = x, y = y,
			dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size, 
			dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)

		self.game = game       
		self.size = size

	def die(self):
		# Destroy asteroid.
		# If the asteroid isn't small, replace with two smaller asteroids.
		Asteroid.total -= 1

		self.game.score.value += int(Asteroid.POINTS / self.size)
		self.game.score.right = games.screen.width - 10

		if self.size != Asteroid.SMALL:
			for i in range(Asteroid.SPAWN):
				new_asteroid = Asteroid(game = self.game,
										x = self.x,
										y = self.y,
										size = self.size - 1)
				games.screen.add(new_asteroid)
			
		# If all asteroids are gone, advance to the next level.   
		if Asteroid.total == 0 and Comet.total == 0:
			self.game.advance()
        
		super(Asteroid, self).die()

class Spaceship(Collider):
	# The player's spaceship.
	image = games.load_image("SpaceShip.png")
	sound = games.load_sound("thrust.wav")
	ROTATION_STEP = 3
	VELOCITY_STEP = .03
	VELOCITY_MAX = 3
	MISSILE_DELAY = 25

	def __init__(self, game, x, y):
	# Initialise the spaceship sprite.
		super(Spaceship, self).__init__(image = Spaceship.image, x = x, y = y)
		self.game = game
		self.missile_wait = 0
	
	def update(self):
		# Rotate spaceship using left and right arrows.
		super(Spaceship, self).update()

		if games.keyboard.is_pressed(games.K_LEFT):
			self.angle -= Spaceship.ROTATION_STEP        
		if games.keyboard.is_pressed(games.K_RIGHT):
			self.angle += Spaceship.ROTATION_STEP

		# Apply thrust based on the up-arrow key.
		if games.keyboard.is_pressed(games.K_UP):
			Spaceship.sound.play()
          
			# Change the velocity based on the spaceship's angle.
			angle = self.angle * math.pi / 180  # Convert to radians.
			self.dx += Spaceship.VELOCITY_STEP * math.sin(angle)
			self.dy += Spaceship.VELOCITY_STEP * -math.cos(angle)

			# Cap velocity in each direction.
			self.dx = min(max(self.dx, -Spaceship.VELOCITY_MAX), Spaceship.VELOCITY_MAX)
			self.dy = min(max(self.dy, -Spaceship.VELOCITY_MAX), Spaceship.VELOCITY_MAX)

		# If waiting until the ship can fire next, decrease wait.
		if self.missile_wait > 0:
			self.missile_wait -= 1

        # Fire a missile if spacebar pressed and missile wait is over.
		if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
			new_missile = Missile(self.x, self.y, self.angle)
			games.screen.add(new_missile)
			self.missile_wait = Spaceship.MISSILE_DELAY


	def die(self):
		# Destroy the spaceship and end the game.
		self.game.end()
		super(Spaceship, self).die()	

class Missile(Collider):
	# A missile launched by the player's ship.
	image = games.load_image("missile.bmp")
	sound = games.load_sound("missile.wav")
	BUFFER = 60
	VELOCITY_FACTOR = 7
	LIFETIME = 40

	def __init__(self, ship_x, ship_y, ship_angle):
		# Initialise the missile sprite.
		Missile.sound.play()

		# Convert to radians.
		angle = ship_angle * math.pi / 180  

		# calculate missile's starting position 
		buffer_x = Missile.BUFFER * math.sin(angle)
		buffer_y = Missile.BUFFER * -math.cos(angle)
		x = ship_x + buffer_x
		y = ship_y + buffer_y

		# Calculate the missile's velocity components.
		dx = Missile.VELOCITY_FACTOR * math.sin(angle)
		dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

		# Create the missile.
		super(Missile, self).__init__(	image = Missile.image,
										x = x, y = y,
										dx = dx, dy = dy )
		self.lifetime = Missile.LIFETIME

	def update(self):
		# Move the missile.
		super(Missile, self).update()

		# If lifetime is up, destroy the missile.
		self.lifetime -= 1
		if self.lifetime == 0:
			self.destroy()

class Explosion(games.Animation):
	# Explosion animation.
	sound = games.load_sound("explosion.wav")
	images = [	"explosion1.bmp",
				"explosion2.bmp",
				"explosion3.bmp",
				"explosion4.bmp",
				"explosion5.bmp",
				"explosion6.bmp",
				"explosion7.bmp",
				"explosion8.bmp",
				"explosion9.bmp" ]

	def __init__(self, x, y):
		super(Explosion, self).__init__(images = Explosion.images,
										x = x, y = y,
										repeat_interval = 4, n_repeats = 1,
										is_collideable = False)
		Explosion.sound.play()
			
class Game(object):
	# The game itself.
	def __init__(self):
		# Initialize the Game object.
		# Set level.
		self.level = 0

		# Load sound for level advance.
		self.sound = games.load_sound("level.wav")

		# Create score.
		self.score = games.Text(value = 0,
								size = 30,
								color = color.white,
								top = 5,
								right = games.screen.width - 10,
								is_collideable = False)
		games.screen.add(self.score)

		# Create player's ship.
		self.ship = Spaceship(	game = self, 
								x = games.screen.width/2,
								y = games.screen.height/2 )
		games.screen.add(self.ship)

	def play(self):
		# Play the game.
		# Start the theme music.
		games.music.load("StarWars.wav")
		games.music.play(-1)

		# Load and set background.
		nebula_image = games.load_image("Stars.jpeg")
		games.screen.background = nebula_image

		# Advance to level 1.
		#self.advance()
		# If all asteroids are gone, advance to the next level.   
		if Asteroid.total == 0 and Comet.total == 0:
		 self.advance()

		# Start play.
		games.screen.mainloop()

	def advance(self):
		# Advance to the next game level.
		self.level += 1
        
		# The space around the spaceship when creating asteroids and comets.
		BUFFER = 150
     
		# Create new asteroids and comets.
		for i in range(self.level):
			# x and y should be BUFFER distance from the spaceship.
			# Choose minimum distance along x-axis and y-axis.
			x_min = random.randrange(BUFFER)
			y_min = BUFFER - x_min

			# Choose distance along x-axis and y-axis based on minimum distance.
			x_distance = random.randrange(x_min, games.screen.width - x_min)
			y_distance = random.randrange(y_min, games.screen.height - y_min)

			# Calculate location based on distance.
			x = self.ship.x + x_distance
			y = self.ship.y + y_distance

			# Wrap around screen, if necessary.
			x %= games.screen.width
			y %= games.screen.height
       
			# Create the asteroid.
			new_asteroid = Asteroid(game = self,
									x = x, y = y,
									size = Asteroid.LARGE)
			games.screen.add(new_asteroid)
			
			#Create the comet
			new_comet = Comet(game = self,
			                  x = x, y = y)
			games.screen.add(new_comet)

		# Display level number.
		level_message = games.Message(	value = "Level " + str(self.level),
										size = 40,
										color = color.yellow,
										x = games.screen.width/2,
										y = games.screen.width/10,
										lifetime = 3 * games.screen.fps,
										is_collideable = False )
		games.screen.add(level_message)

		# Play new level sound (except at first level).
		if self.level > 1:
			self.sound.play()
            
	def end(self):
		# End the game.
		# Show 'Game Over' for 5 seconds.
		end_message = games.Message(value = "Game Over",
									size = 90,
									color = color.red,
									x = games.screen.width/2,
									y = games.screen.height/2,
									lifetime = 5 * games.screen.fps,
									after_death = games.screen.quit,
									is_collideable = False)
		games.screen.add(end_message)

def main():
	meteormayhem = Game()
	meteormayhem.play()

# Start the program
main()


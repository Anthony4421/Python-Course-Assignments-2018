#Assignment 6
#Create a Television Object
#Anthony Swift
 

class Television(object):
 def __init__(self, model, screen_size, volume, channel):
  #Print message each time an object is created
  print("\nA new television has been built!")
  #Setup the attributes
  self.model = model
  self.screen_size = screen_size
  self.__volume = volume
  self.__channel = channel
  
 @property 
 def volume(self):
  return self.__volume
 @volume.setter
 def volume(self,vol):
  if vol > 80:
   print("Volume is too loud!")
  else:
   self.__volume = vol
   print("Volume set to", self.__volume)
 @property 
 def channel(self):
  return self.__channel
 @channel.setter
 def channel(self,chan):
  if chan > 50:
   print("Invalid channel number")
  else:
   self.__channel = chan
   print("Channel changed to: ", self.__channel)
  
  
 def television_details(self):
  #Print details of the television created
  print(self.model, "with", self.screen_size, "inch screen")
  

#Create both sony and samsung television objects and set attributes  
#Calls the television_Details method to print the details of each television

sony = Television("Bravia", 60, 30, 1)
print("It is a Sony",end = " ")
sony.television_details()

samsung = Television("KU6020", 65, 30, 1)
print("It is a Samgsung",end = " ")
samsung.television_details()

#Ask user to change volume and channel on both televisions
#Indirectly calls the methods that changes the volume and channels

print("\nChanging the volume on the Sony...")
vol = int(input("Provide a volume setting between 1 and 100: "))
sony.volume = vol

print("\nChanging the volume on the Samgsung...")
vol = int(input("Provide a volume setting between 1 and 100: "))
samsung.volume = vol

print("\nChanging the channel on the Sony...")
chan = int(input("Provide a channel between 1 and 100: "))
sony.channel = chan

print("\nChanging the channel on the Samgsung...")
chan = int(input("Provide a channel between 1 and 100: "))
samsung.channel = chan









 
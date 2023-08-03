# LightStrike

The three Python and Json files are uploaded on Skydio's software developer console and then being used as a skill to be performed with the drone 
or in a simulation on the Skydio's Mobile App.


## How we built it
We used SkyDio’s built in methods for “skill” creation. Essentially, a skill is a program that will operate and cause actions on the drone after being selected by the user in the drone’s interface.
We had to use Python to create movement patterns and a score count, and we used an Arduino board, IR receiver, and IR emitter to detect when the drone is hit by the player. 


## Challenges we ran into
Initially, we could not access SkyDio’s SDK or API, but after emailing their support staff we were able to get permission a few hours later.
Then, while creating the game software, all but one of our simulators stopped working. While testing in the drone room, there was not enough space to allow for the drone to act the way we were asking it to.

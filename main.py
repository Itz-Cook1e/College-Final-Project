# Assignment:
# Write a program that will tell a robot vacuum how to clean my house. It is a two story house with tile/laminate on the first floor, carpeted stairs, 
# and mixed carpet/hard floors upstairs. Mop the hard floops and vacuum the carpet. As far as I know, there are no models on the market that will 
# currently do stairs, so get creative! I do not care if your robot works like any existing models. Assume that the robot is parked at a charging station 
# where it can empty dirt, empty dirty mop water, and fill up with clean mop water. Also assume that your robot will get be given a start command when it's time. 
# I want you to think about this as a top down design. Ask questions, and answer them with functions. What is the overall goal? Clean ths house. 
# Your main program might be something like
# systemChecks() cleanHouse()
# systemChecks might look like:
# checkDirtLevel() checkCleanWater() checkDirtyWater() checkBattery()
# Then ask yourself what each function needs to do. In checkDirtLevel, you might consult a sensor, and if it is more than say, 75% full, 
# return to the station if you aren't there, and dump the dirt. You might just get a random number for the sensors, or you might add a certain amount of 
# dirt after each room.
# The cleanHouse function should probably include a list of rooms, check the floor type, do a systemCheck, etc.
# What I want to see as output is something like:
# Starting up Checking dirt level Dirt container 5% full Checking clean water Clean water is 20% full Filling clean water Clean water is 100% full Dirty 
# water is empty Current location: kitchen. Hard floor.
# Mopping Obstacle encountered Turning 90 degrees right Moving 1 foot Turning 90 degrees right Mopping Dirty water 80% full Return to station Empty 
# dirty water etc.
# If you want to add detail, mopping can include spraying cleaner, scrubbing, wet vacuuming, rinsing, more wet vacuuming, etc. On second thought, 
# the output is going to get long, so maybe just give me a comment explaining that "mopping" means to spray cleaner, move forward 1 foot while scrubbing, 
# reverse, spray clear water, move 1 foot while wet vacumming, reverse and move forward 1 foot. Or something. :) Also give some thought to obstacles. 
# Do you want to have a pre-programmed path that is followed? Go until you hit an obstacle and then turn in a random direction? If you do a random turn, 
# how will you decide the room has been cleaned enough?
# Be creative. Use lots of functions, loops, if statements, lists. Start with the big picture, then break it down into smaller and smaller pieces.


# Import needed library
import time

# Create places for Narwal Cleaner to clean
places = {'Kitchen',
        "Kid's Bathroom",
        "Kid's Bedroom",
        "Kid's Closet",
        'Office',
        "Downstair's Hallway",
        'Stairs',
        "Upstair's Hallway",
        "Upstair's Hallway Closet",
        'Master Bathroom',
        'Master Bedroom',
        'Master Closet'
}

# Narwal Cleaner dirty/low battery? Time for a charge function!
def charge():
    print( )
    print('Narwal Cleaner: Returning to home.')
    time.sleep(2)
    print('Narwal Cleaner: Returning to home.')
    time.sleep(2)
    print('Narwal Cleaner: Returning to home.')
    time.sleep(2)
    print('Narwal Cleaner: Returning to home.')
    time.sleep(2)
    print('Narwal Cleaner: Returned home.')
    print( )
    print('Narwal Cleaner: Starting recharge/self clean process.')
    time.sleep(7)
    print('Narwal Cleaner: Finished process.')
    print( )
    print('Narwal Cleaner: Returning to previous spot.')

# It appears Narwal Cleaner got stuck on your dirty clothes! Time to call the stuck function!
def stuck():
    print( )
    print('Narwal Cleaner: Narwal Cleaner is stuck! Move to new location to continue cleaning.')
    time.sleep(7)
    print("Narwal Cleaner: It appears you can't move Narwal Cleaner. Attempting maneuver to release Narwal Cleaner.")
    time.sleep(5)
    print('Narwal Cleaner: Narwal Cleaner has been un-stuck. Resuming cleaning process!')
    print( )

# Narwal Cleaner full? Full function initiated!
def full():
    print('Narwal Cleaner: Narwal Cleaner is full. ')
    charge()

# Whats this for again? Narwal Cleaner isnt full...
def not_full():
    print('Narwal Cleaner: Narwal Cleaner is not full. Continuing the cleaning process.')

# The MAIN function. The whole project revolves around the clean function. Want a clean house? Use the Clean function!
def clean():
    for place in places:
        print(place)
    print( )
    all_places = input('Narwal Cleaner: Do you wish to clean all of the above places? (y/n): ')
    all_places.lower()
    if all_places == 'y':
        print( )
        print('Narwal Cleaner: Cleaning started.')
        dirt_levels = 0
        stuck_probability = 0
        for place in places:
            print(f'Narwal Cleaner: Starting to clean {place}.')
            time.sleep(5)
            stuck_probability = stuck_probability+1
            if stuck_probability == 4:
                stuck()
            else:
                pass
            print(f'Narwal Cleaner: Finished cleaning {place}.')
            print('Narwal Cleaner: Checking dirt levels...')
            time.sleep(2)
            dirt_levels = dirt_levels + 20
            dirt_level = str(dirt_levels)
            print(f'Narwal Cleaner: Dirt levels at {dirt_level}%')
            if dirt_levels == 100:
                full()
                print( )
                dirt_levels = 0
                pass
            if dirt_levels < 100:
                not_full()
                print( )
                pass
        print('Narwal Cleaner: Done cleaning! Thank you for using Narwal Cleaning System!')
        raise SystemExit
    if all_places == 'n':
        print( )
        print('Narwal Cleaner: Unfortunatly Narwal Cleaner is only able to clean all places listed. Please either purchase the Narwal Cleaner 2.0 or come back at a later date and try again.')
        raise SystemExit
    else:
        print( )
        print('Narwal Cleaner: Narwal Cleaner had trouble iterperting that message. Please try again.')
        raise SystemExit

# We need to be able to start somewhere... Right? This fuction allows the process to start!
def start():
    clean()

# Call the start fuction to begin the cleaning process offered by Narwal Cleaner!
start()

# Comment with name, date, and assignment name redacted

# code with a # in front of it is a comment. It is my way of writing to you. The computer will ignore it.
# it is always important to put comments in your code so you can remember what you were doing when you come back several years later and need to fix something
# it also makes you way easier to work with

# this is an import instruction. It teaches the program how to do something from somebody else's code. We put this one in here because we want to teach a computer how to read input from the command line
import sys

# we're going to be fancy and do a special function to read the input from the user
# this will save us from writing the same code out over and over
# we put our functions at the top so that way when we try to use them later the computer has some idea what we're talking about
def get_answer(options, prompt):
    # this means ask the user for an input, and store it in answer
    # the variable answer is local to this command. You won't be able to access it after leaving this area
    # the term .lower() is added in so that if you randomly use capital letters you don't confuse the computer
    answer = raw_input(prompt).lower()
    
    # now we're going to check all the options provided and see if what you typed is in there
    for option in options:
        # if the one we currently found is the one we're looking for
        if answer == option:
            # if we found the right thing, return it
            return answer
    # if the answer we gave wasn't in there, tell the user it isn't a valid answer and ask again
    print "Sorry, I didn't understand that answer. Please try again."
    
    # we'll just call the function again, and pass whatever it figures out back.
    # this way the computer can ask you as many times as you want until you get it right
    return get_answer(options, prompt)
    

# here is a print statement. This is how we teach the computer to write to the screen. Most of the storytelling is done here.
print "A human seeing this city would dispair in the emptiness. Despite the billions of dollars and millions of man-hours of planning and labor put in to raise skyscrapers from the ground and lay the streets between them, less than 10% of the city is occupied at all. Whole malls stand empty, waiting for stores to fill them. 30-story buildings of brand new apartments have waited for years without anybody ever coming home to a single one of them. Like so many of China's great top-down projects, it was completed and then abandoned without plans for the next step."

print "That despair means nothing to you though, because you are a street cat. You've never had a pet human to feed and care for you. As a rule humans don't care for you at all, and you expect this to remain how things are for the rest of your life. Like the humans, you haven't planned your next steps either, but you are hungry. Where will you hunt tonight? You could go try a Dumpster behind one of the few open Restaurants, or find a damaged Roof to search for nests."

# this is here we read the input from the command line
destination = get_answer(["roof", "restaurant", "dumpster"], "Where do you go? ")

# here we are using the input to determine what path the story should take. The double equals slign means "check if it is" as compared to the single equals sign above which means "now it is because I say so."
# screwing up double equals sign vs single equals sign is one of the most common mistakes programmers make. Don't feel bad when you screw it up, and keep an eye out for it when your code is behaving poorly
if destination == "roof":
    print "You know the way by several paths. You can go Around the long way and avoid potential trouble, or you can take a Shortcut across another cat's territory."
    path = raw_input("Which way do you go? ").lower()
    if path == "around":
        print "You decide on the safer route, and take your time winding your way through the patches of territory where you know you won't be bothered."
        print "You win."
    elif path == "shortcut":
        print "A massive angry tom doesn't appreciate your lack of respect for his territory. You attempt to explain that you mean no harm, but he interrupts you with a loud open-mouthed hiss, as he flattens his ears against his head, turns slightly sideways and ducks his head down." 
        response = get_answer(["back down", "stand your ground"], "Do you Back Down or Stand Your Ground? ")
        if response == "back down":
            print "The tom was clearly terrified of you, but backing down has shown you're scared of him too, and he is far bigger than you. He rushes in for the attack and bites you several times."
            print "You lose."
        elif response == "stand your ground":
            print "The tom was scared of you before you started trying to be scary, and the sight of you growling and ready to pounce is enough to make him turn tail and run. After he leaves, you find what he was so scared of losing: an entire fish stolen fresh from the market! You will eat well tonight!"
            print "You win."
elif destination == "dumpster" or destination == "restaurant":
    print "You find your way to a nearby restaurant where you have had decent luck in the past. You can try to Hunt the rats near their entrances or you can Scrounge through the dumpster to see what you uncover or run into."
    look_where = get_answer(["scrounge", "hunt"], "Where do you look for food? ")
    if look_where == "scrounge":
        print "You start hunting around the dumpster, but it looks like the restaurant owner is sick of having uninvited visitors there. Your tail snags a snap trap, and your tail is instantly broken. It will heal, but it will be forever crooked, and it's going to hurt terribly for several weeks before then."
        print "You lose."
    elif look_where == "hunt":
        print "You're in luck! It looks like one of the little brats has been in the baijiu. You snatch him up and carry him home, where he makes an excellent meal."
        print "You win."
        
            
 
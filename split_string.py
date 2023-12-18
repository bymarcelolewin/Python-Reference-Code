text = """
Once upon a time warp. . . .

In a galaxy very, very, very, very, far away, there lived a ruthless 
race of beings known as . . . Spaceballs.

Chapter Eleven

The evil leaders of Planet Spaceball, having foolishly spuandered 
their precious atmosphere, have devised a secret plan to take every 
breath of air away from their peace-loving neighbor, Planet Druidia.

Today is Princess Vespa's wedding day. Unbeknownest to the princess, 
but knowest to us, danger lurks in the stars above. . . 

If you can read this, you don't need glasses.


EXT. SPACEBALL 1 - SPACE SPACEBALL 1 passes by at a slow speed. It 
takes the ship about two minutes to pass. At the end of the ship is 
a bumper sticker that says, "WE BRAKE FOR NOBODY."

INT. SPACEBALL 1 - SPACE SANDURZ is standing in the front of the 
ship.

RICO Colonel Sandurz.

SANDURZ What is it, Sergeant Rico?

RICO You told me to let you know the moment Planet Druidia was in 
sight, sir.

SANDURZ So.

RICO Planet Druidia is in sight, sir.

SANDURZ You're really a Spaceball. You know that, don't you?

RICO Thanks, sir.

SANDURZ Have you notified Lord Helmet?

RICO Yes, sir. I took the liberty. He's on his way.

VOICE (O.S.) Make way for Dark Helmet.

SANDURZ All rise in the presence of Dark Helmet.

A door opens revealing DARK HELMET, he resembles Darth Vader, 
walking toward camera. He stops in front of camera, and is having 
trouble breathing with the mask down.

HELMET (pulls mask up) I can't breathe in this thing.

SANDURZ We're approaching Planet Druidia, sir.

HELMET Good. I'll call Spaceball City, and notify President Skroob 
immediately.

RICO I already called him, sir. He knows everything.

HELMET What? You went over my helmet?

RICO Well, not exactly over it, sir. More on the side. I'll always 
call you first. It'll never happen again. Never, ever!

HELMET (puts on Schwartz ring)

RICO Oh shit! No, no, no, no, no, please, no, no, please, no, not 
that. (covers his neck)

HELMET (pulls mask down) Yes. That. (shoots a green ray at Rico's 
crouch)

RICO Whaoooooooo! Owwwwwwwwww!

GUARDS take him away. HELMET Sandurz.

SANDURZ (covers his crouch) Sir?

HELMET I don't see Planet Druidia. Where is it?

SANDURZ We don't have visual contact yet, sir, but we have it on the 
radar screen. Shall I punch it up for you?

HELMET Na, nevermind. I'll do it myself.

HELMET and SANDURZ walk to the radar screen. HELMET stops in front 
of the coffee maker.

SANDURZ Very good, sir. HELMET What's the matter with this thing? 
What's all that churning and bubbling? You call that a radar screen. 
SANDURZ No, sir. We call it, "Mr. Coffee." (points at 
label, "Mr. Coffee") Care for some?

HELMET Yes! I always have coffee when I watch radar. You know that.

SANDURZ Of course I do, sir. HELMET Everybody knows that.

EVERYBODY (covers their crouch) Of course we do, sir.

HELMET (takes coffee) Now that I have my coffee, I'm ready to watch 
radar. Where is it?

SANDURZ (points to label "Mr. Radar") Right here, sir.

HELMET Switch to teleview.

RADAR changes to a picture of Planet Druidia.

"""

#make all text lower case, remove any periods, remove any commas, then split the string into words
t = text.lower().replace(".", "").replace(",", "").split()

#prints all the words
#print(t)

#prints the number of words
print(f"Number of words: {len(t)}")

word_count = {}

for word in t:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print (word_count)
print(f"Number of unique words: {len(word_count)}")
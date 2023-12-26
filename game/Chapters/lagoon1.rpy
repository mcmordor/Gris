    #####Start of Chapter 1#####
    ##Scene --> Backgrounds
    ##Show --> layer above Backgrounds
    ##call --> call label than go back to where you left off
    ##jump --> jump to label and keep going.
label exterior_rattle_snake_rapids:
    play music "audio/music/lagoon_fun.mp3" fadein 1.0 volume 0.5
    scene rattle_snake_rapids_exterior
    with fade
    show Gris zorder 3 at mid_right
    Gris "I'm not saying we would cause a terrorist attack, just that legally we're allowed to."
    show Gritch zorder 2 at off_right
    Gritch "The laws would change, and you'd go to prison for the rest of your life, Gris."
    show Grevor zorder 1 at off_left
    Grevor "Yeah, but what if one of us goes through TSA with a suitcase full of kindling and someone else wears a flint watch and steel necklace?"
    Gritch "I'd call my supervisor immediately."
    show Graustin zorder 5 at mid_left    
    Graustin "Yeah, but what if it was just a small, normal amount of kindling?"
    Gritch "Anything sketchy you try to do at the airport will get you detained."
    Gris "Gritch! They have no rules for that!"
    Gritch "What you're doing now is conspiracy, and I'd be a co-conspirator if anyone found out."
    Gris "Come on, they wouldn't do that, it's not illegal."
    Grevor "Technically we wouldn't be doing anything wrong."
    Gritch "Try it and see what happens. Go to jail for the rest of your life."
    Gris "Conspiracy to do what?! I think you're changing the rules on us, Gritch. That's not what you said would happen."

    
    play sound "audio/sfx/waterphone.mp3" fadein 1.0
    stop music fadeout 1.0 
    lagoon_passenger "Can you keep it down? My kid doesn't like swears."
    kid "..."
    Gritch "..."
    Gris "..."
    Grevor "..."
    Graustin "Oh, I'm sorry! I'm not allowed to talk to you."
    play music "audio/music/lagoon_fun.mp3" fadein 1.0
    lagoon_passenger "*frowns*"
    employee "How many?"
    Gris "Oh, we're up next."
    Grevor "One, plus my friends."
    employee "..."
    Gritch "We'll ride with the kid."
    lagoon_passenger "*frowns harder*"
    stop music fadeout 1.0  
    play music "audio/music/gruckintro.mp3" noloop volume 0.25
    queue music "audio/music/gruckiloop1.mp3" loop volume 0.25
    Graustin "Hurry before Mr. Gr..."

    #Grooki
    play sound "audio/sfx/jump.mp3" volume 1.0
    window auto hide
    show mr_grucki zorder 4 at left
    show mr_grucki:
        default
        subpixel True 
        parallel:
            xpos -477 
            linear 0.95 xpos 171 
            linear 2.06 xpos 819 
            linear 2.64 xpos 738 
            linear 1.35 xpos 810 
        parallel:
            ypos 0 
            linear 0.01 ypos 0 
            linear 0.94 ypos 1953 
            linear 0.89 ypos 1431 
            linear 1.17 ypos 972 
            linear 2.64 ypos 1188 
            linear 1.35 ypos 1251 
        parallel:
            zpos 0.0 rotate 0.0 
            linear 7.00 zpos 153.0 rotate 18.0 
    with Pause(7.10)
    show mr_grucki:
        pos (810, 1251) zpos 153.0 rotate 18.0 
    window auto show
    hide Graustin
    show graustin_annoyed_fb zorder 5
    show graustin_annoyed_fb:
        pos (819, 1334) zpos 684.0 
    Graustin "FPHE! GFIUCK!"
    
    # Mr. Grucki arrives and jumps on Graustin's back like a spider monkey.
    play sound "audio/sfx/yeah_boy.mp3" volume 2.0
    mr_grucki "Make that one more! Come on, kids... HEHEHEHE!"
    mr_grucki "Have ya been boning up on your ol' Grootah Studies?"
    Grevor "Uh... hey, Mr. Grucki."
    mr_grucki "Oh well, if it isn't Cotton."
    mr_grucki "Say, Cotton, why don't you fucking NOT ride with us!"
    Grevor ":("
    play sound "audio/sfx/wicked_laugh.mp3" volume 0.75 
    mr_grucki ":)!!!!!"
    Gritch "You heard him, Cotton... I mean, Grevor. Gotta obey your elders."
    Gris "Oh fuck, Mr. Grucki is still alive."
    mr_grucki "Here, kids. I gotta Snapchat this real quick."
    Graustin "Heh, ya mind getting off my back? I'm quite winded."
    mr_grucki "Only if all of you promise to take this salvia."
    Gritch "I AM NOT DOING THAT!"
    Graustin "Please, Gritch. I'm going to snap in half if Mr. Grucki doesn't stop wriggling around up there."
    Gritch "No, I think you should have to die. I won't do it. Sorry, Graustin."
    Grevor "Gritch, open your mouth, or we're gonna titty twist ya."
    Gris "YEAH, WE'RE GONNA TITTY TWIST!!!"
    play sound "audio/sfx/deep_ohno.mp3" volume 1.0
    Gritch "NOO! NOO, GET OFF ME!"

    # Grevor shoves the salvia into Gritch's mouth.
    Grevor "Now shove the whole thing in his mouth so we don't have to take any!"
    Gritch "MMPHH!!!"
    Gris "Hehehe, now he's gonna trip balls."
    mr_grucki "Now it's all your turn! TAKE A WHIFF OF THIS!"

    # Narrator describes the scene as they get on the ride.
    play music "audio/music/gruckend.mp3" volume 0.25 noloop
    play sound "audio/sfx/wicked_laugh.mp3" volume 0.75 
    queue sound "audio/sfx/yeah_boy.mp3" volume 2.0
    stop music fadeout 1.0
    narrator "Mr. Grucki fingers each of their mouths full of the hellish chew, and they hop on for the ride of their lives."

    # End Scene. Transition to the Rattle Snake Rapids ride.
    scene black
    with dissolve
    # The script continues with the psychedelic trip sequence as previously described.
    jump black

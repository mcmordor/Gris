label black:
    scene rattle_snake_rapids_exterior
    with fade
    # The group is now on the ride, Mr. Grucki has just forced Salvia on them.
    Gritch "I can't believe we're doing this. This is insane!"
    Grevor "Just go with it, man. It's too late to back out now."
    Grevor "Anyways, do you think Salvia is anabolic?"
    Grevor "cuz that woudl be sick as hell"
    Graustin "What if we see the 'other side', the place beyond life and death?"
    Gritch "NO!"
    #Mr Gucki Panting and pacing like a feral dog
    show graustin_torso:
        default
        subpixel True pos (1035, 1251) zpos 423.0 
    
    Graustin  "Mr. Grucki, what troubles you so?"
    hide graustin_torso
    #Mr Grucki PAcing Animatin
    window auto hide
    play sound "audio/sfx/jump.mp3" loop
    play music "audio/music/gruckiloop1.mp3"
    show mr_grucki:
        default
        subpixel True 
        parallel:
            xpos 252 
            linear 0.32 xpos 549 
            linear 0.42 xpos 846 
            linear 0.61 xpos 1125 
            linear 0.82 xpos 1170 
            linear 1.10 xpos 1521 
            linear 1.11 xpos 1116 
            linear 0.87 xpos 828 
            linear 1.25 xpos 252 
        parallel:
            ypos 1197 
            linear 0.32 ypos 1305 
            linear 0.42 ypos 1197 
            linear 0.61 ypos 1368 
            linear 0.40 ypos 1278 
            linear 0.42 ypos 1341 
            linear 1.10 ypos 1458 
            linear 1.11 ypos 1557 
            linear 0.87 ypos 1368 
            linear 0.95 ypos 1524 
            linear 0.30 ypos 1197 
        parallel:
            zpos 45.0 
            linear 0.32 zpos 117.0 
            linear 1.03 zpos 153.0 
            linear 1.61 zpos 0.0 
            linear 0.31 zpos 117.0 
            linear 1.11 zpos 36.0 
            linear 0.87 zpos 162.0 
            linear 0.67 zpos 288.0 
            linear 0.58 zpos 45.0 
        parallel:
            xrotate 0.0 
            linear 0.32 xrotate -9.0 
            linear 0.42 xrotate 0.0 
            linear 2.53 xrotate -27.0 
            linear 0.44 xrotate 36.0 
            linear 1.54 xrotate 0.0 
        parallel:
            yrotate 0.0 
            linear 5.25 yrotate -36.0 
            linear 1.25 yrotate 0.0 
        parallel:
            rotate 0.0 
            linear 0.32 rotate -9.0 
            linear 0.42 rotate 0.0 
            linear 0.61 rotate -18.0 
            linear 0.40 rotate 0.0 
            linear 0.42 rotate 27.0 
            linear 0.79 rotate 0.0 
            linear 0.31 rotate -18.0 
            linear 0.44 rotate 0.0 
            linear 1.54 rotate -18.0 
            linear 0.67 rotate -26.35 
            linear 0.58 rotate 0.0 
    with Pause(6.60)
    show mr_grucki:
        pos (252, 1197) zpos 45.0 xrotate 0.0 yrotate 0.0 rotate 0.0 
    window auto show
    play music "audio/music/gruckend.mp3" noloop
    stop sound 
    mr_grucki "I can't stand still! You know, I get the best stuff right here in Lagoon. Farmington's got nothing on me!"
    kid "Daddy, are they allowed to do this?"
    lagoon_passenger "I don't know son, I think that man is their...teacher?"
    lagoon_passenger "They are probably special needs or something. Just try not to look at them."
    hide mr_grucki
    Gritch "STOP IT! DON'T SAY THAT!!!"
    Graustin "Mr. Grucki, stop pacing! You're scaring Gris!"
    show Gris CU_shocked
    Gris "..."
    Gris " "
    hide Gris CU_shocked
    mr_grucki "This park's my kingdom, and I rule the underground here!"
    Gritch "MR GRUCKI! STOP BEING A WEIRDO RIGHT NOW!!!"
    Graustin "*Gasp* Gritch..."
    Grevor "Gritch, why are you freaking out man? It's just a ride."
    Gritch "This is not 'just a ride' for me, Grevor! We're breaking the law!"
    jump grucki_transformation

label grucki_transformation:
    scene psychedelic_trip_background
    with dissolve
    define goblin_sacrifices = 0
    # Mr. Grucki undergoes a terrifying transformation.
    narrator "Before their eyes, Mr. Grucki's form twists and contorts, his body elongating and morphing into a grotesque, giant, skin-like cat."
    #show mr_grucki_cat_form

    mr_grucki "My little playthings, it's time for a game. Will you offer yourselves to my barbed tongue?"
    
    # The monstrous Mr. Grucki presents a horrifying challenge.
    narrator "Each goblin must choose a part of their body for the creature to lick with its razor-sharp tongue. But too many licks from the same person, and they'll be torn apart."

    # The player makes a choice for each character.
    label sacrifice_choice:
        menu:
            "Gris offers his arm":
                Gris "Take my arm, but nothing more."
                $ grisLick =1
                narrator "The monstrous cat licks Gris's arm, its tongue like sandpaper, leaving the skin raw and bleeding."
            "Grevor offers his leg":
                Grevor "My leg... do what you must."
                $ grevorLick =1
                narrator "With each lick, Grevor winces in pain, the barbs scraping flesh from bone."
            "Graustin offers his hand":
                Graustin "Here, my hand... it's all I can bear to give."
                $ graustinLick =1
                narrator "Graustin's hand is left red and torn, each lick a new agony."
            "Gritch refuses to offer anything":
                Gritch "I won't play this game! I refuse!"
                $ goblin_sacrifices = 3
                narrator "The creature turns on Gritch, its maw opening wide, ready to consume him whole."

    # The consequence of the choices made.
    if goblin_sacrifices >= 3:
        # The chosen character meets a gruesome end.
        narrator "With a horrifying screech, the creature lunges, tearing the goblin to shreds as the others watch in horror."
        scene goblin_death
        with shake
    else:
        # The group narrowly escapes the creature's wrath.
        narrator "The creature, sated by the offerings, recedes into the shadows, leaving the goblins trembling and scarred."
        scene psychedelic_trip_background
        with dissolve

    return




    # The ride begins to move, and the world starts to change around them.
    show ride_starting
    #with shake

    # As the effects of Salvia kick in, each character begins to experience vivid hallucinations.
    # The narrative shifts to reflect their inner psyches and fears.
    label psychedelic_trip:
        scene psychedelic_trip
        with dissolve

        # Each character confronts their own demons and desires in surreal vignettes.
        #show Gris facing his demons
        Gris "Is this reality? Or am I still dreaming of the stage I never reached?"

        #show Grevor in a surreal UFC fight
        Grevor "I must fight! Fight against the chains that bind me, the expectations that weigh me down!"

        #show Graustin in a kitchen nightmare
        Graustin "The dishes... they're speaking to me, telling me secrets of the universe!"

        #show Gritch chased by TSA agents
        Gritch "I can't escape them, even in my mind. The endless scrutiny, the judgment!"

    # As the ride comes to an end, the characters return to their senses, each changed in some way.
    label ride_ends:
        scene rattle_snake_rapids_exterior
        with fade

        # The friends are quiet, each processing the journey they've been on.
        Gris "Was any of that real? What does it mean?"
        Grevor "I... I need to call Gruz. I need to set things right."
        Graustin "I saw beauty in the madness... I need to capture it, in my cooking."
        Gritch "I think... I need a vacation. Somewhere far from any airport."

    # The Lagoon Passenger and Kid reappear, giving the friends a grounding in reality.
    #show lagoon_passenger with kid
    lagoon_passenger "Are you boys alright? You were screaming the whole time."
    kid "Mommy, are they monsters?"

    # Mr. Grucki is nowhere to be seen.
    Gris "Where did Mr. Grucki go? Was he even here to begin with?"

    # The chapter closes with the friends leaving the ride, contemplating their experiences.
    narrator "The goblin friends left Rattle Snake Rapids with more than just a story. They carried with them a piece of the ride's madness, a shared hallucination that would bind them forever."

    # The scene transitions to the aftermath, setting up the next chapter of the game.
    scene aftermath
    with fade
    Gris "What do we do now?"
    Grevor "We live, Gris. We live like we've seen the edge and came back."
    Graustin "To the kitchen, my sanctuary! I have a masterpiece to create."
    Gritch "And I... I think I'll write a book. 'TSA and Beyond: A Goblin's Tale.'"
    Gris "Let's go home, guys."

    return



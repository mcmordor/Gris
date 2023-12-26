label black:
    scene rattle_snake_rapids_exterior
    with fade
    # The group is now on the ride, Mr. Grucki has just forced Salvia on them.
    Gris "I can't believe we're doing this. This is insane!"
    Grevor "Just go with it, man. It's too late to back out now."
    Grevor "Anyways, do you think Salvia is anabolic?"
    Grevor "cuz that woudl be sick as hell"
    Graustin "What if we see the 'other side', the place beyond life and death?"
    Gritch "NO!"
    #Mr Gucki Panting and pacing like a feral dog
    Graustin  "Mr. Grucki, what troubles you so?"
    mr_grucki "I can't stand still! You know, I get the best stuff right here in Lagoon. Farmington's got nothing on me!"
    kid "Daddy, are they allowed to do this?"
    lagoon_passenger "I don't know son, I think that man is their...teacher?"
    lagoon_passenger "They are probably special needs or something. Just try not to look at them."
    Gritch "STOP IT! DON'T SAY THAT!!!"
    Graustin "Mr. Grucki, stop pacing! You're scaring Gris!"
    Gris "..."
    Gris " "
    mr_grucki "This park's my kingdom, and I rule the underground here!"
    Gritch "MR GRUCKI! STOP BEING A WEIRDO RIGHT NOW!!!"
    Graustin "*Gasp* Gritch..."
    Grevor "Gritch, why are you freaking out man? It's just a ride."
    Gritch "This is not 'just a ride' for me, Grevor! We're breaking the law!"
    jump grucki_transformation

label grucki_transformation:
    scene psychedelic_trip_background
    with dissolve

    # Mr. Grucki undergoes a terrifying transformation.
    narrator "Before their eyes, Mr. Grucki's form twists and contorts, his body elongating and morphing into a grotesque, giant, skin-like cat."
    #show mr_grucki_cat_form

    mr_grucki_cat "My little playthings, it's time for a game. Will you offer yourselves to my barbed tongue?"
    
    # The monstrous Mr. Grucki presents a horrifying challenge.
    narrator "Each goblin must choose a part of their body for the creature to lick with its razor-sharp tongue. But too many licks from the same person, and they'll be torn apart."

    # The player makes a choice for each character.
    label sacrifice_choice:
        $ grisLick = 0
        $ grevorLick = 0
        $ graustinLick = 0
        $ gritchLick = 0
        menu:
            "Gris offers his arm":
                Gris "Take my arm, but nothing more."
                $ grisLick +=1
                narrator "The monstrous cat licks Gris's arm, its tongue like sandpaper, leaving the skin raw and bleeding."
            "Grevor offers his leg":
                Grevor "My leg... do what you must."
                $ grisLick +=1
                narrator "With each lick, Grevor winces in pain, the barbs scraping flesh from bone."
            "Graustin offers his hand":
                Graustin "Here, my hand... it's all I can bear to give."
                $ grisLick +=1
                narrator "Graustin's hand is left red and torn, each lick a new agony."
            "Gritch refuses to offer anything":
                Gritch "I won't play this game! I refuse!"
                $ grisLick +=1
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



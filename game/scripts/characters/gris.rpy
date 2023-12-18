init python:
    #Generate seperate audio channel from voice for beeps.
    renpy.music.register_channel(name='beeps', mixer='voice')
    renpy.music.set_volume('beeps', 0.5)
    
    #Character callback that generates the sound.
    def e(event, **kwargs):
        if event == "show":  # When the text is shown
            print("Playing beep sound for Gris")  # Debug message
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":  # When the text is finished displaying or you open a menu.
            renpy.sound.stop(channel="beeps")


#Gris the Goblin
define Gris = Character("Gris", color="#ADD8E6", callback=e)
#Gris Torso Shots
image Gris happy = "characters/Gris/Torso/Gris_Happy_Torso.png"
image Gris annoyed  = "characters/Gris/Torso/Gris_Annoyed_Torso.png"
image Gris shocked = "characters/Gris/Torso/Gris_Surprised_Torso.png"
image Gris flirt = "characters/Gris/Torso/Gris_Flirt_Torso.png"
image Gris = "characters/Gris/Torso/Gris_Torso.png"


#Gris FullBody Shots
image Gris FB_happy = "characters/Gris/FullBody/Gris_Happy_FB.png"
image Gris FB_annoyed  = "characters/Gris/FullBody/Gris_Annoyed_FB.png"
image Gris FB_shocked = "characters/Gris/FullBody/Gris_Surprised_FB.png"
image Gris FB = "characters/Gris/FullBody/Gris_FB.png"

#Gris Close Up Shots
image Gris CU_happy = "characters/Gris/CloseUp/Gris_Happy_CloseUp.png"
image Gris CU_annoyed  = "characters/Gris/CloseUp/Gris_Annoyed_CloseUp.png"
image Gris CU_shocked = "characters/Gris/CloseUp/Gris_Surprised_CloseUp.png"
image Gris CU_flirt = "characters/Gris/CloseUp/Gris_Flirt_CloseUp.png"
image Gris CU = "characters/Gris/CloseUp/Gris_CloseUp.png"
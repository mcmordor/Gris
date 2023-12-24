# Character Creation Screen
label character_creation:
    scene bg_character_creation
    with fade

    $ character = Character()

    # Character Name
    label enter_name:
    scene bg_name_entry
    with fade
    $ character.name = renpy.input("Enter your character's name:")
    if character.name == "":
        jump enter_name

    # Background Selection
    scene bg_background_selection
    with fade
    menu:
        "Choose your background:"
        "Woodsman":
            $ character.background = "Woodsman"
        "Scholar":
            $ character.background = "Scholar"
        "Mercenary":
            $ character.background = "Mercenary"

    # Trait Selection
    scene bg_trait_selection
    with fade
    menu:
        "Select a trait:"
        "Brave":
            $ character.trait = "Brave"
        "Cunning":
            $ character.trait = "Cunning"
        "Wise":
            $ character.trait = "Wise"

    # Ability Score Rolling
    scene bg_ability_scores
    with fade
    call roll_ability_scores

    # Inventory Management
    scene bg_inventory_management
    with fade
    call manage_inventory

    return

# Ability Score Rolling
label roll_ability_scores:
    # Add the code/logic for rolling ability scores here
    return

# Inventory Management
label manage_inventory:
    # Add the code/logic for inventory management here
    return

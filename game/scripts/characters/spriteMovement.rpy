transform move_left_offscreen:
    xoffset 0
    linear 3.0 xoffset -1500
    pause 3.0  # This ensures the transform completes before proceeding.
transform move_right_onscreen:
    xoffset -1500
    linear 1 xoffset 0
    pause 1.0  # This ensures the transform completes before proceeding.

transform off_left:
    xalign 0
    xoffset -200

transform off_right:
    xalign 1.0
    xoffset 200

transform mid_left:
    xalign 0.5
    xoffset -200

transform mid_right:
    xalign 0.5
    xoffset 100

transform icon:
    xalign 0.0
    xoffset 50
    yoffset -50
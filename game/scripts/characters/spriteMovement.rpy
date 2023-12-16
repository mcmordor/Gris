transform move_left_offscreen:
    xoffset 0
    linear 3.0 xoffset -1500
    pause 3.0  # This ensures the transform completes before proceeding.
transform move_right_onscreen:
    xoffset -1500
    linear 1 xoffset 0
    pause 1.0  # This ensures the transform completes before proceeding.

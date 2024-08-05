'''On the way back to the start, at Position D, research
something you can do with the robot and implement it
here. This will also be the final reset point on the way
back to the Start Position (A) for the end of the course.
You are not required to do the zigzag again - just go
straight through.'''

#DESCRIPTION: Robot fires full-auto with both Gun and IR Laser in an "X" pattern.
#AUTHOR:      Robot Group 5 (Zachary Collier)
#DATE:        August 5th 2024
#NOTE:        Robot used is the RoboMaster S1 by DJI.

def robo_research_full_auto_sweep():
    gimbal_ctrl.recenter()
    gimbal_ctrl.set_rotate_speed(50)
    gun_ctrl.set_fire_count(5)
    ir_blaster_ctrl.set_fire_count(2)
    gimbal_ctrl.angle_ctrl(-15, -25)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_breath)
    time.sleep(0.5)
    gun_ctrl.fire_continuous()
    ir_blaster_ctrl.fire_continuous()
    gimbal_ctrl.angle_ctrl(35, 25)
    time.sleep(1)
    gun_ctrl.stop()
    ir_blaster_ctrl.stop()
    gimbal_ctrl.angle_ctrl(-15, 25)
    gun_ctrl.fire_continuous()
    ir_blaster_ctrl.fire_continuous()
    gimbal_ctrl.angle_ctrl(35, -25)
    time.sleep(1)
    gun_ctrl.stop()
    ir_blaster_ctrl.stop()
    media_ctrl.play_sound(rm_define.media_sound_recognize_success, wait_complete_flag=False)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_always_on)
    time.sleep(1)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_always_off)
    gimbal_ctrl.set_rotate_speed(60)
    gimbal_ctrl.recenter()


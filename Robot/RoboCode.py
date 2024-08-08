counter = 0
 
def start():
    global counter
    gimbal_ctrl.recenter()
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(60)
    chassis_ctrl.set_rotate_speed(30)
    chassis_ctrl.set_trans_speed(0.8)
 
    section_b()
 
    move_to_pillar_c()
    scan_at_pillar()
    counter += 1
    
    move_to_pillar_e()
    scan_at_pillar()
    counter += 1
 
    move_to_f()
    scan_at_pillar()
    
    move_to_pillar_g()
    scan_at_pillar()
    move_to_h()
    move_to_d()
    robo_research_full_auto_sweep()
    move_to_a()
 
def section_b():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.8)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 0.8)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 0.45)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 1.6)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 0.45)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 0.53)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 39)
    chassis_ctrl.move_with_distance(0, 1.65)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 51)
    chassis_ctrl.move_with_distance(0, 0.4)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 0.8)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 0.4)
    time.sleep(5)
    
def vision_recognized_marker_letter_F(msg):
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    gun_ctrl.fire_once()
 
def vision_recognized_marker_letter_D(msg):
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
 
def vision_recognized_marker_letter_P(msg):
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    print("made it to p")
    return_to_start()
 
def move_to_pillar_c():
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 1.6)
 
def move_to_pillar_e():
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 4.90)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0, 3.75)
 
def move_to_f():
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 4.8)
 
def move_to_pillar_g():
    gimbal_ctrl.recenter()
    time.sleep(5)
    chassis_ctrl.move_with_distance(0, 4.40)
 
def move_to_h():
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 1)
 
def move_to_d():
    gimbal_ctrl.recenter()
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
    gimbal_ctrl.recenter()
    time.sleep(5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 3.30)
 
def move_to_a():
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2)
 
def scan_at_pillar():
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    print("scanned pillar")
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(180)
 
 
def return_to_start():
    global counter
    gimbal_ctrl.recenter()
    if counter == 0:
        print("post counter 1")
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 0.65)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 0.65)
        time.sleep(5)
    elif counter == 1:
        print("post counter 2")
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        time.sleep(5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 4)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4)
        time.sleep(5)
    elif counter == 2:
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        time.sleep(5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 3.24)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.24)
        time.sleep(5)
    else:
        print("counter error")
 
    
def vision_recognized_marker_number_one(msg):
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)  
    chassis_ctrl.move_with_distance(-180, 0.2)
    gimbal_ctrl.yaw_ctrl(20)
    gimbal_ctrl.yaw_ctrl(-20)
    gimbal_ctrl.pitch_ctrl(20)
    gimbal_ctrl.pitch_ctrl(-20)
    chassis_ctrl.move_with_distance(180, 0.2)
    time.sleep(2)
 
def vision_recognized_marker_number_two(msg):
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    led_ctrl.set_flash(rm_define.armor_all, 3)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 69, 215, 255, rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 150, rm_define.effect_always_on)
    time.sleep(2)
 
def vision_recognized_marker_number_three(msg):
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    chassis_ctrl.move_with_distance(-180, 0.2)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(180, 0.2)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(180, 0.2)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(180, 0.2)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 0.2)
    gimbal_ctrl.yaw_ctrl(20)
    gimbal_ctrl.pitch_ctrl(20)
    gimbal_ctrl.yaw_ctrl(-20)
    gimbal_ctrl.pitch_ctrl(-20)
    gimbal_ctrl.pitch_ctrl(20)
    gimbal_ctrl.pitch_ctrl(-20)
    gimbal_ctrl.recenter()
    led_ctrl.set_top_led(rm_define.armor_top_all, 69, 215, 255, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 150, rm_define.effect_always_on)
    led_ctrl.turn_off(rm_define.armor_all)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 69, 215, 255, rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 150, rm_define.effect_always_on)
    time.sleep(2)
 
def robo_research_full_auto_sweep():
    gimbal_ctrl.recenter()
    gimbal_ctrl.set_rotate_speed(50)
    gun_ctrl.set_fire_count(5)
    ir_blaster_ctrl.set_fire_count(2)
    gimbal_ctrl.angle_ctrl(-10, -20)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_breath)
    time.sleep(0.5) #Simulate spinup
    gun_ctrl.fire_continuous()
    ir_blaster_ctrl.fire_continuous()
    gimbal_ctrl.angle_ctrl(35, 25)
    gun_ctrl.stop()
    ir_blaster_ctrl.stop()
    gimbal_ctrl.angle_ctrl(-15, 25)
    gun_ctrl.fire_continuous()
    ir_blaster_ctrl.fire_continuous()
    gimbal_ctrl.angle_ctrl(30, -20)
    gun_ctrl.stop()
    ir_blaster_ctrl.stop()
    media_ctrl.play_sound(rm_define.media_sound_recognize_success, wait_complete_flag=False)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_always_on)
    time.sleep(1) #Simulate cooldown
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_always_off)
    gimbal_ctrl.set_rotate_speed(60)
    gimbal_ctrl.recenter()
#DESCRIPTION: Robot scans for F (Fire Weapon), D (Danger, pass), or P (Person, return to start then return to position) at pillars C, E, G.
#AUTHOR:      Robot Group 5 (Zachary Collier)
#DATE:        August 2nd 2024
#NOTE:        Robot used is the RoboMaster S1 by DJI.
# move_with_distance takes in two parameters, the first is an angle (0 meaning
# move straight ahead forward), and the second is a distance in meters (in this case,
# move 0.3 meters forward – the max distance is 5 meters - if you need to move
# more than 5 meters you need to set up two – or more – commands.)

def vision_recognized_marker_letter_F(msg):
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    gun_ctrl.fire_once()

def vision_recognized_marker_letter_D(msg):
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)

def scan_at_pillar_c():
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(+180)
    
    def vision_recognized_marker_letter_P(msg):
        vision_ctrl.disable_detection(rm_define.vision_detection_marker)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 3.6)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.6)

def scan_at_pillar_e():
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(+180)
    
    def vision_recognized_marker_letter_P(msg):
        vision_ctrl.disable_detection(rm_define.vision_detection_marker)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 2.3)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.3)

def scan_at_pillar_g():
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(+180)
    
    def vision_recognized_marker_letter_P(msg):
        vision_ctrl.disable_detection(rm_define.vision_detection_marker)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 5)
        chassis_ctrl.move_with_distance(-180, 1)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1)
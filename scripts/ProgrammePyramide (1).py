from pyniryo import *
robot = NiryoRobot("10.10.10.10")
robot.set_arm_max_velocity(100)
Home = robot.get_pose()
# def pickpandplaceniryo(x,y):
#     x = X[0]
#     y = X[1]
#     z = X[2]
#     Robot.update_tool()
#     Robot.release_with_tool()
#     Robot.move_pose(x)
#     Robot.grasp_with_tool()
#     Robot.move_pose(y)
#     Robot.release_with_tool()
#     Robot.move_pose(Home)
#

def pyramideniryo(x,y,z,o):
    l = [x,y,z]
    lunpy = []
    robot.update_tool()
    c = 0
    for i in l:
        Robot.release_with_tool()
        Robot.move_pose(i)
        Robot.grasp_with_tool()
        Robot.move_pose(Home)
        new_place_pose = o.copy_with_offsets(z_offset=0.01 * c)
        lunpy.append(new_place_pose)
        Robot.move_pose(new_place_pose)
        Robot.release_with_tool()
        Robot.move_pose(Home)
        c = c + 1
    for i in lunpy:
        Robot.release_with_tool()
        Robot.move_pose(lunpy[c-1])
        Robot.grasp_with_tool()
        Robot.move_pose(Home)
        Robot.move_pose(l[c-1])
        Robot.release_with_tool()
        Robot.move_pose(Home)
        c = c - 1
    x = PoseObject(x = 0.240, y = 0.090, z = 0.120, roll = 0, pitch = 1.57, yaw = 0)
    y = PoseObject(x = 0.203, y = 0.200, z = 0.120, roll = 0, pitch = 1.57, yaw = 0)
    z = PoseObject(x = 0.242, y = -0.150, z = 0.120, roll = 0, pitch = 1.57, yaw = 0)
    o = PoseObject(x = 0.235, y = 0.0,z = 0.120, roll = 0, pitch = 1.57, yaw = 0)

pyramide(x,y,z,o)
robot.close_connection()
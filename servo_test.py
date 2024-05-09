import os
from dynamixel_sdk import *
from time import sleep

# ngl I don't see the point of this.
if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

###### CONSTANTS ######

# Control table addresses
# https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/
ADDR_MX_TORQUE_ENABLE = 24
ADDR_MX_GOAL_POSITION = 30
ADDR_MX_PRESENT_POSITION = 36
ADDR_MX_MOVE_SPEED = 32

# Protocol version
# Note: Dynamixel AX-12A use only Protocol 1
PROTOCOL_VERSION = 1.0

# Dynamixel IDs are obtained using Dynamixel Wizard
# leg 1
DXL_ID1 = 1
DXL_ID2 = 3
DXL_ID3 = 5
# leg 2
DXL_ID4 = 2
DXL_ID5 = 4
DXL_ID6 = 6
# leg 3
DXL_ID7 = 14
DXL_ID8 = 16
DXL_ID9 = 18
# leg 4
DXL_ID10 = 8
DXL_ID11 = 10
DXL_ID12 = 12
# leg 5
DXL_ID13 = 7
DXL_ID14 = 9
DXL_ID15 = 11
# leg 6
DXL_ID16 = 13
DXL_ID17 = 15
DXL_ID18 = 17

BAUDRATE = 1000000 # Must be 1000000 to work with the AX series.
DEVICENAME = 'COM11' # Port used to connect, depends on device

TORQUE_ENABLE = 1 # Value for enabling the torque
TORQUE_DISABLE = 0 # Value for disabling the torque
DXL_MOVING_STATUS_THRESHOLD = 10 # Dynamixel moving status threshold

# Initialize PortHandler instance and set the port path
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance and set the protocol version
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()

class Servo:
    def __init__(self, id: int) -> None:
        self.id = id
    
    def set_torque_value(self, enable_val: int) -> bool:
        # enable_val = 1 (torque is enabled); enable_val = 0 (torque is disabled, is default of each AX-12A servo)
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, self.id, ADDR_MX_TORQUE_ENABLE, enable_val)
        if dxl_comm_result != COMM_SUCCESS: # incorrect status packet
            print("Servo ID #" + str(self.id) + " %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("Servo ID #" + str(self.id) + " %s" % packetHandler.getRxPacketError(dxl_error))
        else:
            if enable_val == 1:
                print("Servo ID #" + str(self.id) + " torque enabled")
            else:
                print("Servo ID #" + str(self.id) + " torque disabled")
            return True
        return False
    
    def set_speed(self, speed: int) -> bool:
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, self.id, ADDR_MX_MOVE_SPEED, speed)
        if dxl_comm_result != COMM_SUCCESS: # incorrect status packet
            print("Servo ID #" + str(self.id) + " %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("Servo ID #" + str(self.id) + " %s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Servo ID #" + str(self.id) + " speed set to " + str(speed))
            return True
        return False
    
    def set_goal_position(self, position: int) -> bool:
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, self.id, ADDR_MX_GOAL_POSITION, position)
        if dxl_comm_result != COMM_SUCCESS: # incorrect status packet
            print("Servo ID #" + str(self.id) + " %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("Servo ID #" + str(self.id) + " %s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Servo ID #" + str(self.id) + " goal set to " + str(position))
            return True
        return False

    def get_goal_position(self) -> int | bool:
        dxl_goal_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, self.id, ADDR_MX_GOAL_POSITION)
        if dxl_comm_result != COMM_SUCCESS: # incorrect status packet
            print("Servo ID #" + str(self.id) + " %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("Servo ID #" + str(self.id) + " %s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Servo ID #" + str(self.id) + " goal position:", dxl_goal_position)
            return dxl_goal_position
        return False

    def get_current_position(self) -> int | bool:
        dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, self.id, ADDR_MX_PRESENT_POSITION)
        if dxl_comm_result != COMM_SUCCESS: # incorrect status packet
            print("Servo ID #" + str(self.id) + " %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("Servo ID #" + str(self.id) + " %s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Servo ID #" + str(self.id) + " current position:", dxl_present_position)
            return dxl_present_position
        return False

def main() -> None:
    # instances of the servos
    servoList = [Servo(DXL_ID16), Servo(DXL_ID17), Servo(DXL_ID18),
                 Servo(DXL_ID10), Servo(DXL_ID11)]
    # Servo(DXL_ID1), Servo(DXL_ID2), Servo(DXL_ID3), 
    # Servo(DXL_ID4), Servo(DXL_ID5), Servo(DXL_ID6), 
    # Servo(DXL_ID7), Servo(DXL_ID8), Servo(DXL_ID9), 
    # Servo(DXL_ID10), Servo(DXL_ID11), Servo(DXL_ID12), 
    # Servo(DXL_ID13), Servo(DXL_ID14), Servo(DXL_ID15), 
    # Servo(DXL_ID16), Servo(DXL_ID17), Servo(DXL_ID18)

    # Enable Dynamixel Torque
    for servo in servoList:
        is_set_torque = servo.set_torque_value(TORQUE_ENABLE)
        while not is_set_torque:
            is_set_torque = servo.set_torque_value(TORQUE_ENABLE)

    # Set the speed of the servos
    for servo in servoList:
        is_set_speed = servo.set_speed(100)
        while not is_set_speed:
            is_set_speed = servo.set_speed(100)

    # Write goal position
    for servo in servoList:
        is_set_goal = servo.set_goal_position(500)
        while not is_set_goal:
            is_set_goal = servo.set_goal_position(500)

    # get the goal positions after overriding
    goal_positions_dict = {}
    for servo in servoList:
        get_goal = servo.get_goal_position()
        while get_goal == False:
            get_goal = servo.get_goal_position()
        goal_positions_dict[str(servo.id)] = get_goal

    move = True
    while move:
        # get the current positions, insert into dictionary using servo id as key
        servo_pos_dict = {}
        for servo in servoList:
            get_current = servo.get_current_position()
            while get_current == False:
                get_current = servo.get_current_position()
            servo_pos_dict[str(servo.id)] = get_current

        move_verdict = []

        # check goal positions against current positions; both dictionaries share keys
        for a in goal_positions_dict.keys():
            # check if the current position is within a tolerance for the goal
            if (goal_positions_dict[a] - DXL_MOVING_STATUS_THRESHOLD <= servo_pos_dict[a] <= goal_positions_dict[a] + DXL_MOVING_STATUS_THRESHOLD):
                move_verdict.append(True)
            else:
                move_verdict.append(False)

        print(goal_positions_dict, servo_pos_dict)
        
        # if each servo is within the threshold for reaching the goal, the program can stop having it try moving
        if all(ele == True for ele in move_verdict):
            move = False
        else:
            move = True
            for servo in range(len(servoList)):
                if move_verdict[servo] == False:
                    is_set_goal = servoList[servo].set_goal_position(500)
                    while not is_set_goal:
                        is_set_goal = servoList[servo].set_goal_position(500)

    # Disable Dynamixel Torque
    for servo in servoList:
        is_set_torque = servo.set_torque_value(TORQUE_DISABLE)
        while not is_set_torque:
            is_set_torque = servo.set_torque_value(TORQUE_DISABLE)

    # print current positions
    for servo in servoList:
        get_current = servo.get_current_position()
        while get_current == False:
            get_current = servo.get_current_position()

    # Close port
    portHandler.closePort()

if __name__ == "__main__":
    main()
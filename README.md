# A Step-by-Step Guide to getting started with helping Mr. Krabs walk, Python edition

## Getting Dynamixel SDK on your computer

1. Clone the [Dynamixel SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/download/#repository) and put it in a place easy to access.

2. Open Terminal (or Command Prompt) and navigate to the location the folder is in.

3. Move into the Python folder and run the setup file with `python setup.py install` (for [Windows](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_windows/#python-windows)) or `sudo python setup.py install` (for [Linux](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_linux/#python-linux)). (there are no [Mac instructions](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_macos/#python-macos) as of writing this, though it's probably similar).

## Getting RoboPlus (more specifically, Dynamixel Wizard)

1. Going [here](https://en.robotis.com/service/downloadpage.php?ca_id=10), download **RoboPlus** (an issue here is that it might only be usable on Windows).

2. After installing the program, open Dynamixel Wizard and plug in the [U2D2](https://emanual.robotis.com/docs/en/parts/interface/u2d2/) to your computer.

3. Find the port that the U2D2 is using and, through the dropdown menu in the top left, select the port.

4. Using the 3-Pin Power hub thing, hook up each leg to it via daisy chain so that each leg is 3 servos and then it's connected back to the hub.

5. Power the servos with a power supply (or a battery, but that hasn't been figured out yet) by wiring it to the 3-Pin Power hub.
    - Note: when using the power supply, make sure the current it can use is dialed up to the highest setting and the Voltage output is 12.

6. Click the Open Port button (looks like a blue wire), select 1000000 as the baud rate, DXL 1.0, and then click Start searching. If done correctly, then each servo connected in a daisy chain to the power hub that the U2D2 is also hooked up to will show up with their respective IDs.

7. You can now change the IDs of the servos if needed (each needs a different ID number) as well as see the address table for the servo found [here](https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/#control-table-data-address).

## Running the Servo Test

1. Open the file, and change the `DEVICENAME` variable to match the U2D2 port.

2. You should be good to go if you installed the Dynamixel SDK and the servo IDs match what's in the file (if the IDs are changed, make the corresponding changes in the file).
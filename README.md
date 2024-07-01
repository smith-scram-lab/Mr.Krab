# A Step-by-Step Guide to getting started with helping Mr. Krabs walk, Python edition

The below process in its entirety only needs to be completed once in order for your computer to communicate with Mr. Krabs. After it has been done once, all that needs to be done is to plug in the U2D2 and turn on the power supply before running the code. Instructions for Raspberry Pi are also integrated into this guide.

## Getting Dynamixel SDK on your computer

1. Clone the [Dynamixel SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/download/#repository) and put it in a place easy to access. To get Dynamixel SDK on Raspberry Pi, run the following commands in the terminal:
    - `sudo apt install git`
    - `git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git`
    - `sudo apt install gcc`
    - `sudo apt install build-essential` 

    Then follow the remaining instructions for setting up Dynamixel SDK

2. Open Terminal (or Command Prompt) and navigate to the location the folder is in.

3. Move into the Python folder and run the setup file with `python setup.py install` (for [Windows](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_windows/#python-windows)) or `sudo python setup.py install` (for [Linux](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_linux/#python-linux)). There are no [Mac instructions](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_macos/#python-macos) as of writing this, though it's probably similar to Linux.

## Getting RoboPlus for Dynamixel Wizard

NOTE: This section is not necessary for Raspberry Pi. RoboPlus does not need to be installed for Dynamixel and U2D2 on Raspberry Pi.

1. Going [here](https://en.robotis.com/service/downloadpage.php?ca_id=10), download **RoboPlus** located close to the bottom of the page (if you don't use a Windows machine, you can use [DYNAMIXEL Wizard 2.0](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/). See below for more instructions for this software).

2. After installing the program, open RoboPlus and navigate to Dynamixel Wizard. Plug in the [U2D2](https://emanual.robotis.com/docs/en/parts/interface/u2d2/) into your computer.

![Port Select](imgs/u2d2.jpg)

<p style="text-align: center;"> <em> The U2D2 </em> </p>

3. Find the port that the U2D2 is using and, through the dropdown menu in the top left, select the port.

![Port Select](imgs/wiz1_port.png)

<p style="text-align: center;"> <em> Port Selection </em> </p>

   If "No Port" appears in dropdown menu:
   - Windows:
       - Open device manager. Select Ports Item. If Ports Item not appearing, open the View menu, select "show hidden devices, and port should appear. Double click to open any ports that appear in order to ensure the device has been configured.
       - With Port now appearing in device manager, the port should now be able to be selected in Dynamixel Wizard.  

4. Using the 3-Pin Power hub, hook up each leg to it via daisy chain so that each leg is 3 servos chained and then it's connected back to the hub.

![Port Select](imgs/3pin.jpg)

<p style="text-align: center;"> <em> Servos plugged into the Power Hubs </em> </p>

5. Power the servos with a power supply (or a battery, but that hasn't been figured out yet) by wiring it to the 3-Pin Power hub.
    - NOTE: when using the power supply, make sure the current it can use is dialed up to the highest setting and the Voltage output is 12. Low current makes it so that the servos aren't supplied enough power for each to move in close succession.

![Port Select](imgs/power.jpg)

<p style="text-align: center;"> <em> Power supply settings </em> </p>

![Port Select](imgs/set.jpg)

<p style="text-align: center;"> <em> Setup of the power hub and power supply </em> </p>

1. Click the Open Port button, select 1000000 as the baud rate, DXL 1.0, and then click "Start searching." If done correctly, then each servo connected in a daisy chain to the power hub that the U2D2 is also hooked up to (can also be further daisy chained to other hubs) will show up with their respective IDs.

![Port Select](imgs/wiz1_open.png)

<p style="text-align: center;"> <em> Port Open </em> </p>

![Port Select](imgs/wiz1_scan.png)

<p style="text-align: center;"> <em> Port Scan Settings </em> </p>

![Port Select](imgs/wiz1_scanned.png)

<p style="text-align: center;"> <em> Scan Results </em> </p>

7. You can now change the IDs of the servos if needed (each needs a different ID number) as well as see the address table for the servo found [here](https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/#control-table-data-address).

![Port Select](imgs/wiz1_id.png)

<p style="text-align: center;"> <em> Servo IDs </em> </p>

![Port Select](imgs/wiz1_table.png)

<p style="text-align: center;"> <em> Servo Address Table </em> </p>

8. Don't forget to close the port after finishing and before running the program as only 1 program can use the port at a time.

![Port Select](imgs/wiz1_close.png)

<p style="text-align: center;"> <em> Port Close </em> </p>

## Using DYNAMIXEL Wizard 2.0

NOTE: This section is not necessary for Raspberry Pi. Dynamixel Wizard does not need to be installed for Dynamixel and U2D2 on Raspberry Pi.

1. Download it for your OS at the same link as the one above and run the installer.

2. After opening, click on the gear to open settings.

![Port Select](imgs/wiz2_options.png)

<p style="text-align: center;"> <em> Options </em> </p>

3. Change the Protocol to 1.0, the Port the U2D2 is connected to and the baudrate to 1000000.

![Port Select](imgs/wiz2_options_set.png)

<p style="text-align: center;"> <em> Settings </em> </p>

4. Click Ok and then click the magnifying glass to start scanning.

![Port Select](imgs/wiz2_scan.png)

<p style="text-align: center;"> <em> Scan Button </em> </p>

5. Like the version of Dynamixel Wizard from RoboPlus, this allows you to see each servo's ID and to move them through click and drag. However this doesn't let you change the ID unless you reset the firmware.

![Port Select](imgs/wiz2_id.png)

<p style="text-align: center;"> <em> Servo IDs </em> </p>

![Port Select](imgs/wiz2_table.png)

<p style="text-align: center;"> <em> Servo Address Table </em> </p>

![Port Select](imgs/wiz2_close.png)

<p style="text-align: center;"> <em> Close Port </em> </p>

## Running the Servo Test in IDE

1. Open the file, and change the `DEVICENAME` variable to match the U2D2 port.
    - NOTE: the port being used for Raspberry Pi will **always** be `/dev/ttyUSB0` regardless of which port it is plugged into, as this is the shared name for all USB ports on Raspberry Pi.

2. You should be good to go if you installed the Dynamixel SDK and the servo IDs match what's in the file (if the IDs are changed, make the corresponding changes in the file).

3. Run in the terminal or by clicking the Run button in the IDE you're using.


## Running the Servo Test in SSH for Raspberry Pi

I recommend making following the steps for setting up laptop/PC connection before attempting Raspberry Pi so you can use Dynamixel Wizard to ensure that all servos are behaving as expected and being recognized properly. These softwares can't be used easily on Raspberry Pi and ultimately aren't necessary for overall functionality (RoboPlus and Dynamixel Wizard are x64 software and it is difficult to make this work on Raspbian OS, which uses ARM64 architecture. There are some hacks and clever ways to attempt to get around this, but I have found that it is overall not worth the effort and time investment when it isn't even strictly necessary). After you have done the steps for laptop/PC and all servos are behaving and being recognized correctly, you can run the code remotely on the Raspberry Pi using SSH

1. Establish an SSH connection with Raspberry Pi device using the device name, IP address, and passcode.

2. Plug in U2D2 into any of the Raspberry Pi USB ports

3. Open the file, and set the `DEVICENAME` variable to `/dev/ttyUSB0` 

4. You should be good to go if you installed the Dynamixel SDK. To ensure servo IDs match what's in the file and the servos respond as expected, **do not** make any changes to ID names in the file, because we can't alter servo names in Dynamixel Wizard

5. Run in the terminal or by clicking the Run button in the IDE you're using.



# import smbus
# import time

# bus_number = 1
# device_address = 0x48
# bus = smbus.SMBus(bus_number)

# def write_command(register, data):
#     bus.write_byte_data(device_address, register, data)
#     time.sleep(0.01)  


# def send_commands(mode_commands):
#     for command in mode_commands.split('\n'):
#         command = command.strip()
#         if command and not command.startswith(';') and not command.startswith('delay') and not command.startswith('End'):
#             if command.split()[0].isdigit(): 
#                 register, data = [int(x, 16) for x in command.strip().split(';')[0].strip().split()[1:]]
#                 print(register, data)
#                 write_command(register, data)



# # modes = [
# #     "Color Bars 576i MIPI Out:\ndelay 10 ;  \n42 0F 00 ; Exit Power Down Mode\n42 00 04 ; ADI Required Write \n42 0C 37 ; Force Free-run mode \n42 02 84 ; Force standard to PAL \n42 14 11 ; Set Free-run pattern to color bars \n42 03 4E ; ADI Required Write \n42 04 57 ; Power-up INTRQ pin\n42 13 00 ; Enable INTRQ output driver\n42 17 41 ; select SH1\n42 1D C0 ; Tri-State LLC output driver\n42 52 CB ; ADI Required Write\n42 80 51 ; ADI Required Write\n42 81 51 ; ADI Required Write\n42 82 68 ; ADI Required Write\n42 5D 3C ; Enable Diagnostic pin 1 - Level=1.125V\n42 5E 3C ; Enable Diagnostic pin 2 - Level=1.125V\n42 FE 88 ; Set CSI Map Address\n88 DE 02 ; Power up MIPI D-PHY\n88 D2 F7 ; ADI Required Write\n88 D8 65 ; ADI Required Write\n88 E0 09 ; ADI Required Write \n88 2C 00 ; ADI Required Write\n88 00 00 ; Power up MIPI CSI-2 Tx --done--\nEnd",
# #     "Color Bars 480i MIPI Out:\ndelay 10 ; \n42 0F 00 ; Exit Power Down Mode\n42 00 04 ; ADI Required Write \n42 0C 37 ; Force Free-run mode \n42 02 54 ; Force standard to NTSC-M \n42 14 11 ; Set Free-run pattern to color bars \n42 03 4E ; ADI Required Write \n42 04 57 ; Power-up INTRQ pin\n42 13 00 ; Enable INTRQ output driver\n42 17 41 ; select SH1\n42 1D C0 ; Tri-State LLC output driver\n42 52 CB ; ADI Required Write\n42 80 51 ; ADI Required Write\n42 81 51 ; ADI Required Write\n42 82 68 ; ADI Required Write\n42 5D 3C ; Enable Diagnostic pin 1 - Level=1.125V\n42 5E 3C ; Enable Diagnostic pin 2 - Level=1.125V\n42 FE 88 ; Set CSI Map Address\n88 DE 02 ; Power up MIPI D-PHY\n88 D2 F7 ; ADI Required Write\n88 D8 65 ; ADI Required Write\n88 E0 09 ; ADI Required Write \n88 2C 00 ; ADI Required Write\n88 00 00 ; Power up MIPI CSI-2 Tx --done--\nEnd",
# #     "Color Bars 576p MIPI Out:\ndelay 10 ;\n42 0F 00 ; Exit power down mode\n42 00 04 ; ADI Required Write \n42 0C 37 ; Force Free-run mode \n42 02 84 ; Force standard to PAL \n42 14 11 ; Set Free-run pattern to color bars\n42 03 4E ; ADI Required Write\n42 04 57 ; Enable Intrq pin\n42 13 00 ; Enable INTRQ output driver\n42 17 41 ; select SH1\n42 1D C0 ; Tri-State LLC output driver\n42 52 CB ; ADI Required Write\n42 80 51 ; ADI Required Write\n42 81 51 ; ADI Required Write\n42 82 68 ; ADI Required Write\n42 5D 3C ; Enable Diagnostic pin 1 - Level=1.125V\n42 5E 3C ; Enable Diagnostic pin 2 - Level=1.125V\n42 FD 84 ; Set VPP Map Address\n84 A3 00 ; ADI Required Write\n84 5B 00 ; Advanced Timing Enabled\n84 55 80 ; Enable I2P\n42 FE 88 ; Set CSI Map Address\n88 01 20 ; ADI Required Write\n88 02 28 ; ADI Required Write\n88 03 38 ; ADI Required Write\n88 04 30 ; ADI Required Write\n88 05 30 ; ADI Required Write\n88 06 80 ; ADI Required Write\n88 07 70 ; ADI Required Write\n88 08 50 ; ADI Required Write\n88 DE 02 ; Power up D-PHY\n88 D2 F7 ; ADI Required Write\n88 D8 65 ; ADI Required Write\n88 E0 09 ; ADI Required Write\n88 2C 00 ; ADI Required Write\n88 1D 80 ; ADI Required Write\n88 00 00 ; Power up MIPI CSI-2 Tx --done--\nEnd"
# # ]

# for mode in modes:
#     send_commands(mode)


import time
import smbus2

DEVICE_ADDRESS = 0x48
COMMAND_DELAY = 0

with open("/home/qt/Desktop/i2c_csi_transmit/ADV7282M_Cust-VER.4.5[1].txt", "r") as file:
    commands = file.readlines()

bus = smbus2.SMBus(1)

for command in commands:
    if not (command.startswith(";") or command.startswith("#") or command.startswith(":")):
        pass
    else:
        print(command)






    # command_bytes = [int(byte, 16) for byte in command.strip().split()]
    
    # for byte in command_bytes:
    #     bus.write_byte(DEVICE_ADDRESS, byte)
    #     print(DEVICE_ADDRESS, byte)
    #     time.sleep(COMMAND_DELAY)

bus.close()


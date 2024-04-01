import smbus
import time

bus_number = 1
bus = smbus.SMBus(bus_number)

def write_command(device_address, register, data):
    bus.write_byte_data(device_address, register, data) 
    time.sleep(0.01)  


def send_commands(mode_commands):
    for command in mode_commands.split('\n'):
        command = command.strip()
        if command and not command.startswith(';') and not command.startswith('delay') and not command.startswith('End'):
            if command.split()[0].isdigit():
                byte = command.strip().split(';')[0].strip().split()[1:]
                device_address = ''.join(command.strip().split(';')[0].strip().split()[0:1])
                register = byte[0]
                data = byte[1]
                print(device_address, register, data)
                # write_command(device_address, register, data)


modes = {"Color Bars 576i MIPI Out":""":Color Bars 576i MIPI Out:
delay 10 ; 	
42 0F 00 ; Exit Power Down Mode
42 00 04 ; ADI Required Write 
42 0C 37 ; Force Free-run mode 
42 02 84 ; Force standard to PAL 
42 14 11 ; Set Free-run pattern to color bars 
42 03 4E ; ADI Required Write 
42 04 57 ; Power-up INTRQ pin
42 13 00 ; Enable INTRQ output driver
42 17 41 ; select SH1
42 1D C0 ; Tri-State LLC output driver
42 52 CB ; ADI Required Write
42 80 51 ; ADI Required Write
42 81 51 ; ADI Required Write
42 82 68 ; ADI Required Write
42 5D 3C ; Enable Diagnostic pin 1 - Level=1.125V
42 5E 3C ; Enable Diagnostic pin 2 - Level=1.125V
42 FE 88 ; Set CSI Map Address
88 DE 02 ; Power up MIPI D-PHY
88 D2 F7 ; ADI Required Write
88 D8 65 ; ADI Required Write
88 E0 09 ; ADI Required Write 
88 2C 00 ; ADI Required Write
88 00 00 ; Power up MIPI CSI-2 Tx --done--
End""",
"CVBS Single Ended In Ain 1":""":AUTODETECT CVBS Single Ended In Ain 1, MIPI Out:
delay 10 ; 
42 0F 00 ; Exit Power Down Mode
42 00 00 ; INSEL = CVBS in on Ain 1
42 0E 80 ; ADI Required Write 
42 9C 00 ; ADI Required Write 
42 9C FF ; ADI Required Write 
42 0E 00 ; Enter User Sub Map
42 03 4E ; ADI Required Write 
42 04 57 ; Power-up INTRQ pin
42 13 00 ; Enable INTRQ output driver
42 17 41 ; select SH1
42 1D C0 ; Tri-State LLC output driver
42 52 CB ; ADI Required Write
42 80 51 ; ADI Required Write
42 81 51 ; ADI Required Write
42 82 68 ; ADI Required Write
42 5D 3C ; Enable Diagnostic pin 1 - Level=1.125V
42 5E 3C ; Enable Diagnostic pin 2 - Level=1.125V
42 FE 88 ; Set CSI Map Address
88 DE 02 ; Power up MIPI D-PHY
88 D2 F7 ; ADI Required Write
88 D8 65 ; ADI Required Write
88 E0 09 ; ADI Required Write 
88 2C 00 ; ADI Required Write
88 00 00 ; Power up MIPI CSI-2 Tx --done--
End""",
"CVBS Single Ended In Ain 2":"""AUTODETECT CVBS Single Ended In Ain 2, MIPI Out: 
delay 10 ; 
42 0F 00 ; Exit Power Down Mode
42 00 01 ; INSEL = CVBS in on Ain 2
42 0E 80 ; ADI Required Write 
42 9C 00 ; ADI Required Write 
42 9C FF ; ADI Required Write 
42 0E 00 ; Enter User Sub Map
42 03 4E ; ADI Required Write 
42 04 57 ; Enable Intrq pin
42 13 00 ; Enable INTRQ output driver
42 17 41 ; select SH1
42 1D C0 ; Tri-State LLC output driver
42 52 CB ; ADI Required Write
42 80 51 ; ADI Required Write
42 81 51 ; ADI Required Write
42 82 68 ; ADI Required Write
42 5D 3C ; Enable Diagnostic pin 1 - Level=1.125V
42 5E 3C ; Enable Diagnostic pin 2 - Level=1.125V
42 FE 88 ; Set CSI Map Address
88 DE 02 ; Power up MIPI D-PHY
88 D2 F7 ; ADI Required Write
88 D8 65 ; ADI Required Write
88 E0 09 ; ADI Required Write 
88 2C 00 ; ADI Required Write
88 00 00 ; Power up MIPI CSI-2 Tx --done--
End""",
"CVBS Single Ended In Ain 3":"""AUTODETECT CVBS Single Ended In Ain 3, MIPI Out: 
delay 10 ; 
42 0F 00 ; Exit Power Down Mode
42 00 02 ; INSEL = CVBS in on Ain 3
42 0E 80 ; ADI Required Write 
42 9C 00 ; ADI Required Write 
42 9C FF ; ADI Required Write 
42 0E 00 ; Enter User Sub Map
42 03 4E ; ADI Required Write 
42 04 57 ; Enable Intrq pin
42 13 00 ; Enable INTRQ output driver
42 17 41 ; select SH1
42 1D C0 ; Tri-State LLC output driver
42 52 CB ; ADI Required Write
42 80 51 ; ADI Required Write
42 81 51 ; ADI Required Write
42 82 68 ; ADI Required Write
42 5D 3C ; Enable Diagnostic pin 1 - Level=1.125V
42 5E 3C ; Enable Diagnostic pin 2 - Level=1.125V
42 FE 88 ; Set CSI Map Address
88 DE 02 ; Power up MIPI D-PHY
88 D2 F7 ; ADI Required Write
88 D8 65 ; ADI Required Write
88 E0 09 ; ADI Required Write 
88 2C 00 ; ADI Required Write
88 00 00 ; Power up MIPI CSI-2 Tx --done--
End""",
"CVBS Single Ended In Ain 4":"""AUTODETECT CVBS Single Ended In Ain 4, MIPI Out: 
delay 10 ; 
42 0F 00 ; Exit Power Down Mode
42 00 03 ; INSEL = CVBS in on Ain 4
42 0E 80 ; ADI Required Write 
42 9C 00 ; ADI Required Write 
42 9C FF ; ADI Required Write 
42 0E 00 ; Enter User Sub Map
42 03 4E ; ADI Required Write 
42 04 57 ; Enable Intrq pin
42 13 00 ; Enable INTRQ output driver
42 17 41 ; select SH1
42 1D C0 ; Tri-State LLC output driver
42 52 CB ; ADI Required Write
42 80 51 ; ADI Required Write
42 81 51 ; ADI Required Write
42 82 68 ; ADI Required Write
42 5D 3C ; Enable Diagnostic pin 1 - Level=1.125V
42 5E 3C ; Enable Diagnostic pin 2 - Level=1.125V
42 FE 88 ; Set CSI Map Address
88 DE 02 ; Power up MIPI D-PHY
88 D2 F7 ; ADI Required Write
88 D8 65 ; ADI Required Write
88 E0 09 ; ADI Required Write 
88 2C 00 ; ADI Required Write
88 00 00 ; Power up MIPI CSI-2 Tx --done--
End""",
}



print("Choose a mode:")
for idx, mode in enumerate(modes):
    print(f"{idx + 1}: {mode}")

selected_mode_index = int(input("Enter the mode number: ")) - 1
selected_mode = list(modes.keys())[selected_mode_index]

send_commands(modes[selected_mode])
### RpiSerial

**Purpose**: Provide a library for developers to interface serial devices like as GPS, RFID, GSM, Bluetooth, Fingerprint modules to Raspberry pi, jetson nano, banana pi, mango pi, etc..

**Author**: Ashish Sharma

**Licence**: MIT Licence

**Versions of Python supported**: 3.0+.

# Serial Device Interfacing Examples
**For Bluetooth**:
```from RpiSerial import RpiSerial as r
a = r.Bluetooth(port = "Your Port Number",baudrate = Your Baudrate)
# For Sending Message
a.write("Message you want to send")
# For Receive Message
x = a.read()
print(x)
```
**For RFID**:
```from RpiSerial import RpiSerial as r
a = r.RFID(port = "Your Port Number",baudrate = Your Baudrate)
# For Receive Message
x = a.read()
print(x)
```
**For GPS**:
```from RpiSerial import RpiSerial as r
a = r.GPS(port = "Your Port Number",baudrate = Your Baudrate)
# For Receiving Message
Latitude, Longitude, Time, Date = a.read() # Date and Time is in IST(Indian Standard Time) Format
print(Latitude, Longitude, Time, Date)
```
**For GSM**:
```from RpiSerial import RpiSerial as r
a = r.GSM(port = "Your Port Number",baudrate = Your Baudrate)
# For Sending Message
x = a.send_message("Contact Number","Message you want to send") # This Function is returned Acknowledgement
print(x) # Print Acknowledgement
# For Receiving Message
x = a.recv_message(Message Index Number stored in SIM Card) # This Function is returned Message for Example a.recv_message(0)
print(x) # Print Message
# For Making Call
x = a.call("Contact Number")   # This Function is returned Acknowledgement
print(x) # Print Acknowledgement
# For Sending AT Command
x = a.call("AT command with carriage return")   # This Function is returned Acknowledgement for giving AT command
print(x) # Print Acknowledgement
```

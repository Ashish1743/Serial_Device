import RPi.GPIO as r
import time as t
import serial
class LCD:
    def __init__(self,RS1,EN1,D4,D5,D6,D7):
        global a,li,RS,EN
        r.setmode(r.BOARD)
        r.setwarnings(False)
        li=[D4,D5,D6,D7]
        RS=RS1
        EN=EN1
        a=len(li)
        for i in range (0,a):
            r.setup(li[i],r.OUT)
        r.setup(RS,r.OUT)
        r.setup(EN,r.OUT)

        for i in range (0,a):
            r.output(li[i],0)
        r.output(RS,0)
        r.output(EN,0)        
        self.CMD(0x01)
        self.CMD(0x02)
        self.CMD(0x28)
        self.CMD(0x06)
        self.CMD(0x0c)
    def PORT(self,P):
        j=0x10
        for i in range (0,a):
            if((P & j)==j):
                r.output(li[i],1)
            else:
                r.output(li[i],0)
            j=j*2

    def CMD(self,C):
        P=(C & 0xF0)
        self.PORT(P)
        r.output(RS,0)
        r.output(EN,1)
        t.sleep(0.01)
        r.output(EN,0)

        P=((C<<4) & 0xF0)
        self.PORT(P)
        r.output(RS,0)
        r.output(EN,1)
        t.sleep(0.01)
        r.output(EN,0)
        
    def DATA(self,d):
        P=(d & 0xF0)
        self.PORT(P)
        r.output(RS,1)
        r.output(EN,1)
        t.sleep(0.01)
        r.output(EN,0)

        
        P=((d<<4) & 0xF0)
        self.PORT(P)
        r.output(RS,1)
        r.output(EN,1)
        t.sleep(0.01)
        r.output(EN,0)

    def data_as_string(self,loc,s):
        g=''
        g=s
        self.CMD(loc)
        for i in range(0,len(g)):
            self.DATA(ord(g[i]))
    def clear_screen(self):
        self.CMD(0x01)

class Bluetooth:
    def Bluetooth_init(self,port,boudrate):
        self.Bluetooth_data=serial.Serial(port,boudrate,timeout=0.5)
    def read(self):
        B_data = self.Bluetooth_data.readline().decode('utf-8')
        if B_data == '':
            pass
        else:
            return B_data
    def write(self,data):
        data = bytes(data.encode('utf-8'))
        self.Bluetooth_data.write(data)
        
class RFID:
    def RFID_init(self,port,boudrate):
        self.RFID_data=serial.Serial(port,boudrate,timeout=0.3)
    def read(self):
        B_data = self.RFID_data.readline().decode('utf-8')
        if B_data == '':
            pass
        else:
            return B_data

class GPS:
    def GPS_init(self,port,boudrate):
        self.GPS_data=serial.Serial(port,boudrate,timeout=0.5)
        
    def read(self):
        while True:
            try:
                GPS_recdata = self.GPS_data.readline().decode('utf-8')
                GPS_NEW_DATA=GPS_recdata.split(',')
                if '$GPRMC' in GPS_NEW_DATA:
                    Lat  = str(float(GPS_NEW_DATA[3])/100).split('.')
                    Lat1 = Lat[0]
                    Lat2 = str(int(int(Lat[1])/60))
                    Lat  = Lat1+'.'+Lat2
                    
                    Long = str(float(GPS_NEW_DATA[5])/100).split('.')
                    Long1 = Long[0]
                    Long2 = str(int(int(Long[1])/60))
                    Long  = Long1+'.'+Long2
                    
                    Time = str(int(float(GPS_NEW_DATA[1])))
                    Second = int(Time[-2::])
                    Minute = int(Time[-4:-2])+30
                    Hour   = int(Time[0:-4])+5
                    if Minute >= 60:
                        Minute = Minute-60
                        Hour = Hour+1
                    Time = str(Hour)+":"+str(Minute)+":"+str(Second)
                    
                    Date = GPS_NEW_DATA[9]
                    Date = Date[0:-4]+"/"+Date[-4:-2]+"/"+Date[-2::]
                    
                    return Lat,Long,Time,Date
                else:
                    pass
            except UnicodeDecodeError:
                pass       
##class FingerPrint:
##class GSM:


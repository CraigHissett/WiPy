from pyb import Timer
from pyb import Pin
from network import WLAN
from pyb import Sleep

def Setup_Pins()
# initialize GPIO7 and GPIO 8 in gpio mode (af=0) and make output
# These will be the standard pins required for motor control
LMotorB = Pin('GPIO7', af=0, mode=Pin.OUT)
RMotorB = Pin('GPIO8', af=0, mode=Pin.OUT)
LMotorB.low()
RMotorB.low()

# assign GPIO9 and 10 to alternate function 3 (PWM)
# These will be the pins to control speed
LMotorA = Pin('GPIO9', af=3, type=Pin.STD)
RMotorA = Pin('GPIO10', af=3, type=Pin.STD)

# Enable timer channels 3B and 4A for PWM pins
LMTimer = Timer(3, mode=Timer.PWM, width=16)
RMTimer = Timer(4, mode=Timer.PWM, width=16)
# enable channel A @1KHz with a 50% duty cycle
LMT_a = LMTimer.channel(Timer.B, freq=1000, duty_cycle=50)
RMT_a = RMTimer.channel(Timer.A, freq=1000, duty_cycle=50)

def Setup_WIFI()
wifi = WLAN(WLAN.STA)
# go for fixed IP settings
wifi.ifconfig('192.168.0.107', '255.255.255.0', '192.168.0.1', '8.8.8.8')
wifi.scan()     # scan for available netrworks
wifi.connect(ssid='mynetwork', security=2, key='mynetworkkey')
while not wifi.isconnected():
    pass
print(wifi.ifconfig())
# enable wake on WLAN
wifi.callback(wakes=Sleep.SUSPENDED)
# go to sleep
Sleep.suspend()
# now, connect to the FTP or the Telnet server and the WiPy will wake-up

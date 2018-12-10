'''
Upper level interface for Espec Corp. SCP220 Controllers

:copyright: (C) Espec North America, INC.
:license: MIT, see LICENSE for more details.
'''
from chamberconnectlibrary.scp220 import SCP220
from chamberconnectlibrary.especp300 import EspecP300

class EspecSCP220(EspecP300):
    '''
    A class for interfacing with Espec controllers (P300)

    Kwargs:
        interface (str): The connection method::
            "TCP" -- Use a Ethernet to serial adapter with raw TCP
            "Serial" -- Use a hardware serial port
        adr (int): The address of the controller (default=1)
        host (str): The hostname (IP address) of the controller when interface="TCP"
        serialport (str): The serial port to use when interface="Serial" (default=3(COM4))
        baudrate (int): The serial port's baud rate to use when interface="Serial" (default=9600)
        loops (int): The number of control loops the controller has (default=1, max=2)
        cascades (int): The number of cascade control loops the controller has (default=0, max=1)
        lock (RLock): The locking method to use when accessing the controller (default=RLock())
        freshness (int): The length of time (in seconds) a command is cached (default = 0)
    '''

    def __init__(self, **kwargs):
        super(EspecSCP220, self).__init__(**kwargs)
        ttp = (self.temp, self.humi)
        self.lp_exmsg = 'The SCP220 controller only supports 2 loops (%d:temperature,%d:humidity)' % ttp
        self.cs_exmsg = 'The SCP220 controller can only have loop %d as cascade' % self.temp
        self.total_programs = 30

    def connect(self):
        '''
        connect to the controller using the parameters provided on class initialization
        '''
        self.client = SCP220(self.interface, **self.connect_args)
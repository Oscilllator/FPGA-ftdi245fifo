#-*- coding:utf-8 -*-
# Python3
#
# This program is a test of FPGA+FTDI USB chips (FT232H, FT600, or FT601)
# It sends 16 bytes to FTDI chip. The FPGA immediately returns these data (loopback).
# The program will receive these bytes (they should be as same as the sended 16 bytes)
#
# The corresponding FPGA top-level design can be found in fpga_top_ft232h_loopback.v (if you are using FT232H or FT2232H chips)
#                                                   Or see fpga_top_ft600_loopback.v (if you are using an FT600 chip)
#

import os
# Add the directory containing libftd2xx.so to the library path
script_dir = os.path.dirname(os.path.abspath(__file__))
# lib_dir = os.path.join(script_dir, "release", "build")
lib_dir = script_dir
os.environ['LD_LIBRARY_PATH'] = lib_dir + ":" + os.environ.get('LD_LIBRARY_PATH', '')
print(f"Added {lib_dir} to LD_LIBRARY_PATH")
print(f"LD_LIBRARY_PATH: {os.environ['LD_LIBRARY_PATH']}")

# Explicitly set the library path for ctypes
from ctypes import CDLL
ftd2xx_lib = CDLL(os.path.join(lib_dir, "libftd2xx.so"))


from USB_FTX232H_FT60X import USB_FTX232H_FT60X_sync245mode          # see USB_FTX232H_FT60X.py



if __name__ == '__main__':
    
    usb = USB_FTX232H_FT60X_sync245mode(device_to_open_list =
        (('FTX232H', 'USB <-> Serial Converter'   ),           # firstly try to open FTX232H (FT232H or FT2232H) device named 'USB <-> Serial Converter'. Note that 'USB <-> Serial Converter' is the default name of FT232H or FT2232H chip unless the user has modified it. If the chip's name has been modified, you can use FT_Prog software to look up it.
         ('FT60X'  , 'FTDI SuperSpeed-FIFO Bridge'))           # secondly try to open FT60X (FT600 or FT601) device named 'FTDI SuperSpeed-FIFO Bridge'. Note that 'FTDI SuperSpeed-FIFO Bridge' is the default name of FT600 or FT601 chip unless the user has modified it.
    )
    
    
    data_send = b'0123456789abcdef' * 10
    txlen = usb.send(data_send)
    
    print(f"sending  {len(data_send)} bytes: {data_send}")
    data_recv = usb.recv(txlen + 1)
    
    print(f"received {len(data_recv)} bytes: {data_recv}")
    print([''.join(f"{x:08b}" for x in data_send)])
    print([''.join(f"{x:08b}" for x in data_recv[1:])])
    # xor send and receive:
    xor = [x^y for x,y in zip(data_send, data_recv[1:])]
    print((''.join(f"{x:08b}" for x in xor)).replace('0', '.'))


    usb.close()

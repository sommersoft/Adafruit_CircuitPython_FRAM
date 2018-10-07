## Simple Example For CircuitPython/Python SPI FRAM Library

import board
import adafruit_fram

## Create a FRAM object.
cs = board.D5
fram = adafruit_fram.FRAM_SPI(board.SCK, board.MOSI, board.MISO, cs)

## Write a single-byte value to register address '0'

fram.write_single(0, 1)

## Read that byte to ensure a proper write.
## Note: 'read()' returns a bytearray

print(fram.read(0)[1])

## Or write a sequential value, then read the values back.
## Note: 'read()' returns a bytearray. It also allocates
##       a buffer the size of 'length', which may cause
##       problems on memory-constrained platforms.

#values = list(range(100)) # or bytearray or tuple
#fram.write_sequence(0, values)
#fram.read(0, length=100)

import machine
import time

adc = machine.ADC(0)
uart = machine.UART(1, 9600)

while True:
    npcl = uart.readline()
    if npcl:
        npcl = int(npcl.strip())
        adc.atten(adc.ATTN_11DB) # set the input range from 0 to 3.3V
        adc.width(adc.WIDTH_12BIT) # set the ADC resolution to 12 bits
        adc.vref(3300) # set the reference voltage to 3.3V
        adc.dif_p_n(False)
        adc.np_cycles(npcl)
        voltage = adc.read()
        uart.write("{}\n".format(voltage))

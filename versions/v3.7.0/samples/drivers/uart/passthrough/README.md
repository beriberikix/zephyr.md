---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/uart/passthrough/README.html
original_path: samples/drivers/uart/passthrough/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# UART Passthrough

## Overview

This sample will virtually connect two UART interfaces together, as if Zephyr
and the processor were not present. Data read from the console is transmitted
to the “*other*” interface, and data read from the “*other*” interface is
relayed to the console.

The source code for this sample application can be found at:
[samples/drivers/uart/passthrough](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/uart/passthrough).

## Requirements

1. One UART interface, identified as Zephyr’s console.
2. A second UART connected to something interesting (e.g: GPS), identified as
   the chosen `uart,passthrough` device - the pins and baudrate will need to
   be configured correctly.

## Building and Running

Build and flash the sample as follows, changing `nucleo_l476rg` for your
board:

```shell
west build -b nucleo_l476rg samples/drivers/uart/passthrough
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build zephyr-v3.5.0-2988-gb84bab36b941 ***
Console Device: 0x8003940
Other Device:   0x800392c
$GNGSA,A,3,31,29,25,26,,,,,,,,,11.15,10.66,3.29,1*06
$GNGSA,A,3,,,,,,,,,,,,,11.15,10.66,3.29,2*0F
$GNGSA,A,3,,,,,,,,,,,,,11.15,10.66,3.29,3*0E
$GNGSA,A,3,,,,,,,,,,,,,11.15,10.66,3.29,4*09
$GNGSA,A,3,,,,,,,,,,,,,11.15,10.66,3.29,5*08
```

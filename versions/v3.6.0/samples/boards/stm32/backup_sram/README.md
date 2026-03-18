---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/boards/stm32/backup_sram/README.html
original_path: samples/boards/stm32/backup_sram/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# STM32 Backup SRAM

## Overview

Multiple STM32 microcontrollers have a small backup SRAM that can be used as a
NVM when VBAT pin is supplied with a voltage source, e.g. a coin button cell.

This example shows how to define a variable on the Backup SRAM. Each time the
application runs the current value is displayed and then incremented by one. If
VBAT is preserved, the incremented value will be shown on the next power-cycle.

Note

On most boards VBAT is typically connected to VDD thanks to a jumper.
To exercise this sample with an independent VBAT source, you will need to
remove the jumper.

## Building and Running

In order to run this sample, make sure to enable `backup_sram` node in your
board DT file.

```shell
west build -b nucleo_h743zi samples/boards/stm32/backup_sram
```

### Sample Output

```shell
Current value in backup SRAM: 11
Next reported value should be: 12
Keep VBAT power source and reset the board now!
```

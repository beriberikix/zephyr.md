---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/ti/cc13x2_cc26x2/system_off/README.html
original_path: samples/boards/ti/cc13x2_cc26x2/system_off/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# cc13x2\_cc26x2 System Off demo

## Overview

This sample can be used for basic power measurement and as an example of
the various sleep modes on TI CC13x2/CC26x2 platforms. The functional
behavior is:

- Busy-wait for 5 seconds
- Sleep for 2 milliseconds (Idle mode)
- Sleep for 3 seconds (Standby mode)
- Turn the system off after enabling wakeup through a button press
  (Shutdown mode)

A power monitor (e.g. [EnergyTrace](http://www.ti.com/tool/ENERGYTRACE))
can be used to distinguish among these states.

## Requirements

This application uses the CC13x2/CC26x2 LaunchPad for the demo.

## Building, Flashing and Running

```shell
west build -b cc1352r1_launchxl samples/boards/ti/cc13x2_cc26x2/system_off
west flash
```

After flashing the device, run the code:

1. Unplug the USB cable from the LaunchPad and reconnect it to fully
   power-cycle it.
2. Open UART terminal.
3. Hit the Reset button on the LaunchPad.
4. Device will turn off the external flash, which is on by default, to
   reduce power consumption.
5. Device will demonstrate active, idle and standby modes.
6. Device will explicitly turn itself off by going into shutdown mode.
   Press Button 1 to wake the device and restart the application as if
   it had been powered back on.

### Sample Output

#### cc1352rl\_launchxl output

```shell
*** Booting Zephyr OS build zephyr-v2.2.0-664-gd774727cc66e  ***

cc1352r1_launchxl system off demo
Busy-wait 5 s
Sleep 2000 us (IDLE)
Sleep 3 s (STANDBY)
Entering system off (SHUTDOWN); press BUTTON1 to restart
```

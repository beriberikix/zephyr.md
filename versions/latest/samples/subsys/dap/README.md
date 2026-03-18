---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/dap/README.html
original_path: samples/subsys/dap/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# DAP Sample Application

## Overview

This sample app demonstrates use of a SWDP interface driver and CMSIS DAP
controller through USB Bulk interface.

## Requirements

This sample supports multiple hardware configurations:

The simplest configuration would be to connect SWDIO to dio, SWDCLK to clk
and optionally nRESET to reset. The optional noe pin is used to enable the port,
e.g. if the SWD connections are multiplexed.

## Building and Running

In order for our debug adapter to be recognized by pyOCD we need to change
Zephyr’s VID/PID to IDs known to pyOCD, this is up to the user.
The following commands build and flash DAP sample.

```shell
west build -b nrf52840dk_nrf52840 samples/subsys/dap
west flash
```

Connect HIC to the target and try some pyOCD commands, for example:

```shell
pyocd commander -t nrf52840

0029527 W Board ID FE5D is not recognized [mbed_board]
Connected to NRF52840 [Sleeping]: FE5D244DFE1F33DB
pyocd> read32 0x20004f18 32
20004f18:  20001160 2000244c 00000000 0000e407    | ..` .$L........|
20004f28:  ffffffff ffffffff 00000000 aaaaaaaa    |................|
pyocd> halt
Successfully halted device
pyocd> reg
general registers:
      lr: 0x00009cdd                   r7: 0x00000000 (0)
      pc: 0x000033ca                   r8: 0x00000000 (0)
      r0: 0x00000000 (0)               r9: 0x00000000 (0)
      r1: 0x20002854 (536881236)      r10: 0x00000000 (0)
      r2: 0x20000be4 (536873956)      r11: 0x00000000 (0)
      r3: 0x00000000 (0)              r12: 0x00000000 (0)
      r4: 0x200017e8 (536877032)       sp: 0x20002898
      r5: 0x20001867 (536877159)     xpsr: 0x61000000 (1627389952)
      r6: 0x00000000 (0)
```

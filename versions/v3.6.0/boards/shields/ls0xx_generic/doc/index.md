---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/ls0xx_generic/doc/index.html
original_path: boards/shields/ls0xx_generic/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Sharp memory display generic shield

## Overview

This is a generic shield for Sharp memory pixel LCD. It supports
displays of LS0XX type. These displays have an SPI interface and
few other pins. Note that the SCS is active high for this display.

The DISP pin controls whether to display memory
contents or show all white pixels, this can be connected
directly to VDD, to always display memory contents or connected
to a gpio. If devicetree contains `disp-en-gpios` then it will be set to
high during driver initialization. Display blanking apis can be used
to control it.

Sharp memory displays require toggling the VCOM signal periodically
to prevent a DC bias occurring in the panel as mentioned in the [appnote](https://www.sharpsma.com/documents/1468207/1485747/Memory+LCD+Theory%2C+Programming%2C+and+Interfaces) [[1]](#id1)
and [datasheet](https://www.mouser.com/datasheet/2/365/LS013B7DH03%20SPEC_SMA-224806.pdf) [[2]](#id3). The DC bias can damage the LCD and reduce the life.
This signal must be supplied from either serial input (sw) or an external
signal on the EXTCOMIN pin.

Currently the driver only supports VCOM toggling using the EXTCOMIN pin
(EXTMODE pin is connected to VDD).
When `extcomin-gpios` is defined, driver starts a thread which will
toggle EXTCOMIN at `extcomin-frequency` frequency. Higher frequency
gives better contrast while lower frequency saves power.

To use a different method of toggling for example pwm, user may not
define `extcomin-gpios` and implement their preferred method in
application code.

### Pins Assignment of the Generic Sharp memory Display Shield

| Pin | Function |
| --- | --- |
| SCS | Serial Slave Select |
| SI | Serial Data Input |
| SCLK | Serial Clock Input |
| EXTCOMIN | VCOM Inversion Polarity Input (VCOM can be controlled through SW) |
| DISP | Display ON/OFF switching signal (Can be connected directly to VDD) |
| EXTMODE | COM Inversion Selection |

### Current supported displays

Following displays are supported but shield only exists
for LS013B7DH03. Other shields can be added by using the LS013B7DH03 as
a reference and changing the width, height, etc configurations.

LS012B7DD01
LS012B7DD06
LS013B7DH03
LS013B7DH05
LS013B7DH06
LS027B7DH01A
LS032B7DD02
LS044Q7DH01

| Display | Shield Designation |
| --- | --- |
| LS013B7DH03 | ls013b7dh03 |

## Requirements

This shield can only be used with a board that provides a configuration
for Arduino connectors and defines node aliases for SPI and GPIO interfaces
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `-DSHIELD=ls013b7dh03` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk_nrf52840 samples/subsys/display/lvgl -- -DSHIELD=ls013b7dh03
```

## References

[[1](#id2)]

[https://www.sharpsma.com/documents/1468207/1485747/Memory+LCD+Theory%2C+Programming%2C+and+Interfaces](https://www.sharpsma.com/documents/1468207/1485747/Memory+LCD+Theory%2C+Programming%2C+and+Interfaces)

[[2](#id4)]

[https://www.mouser.com/datasheet/2/365/LS013B7DH03%20SPEC\_SMA-224806.pdf](https://www.mouser.com/datasheet/2/365/LS013B7DH03%20SPEC_SMA-224806.pdf)

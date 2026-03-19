---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/seeed/wio_terminal/doc/index.html
original_path: boards/seeed/wio_terminal/doc/index.html
---

# Wio Terminal

Board Overview

[![../../../../_images/wio_terminal.png](../../../../_images/wio_terminal.png)
](../../../../_images/wio_terminal.png)

Wio Terminal

Name:
:   `wio_terminal`

Vendor:
:   Seeed Technology Co., Ltd

Architecture:
:   arm

SoC:
:   samd51p19a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/seeed/wio_terminal/doc/index.rst/../..)

## Overview

The Wio Terminal is a small (72 mm x 57 mm x 12 mm) and powerful ARM board with
wireless connectivity (2.4G/5G dual-band Wi-Fi and BLE 5.0), LCD display,
USB C port, FPC connector, microSD card slot, Raspberry Pi compatible 40-pins
header and 2 Grove connectors.

## Hardware

- ATSAMD51P19 ARM Cortex-M4F processor at 120 MHz
- 512 KiB flash memory and 192 KiB of RAM
- 4 MiB external flash
- MicroSD card slot
- RTL8720DN 2.4G/5G Dual Bands Wireless and BLE5.0 Combo Module
- 2.4inch LCD display
- LIS3DH accelerometer
- Microphone 1.0V-10V -42dB
- Speaker ≥78dB @10cm 4000Hz
- Light Sensor 400-1050nm
- Infrared Emitter 940nm
- GPIO 40 pin (Raspberry Pi compatible)
- 2x Grove connectors
- 1x user LED
- 3x user buttons
- 5-way user button
- Power/Reset/Boot mode switch
- Native USB port

### Supported Features

The `wio_terminal` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

Zephyr can use the default Cortex-M SYSTICK timer or the SAM0 specific RTC.
To use the RTC, set `CONFIG_CORTEX_M_SYSTICK=n` and set
[`CONFIG_SYS_CLOCK_TICKS_PER_SEC`](../../../../kconfig.md#CONFIG_SYS_CLOCK_TICKS_PER_SEC "CONFIG_SYS_CLOCK_TICKS_PER_SEC") to no more than 32 kHZ divided
by 7, i.e. no more than 4500.

### Connections and IOs

The [Wio Terminal Getting started guide](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/) [[1]](#id2) has detailed information about the
board including [pinouts](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#pinout-diagram) [[2]](#id4) and its [schematics](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#resources) [[3]](#id6).

### System Clock

The SAMD51 MCU is configured to use the 32.768 kHz internal oscillator with the
on-chip PLL generating the 120 MHz system clock.

### Serial Port

Zephyr console output is available using the USB connector, which is used to
make the console available on PC as USB CDC class.

### USB Device Port

The SAMD51 MCU has a USB device port that can be used to communicate with a
host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for more, such as the
[USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which sets up a virtual serial port that echos
characters back to the host PC.

## Programming and Debugging

The Wio Terminal ships with an UF2 bootloader that is BOSSA compatible. The
bootloader can be entered by quickly tapping the reset button twice.

The UF2 file is generated when building the application, and it is possible to
use it to flash the target. Enter the bootloader by quickly sliding the power
button twice, and copy the UF2 file to the USB mass storage device. The device
reboots on the new firmware after the UF2 file has finished transferring.

### Flashing

1. Build the Zephyr kernel and the `button` sample application:

   ```shell
   west build -b wio_terminal samples/basic/button
   ```
2. Swipe the reset/power button down twice quickly to enter bootloader mode
3. Flash the image:

   ```shell
   west build -b wio_terminal samples/basic/button
   west flash
   ```

   You should see the blue (user) LED flashing whenever you press the third
   (counting from the top left) user button at the top of the Wio Terminal.

### Debugging

In addition to the built-in bootloader, the Wio Terminal can be flashed and
debugged using an SWD probe such as the Segger J-Link.

1. Solder cables to the `SWCLK`, `SWDIO`, `RESET`,
   `GND`, and `3V3` pins. See [Test with SWD](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#test-with-swd) [[4]](#id8) for more
   information.
2. Connect the board to the probe by connecting the `SWCLK`,
   `SWDIO`, `RESET`, `GND`, and `3V3` pins on the
   Wio Terminal to the `SWCLK`, `SWDIO`, `RESET`,
   `GND`, and `VTref` pins on the [J-Link](https://www.segger.com/products/debug-probes/j-link/technology/interface-description/) [[5]](#id10).
3. Flash the image:

   ```shell
   west build -b wio_terminal samples/basic/button
   west flash -r openocd
   ```
4. Start debugging:

   ```shell
   west build -b wio_terminal samples/basic/button
   west debug
   ```

## References

[[1](#id3)]

[https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/)

[[2](#id5)]

[https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#pinout-diagram](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#pinout-diagram)

[[3](#id7)]

[https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#resources](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#resources)

[[4](#id9)]

[https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#test-with-swd](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#test-with-swd)

[[5](#id11)]

[https://www.segger.com/products/debug-probes/j-link/technology/interface-description/](https://www.segger.com/products/debug-probes/j-link/technology/interface-description/)

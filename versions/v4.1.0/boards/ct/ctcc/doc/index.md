---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ct/ctcc/doc/index.html
original_path: boards/ct/ctcc/doc/index.html
---

# CTHINGS.CO Connectivity Card

Board Overview

[![../../../../_images/ctcc_nrf52840_m2.webp](../../../../_images/ctcc_nrf52840_m2.webp)
](../../../../_images/ctcc_nrf52840_m2.webp)

CTHINGS.CO Connectivity Card

Name:
:   `ctcc`

Vendor:
:   CTHINGS.CO

Architecture:
:   arm

SoC:
:   nrf9161, nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ct/ctcc/doc/index.rst/../..)

## Overview

Connectivity Cards come with either M.2 or mPCIe form factor with various SoCs, enabling different
radio interfaces.

- The Connectivity Card nRF52840 enables BLE and IEEE 802.15.4 over mPCIe or M.2
  using USB device with on-board nRF52840 SoC
- The Connectivity Card nRF9161 enables LTE-M/NB-IoT and DECT NR+ over mPCIe or M.2
  using on-board USB-UART converter

Connectivity Card has following features:

- CLOCK
- FLASH
- GPIO
- MPU
- NVIC
- RADIO (Bluetooth Low Energy and 802.15.4) (only nRF52840)
- RADIO (LTE-M/NB-IoT and DECT NR+) (only nRF9161)
- RTC
- USB (only nRF52840)
- UARTE (only nRF9161)
- WDT

![CTCC nRF52840 mPCIe](../../../../_images/ctcc_nrf52840_mpcie.webp)

ctcc/nrf52840 mPCie board

![CTCC nRF52840 M.2](../../../../_images/ctcc_nrf52840_m21.webp)

ctcc/nrf52840 M.2 board

![CTCC nRF9161 mPCIe](../../../../_images/ctcc_nrf9161_mpcie.webp)

ctcc/nrf9161 mPCIe board

More information about the board can be found at the
[Connectivity Cards Website](https://cthings.co/products/connectivity-cards) [[1]](#id5) and for SoC information: [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id7).

## Hardware

- The `ctcc/nrf52840` board target has one external oscillator of the 32.768 kHz.
- The `ctcc/nrf9161` board target has one external SPI NOR 64Mbit memory and one on-board USB-UART
  converter (CP210X).

### Supported Features

The `ctcc` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

#### LED

Note that boards do not have on-board LEDs, however they expose
LED signals on mPCIe/M.2 pins.

nRF52840:

- LED1 = P0.23
- LED2 = P0.22

nRF9161:

- LED1 = P0.11
- LED2 = P0.12

## Programming and Debugging

Applications for `ctcc` boards can be
built in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) for more details).

### Flashing

The board supports the following programming options:

1. Using an external [debug probe](../../../../develop/flash_debug/probes.md#debug-probes)
2. Using [MCUboot](https://github.com/zephyrproject-rtos/mcuboot) [[3]](#id9) with MCUmgr support

Below instructions are provided for `ctcc/nrf52840`, to use `nrf9161` target, the USB device configs have
to be replaced with UART configurations.

#### Option 1: Using an External Debug Probe

Connectivity Card can be programmed using an external debug probe (Segger J-Link) by connecting
to on-board SWD test pads.

For Segger J-Link debug probes, follow the instructions in the
[Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install and configure all the necessary
software. Further information can be found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing).

Then build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Console over USB CDC ACM](../../../../samples/subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.") application which prints out
logs on emulated USB port.

```shell
# From the root of the zephyr repository
west build -b ctcc/nrf52840 samples/subsys/usb/console
west flash
```

#### Option 2: Using MCUboot with MCUmgr support

It is also possible to use the MCUboot bootloader with [MCUmgr](../../../../services/device_mgmt/mcumgr.md#mcu-mgr) support to flash
Zephyr applications.

Install a MCUmgr-compatible tool from [supported list](../../../../services/device_mgmt/mcumgr.md#mcumgr-tools-libraries)
and make sure MCUboot’s `imgtool` is available for signing your binary
for MCUboot as described on [Signing Binaries](../../../../develop/west/sign.md#west-sign).

1. Compile MCUboot as a Zephyr application with `MCUmgr` support.

   nRF52840nRF9161

   To build the MCUboot:

   ```shell
   west build -b ctcc/nrf52840 -d build/mcuboot mcuboot/boot/zephyr
   ```

   To build the MCUboot:

   ```shell
   west build -b ctcc/nrf9161 -d build/mcuboot mcuboot/boot/zephyr
   ```
2. Flash it onto the board as described in Option 1.
3. Flash other Zephyr application over USB using [MCUmgr-compatible tool](../../../../services/device_mgmt/mcumgr.md#mcumgr-tools-libraries) and reset target to boot into the image.

   nRF52840nRF9161

   Build the blinky example with MCUboot support:

   ```shell
   # From the root of the zephyr repository
   west build -b ctcc/nrf52840 samples/basic/blinky -- -DCONFIG_BOOTLOADER_MCUBOOT=y -DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE=\"path/to/mcuboot/boot/root-rsa-2048.pem\"
   ```

   Build the blinky example with MCUboot support:

   ```shell
   # From the root of the zephyr repository
   west build -b ctcc/nrf9161 samples/basic/blinky -- -DCONFIG_BOOTLOADER_MCUBOOT=y -DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE=\"path/to/mcuboot/boot/root-rsa-2048.pem\"
   ```

Note

In all examples it is assumed to use default `root-rsa-2048.pem` file from `mcuboot/boot`
directory. Providing certificate in build args produces signed binary automatically.
Do not use this certificate in your production firmware!

### Debugging

These boards do not have an on-board J-Link debug IC, however
instructions from the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page also apply to them,
with the additional step of connecting an external debugger.

To test flashed software, plug in `ctcc` card to mPCIe/M.2 slot or use mPCIe/M.2 adapter to USB and plug such adapter to USB port.

> - For `ctcc/nrf52840` check on Linux system by entering `lsusb` command if the following device appears: `NordicSemiconductor MCUBOOT` or `NordicSemiconductor USB-DEV` (when booted into blinky example).
> - For `ctcc/nrf9161` it’s not possible to see a change in `lsusb` due to the on-board USB-UART converter. Intead, connect to the UART console using a terminal emulation program of your choice.

## References

[[1](#id6)]

[https://cthings.co/products/connectivity-cards](https://cthings.co/products/connectivity-cards)

[[2](#id8)]

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)

[[3](#id10)]

[https://github.com/zephyrproject-rtos/mcuboot](https://github.com/zephyrproject-rtos/mcuboot)

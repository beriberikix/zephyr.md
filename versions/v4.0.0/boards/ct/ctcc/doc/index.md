---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/ct/ctcc/doc/index.html
original_path: boards/ct/ctcc/doc/index.html
---

# Connectivity Card nRF52840

Board Overview

[![../../../../_images/ctcc_nrf52840_m2.webp](../../../../_images/ctcc_nrf52840_m2.webp)
](../../../../_images/ctcc_nrf52840_m2.webp)

Connectivity Card nRF52840

Vendor:
:   CTHINGS.CO

Architecture:
:   arm

SoC:
:   nrf52840

## Overview

The Connectivity Card nRF52840 enables BLE and IEEE 802.15.4 connectivity
over mPCIe or M.2 using USB port with on-board nRF52840 SoC.

This board has following features:

- CLOCK
- FLASH
- GPIO
- MPU
- NVIC
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- USB
- WDT

![CTCC nRF52840 mPCIe](../../../../_images/ctcc_nrf52840_mpcie.webp)

ctcc/nrf52840 mPCie board

![CTCC nRF52840 M.2](../../../../_images/ctcc_nrf52840_m21.webp)

ctcc/nrf52840 M.2 board

More information about the board can be found at the
[ctcc\_nrf52840 Website](https://cthings.co/products/connectivity-cards) [[1]](#id4) and for SoC information: [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id6).

## Hardware

The `ctcc/nrf52840` board target has one external oscillator of the 32.768 kHz.

### Supported Features

The `ctcc/nrf52840` board target supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| RADIO | on-chip | Bluetooth, ieee802154 |
| RTC | on-chip | system clock |
| USB | on-chip | usb |
| WDT | on-chip | watchdog |

### Connections and IOs

#### LED

Note that board does not have on-board LEDs, however it exposes
LED signals on mPCIe/M.2 pins.

- LED1 = P0.23
- LED2 = P0.22

## Programming and Debugging

Applications for the `ctcc/nrf52840` board target can be
built in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) for more details).

### Flashing

The board supports the following programming options:

1. Using an external [debug probe](../../../../develop/flash_debug/probes.md#debug-probes)
2. Using MCUboot with DFU support

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

### Debugging

The `ctcc/nrf52840` board target does not have an on-board J-Link debug IC, however
instructions from the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page also apply to this board,
with the additional step of connecting an external debugger.

#### Option 2: Using MCUboot with DFU support

It is also possible to use the MCUboot bootloader with DFU support to flash
Zephyr applications. You need to flash MCUboot with DFU support and fill in slot0 with
some application one-time using Option 1. Then you can re-flash an application using DFU utility
by loading images to slot1. Note, it’s not possible to have only MCUboot and load directly
software to slot0 due to DFU implementation in Zephyr, which for present slot0 and slot1 in flash
map, it assumes only slot1 partition as writeable.

Install `dfu-util` first and make sure MCUboot’s `imgtool` is
available for signing your binary for MCUboot as described on [Signing Binaries](../../../../develop/west/sign.md#west-sign).

Next, do the **one-time setup** to flash MCUboot with DFU support.
We’ll assume you’ve cloned the [MCUboot](https://github.com/JuulLabs-OSS/mcuboot) [[3]](#id8) as a submodule when initializing
Zephyr repositories using [West (Zephyr’s meta-tool)](../../../../develop/west/index.md#west) tool.

1. Compile MCUboot as a Zephyr application with DFU support.

   ```shell
   west build -b ctcc/nrf52840 -d build/mcuboot mcuboot/boot/zephyr -- -DCONFIG_BOOT_USB_DFU_WAIT=y
   ```
2. Flash it onto the board as described in Option 1.
3. Flash other Zephyr application to fill in slot0 e.g:

   ```shell
   # From the root of the zephyr repository
   west build -b ctcc/nrf52840 -d build/dfu samples/subsys/usb/dfu -- -DCONFIG_BOOTLOADER_MCUBOOT=y -DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE=\"path/to/mcuboot/boot/root-rsa-2048.pem\"
   ```

You can now flash a Zephyr application to the board using DFU util.
As an example we’ll use the [Console over USB CDC ACM](../../../../samples/subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.") sample.

> ```shell
> # From the root of the zephyr repository
> west build -b ctcc/nrf52840 samples/subsys/usb/console -- -DCONFIG_BOOTLOADER_MCUBOOT=y -DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE=\"path/to/mcuboot/boot/root-rsa-2048.pem\"
> west flash
> ```

Note

In all examples it is assumed to use default `root-rsa-2048.pem` file from `mcuboot/boot`
directory. Providing certificate in build args produces signed binary automatically.
Do not use this certificate in your production firmware!

1. Plug in `ctcc/nrf52840` card to mPCIe/M.2 slot or use mPCIe/M.2 adapter to USB
   and plug such adapter to USB port.

   You should see `NordicSemiconductor MCUBOOT` or `NordicSemiconductor Zephyr DFU sample`
   (if you flashed `dfu` sample to slot0) device once plugging it into host
   USB port. You can check that on Linux system by entering `lsusb` command.

   To check if DFU device is visible you can enter `sudo dfu-util -l` command. Once the
   device is visible you can flash Zephyr image using DFU util: `sudo dfu-util --alt 1 --download build/zephyr/zephyr.signed.bin`

## References

[[1](#id5)]

[https://cthings.co/products/connectivity-cards](https://cthings.co/products/connectivity-cards)

[[2](#id7)]

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)

[[3](#id9)]

[https://github.com/JuulLabs-OSS/mcuboot](https://github.com/JuulLabs-OSS/mcuboot)

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/nrf52840dongle_nrf52840/doc/index.html
original_path: boards/arm/nrf52840dongle_nrf52840/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nRF52840 Dongle

## Overview

The nRF52840 Dongle (PCA10059) hardware provides support for the Nordic
Semiconductor nRF52840 ARM Cortex-M4F CPU and the following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- SPI
- UART
- USB
- WDT

![nRF52840 Dongle](../../../../_images/nrf52840dongle_nrf52840.jpg)

nRF52840 Dongle

More information about the board can be found at the
[nRF52840 Dongle website](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-Dongle) [[1]](#id2). The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
contains the processor’s information and the datasheet.

## Hardware

The `nrf52840dongle_nrf52840` has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 32 MHz.

### Supported Features

The `nrf52840dongle_nrf52840` board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| ADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| I2C(M) | on-chip | i2c |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| PWM | on-chip | pwm |
| RADIO | on-chip | Bluetooth, ieee802154 |
| RTC | on-chip | system clock |
| SPI(M/S) | on-chip | spi |
| UART | on-chip | serial |
| USB | on-chip | usb |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.
See [nRF52840 Dongle website](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-Dongle) [[1]](#id2) and [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
for a complete list of nRF52840 Dongle board hardware features.

### Connections and IOs

#### LED

- LED0 (green) = P0.6
- LED1 (red) = P0.8
- LED1 (green) = P1.9
- LED1 (blue) = P0.12

#### Push buttons

- BUTTON1 = SW1 = P1.6
- RESET = SW2 = P0.18

## Programming and Debugging

Applications for the `nrf52840dongle_nrf52840` board configuration can be
built in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) for more details).

### Flashing

The board supports the following programming options:

1. Using the built-in bootloader only
2. Using MCUboot in serial recovery mode
3. Using an external [debug probe](../../../../develop/flash_debug/probes.md#debug-probes)

These instructions use the [west](../../../../develop/west/index.md#west) tool and assume you are in the
root directory of your [west installation](../../../../glossary.md#term-west-installation).

#### Option 1: Using the Built-In Bootloader Only

The board is factory-programmed with Nordic’s bootloader from Nordic’s nRF5
SDK. With this option, you’ll use Nordic’s [nrfutil](https://github.com/NordicSemiconductor/pc-nrfutil) [[4]](#id10) program to create
firmware packages supported by this bootloader and flash them to the
device. Make sure `nrfutil` is installed before proceeding.

1. Reset the board into the Nordic bootloader by pressing the RESET button.

   The push button is on the far side of the board from the USB connector. Note
   that the button does not face up. You will have to push it from the outside
   in, towards the USB connector:

   ![Location of RESET button and direction of push](../../../../_images/nRF52840_dongle_press_reset.svg)

   The red LED should start a fade pattern, signalling the bootloader is
   running.
2. Compile a Zephyr application; we’ll use [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.").

   ```shell
   west build -b nrf52840dongle_nrf52840 zephyr/samples/basic/blinky
   ```
3. Package the application for the bootloader using `nrfutil`:

   ```shell
   nrfutil pkg generate --hw-version 52 --sd-req=0x00 \
           --application build/zephyr/zephyr.hex \
           --application-version 1 blinky.zip
   ```
4. Flash it onto the board. Note `/dev/ttyACM0` is for Linux; it will be
   something like `COMx` on Windows, and something else on macOS.

   ```shell
   nrfutil dfu usb-serial -pkg blinky.zip -p /dev/ttyACM0
   ```

   When this command exits, observe the green LED on the board blinking,
   instead of the red LED used by the bootloader.

For more information, see [Nordic Semiconductor USB DFU](https://infocenter.nordicsemi.com/index.jsp?topic=%2Fcom.nordic.infocenter.sdk5.v15.2.0%2Fsdk_app_serial_dfu_bootloader.html) [[3]](#id8).

#### Option 2: Using MCUboot in Serial Recovery Mode

It is also possible to use the MCUboot bootloader with this board to flash
Zephyr applications. You need to do some one-time set-up to build and flash
MCUboot on your board. From that point on, you can build and flash other Zephyr
applications using MCUboot’s serial recovery mode. This process does not
overwrite the built-in Nordic bootloader, so you can always go back to using
Option 1 later.

Install [nrfutil](https://github.com/NordicSemiconductor/pc-nrfutil) [[4]](#id10) and [mcumgr](https://github.com/apache/mynewt-mcumgr-cli) [[6]](#id15) first, and make sure MCUboot’s `imgtool` is
available for signing your binary for MCUboot as described on [Signing Binaries](../../../../develop/west/sign.md#west-sign).

Next, do the **one-time setup** to flash MCUboot. We’ll assume you’ve cloned
the [MCUboot](https://github.com/JuulLabs-OSS/mcuboot) [[5]](#id13) repository into the directory `mcuboot`, and that it is next
to the zephyr repository on your computer.

1. Reset the board into the Nordic bootloader as described above.
2. Compile MCUboot as a Zephyr application.

   ```shell
   west build -b nrf52840dongle_nrf52840 -d build/mcuboot mcuboot/boot/zephyr
   ```
3. Package the application for the bootloader using `nrfutil`:

   ```shell
   nrfutil pkg generate --hw-version 52 --sd-req=0x00 \
           --application build/mcuboot/zephyr/zephyr.hex \
           --application-version 1 mcuboot.zip
   ```
4. Flash it onto the board. Note `/dev/ttyACM0` is for Linux; it will be
   something like `COMx` on Windows, and something else on macOS.

   ```shell
   nrfutil dfu usb-serial -pkg mcuboot.zip -p /dev/ttyACM0
   ```

You can now flash a Zephyr application to the board using MCUboot’s serial
recovery mode. We’ll use the [SMP server](../../../../samples/subsys/mgmt/mcumgr/smp_svr/README.md#smp-svr "Implement a Simple Management Protocol (SMP) server.") sample since it’s ready to be
compiled for chain-loading by MCUboot (and itself supports firmware updates
over Bluetooth).

1. Boot into MCUboot serial recovery mode by plugging the board in with the SW1
   button pressed down. See above for a picture showing where SW1 is.

   **Do not press RESET**; that will run the Nordic bootloader, which is
   different than MCUboot.

   A serial port will enumerate on your board. On Windows, “MCUBOOT” should
   appear under “Other Devices” in the Device Manager (in addition to the usual
   `COMx` device). On Linux, something like
   `/dev/serial/by-id/usb-ZEPHYR_MCUBOOT_0.01-if00` should be created.

   If no serial port appears, try plugging it in again, making sure SW1 is
   pressed. If it still doesn’t appear, retry the one-time MCUboot setup.
2. Compile `smp_svr`.

   ```shell
   west build -b nrf52840dongle_nrf52840 -d build/smp_svr zephyr/samples/subsys/mgmt/mcumgr/smp_svr
   ```
3. Sign `smp_svr` for chain-loading by MCUboot.

   ```shell
   west sign -t imgtool --bin --no-hex -d build/smp_svr \
             -B smp_svr.signed.bin -- --key mcuboot/root-rsa-2048.pem
   ```
4. Flash the application to the MCUboot serial port using `mcumgr`:

   ```shell
   mcumgr --conntype=serial --connstring='dev=/dev/ttyACM0,baud=115200' \
          image upload -e smp_svr.signed.bin
   ```
5. Reset the device:

   ```shell
   mcumgr --conntype=serial --connstring='dev=/dev/ttyACM0,baud=115200' reset
   ```

You should now be able to scan for Bluetooth devices using a smartphone or
computer. The device you just flashed will be listed with `Zephyr` in its
name.

Note

This board supports building other Zephyr applications for flashing with
MCUboot in this way also. Just make sure [`CONFIG_BOOTLOADER_MCUBOOT`](../../../../kconfig.md#CONFIG_BOOTLOADER_MCUBOOT "CONFIG_BOOTLOADER_MCUBOOT")
is set when building your application. For example, to compile blinky for
loading by MCUboot, use this:

```shell
west build -b nrf52840dongle_nrf52840 -d build/blinky zephyr/samples/basic/blinky -- -DCONFIG_BOOTLOADER_MCUBOOT=y
```

You can then sign and flash it using the steps above.

#### Option 3: Using an External Debug Probe

If you have one, you can also use an external [debug probe](../../../../develop/flash_debug/probes.md#debug-probes)
to flash and debug Zephyr applications, but you need to solder an SWD header
onto the back side of the board.

For Segger J-Link debug probes, follow the instructions in the
[Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install and configure all the necessary
software. Further information can be found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing).

Locate the DTS file for the board under: boards/arm/nrf52840dongle\_nrf52840.
This file requires a small modification to use a different partition table.
Edit the include directive to include “fstab-debugger” instead of “fstab-stock”.

In addition, the Kconfig file in the same directory must be modified by setting
`BOARD_HAS_NRF5_BOOTLOADER` to be default `n`, otherwise the code will be
flashed with an offset.

Then build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nrf52840dongle_nrf52840 samples/basic/blinky
west flash
```

Observe the LED on the board blinking.

### Debugging

The `nrf52840dongle_nrf52840` board does not have an on-board J-Link debug IC
as some nRF5x development boards, however, instructions from the
[Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page also apply to this board, with the additional step
of connecting an external debugger.

## Testing the LEDs and buttons on the nRF52840 Dongle

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")

You can build and program the examples to make sure Zephyr is running correctly
on your board.

## References

[1]
([1](#id3),[2](#id4))

[https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-Dongle](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-Dongle)

[2]
([1](#id6),[2](#id7))

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)

[[3](#id9)]

[https://infocenter.nordicsemi.com/index.jsp?topic=%2Fcom.nordic.infocenter.sdk5.v15.2.0%2Fsdk\_app\_serial\_dfu\_bootloader.html](https://infocenter.nordicsemi.com/index.jsp?topic=%2Fcom.nordic.infocenter.sdk5.v15.2.0%2Fsdk_app_serial_dfu_bootloader.html)

[4]
([1](#id11),[2](#id12))

[https://github.com/NordicSemiconductor/pc-nrfutil](https://github.com/NordicSemiconductor/pc-nrfutil)

[[5](#id14)]

[https://github.com/JuulLabs-OSS/mcuboot](https://github.com/JuulLabs-OSS/mcuboot)

[[6](#id16)]

[https://github.com/apache/mynewt-mcumgr-cli](https://github.com/apache/mynewt-mcumgr-cli)

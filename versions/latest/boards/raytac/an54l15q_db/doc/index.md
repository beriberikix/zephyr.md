---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/raytac/an54l15q_db/doc/index.html
original_path: boards/raytac/an54l15q_db/doc/index.html
---

# AN54L15Q-DB

Board Overview

[![../../../../_images/raytac_an54l15q_db.webp](../../../../_images/raytac_an54l15q_db.webp)
](../../../../_images/raytac_an54l15q_db.webp)

AN54L15Q-DB

Name:
:   `raytac_an54l15q_db`

Vendor:
:   Raytac Corporation

Architecture:
:   riscv, arm

SoC:
:   nrf54l15

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/raytac/an54l15q_db/doc/index.rst/../..)

## Overview

The Raytac AN54L15Q-DB demonstration board is a development board based on the Raytac AN54L15Q module.
It uses the Nordic Semiconductor nRF54L15 SoC solution. The idea is to connect all the module’s pins
to a 2.54mm pin header. It can easily open the verification module functions and connect with other
peripheral devices and sensor pins, making it a useful tool for early software development.

Note

You can find more information about the nRF54L15 SoC on the [nRF54L15 website](https://www.nordicsemi.com/Products/nRF54L15) [[1]](#id2).
For the nRF54L15 technical documentation and other resources (such as
SoC Datasheet), see the [nRF54L15 documentation](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/app_dev/device_guides/nrf54l/index.html) [[2]](#id4) page.

## Hardware

The Raytac AN54L15Q-DB has two crystal oscillators:

- High-frequency 32 MHz crystal oscillator (HFXO)
- Low-frequency 32.768 kHz crystal oscillator (LFXO)

The crystal oscillators can be configured to use either
internal or external capacitors.

- Module Demo Board built by AN54L15Q
- Nordic nRF54L15 SoC Solution
- A recommended 3rd-party module by Nordic Semiconductor.
- Intended for Bluetooth specification BT6
- Intended for FCC, IC, CE, Telec (MIC), KC, SRRC, NCC, RCM, WPC
- 128 MHz ARM® Cortex™-M33 processor with TrustZone® technology
- 128 MHz RISC-V coprocessor with TrustZone® technology
- 1.5MB Flash Memory / 256KB RAM
- RoHS & Reach Compliant.
- 31 GPIO
- Chip Antenna
- Interfaces: SPI, UART, I2C, I2S, PDM, PWM, ADC, and NFC
- Highly flexible multiprotocol SoC ideally suited for Bluetooth® Low Energy,
  ANT+, Zigbee, Thread (802.15.4), and Matter ultra low-power wireless applications.

### Supported Features

The `raytac_an54l15q_db` board supports the hardware features listed below.

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

- LED0 (green) = P2.09
- LED1 (green) = P1.10
- LED2 (green) = P2.07
- LED3 (green) = P1.14

#### Push buttons

- BUTTON1 = SW0 = P1.13
- BUTTON2 = SW1 = P1.09
- BUTTON3 = SW2 = P1.08
- BUTTON4 = SW3 = P0.04

#### UART

- RX = P1.05
- TX = P1.04
- RTS = P1.06
- CTS = P1.07

## Programming and Debugging

The `raytac_an54l15q_db` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `raytac_an54l15q_db/nrf54l15/cpuapp` board can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

Note

The `raytac_an54l15q_db` board does not have an on-board J-Link debug IC;
Use the Debug out connector of the nRF5340-DK or nRF54L15-DK to connect to the J1
or J9 SWD connector, and use SEGGER J-Link OB IF to debug.

### Flashing

As an example, this section shows how to build and flash the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

Warning

When programming the device, you might get an error similar to the following message:

```text
ERROR: The operation attempted is unavailable due to readback protection in
ERROR: your device. Please use --recover to unlock the device.
```

This error occurs when readback protection is enabled.
To disable the readback protection, you must *recover* your device.

Enter the following command to recover the core:

```text
west flash --recover
```

The `--recover` command erases the flash memory and then writes a small binary into
the recovered flash memory.
This binary prevents the readback protection from enabling itself again after a pin
reset or power cycle.

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing).

To build and program the sample to the Raytac AN54L15Q-DB, complete the following steps:

First, connect the Raytac AN54L15Q-DB’s J10 connector to you computer using a USB to TTL
converter. Then run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the USB to TTL converter
can be found. For example, under Linux, `/dev/ttyUSB0`.

Next, build the sample by running the following command:

```shell
# From the root of the zephyr repository
west build -b raytac_an54l15q_db/nrf54l15/cpuapp samples/hello_world
west flash
```

## References

[[1](#id3)]

[https://www.nordicsemi.com/Products/nRF54L15](https://www.nordicsemi.com/Products/nRF54L15)

[[2](#id5)]

[https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/app\_dev/device\_guides/nrf54l/index.html](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/app_dev/device_guides/nrf54l/index.html)

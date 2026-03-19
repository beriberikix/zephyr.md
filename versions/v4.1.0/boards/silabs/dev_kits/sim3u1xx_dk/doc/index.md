---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/silabs/dev_kits/sim3u1xx_dk/doc/index.html
original_path: boards/silabs/dev_kits/sim3u1xx_dk/doc/index.html
---

# SiM3U1xx 32-bit MCU USB Development Kit

Board Overview

[![../../../../../_images/sim3u1xx_dk.webp](../../../../../_images/sim3u1xx_dk.webp)
](../../../../../_images/sim3u1xx_dk.webp)

SiM3U1xx 32-bit MCU USB Development Kit

Name:
:   `sim3u1xx_dk`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   sim3u167

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/dev_kits/sim3u1xx_dk/doc/index.rst/../..)

## Overview

This is a [development kit](https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit) [[3]](#id6) that is used to develop software for the SiM3U1xx MCUs.

## Hardware

- Silicon Labs SiM3U167-B-GM SoC
- CPU core: ARM Cortex®-M3
- Flash memory: 256 kB
- RAM: 32 kB
- IO:

  - 2x user LEDs
  - 2x user push buttons
  - 2x power LEDs
  - Reset push button
  - Potentiometer
  - Analog terminals
  - Capacitive sensing slider and button
  - USB virtual COM port

For more information about the SiM3U167 SoC and the SiM3U1xx board, refer to these documents:

- Silicon Labs [SiM3U1xx](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx) [[1]](#id2)
- Silicon Labs [SiM3U167-B-GM](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx/device.sim3u167-b-gm) [[2]](#id4)
- Silicon Labs [SiM3U1xx-B-DK](https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit) [[3]](#id6)
- Silicon Labs SiM3U1xx-B-DK MCU card [user’s guide](https://www.silabs.com/documents/public/user-guides/UPMU-M3U160.pdf) [[4]](#id8)
- Silicon Labs SiM3U1xx and SiM3C1xx Revision B [Errata](https://www.silabs.com/documents/public/errata/SiM3U1xx-SiM3C1xxErrata.pdf) [[5]](#id10)

### Supported Features

The board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| AES | on-chip | crypto |
| DMA | on-chip | dma |
| FLASH | on-chip | flash memory |
| GPIO | on-chip | gpio |
| UART | on-chip | serial port-polling; serial port-interrupt |

### Connections and IOs

| Pin | Name | Note |
| --- | --- | --- |
| PB1.12 | TX (O) | Serial connection to host via USB virtual COM port |
| PB1.13 | RX (I) |
| PB1.14 | RTS (O) |
| PB1.15 | CTS (I) |
| PB2.8 | Push button switch (SW2) |  |
| PB2.9 | Push button switch (SW3) |  |
| PB2.10 | Red LED (DS3) |  |
| PB2.11 | Yellow LED (DS4) |  |
| PB1.5 | Potentiometer |  |
| PB2.12 | Potentiometer bias |  |

## Programming and Debugging

### Flashing

The sample application [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example. Build the Zephyr kernel and
application:

```shell
# From the root of the zephyr repository
west build -b sim3u1xx_dk samples/hello_world
```

Connect the sim3u1xx\_dk to your host computer using both USB port and you should see a USB serial
connection.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you’ll see the following message on the corresponding serial port
terminal session:

```shell
Hello World! sim3u1xx_dk/sim3u167
```

## References

[[1](#id3)]

[https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx)

[[2](#id5)]

[https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx/device.sim3u167-b-gm](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx/device.sim3u167-b-gm)

[3]
([1](#id7),[2](#id12))

[https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit](https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit)

[[4](#id9)]

[https://www.silabs.com/documents/public/user-guides/UPMU-M3U160.pdf](https://www.silabs.com/documents/public/user-guides/UPMU-M3U160.pdf)

[[5](#id11)]

[https://www.silabs.com/documents/public/errata/SiM3U1xx-SiM3C1xxErrata.pdf](https://www.silabs.com/documents/public/errata/SiM3U1xx-SiM3C1xxErrata.pdf)

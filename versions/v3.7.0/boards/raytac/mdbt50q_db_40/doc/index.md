---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/raytac/mdbt50q_db_40/doc/index.html
original_path: boards/raytac/mdbt50q_db_40/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Raytac MDBT50Q-DB-40

## Overview

The Raytac MDBT50Q-DB-40 hardware provides support for the
Nordic Semiconductor nRF52840 ARM Cortex-M4F CPU and the following devices:

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
- Segger RTT (RTT Console)
- SPI
- UART
- USB
- WDT

[![MDBT50Q-DB-40](../../../../_images/mdbt50q_db_40.jpg)](../../../../_images/mdbt50q_db_40.jpg)

More information about the board can be found at the [MDBT50Q-DB-40 website](https://www.raytac.com/product/ins.php?index_id=81) [[1]](#id1).
The [MDBT50Q-DB-40 Specification](https://www.raytac.com/download/index.php?index_id=43) [[2]](#id4) contains the demo board’s datasheet.
The [MDBT50Q-DB-40 Schematic](https://www.raytac.com/upload/catalog_b/134ade06b5db3dd5803d27c5b17f22f3.jpg) [[3]](#id8) contains the demo board’s schematic.

## Hardware

- Module Demo Board build by MDBT50Q-1MV2
- Nordic nRF52840 SoC Solution Version: 2
- A recommnded 3rd-party module by Nordic Semiconductor.
- BT5.2&BT5.1&BT5 Bluetooth Specification Cerified
- Supports BT5 Long Range Features
- Cerifications: FCC, IC, CE, Telec(MIC), KC, SRRC, NCC, RCM, WPC
- 32-bit ARM® Cortex™ M4F CPU
- 1MB Flash Memory/256kB RAM
- RoHs & Reach Compiant.
- 48 GPIO
- Chip Antenna
- Interfaces: SPI, UART, I2C, I2S, PWM, ADC, NFC, and USB
- Highly flexible multiprotocol SoC ideally suited for Bluetooth® Low Energy, ANT+, Zigbee, Thread (802.15.4) ultra low-power wireless applications.
- 3 User LEDs
- 4 User buttons
- 1 Mini USB connector for power supply and USB communication
- SWD connector for FW programing
- J-Link interface for FW programing
- UART interface for UART communication

### Supported Features

The raytac\_mdbt50q\_db\_40/nrf52840 board configuration supports the following
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
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| QSPI(M) | on-chip | qspi |
| UART | on-chip | serial |
| USB | on-chip | usb |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.
See [MDBT50Q-DB-40 website](https://www.raytac.com/product/ins.php?index_id=81) [[1]](#id1) and [MDBT50Q-DB-40 Specification](https://www.raytac.com/download/index.php?index_id=43) [[2]](#id4)
for a complete list of Raytac MDBT50Q-DB-40 board hardware features.

### Connections and IOs

#### LED

- LED1 (green) = P0.13
- LED2 (red) = P0.14
- LED3 (blue) = P0.15

#### Push buttons

- BUTTON1 = SW1 = P0.11
- BUTTON2 = SW2 = P0.12
- BUTTON3 = SW3 = P0.24
- BUTTON4 = SW4 = P0.25

#### UART

- RXD = P0.08
- TXD = P0.06
- RTS = P0.05
- CTS = P0.07

## Programming and Debugging

Applications for the `raytac_mdbt50q_db_40/nrf52840` board configuration can be
built, flashed, and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

Note

Flashing and Debugging Zephyr onto the raytac\_mdbt50q\_db\_40/nrf52840 board
requires an external J-Link programmer. The programmer is attached to the J1
or J9 SWD connector.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

Use a USB to TTL converter to connect the computer and raytac\_mdbt50q\_db\_40/nrf52840
J10 connector. Then run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the USB to TTL converter
can be found. For example, under Linux, `/dev/ttyUSB0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b raytac_mdbt50q_db_40/nrf52840 samples/hello_world
west flash
```

### Debugging

The `raytac_mdbt50q_db_40/nrf52840` board does not have an on-board-J-Link debug IC,
however, instructions from the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page also apply to this board.
Use the Debug out connector of nRF52x DK to connect to the J1 connector, and use SEGGER
J-Link OB IF to debug.

## Testing the LEDs and buttons in the MDBT50Q-DB-40

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

```shell
samples/basic/blinky
samples/basic/button
```

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/raytac/mdbt50q\_db\_40/raytac\_mdbt50q\_db\_40\_nrf52840.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raytac/mdbt50q_db_40/raytac_mdbt50q_db_40_nrf52840.dts).

### Selecting the pins

Pins can be configured in the board pinctrl file. To see the available mappings,
open the [MDBT50Q-DB-40 Specification](https://www.raytac.com/download/index.php?index_id=43) [[2]](#id4), chapter 2.5 ‘Pin Assignment’.
Select the pins marked ‘General-purpose I/O’. Note that pins marked as ‘low-frequency I/O
only’ can only be used in under-10KHz applications. They are not suitable for SPI, I2C,
UART, and PWM.

## References

[1]
([1](#id2),[2](#id3))

[https://www.raytac.com/product/ins.php?index\_id=81](https://www.raytac.com/product/ins.php?index_id=81)

[2]
([1](#id5),[2](#id6),[3](#id7))

[https://www.raytac.com/download/index.php?index\_id=43](https://www.raytac.com/download/index.php?index_id=43)

[[3](#id9)]

[https://www.raytac.com/upload/catalog\_b/134ade06b5db3dd5803d27c5b17f22f3.jpg](https://www.raytac.com/upload/catalog_b/134ade06b5db3dd5803d27c5b17f22f3.jpg)

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/pjrc/teensy4/doc/index.html
original_path: boards/pjrc/teensy4/doc/index.html
---

# PJRC TEENSY 4

## Overview

The Teensy is a complete USB-based microcontroller development system, in a
very small footprint, capable of implementing many types of projects. All
programming is done via the USB port.

Teensy 4.0Teensy 4.1

![TEENSY40](../../../../_images/teensy40.jpg)

(Credit: [https://www.pjrc.com](https://www.pjrc.com))

![TEENSY41](../../../../_images/teensy41.jpg)

(Credit: [https://www.pjrc.com](https://www.pjrc.com))

## Hardware

Teensy 4.0Teensy 4.1

- MIMXRT1062DVL6A MCU (600 MHz, 1024 KB on-chip memory)
- 16 Mbit QSPI Flash
- User LED
- USB 2.0 host connector

See the [Teensy 4.0 Website](https://www.pjrc.com/store/teensy40.html) [[1]](#id3) for a complete hardware description.

- MIMXRT1062DVJ6A MCU (600 MHz, 1024 KB on-chip memory)
- 64 Mbit QSPI Flash
- User LED
- USB 2.0 host connector
- USB 2.0 OTG connector
- 10/100 Mbit/s Ethernet transceiver
- TF socket for SD card

To connect an Ethernet cable, additional [Teensy 4.1 Ethernet Kit](https://www.pjrc.com/store/ethernet_kit.html) [[3]](#id7) is required.

See the [Teensy 4.1 Website](https://www.pjrc.com/store/teensy41.html) [[2]](#id5) for a complete hardware description.

For more information, check the [i.MX RT1060 Datasheet](https://www.nxp.com/docs/en/nxp/data-sheets/IMXRT1060CEC.pdf) [[4]](#id9).

### Supported Features

The Teensy 4.0 board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| ADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| I2S | on-chip | i2s |
| NVIC | on-chip | arch/arm |
| PWM | on-chip | pwm |
| RTC | on-chip | system clock |
| SPI | on-chip | spi |
| CAN | on-chip | can |
| UART | on-chip | serial |
| USB | on-chip | usb |
| TRNG | on-chip | entropy |
| WDT | on-chip | watchdog |

The Teensy 4.1 board configuration supports additional hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| SDHC | on-chip | disk access |
| ENET | on-chip | ethernet |

Other hardware features have not been enabled yet for this board.

### Connections and IOs

Pin mappings from Teensy to MIMXRT1062 SoC.

| Pin | Pad ID | Usage |
| --- | --- | --- |
| 0 | AD\_B0\_03 | GPIO1\_3 / UART6\_RX / CAN2\_RX |
| 1 | AD\_B0\_02 | GPIO1\_2 / UART6\_TX / CAN2\_TX |
| 2 | EMC\_04 | GPIO4\_4 |
| 3 | EMC\_05 | GPIO4\_5 |
| 4 | EMC\_06 | GPIO4\_6 |
| 5 | EMC\_08 | GPIO4\_8 |
| 6 | B0\_10 | GPIO2\_10 |
| 7 | B1\_01 | GPIO2\_17 / UART4\_RX |
| 8 | B1\_00 | GPIO2\_16 / UART4\_TX |
| 9 | B0\_11 | GPIO2\_11 |
| 10 | B0\_00 | GPIO2\_0 |
| 11 | B0\_02 | GPIO2\_2 |
| 12 | B0\_01 | GPIO2\_1 |
| 13 | B0\_03 | GPIO2\_3 / LED |
| 14 | AD\_B1\_02 | GPIO1\_18 / UART2\_TX |
| 15 | AD\_B1\_03 | GPIO1\_19 / UART2\_RX |
| 16 | AD\_B1\_07 | GPIO1\_23 / UART3\_RX / I2C3\_SCL |
| 17 | AD\_B1\_06 | GPIO1\_22 / UART3\_TX / I2C3\_SDA |
| 18 | AD\_B1\_01 | GPIO1\_17 / I2C1\_SDA |
| 19 | AD\_B1\_00 | GPIO1\_16 / I2C1\_SCL |
| 20 | AD\_B1\_10 | GPIO1\_26 / UART8\_TX |
| 21 | AD\_B1\_11 | GPIO1\_27 / UART8\_RX |
| 22 | AD\_B1\_08 | GPIO1\_24 / CAN1\_TX |
| 23 | AD\_B1\_09 | GPIO1\_25 / CAN1\_RX |
| 24 | AD\_B0\_12 | GPIO1\_12 / UART1\_TX / I2C4\_SCL |
| 25 | AD\_B0\_13 | GPIO1\_13 / UART1\_RX / I2C4\_SDA |
| 26 | AD\_B1\_14 | GPIO1\_30 / SPI3\_MOSI |
| 27 | AD\_B1\_15 | GPIO1\_31 / SPI3\_SCK |
| 28 | EMC\_32 | GPIO3\_18 / UART7\_RX |
| 29 | EMC\_31 | GPIO4\_31 / UART7\_TX |
| 30 | EMC\_37 | GPIO3\_23 / CAN3\_RX |
| 31 | EMC\_36 | GPIO3\_22 / CAN3\_TX |
| 32 | B0\_12 | GPIO2\_12 |
| 33 | EMC\_07 | GPIO4\_7 |

Only Teensy 4.0:

| 34 | SD\_B0\_03 | GPIO3\_15 |
| --- | --- | --- |
| 35 | SD\_B0\_02 | GPIO3\_14 |
| 36 | SD\_B0\_01 | GPIO3\_13 |
| 37 | SD\_B0\_00 | GPIO3\_12 |
| 38 | SD\_B0\_05 | GPIO3\_17 |
| 39 | SD\_B0\_04 | GPIO3\_16 |

Only Teensy 4.1:

| 34 | B1\_13 | GPIO2\_29 / UART5\_RX |
| --- | --- | --- |
| 35 | B1\_12 | GPIO2\_28 / UART5\_TX |
| 36 | B1\_02 | GPIO2\_18 |
| 37 | B1\_03 | GPIO2\_19 |
| 38 | AD\_B1\_12 | GPIO1\_28 / SPI3\_CS |
| 39 | AD\_B1\_13 | GPIO1\_29 / SPI3\_MISO |
| 40 | AD\_B1\_04 | GPIO1\_20 |
| 41 | AD\_B1\_05 | GPIO1\_21 |

## Programming and Debugging

### Flashing

Both the Teensy 4.0 and Teensy 4.1 ship with a dedicated bootloader chip,
which supports flashing using USB. This allows easy flashing of new images,
but does not support debugging the device.

1. Build the Zephyr kernel and the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

Teensy 4.0Teensy 4.1

```shell
west build -b teensy40 samples/basic/blinky
```

```shell
west build -b teensy41 samples/basic/blinky
```

1. Connect the board to your host computer using USB.
2. Tap the reset button to enter bootloader mode.
   Red LED blinks.
3. Flash the image.

Teensy 4.0Teensy 4.1

```shell
west build -b teensy40 samples/basic/blinky
west flash
```

```shell
west build -b teensy41 samples/basic/blinky
west flash
```

1. You should see the orange LED blink.

### Configuring a Console

UART-ConsoleUSB-Console

By default console output is mapped to teensy pins 0 (RX1) and 1 (TX1). Connect a usb-to-serial adapter
to use this serial console. Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

By mapping the console output to USB, a usb-to-serial adapter is no longer required.
Utilizing the [CDC-ACM Console Snippet (cdc-acm-console)](../../../../snippets/cdc-acm-console/README.md#snippet-cdc-acm-console) and a config option will enable this feature.

1. If application code doesn´t enable USB device support, this must be done via Kconfig option.

   ```kconfig
   CONFIG_USB_DEVICE_INITIALIZE_AT_BOOT=y
   ```
2. Build application including the snippet.

   ```shell
   west build -b teensy41 -S cdc-acm-console samples/basic/blinky
   west flash
   ```
3. After application startup a serial device named like
   `tty.usbmodem14203` should appear on your host computer.
   You can use e.g. `Serial Monitor` plugin for VScode to monitor.

## References

[[1](#id4)]

[https://www.pjrc.com/store/teensy40.html](https://www.pjrc.com/store/teensy40.html)

[[2](#id6)]

[https://www.pjrc.com/store/teensy41.html](https://www.pjrc.com/store/teensy41.html)

[[3](#id8)]

[https://www.pjrc.com/store/ethernet\_kit.html](https://www.pjrc.com/store/ethernet_kit.html)

[[4](#id10)]

[https://www.nxp.com/docs/en/nxp/data-sheets/IMXRT1060CEC.pdf](https://www.nxp.com/docs/en/nxp/data-sheets/IMXRT1060CEC.pdf)

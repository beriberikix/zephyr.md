---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/adafruit/feather_nrf52840/doc/index.html
original_path: boards/adafruit/feather_nrf52840/doc/index.html
---

# Feather nRF52840 (Express, Sense)

Board Overview

[![../../../../_images/adafruit_feather_nrf52840_sense.jpg](../../../../_images/adafruit_feather_nrf52840_sense.jpg)
](../../../../_images/adafruit_feather_nrf52840_sense.jpg)

Feather nRF52840 (Express, Sense)

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   nrf52840

## Overview

The Adafruit Feather nRF52840 provides support for the Nordic Semiconductor
nRF52840 ARM Cortex-M4F CPU and the following devices:

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

ExpressSense

![Adafruit Feather nRF52840 Express](../../../../_images/adafruit_feather_nrf52840_express.jpg)

![Adafruit Feather nRF52840 Sense](../../../../_images/adafruit_feather_nrf52840_sense1.jpg)

## Hardware

- nRF52840 ARM Cortex-M4F processor at 64 MHz
- 1 MB flash memory and 256 KB of SRAM
- Battery connector and charger for 3.7 V lithium polymer batteries
- Charging indicator LED
- 2 User LEDs
- 1 NeoPixel LED
- Reset button
- SWD connector (Express only)
- SWD solder pads on bottom of PCB (Sense only)
- LSM6DS33 Accel/Gyro (Sense only)
- LIS3MDL magnetometer (Sense only)
- APDS9960 Proximity, Light, Color, and Gesture Sensor (Sense only)
- MP34DT01-M PDM Microphone sound sensor (Sense only)
- SHT3X Humidity sensor (Sense only)
- BMP280 temperature and barometric pressure/altitude (Sense only)

### Supported Features

The Adafruit Feather nRF52840 board configuration supports the
following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| ADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| PWM | on-chip | pwm |
| RADIO | on-chip | Bluetooth, ieee802154 |
| RTC | on-chip | system clock |
| SPI | on-chip | spi |
| UART | on-chip | serial |
| USB | on-chip | usb |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.

### Connections and IOs

ExpressSense

The [Adafruit Feather nRF52840 Express Learn site](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/) [[1]](#id2) has
detailed information about the board including
[pinouts (Express)](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/pinouts) [[2]](#id4) and the [schematic (Express)](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/downloads) [[3]](#id6).

The [Adafruit Feather nRF52840 Sense Learn site](https://learn.adafruit.com/adafruit-feather-sense) [[4]](#id8) has
detailed information about the board including
[pinouts (Sense)](https://learn.adafruit.com/adafruit-feather-sense/pinouts) [[5]](#id10) and the [schematic (Sense)](https://learn.adafruit.com/adafruit-feather-sense/downloads) [[6]](#id12).

#### LED

- LED0 (red) = P1.15 (Express)
- LED0 (red) = P1.9 (Sense)
- LED1 (blue) = P1.10

#### Push buttons

- SWITCH = P1.02
- RESET = P0.18

## Programming and Debugging

### Flashing

Flashing Zephyr onto both the Feather nRF52840 Express and Sense is possible
using the SWD headers. Only the Express board has an SWD connector however.

Both the Feather nRF52840 Express and Sense ship with the [Adafruit nRF52 Bootloader](https://github.com/adafruit/Adafruit_nRF52_Bootloader) [[7]](#id14)
which supports flashing using [UF2](https://github.com/microsoft/uf2) [[8]](#id16). This allows easy flashing of new images,
but does not support debugging the device.

1. Build the Zephyr kernel and the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

ExpressExpress UF2SenseSense UF2

```shell
west build -b adafruit_feather_nrf52840 samples/basic/blinky
```

```shell
west build -b adafruit_feather_nrf52840/nrf52840/uf2 samples/basic/blinky
```

```shell
west build -b adafruit_feather_nrf52840/nrf52840/sense samples/basic/blinky
```

```shell
west build -b adafruit_feather_nrf52840/nrf52840/sense/uf2 samples/basic/blinky
```

1. If using UF2, connect the board to your host computer using USB.
2. Tap the reset button twice quickly to enter bootloader mode.
   A mass storage device named `FTHR840BOOT` for (Express) or
   `FTHRSNSBOOT` (Sense) should appear on the host. Ensure this is
   mounted.
3. Flash the image.

ExpressExpress UF2SenseSense UF2

```shell
west build -b adafruit_feather_nrf52840 samples/basic/blinky
west flash
```

```shell
west build -b adafruit_feather_nrf52840/nrf52840/uf2 samples/basic/blinky
west flash
```

```shell
west build -b adafruit_feather_nrf52840/nrf52840/sense samples/basic/blinky
west flash
```

```shell
west build -b adafruit_feather_nrf52840/nrf52840/sense/uf2 samples/basic/blinky
west flash
```

1. You should see the red LED blink.

## References

[[1](#id3)]

[https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/)

[[2](#id5)]

[https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/pinouts](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/pinouts)

[[3](#id7)]

[https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/downloads](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/downloads)

[[4](#id9)]

[https://learn.adafruit.com/adafruit-feather-sense](https://learn.adafruit.com/adafruit-feather-sense)

[[5](#id11)]

[https://learn.adafruit.com/adafruit-feather-sense/pinouts](https://learn.adafruit.com/adafruit-feather-sense/pinouts)

[[6](#id13)]

[https://learn.adafruit.com/adafruit-feather-sense/downloads](https://learn.adafruit.com/adafruit-feather-sense/downloads)

[[7](#id15)]

[https://github.com/adafruit/Adafruit\_nRF52\_Bootloader](https://github.com/adafruit/Adafruit_nRF52_Bootloader)

[[8](#id17)]

[https://github.com/microsoft/uf2](https://github.com/microsoft/uf2)

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/norik/octopus_som/doc/index.html
original_path: boards/norik/octopus_som/doc/index.html
---

# Octopus SoM

Board Overview

[![../../../../_images/octopus_som.webp](../../../../_images/octopus_som.webp)
](../../../../_images/octopus_som.webp)

Octopus SoM

Name:
:   `octopus_som`

Vendor:
:   Norik Systems

Architecture:
:   arm

SoC:
:   nrf9160

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/norik/octopus_som/doc/index.rst/../..)

## Overview

Octopus SoM is a System on Module (SoM) built around the nRF9160 SiP
offering NB-IoT and LTE-M connectivity, GPS and accelerometer.
It supports on board eSIM and external nano SIM connector. It’s purpose
is to provide flexible hardware platform for IoT applications.

nRF9160 SiP contains ARM Cortex-M33 application processor and the
following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RTC
- Segger RTT (RTT Console)
- SPI
- UARTE
- WDT
- IDAU

More information about the board can be found at the [Octopus SoM Product Page](https://www.norik.com/octopus-som/) [[1]](#id2) and
in the [Octopus SoM Documentation](https://www.norik.com/wp-content/uploads/2024/09/Octopus_SoM_Datasheet.pdf) [[2]](#id4).

## Hardware

The `octopus_som/nrf9160` and `octopus_som/nrf9160/ns` board targets support the
following hardware features:

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
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| SPU | on-chip | system protection |
| UARTE | on-chip | serial |
| WDT | on-chip | watchdog |
| ACCEL | Analog | adxl362 |

### Connections and IOs

#### Accelerometer

- MISO = P0.05
- MOSI = P0.09
- SCK = P0.10
- CS = P0.05
- INT1 = P0.12

#### LED

- LED1 (green) = P0.07

#### SIM select switch

- Select = P0.25

## Programming and Debugging

Norik Octopus SoM can be programmed and debugged using the exposed SWD pins.

### Building an application

In most case you’ll need to use `octopus_som/nrf9160/ns` board target for building examples.
Some examples don’t require non secure mode and can be built with `octopus_som/nrf9160` board target.

### Flashing

Refer to the instruction in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install and
configure all the necessary software.

Use the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample to test if Zephyr is running correctly on your board.

```shell
# From the root of the zephyr repository
west build -b octopus_som/nrf9160 samples/basic/blinky
west flash
```

### Debugging

Refer to the instruction in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page for information on
debugging.

## References

[[1](#id3)]

[https://www.norik.com/octopus-som/](https://www.norik.com/octopus-som/)

[[2](#id5)]

[https://www.norik.com/wp-content/uploads/2024/09/Octopus\_SoM\_Datasheet.pdf](https://www.norik.com/wp-content/uploads/2024/09/Octopus_SoM_Datasheet.pdf)

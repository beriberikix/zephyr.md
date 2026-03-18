---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/actinius/icarus_som/doc/index.html
original_path: boards/actinius/icarus_som/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Actinius Icarus SoM

## Overview

![Icarus SoM](../../../../_images/icarus-som.jpg)

Icarus SoM (nRF9160)

The Icarus SoM is a coin-sized, easy-to-solder cellular IoT Module
built around Nordic Semi’s nRF9160 modem and combines
LTE-M, NB-IoT, GPS, accelerometer as well as an eSIM and option for
an external nano SIM connector.

The main uController is the Nordic Semiconductor nRF9160, with
ARM Cortex-M33F CPU, ARMv8-M Security Extension and the
following devices (provided directly by Nordic):

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

![Icarus SoM Pins](../../../../_images/icarus-som-external-pins.jpg)

Icarus SoM Pins

![Icarus SoM](../../../../_images/icarus-som-peripherals-pins.jpg)

Internal Pinouts

## Hardware

The detailed information about the on-board hardware can be found at the [Icarus SoM Product Website](https://www.actinius.com/icarus-som) [[2]](#id7).

### Supported Features

The actinius\_icarus\_som board configuration supports the following
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
| SPI(M/S) | on-chip | spi |
| SPU | on-chip | system protection |
| UARTE | on-chip | serial |
| ACCEL | st | lis2dh |

## SIM selection

The sim choice (eSIM or nano-SIM) can be configured in Devicetree by adjusting
the `sim` property in the `sim_select` node.

### Security components

- Implementation Defined Attribution Unit ([IDAU](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau) [[1]](#id5)). The IDAU is implemented
  with the System Protection Unit and is used to define secure and non-secure
  memory maps. By default, all of the memory space (Flash, SRAM, and
  peripheral address space) is defined to be secure accessible only.
- Secure boot.

### Building Secure/Non-Secure Zephyr applications

The process requires the following steps:

1. Build the Secure Zephyr application using `-DBOARD=actinius_icarus_som`.
2. Build the Non-Secure Zephyr application using `-DBOARD=actinius_icarus_som/ns`.
3. Merge the two binaries together.

If you are using Segger Embedded Studio v4.18 or later, the two binaries are built, merged, and
burned automatically, unless you have disabled the feature.

When building a Secure/Non-Secure application, the Secure application will
have to set the IDAU (SPU) configuration to allow Non-Secure access to all
CPU resources utilized by the Non-Secure application firmware. SPU
configuration shall take place before jumping to the Non-Secure application.

More information can be found in the [Icarus SoM Product Website](https://www.actinius.com/icarus-som) [[2]](#id7) or the
[Actinius Documentation Portal](https://docs.actinius.com) [[3]](#id10).

## References

[[1](#id6)]

[https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau)

[2]
([1](#id8),[2](#id9))

[https://www.actinius.com/icarus-som](https://www.actinius.com/icarus-som)

[[3](#id11)]

[https://docs.actinius.com](https://docs.actinius.com)

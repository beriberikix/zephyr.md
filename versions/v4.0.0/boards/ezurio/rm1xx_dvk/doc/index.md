---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/ezurio/rm1xx_dvk/doc/index.html
original_path: boards/ezurio/rm1xx_dvk/doc/index.html
---

# RM1xx DVK

Board Overview

[![../../../../_images/rm1xx_dvk.jpg](../../../../_images/rm1xx_dvk.jpg)
](../../../../_images/rm1xx_dvk.jpg)

RM1xx DVK

Vendor:
:   Ezurio

Architecture:
:   arm

SoC:
:   nrf51822

## Overview

Ezurio’s RM1xx is a module which integrates both LoRa and
BLE communications, powered by a Nordic Semiconductor nRF51822 ARM
Cortex-M0 CPU and on-board Semtech SX1272 LoRa RF chip. This board
supports the RM1xx on the RM1xx development board - RM191 for the
915MHz version and RM186 for the 868MHz version.

This development kit has the following features:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- NVIC
- PWM
- RADIO (Bluetooth Low Energy)
- RTC
- Segger RTT (RTT Console)
- SPI
- UART
- WDT

![RM1xx module](../../../../_images/RM186-SM.jpg)

RM1xx module (Credit: Ezurio)

More information about the module can be found on the
[RM1xx homepage](https://www.ezurio.com/wireless-modules/lorawan-solutions/sentrius-rm1xx-lora-ble-module) [[1]](#id3).

The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
contains the processor’s information and the datasheet.

## Hardware

The RM1xx has two internal oscillators. The frequency of
the slow clock is 32.768KHz. The frequency of the main clock
is 16MHz.

### Supported Features

The rm1xx\_dvk board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| ADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| I2C(M) | on-chip | i2c |
| NVIC | on-chip | arch/arm |
| PWM | on-chip | pwm |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| SPU | on-chip | system protection |
| UART | on-chip | serial |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.
See [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
for a complete list of hardware features.

### Connections and IOs

The development board features a Microchip MCP23S08 SPI port expander -
note that this is not currently supported in Zephyr.

Refer to the [Microchip MCP23S08 datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP23008-MCP23S08-Data-Sheet-20001919F.pdf) [[5]](#id12) for further details.

#### Push buttons

- BUTTON2 = SW0 = P0.05

### Internal Memory

#### EEPROM Memory

A 512KB (4Mb) Adesto AT25DF041B EEPROM is available via SPI for storage
of infrequently updated data and small datasets and can be used with
the spi-nor driver. Note that the EEPROM shares the same SPI bus as the
SX1272 LoRa transceiver so priority access should be given to the LoRa
radio.

Refer to the [Adesto AT25DF041B datasheet](https://www.dialog-semiconductor.com/sites/default/files/ds-at25df041b_040.pdf) [[3]](#id8) for further details.

### LoRa

A Semtech SX1272 transceiver chip is present in the module which can be
used in 915MHz LoRa frequency ranges if using an RM191 module or 868MHz
LoRa frequency ranges if uses an RM186 module

Refer to the [Semtech SX1272 datasheet](https://semtech.my.salesforce.com/sfc/p/#E0000000JelG/a/440000001NCE/v_VBhk1IolDgxwwnOpcS_vTFxPfSEPQbuneK3mWsXlU) [[4]](#id10) for further details.

## Programming and Debugging

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board nRF51 DK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b rm1xx_dvk samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging boards
with a Segger IC.

## References

[[1](#id4)]

[https://www.ezurio.com/wireless-modules/lorawan-solutions/sentrius-rm1xx-lora-ble-module](https://www.ezurio.com/wireless-modules/lorawan-solutions/sentrius-rm1xx-lora-ble-module)

[2]
([1](#id6),[2](#id7))

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)

[[3](#id9)]

[https://www.dialog-semiconductor.com/sites/default/files/ds-at25df041b\_040.pdf](https://www.dialog-semiconductor.com/sites/default/files/ds-at25df041b_040.pdf)

[[4](#id11)]

[https://semtech.my.salesforce.com/sfc/p/#E0000000JelG/a/440000001NCE/v\_VBhk1IolDgxwwnOpcS\_vTFxPfSEPQbuneK3mWsXlU](https://semtech.my.salesforce.com/sfc/p/#E0000000JelG/a/440000001NCE/v_VBhk1IolDgxwwnOpcS_vTFxPfSEPQbuneK3mWsXlU)

[[5](#id13)]

[https://ww1.microchip.com/downloads/en/DeviceDoc/MCP23008-MCP23S08-Data-Sheet-20001919F.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP23008-MCP23S08-Data-Sheet-20001919F.pdf)

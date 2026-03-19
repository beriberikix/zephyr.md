---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/st/nucleo_f412zg/doc/index.html
original_path: boards/st/nucleo_f412zg/doc/index.html
---

# Nucleo F412ZG

Board Overview

[![../../../../_images/nucleo_f412zg.jpg](../../../../_images/nucleo_f412zg.jpg)
](../../../../_images/nucleo_f412zg.jpg)

Nucleo F412ZG

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f412zx

## Overview

The Nucleo F412ZG board features an ARM Cortex-M4 based STM32F412ZG MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the Nucleo F412ZG board:

- STM32 microcontroller in LQFP144 package
- Two types of extension resources:

  - ST Zio connector including: support for Arduino\* Uno V3 connectivity
    (A0 to A5, D0 to D15) and additional signals exposing a wide range of
    peripherals
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:

  - 5 V from ST-LINK/V2-1 USB VBUS
  - External power sources: 3.3 V and 7 - 12 V on ST Zio or ST morpho
    connectors, 5 V on ST morpho connector
- Three user LEDs
- Two push-buttons: USER and RESET

More information about the board can be found at the [Nucleo F412ZG website](https://www.st.com/en/evaluation-tools/nucleo-f412zg.html).

## Hardware

Nucleo F412ZG provides the following hardware components:

- STM32F412ZGT6 in LQFP144 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 100 MHz max CPU frequency
- VDD from 1.7 V to 3.6 V
- 1 MB Flash
- 256 KB SRAM
- GPIO with external interrupt capability
- 12-bit ADC with 16 channels, with FIFO and burst support
- RTC
- 14 General purpose timers
- 2 watchdog timers (independent and window)
- SysTick timer
- USART/UART (4)
- I2C (4)
- SPI (5)
- SDIO
- USB 2.0 OTG FS
- DMA Controller
- CRC calculation unit

More information about STM32F412ZG can be found here:

- [STM32F412ZG on www.st.com](https://www.st.com/en/microcontrollers/stm32f412zg.html)
- [STM32F412 reference manual](https://www.st.com/resource/en/reference_manual/dm00180369.pdf)

### Supported Features

The Zephyr nucleo\_412zg board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| USB | on-chip | usb |
| PWM | on-chip | pwm |

Other hardware features are not yet supported on this Zephyr port.

The default configuration can be found in
[boards/st/nucleo\_f412zg/nucleo\_f412zg\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f412zg/nucleo_f412zg_defconfig)

### Connections and IOs

Nucleo F412ZG Board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Available pins:

![Nucleo F412ZG ZIO connectors (left)](../../../../_images/nucleo_f412zg_zio_left.jpg)
![Nucleo F412ZG ZIO connectors (right)](../../../../_images/nucleo_f412zg_zio_right.jpg)
![Nucleo F412ZG Morpho connectors (left)](../../../../_images/nucleo_f412zg_morpho_left.jpg)
![Nucleo F412ZG Morpho connectors (right)](../../../../_images/nucleo_f412zg_morpho_right.jpg)

For more details please refer to [STM32 Nucleo-144 board User Manual](https://www.st.com/resource/en/user_manual/dm00244518.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_3 TX/RX : PD8/PD9 (ST-Link Virtual Port Com)
- UART\_6 TX/RX : PG14/PG9 (Arduino Serial)
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- SPI1 NSS/SCK/MISO/MOSI : PD14/PA5/PA6/PA7 (Arduino SPI)
- PWM\_2\_CH1 : PA0
- USER\_PB : PC13
- LD1 : PB0
- LD2 : PB7
- LD3 : PB14
- USB DM : PA11
- USB DP : PA12

#### System Clock

Nucleo F412ZG System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at 96MHz,
driven by 8MHz high speed external clock.

#### Serial Port

Nucleo F412ZG board has 4 UARTs. The Zephyr console output is assigned to UART3.
Default settings are 115200 8N1.

#### Network interface

Ethernet over USB is configured as the default network interface

## Programming and Debugging

Nucleo F412ZG board includes an ST-LINK/V2-1 embedded debug tool interface.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

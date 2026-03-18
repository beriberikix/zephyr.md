---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/st/nucleo_f722ze/doc/index.html
original_path: boards/st/nucleo_f722ze/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ST Nucleo F722ZE

## Overview

The Nucleo F722ZE board features an ARM Cortex-M7 based STM32F722ZE MCU.

Key Features:

- STM32 microcontroller in LQFP144 package
- USB full-speed/high-speed device
- 3 user LEDs
- 1 user button and 1 reset button
- 32.768 kHz crystal oscillator
- Board connectors:
  :   - USB Micro-AB
      - SWD
      - ST Zio connector (Arduino Uno R3 compatible)
      - ST Morpho connector
- On-board ST-LINK debugger/programmer
- Flexible power supply options, including ST-LINK VBUS and external sources.

[![Nucleo F722ZE](../../../../_images/nucleo_f722ze.jpg)](../../../../_images/nucleo_f722ze.jpg)

## Hardware

Nucleo F722ZE provides the following hardware components:

- STM32F722ZET6 microcontroller in LQFP144 package
- ARM® Cortex®-M4 with FPU
- Adaptive Real-Time Accelerator (ART Accelerator)
- 216MHz max CPU frequency
- 512 KB flash
- 256 KB RAM
- I2C (3)
- USART/UART (4)
- SPI (5)
- I2S (3)
- SAI (2)
- USB OTG Full-speed (1)
- USB OTG Full-speed/high-speed (1)
- SDMMC (2)
- CAN (1)
- Dual mode Quad-SPI
- Random number generator (RNG)
- 3x 12-bit ADC, up to 2.4 MSPS with 24 channels or 7.2 MSPS in triple-interleaved mode
- 2x 12-bit DAC
- 16-channel DMA controller
- 16-bit timers (13) with PWM, pulse counter, and quadrature features
- 32-bit timers (2) with PWM, pulse counter, and quadrature features
- CRC
- 96-bit unique ID
- Die temperature

### Supported Features

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | arch/arm |
| MPU | on-chip | arch/arm |
| ADC | on-chip | adc |
| CAN | on-chip | can |
| USART/UART | on-chip | console, serial |
| TIMER | on-chip | counter, pwm, timer |
| DAC | on-chip | dac |
| DMA | on-chip | dma |
| GPIO | on-chip | gpio |
| HWINFO | on-chip | hwinfo |
| I2C | on-chip | i2c |
| EXTI | on-chip | interrupt\_controller |
| BACKUP\_SRAM | on-chip | memory |
| QUADSPI | on-chip | memory |
| PINMUX | on-chip | pinctrl |
| RCC | on-chip | reset |
| RTC | on-chip | rtc |
| DIE\_TEMP | on-chip | sensor |
| VREF | on-chip | sensor |
| VBAT | on-chip | sensor |
| SPI | on-chip | spi |
| USBOTG\_HS | on-chip | usb |
| USBOTG\_FS | on-chip | usb |
| IWDG | on-chip | watchdog |
| WWDG | on-chip | watchdog |
| RTC | on-chip | rtc |

### Connections and IOs

- SDMMC1: Pins marked as “SDMMC” on the ST Zio connector.
  :   - D0: PC8 (CN8 pin 2)
      - D1: PC9 (CN8 pin 4)
      - D2: PC10 (CN8 pin 6)
      - D3: PC11 (CN8 pin 8)
      - CK: PC12 (CN8 pin 10)
      - CMD: PD2 (CN8 pin 12)
- ADC1:
  :   - IN3: PA3 (CN9 pin 1, Arduino A0)
      - IN10: PC0 (CN9 pin 3, Arduino A1)
- DAC1:
  :   - OUT1: PA4 (CN7 pin 17)
- I2C2: Pins marked as “I2C” on the ST Zio connector.
  :   - SCL: PF1 (CN9 pin 19)
      - SDA: PF0 (CN9 pin 21)
- CAN1: Pins marked as “CAN” on the ST Zio connector.
  :   - RX: PD0 (CN9 pin 25)
      - TX: PD1 (CN9 pin 27)
- USART2: Pins marked as “USART” on the ST Zio connector.
  :   - RX: PD6 (CN9 pin 4)
      - TX: PD5 (CN9 pin 6)
      - RTS: PD4 (CN9 pin 8)
      - CTS: PD3 (CN9 pin 10)
- PWM1: Uses TIMER1.
  :   - PE13 (CN10 pin 10, Arduino D3)
      - PE11 (CN10 pin 6, Arduino D5)
- USART3: Connected to ST-Link virtual COM port.
  :   - TX: PD8
      - RX: PD9
- USART6: Arduino UART port.
  :   - RX: PG9 (CN10 pin 16, Arduino D0)
      - TX: PG14 (CN10 pin 14, Arduino D1)
- USBOTG\_FS: Connected to USB Micro-AB connector (CN13)
  :   - DM: PA11
      - DP: PA12
      - ID: PA10
- QUADSPI: Pins marked as “QSPI” on the ST Zio connector.
  :   - CS: PB6 (CN10 pin 13)
      - CLK: PB2 (CN10 pin 15)
      - IO3: PD13 (CN10 pin 19)
      - IO1: PD12 (CN10 pin 21)
      - IO0: PD11 (CN10 pin 23)
      - IO2: PE2 (CN10 pin 25)

#### System Clock

By default, the system clock is driven by the external clock supplied by
the ST-LINK interface. Nucleo F722ZE system clock can be driven by internal
or external sources.

#### Serial Port

Zephyr console is assigned to UART3 (ST-Link Virtual COM Port) by default,
using 115200 8N1.

## Programming and Debugging

The `nucleo_f722ze` can be flashed and debugged in the typical manner.
The Nucleo F722ZE board includes an ST-LINK V2-1 debugger, which can be used
with the OpenOCD version provided with the Zephyr SDK. Refer to
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for detailed
instructions.

### Flashing

Build the [Hello World](../../../../samples/hello_world/README.md#hello-world) application and flash it using the on-board
ST-LINK interface:

```shell
# From the root of the zephyr repository
west build -b nucleo_f722ze samples/hello_world
west flash
```

### Debugging

```shell
# From the root of the zephyr repository
west build -b nucleo_f722ze samples/hello_world
west debug
```

#### J-Link OB Firmware

Like many other STM32 evaluation boards, the Nucleo F722ZE’s on-board ST-LINK
debug interface may be flashed with [SEGGER J-Link OB firmware](https://www.segger.com/products/debug-probes/j-link/models/other-j-links/st-link-on-board/). This
firmware turns the ST-LINK into a J-Link probe. If the on-board debugger has
been re-flashed with J-Link OB firmware, simply append `--runner jlink` to
all flashing/debugging commands.

## References

More information about the STM32F722ZE:

- [STM32F722ZE on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32f722ze.html)
- [STM32F722ZE Reference Manual (RM0431)](https://www.st.com/resource/en/reference_manual/rm0431-stm32f72xxx-and-stm32f73xxx-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) (PDF)

More information about Nucleo F722ZE:

- [Nucleo F722ZE on www.st.com](https://www.st.com/en/evaluation-tools/nucleo-f722ze.html)
- [STM32 Nucleo-144 User Manual (UM1974)](https://www.st.com/resource/en/user_manual/um1974-stm32-nucleo144-boards-mb1137-stmicroelectronics.pdf) (PDF)

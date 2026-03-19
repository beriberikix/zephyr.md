---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/st/nucleo_l476rg/doc/index.html
original_path: boards/st/nucleo_l476rg/doc/index.html
---

# Nucleo L476RG

Board Overview

[![../../../../_images/nucleo_l476rg.jpg](../../../../_images/nucleo_l476rg.jpg)
](../../../../_images/nucleo_l476rg.jpg)

Nucleo L476RG

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32l476xx

## Overview

The Nucleo L476RG board features an ARM Cortex-M4 based STM32L476RG MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the Nucleo L476RG board:

- STM32 microcontroller in QFP64 package
- Two types of extension resources:

  - Arduino Uno V3 connectivity
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:

  > - USB VBUS or external source(3.3V, 5V, 7 - 12V)
  > - Power management access point
- Three LEDs: USB communication (LD1), user LED (LD2), power LED (LD3)
- Two push-buttons: USER and RESET

More information about the board can be found at the [Nucleo L476RG website](https://www.st.com/en/evaluation-tools/nucleo-l476rg.html).

## Hardware

The STM32L476RG SoC provides the following hardware IPs:

- Ultra-low-power with FlexPowerControl (down to 130 nA Standby mode and 100 uA/MHz run mode)
- Core: ARM® 32-bit Cortex®-M4 CPU with FPU, frequency up to 80 MHz, 100DMIPS/1.25DMIPS/MHz (Dhrystone 2.1)
- Clock Sources:

  - 4 to 48 MHz crystal oscillator
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC ( ±1%)
  - Internal low-power 32 kHz RC ( ±5%)
  - Internal multispeed 100 kHz to 48 MHz oscillator, auto-trimmed by
    LSE (better than ±0.25 % accuracy)
  - 3 PLLs for system clock, USB, audio, ADC
- RTC with HW calendar, alarms and calibration
- LCD 8 x 40 or 4 x 44 with step-up converter
- Up to 24 capacitive sensing channels: support touchkey, linear and rotary touch sensors
- 16x timers:

  - 2x 16-bit advanced motor-control
  - 2x 32-bit and 5x 16-bit general purpose
  - 2x 16-bit basic
  - 2x low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - SysTick timer
- Up to 114 fast I/Os, most 5 V-tolerant, up to 14 I/Os with independent supply down to 1.08 V
- Memories

  - Up to 1 MB Flash, 2 banks read-while-write, proprietary code readout protection
  - Up to 128 KB of SRAM including 32 KB with hardware parity check
  - External memory interface for static memories supporting SRAM, PSRAM, NOR and NAND memories
  - Quad SPI memory interface
- 4x digital filters for sigma delta modulator
- Rich analog peripherals (independent supply)

  - 3x 12-bit ADC 5 MSPS, up to 16-bit with hardware oversampling, 200 uA/MSPS
  - 2x 12-bit DAC, low-power sample and hold
  - 2x operational amplifiers with built-in PGA
  - 2x ultra-low-power comparators
- 18x communication interfaces

  - USB OTG 2.0 full-speed, LPM and BCD
  - 2x SAIs (serial audio interface)
  - 3x I2C FM+(1 Mbit/s), SMBus/PMBus
  - 6x USARTs (ISO 7816, LIN, IrDA, modem)
  - 3x SPIs (4x SPIs with the Quad SPI)
  - CAN (2.0B Active) and SDMMC interface
  - SWPMI single wire protocol master I/F
- 14-channel DMA controller
- True random number generator
- CRC calculation unit, 96-bit unique ID
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™

More information about STM32L476RG can be found here:

- [STM32L476RG on www.st.com](https://www.st.com/en/microcontrollers/stm32l476rg.html)
- [STM32L476 reference manual](https://www.st.com/resource/en/reference_manual/DM00083560.pdf)

### Supported Features

The Zephyr nucleo\_l476rg board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| PWM | on-chip | pwm |
| SPI | on-chip | spi |
| ADC | on-chip | ADC Controller |

Other hardware features are not yet supported on this Zephyr port.

The default configuration can be found in the defconfig file:
[boards/st/nucleo\_l476rg/nucleo\_l476rg\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_l476rg/nucleo_l476rg_defconfig)

### Connections and IOs

Nucleo L476RG Board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Available pins:

![Nucleo L476RG Arduino connectors](../../../../_images/nucleo_l476rg_arduino.jpg)
![Nucleo L476RG Morpho connectors](../../../../_images/nucleo_l476rg_morpho.jpg)

For more details please refer to [STM32 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/dm00105823.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PA9/PA10
- UART\_2 TX/RX : PA2/PA3 (ST-Link Virtual Port Com)
- UART\_3 TX/RX : PB10/PB11
- I2C\_1 SCL/SDA : PB8/PB9 (Arduino I2C)
- I2C\_3 SCL/SDA : PC0/PC1
- SPI\_1 CS/SCK/MISO/MOSI : PB6/PA5/PA6/PA7 (Arduino SPI)
- SPI\_2 CS/SCK/MISO/MOSI : PB12/PB13/PB14/PB15
- SPI\_3 CS/SCK/MISO/MOSI : PA15/PC10/PC11/PC12
- PWM\_2\_CH1 : PA0
- USER\_PB : PC13
- LD2 : PA5

#### System Clock

Nucleo L476RG System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at 80MHz,
driven by 16MHz high speed internal oscillator.

#### Serial Port

Nucleo L476RG board has 6 U(S)ARTs. The Zephyr console output is assigned to UART2.
Default settings are 115200 8N1.

## Programming and Debugging

Nucleo L476RG board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_l476rg` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to Nucleo L476RG

Connect the Nucleo L476RG to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b nucleo_l476rg samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_l476rg samples/hello_world
west debug
```

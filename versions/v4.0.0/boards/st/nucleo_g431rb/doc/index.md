---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/st/nucleo_g431rb/doc/index.html
original_path: boards/st/nucleo_g431rb/doc/index.html
---

# Nucleo G431RB

Board Overview

[![../../../../_images/nucleo_g431rb.jpg](../../../../_images/nucleo_g431rb.jpg)
](../../../../_images/nucleo_g431rb.jpg)

Nucleo G431RB

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32g431xx

## Overview

The Nucleo G431RB board features an ARM Cortex-M4 based STM32G431RB MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the Nucleo G431RB board:

- STM32 microcontroller in LQFP64 package
- Arduino Uno V3 connectivity
- On-board ST-LINK/V3E debugger/programmer with SWD connector
- Flexible board power supply:

  - USB VBUS or external source(3.3V, 5V, 7 - 12V)
  - Power management access point
- Three LEDs: USB communication (LD1), power LED (LD3), user LED (LD2)
- Two push-buttons: RESET and USER

More information about the board can be found at the [Nucleo G431RB website](https://www.st.com/en/evaluation-tools/nucleo-g431rb.html).

## Hardware

The STM32G431RB SoC provides the following hardware IPs:

- Ultra-low-power with FlexPowerControl (down to 28 nA Standby mode and 84
  µA/MHz run mode)
- Core: ARM® 32-bit Cortex® -M4 CPU with FPU, frequency up to 170 MHz
- Clock Sources:

  - 4 to 48 MHz crystal oscillator (HSE)
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC ( ±1%)
  - Internal low-power 32 kHz RC ( ±5%)
  - 2 PLLs for system clock, USB, audio, ADC
- RTC with HW calendar, alarms and calibration
- 14x timers:

  - 1x 32-bit timer and 2x 16-bit timers with up to four IC/OC/PWM or pulse counter and quadrature (incremental) encoder input
  - 2x 16-bit 8-channel advanced motor control timers, with up to 8x PWM channels, dead time generation and emergency stop
  - 1x 16-bit timer with 2x IC/OCs, one OCN/PWM, dead time generation and emergency stop
  - 2x 16-bit timers with IC/OC/OCN/PWM, dead time generation and emergency stop
  - 2x watchdog timers (independent, window)
  - 2x 16-bit basic timers
  - SysTick timer
  - 1x low-power timer
- Up to 86 fast I/Os, most 5 V-tolerant
- Memories

  - Up to 128 KB single bank Flash, proprietary code readout protection
  - Up to 22 KB of SRAM including 16 KB with hardware parity check
- Rich analog peripherals (independent supply)

  - 2x 12-bit ADC 5 MSPS, up to 16-bit with hardware oversampling, 200
    µA/MSPS
  - 4x 12-bit DAC, low-power sample and hold
  - 3x operational amplifiers with built-in PGA
  - 4x ultra-fast rail-to-rail analog comparators
- 16x communication interfaces

  - 1 x FDCAN controller supporting flexible data rate
  - 3x I2C FM+(1 Mbit/s), SMBus/PMBus
  - 4x USARTs (ISO 7816, LIN, IrDA, modem)
  - 1x LPUART
  - 3x SPIs (2x with multiplexed half duplex I2S interface)
  - 1x SAI (serial audio interface)
  - USB 2.0 full-speed interface with LPM and BCD support
  - IRTIM (Infrared interface)
  - USB Type-C™ /USB power delivery controller (UCPD)
- 12-channel DMA controller
- True random number generator (RNG)
- CRC calculation unit, 96-bit unique ID
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell\*

More information about STM32G431RB can be found here:

- [STM32G431RB on www.st.com](https://www.st.com/en/microcontrollers/stm32g431rb.html)
- [STM32G4 reference manual](https://www.st.com/resource/en/reference_manual/dm00355726.pdf)

### Supported Features

The Zephyr nucleo\_g431rb board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| PWM | on-chip | pwm |
| DAC | on-chip | dac |
| COUNTER | on-chip | rtc |
| SPI | on-chip | spi |
| RNG | on-chip | rng |

Other hardware features are not yet supported on this Zephyr port.

The default configuration can be found in the defconfig file:
[boards/st/nucleo\_g431rb/nucleo\_g431rb\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_g431rb/nucleo_g431rb_defconfig)

### Connections and IOs

Nucleo G431RB Board has 6 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32G4 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/dm00556337.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PC4
- UART\_1\_RX : PC5
- LPUART\_1\_TX : PA2
- LPUART\_1\_RX : PA3
- I2C\_1\_SCL : PB8
- I2C\_1\_SDA : PB9
- SPI\_1\_NSS : PB6
- SPI\_1\_SCK : PA5
- SPI\_1\_MISO : PA6
- SPI\_1\_MOSI : PA7
- SPI\_2\_NSS : PB12
- SPI\_2\_SCK : PB13
- SPI\_2\_MISO : PB14
- SPI\_2\_MOSI : PB15
- SPI\_3\_NSS : PA15
- SPI\_3\_SCK : PC10
- SPI\_3\_MISO : PC11
- SPI\_3\_MOSI : PC12
- PWM\_3\_CH1 : PB4
- USER\_PB : PC13
- LD2 : PA5
- DAC1\_OUT1 : PA4

#### System Clock

Nucleo G431RB System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at 150MHz,
driven by 16MHz high speed internal oscillator. The clock can be boosted to 170MHz if boost mode
is selected.

#### Serial Port

Nucleo G431RB board has 3 U(S)ARTs and one LPUART. The Zephyr console output is assigned to LPUART1.
Default settings are 115200 8N1.

Please note that LPUART1 baudrate is limited to 9600 if the MCU is clocked by LSE (32.768 kHz) in
low power mode.

## Programming and Debugging

Nucleo G431RB board includes an ST-LINK/V3E embedded debug tool interface.

Applications for the `nucleo_g431rb` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner pyocd
```

pyOCD can be used after adding “pack” support with the following commands:

```shell
$ pyocd pack --update
$ pyocd pack --install stm32g431rb
```

#### Flashing an application to Nucleo G431RB

Connect the Nucleo G431RB to your host computer using the USB port,
then run a serial host program to connect with your Nucleo board.

```shell
$ minicom -D /dev/ttyACM0
```

Now build and flash an application. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.").

```shell
# From the root of the zephyr repository
west build -b nucleo_g431rb samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_g431rb samples/hello_world
west debug
```

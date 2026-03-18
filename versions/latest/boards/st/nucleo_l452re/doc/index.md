---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/st/nucleo_l452re/doc/index.html
original_path: boards/st/nucleo_l452re/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ST Nucleo L452RE

## Overview

The Nucleo L452RE(-P) boards feature an ARM Cortex-M4 based STM32L452RE MCU
with a wide range of connectivity support and configurations. There are two variants:

- ST Nucleo L452RE
- ST Nucleo L452RE-P

Here some highlights of these boards:

- STM32 microcontroller in LQFP64 package
- Arduino Uno V3 connectivity
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:

  - USB VBUS or external source(3.3V, 5V, 7 - 12V)
  - Power management access point
- Three LEDs: USB communication (LD1), user LED (LD2), power LED (LD3)
- One push-button: RESET

![Nucleo L452RE-P](../../../../_images/nucleo_l452re_p.jpg)

The main difference between the ST Nucleo L452RE and the L452RE-P (note the missing
“-P” at the end) lays in the External Switched Mode Power Supply (SMPS) included in
the P series.

More information about the boards can be found at the [Nucleo L452RE website](https://www.st.com/en/evaluation-tools/nucleo-l452re.html) and
the [Nucleo L452RE-P website](https://www.st.com/en/evaluation-tools/nucleo-l452re-p.html).

## Hardware

The STM32L452RE SoC provides the following hardware IPs:

- Ultra-low-power with FlexPowerControl (down to 28 nA Standby mode and 84
  µA/MHz run mode)
- Core: ARM® 32-bit Cortex® -M4 CPU with FPU, frequency up to 80 MHz,
  100DMIPS/1.25DMIPS/MHz (Dhrystone 2.1)
- Clock Sources:

  - 4 to 48 MHz crystal oscillator
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC ( ±1%)
  - Internal low-power 32 kHz RC ( ±5%)
  - Internal multispeed 100 kHz to 48 MHz oscillator, auto-trimmed by
    LSE (better than ±0.25 % accuracy)
  - 2 PLLs for system clock, USB, audio, ADC
- RTC with HW calendar, alarms and calibration
- Up to 3 capacitive sensing channels: support touchkey, linear and rotary touch sensors
- 12x timers:

  - 1x 16-bit advanced motor-control
  - 1x 32-bit and 3x 16-bit general purpose
  - 2x 16-bit basic
  - 2x low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - SysTick timer
- Up to 26 fast I/Os, most 5 V-tolerant
- Memories

  - Up to 512 KB single bank Flash, proprietary code readout protection
  - 160 KB of SRAM including 32 KB with hardware parity check
  - Quad SPI memory interface
- Rich analog peripherals (independent supply)

  - 1x 12-bit ADC 5 MSPS, up to 16-bit with hardware oversampling, 200
    µA/MSPS
  - 2x 12-bit DAC, low-power sample and hold
  - 1x operational amplifiers with built-in PGA
  - 2x ultra-low-power comparators
- 17x communication interfaces
  - USB 2.0 full-speed crystal less solution with LPM and BCD
  - 1x SAI (serial audio interface)
  - 4x I2C FM+(1 Mbit/s), SMBus/PMBus
  - 3x USARTs (ISO 7816, LIN, IrDA, modem)
  - 1x UART (LIN, IrDA, modem)
  - 1x LPUART (Stop 2 wake-up)
  - 3x SPIs (and 1x Quad SPI)
  - CAN (2.0B Active) and SDMMC interface
  - IRTIM (Infrared interface)
- 14-channel DMA controller
- True random number generator
- CRC calculation unit, 96-bit unique ID
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell\*

More information about STM32L452RE can be found here:

- [STM32L452RE on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32l452re.html)
- [STM32L452 reference manual](https://www.st.com/resource/en/reference_manual/dm00151940.pdf)

### Supported Features

The Zephyr nucleo\_l452re board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| PWM | on-chip | pwm |
| CAN | on-chip | can |

Note

CAN feature requires CAN transceiver

Other hardware features are not yet supported on this Zephyr port.

The default configuration can be found in the defconfig file:
[boards/st/nucleo\_l452re/nucleo\_l452re\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_l452re/nucleo_l452re_defconfig)

And for Nucleo L452RE-P in this defconfig file:
[boards/st/nucleo\_l452re/nucleo\_l452re\_stm32l452xx\_p\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_l452re/nucleo_l452re_stm32l452xx_p_defconfig)

### Connections and IOs

Nucleo L452RE Board has 6 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Available pins:

![Nucleo L452RE Pinout](../../../../_images/nucleo_l452re_pinout.jpg)
![Nucleo L452RE-P Pinout](../../../../_images/nucleo_l452re_p_pinout.jpg)

For more details please refer to [ST Nucleo L452RE User Manual](https://www.st.com/resource/en/user_manual/dm00105823.pdf) or
[ST Nucleo L452RE-P User Manual](https://www.st.com/resource/en/user_manual/dm00387966.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- UART\_2\_TX : PA2
- UART\_2\_RX : PA3
- I2C\_1\_SCL : PB8
- I2C\_1\_SDA : PB7
- PWM\_2\_CH1 : PA0
- SPI\_NSS : PB6
- SPI\_SCK : PA5
- SPI\_MISO : PA6
- SPI\_MOSI : PA7
- CAN\_TX : PA11
- CAN\_RX : PA12
- LD2 : PA5

#### System Clock

Nucleo L452RE System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at 80MHz,
driven by 16MHz high speed internal oscillator.

#### Serial Port

Nucleo L452RE board has 3 U(S)ARTs. The Zephyr console output is assigned to UART2.
Default settings are 115200 8N1.

## Programming and Debugging

Applications for the `nucleo_l452re` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Nucleo L452RE board includes an ST-LINK/V2-1 embedded debug tool
interface. This interface is supported by the openocd version
included in the Zephyr SDK since v0.9.2.

#### Flashing an application to Nucleo L452RE

Connect the Nucleo L452RE to your host computer using the USB port,
then run a serial host program to connect with your Nucleo board.

```shell
$ minicom -D /dev/ttyACM0
```

Now build and flash an application. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello-world).

```shell
# From the root of the zephyr repository
west build -b nucleo_l452re samples/hello_world
west flash
```

For Nucleo L452RE-P, use this command instead:

```shell
# From the root of the zephyr repository
west build -b nucleo_l452re/stm32l452xx/p samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b nucleo_l452re samples/hello_world
west debug
```

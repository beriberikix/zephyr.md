---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/blues/swan_r5/doc/index.html
original_path: boards/blues/swan_r5/doc/index.html
---

# Swan

Board Overview

[![../../../../_images/swan.jpg](../../../../_images/swan.jpg)
](../../../../_images/swan.jpg)

Swan

Name:
:   `swan_r5`

Vendor:
:   Blues Wireless

Architecture:
:   arm

SoC:
:   stm32l4r5xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/blues/swan_r5/doc/index.rst/../..)

## Overview

Swan is a low-cost embeddable STM32L4-based microcontroller designed to
accelerate the development and deployment of battery-powered solutions.
It is especially useful for applications requiring large memory or a high
degree of I/O expandability at an affordable cost, such as edge inferencing
and remote monitoring.

Uniquely for Feather-compatible boards, Swan is designed to satisfy
developers’ needs that span from early prototyping through high-volume
deployment. Developers may begin to use Swan in conjunction with
Adafruit’s myriad sensors and FeatherWing-compatible carriers.
Due to its novel design, for high-volume deployment the low-cost Swan
can also be soldered directly to a parent PCB integrating those sensors,
utilizing the full range of Swan’s I/O capabilities.

The board has three independent power options—USB, Battery, or Line
power—and provides a software-switchable 2 Amp regulator for powering external
sensors. When operating in its low-power operating mode, the entire Swan
board commonly draws only about 8uA while retaining all of its memory,
making it quite suitable for battery-powered devices.

The Swan board features an ARM Cortex-M4 based STM32L4R5ZI MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the board:

- STM32 microcontroller in WLCSP144 package
- 2MB of flash and 640KB of RAM
- Two types of extension resources:

  - Adafruit Feather-compatible connectivity
  - Access to 36 additional STM32 pins (beyond the Feather pins) via 0.05” castellated edge headers
- On-board ST-LINKV3 debugger/programmer with SWD connector
- One Red User LED (LD1)
- Two push-buttons: USER and RESET
- Castellated-edge access to 55 GPIO ports including:

  - 8 analog
  - 16 digital
  - 4x I2C, 3x SPI
  - USB OTG full speed
  - 1x 14-channel DMA
  - tRNG
  - 12-bit ADC, 2 x 12-bit DAC
  - low-power RTC, and CRC calculation peripherals

More information about the board can be found at the [Swan Product Page](https://blues.io/products/swan) [[1]](#id2).

## Hardware

The STM32L4R5ZI SoC provides the following hardware IPs:

- Ultra-low-power with FlexPowerControl (down to 130 nA Standby mode
  and 100 uA/MHz run mode)
- Core: ARM® 32-bit Cortex®-M4 CPU with FPU, adaptive
  real-time accelerator (ART Accelerator) allowing 0-wait-state
  execution from Flash memory, frequency up to 120 MHz, MPU, 150
  DMIPS/1.25 DMIPS/MHz (Dhrystone 2.1), and DSP instructions
- Memories

  - 2-Mbyte Flash, 2 banks read-while-write, proprietary code readout protection
  - 640 Kbytes of SRAM including 64 Kbytes with hardware parity check
  - External memory interface for static memories supporting SRAM,
    PSRAM, NOR, NAND and FRAM memories
  - 2 x OctoSPI memory interface
- True random number generator
- CRC calculation unit, 96-bit unique ID
- Development support: serial wire debug (SWD), JTAG, Embedded Trace
  Macrocell (ETM)

More information about Swan can be found here:

- [Swan Quickstart Guide](https://dev.blues.io/start/swan/swan-quickstart) [[2]](#id4)
- [Swan Datasheet](https://dev.blues.io/hardware/swan-datasheet/) [[3]](#id6)

### Supported Features

The `swan_r5` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

#### Default Zephyr Peripheral Mapping:

- A0 : PA3
- A1 : PA1
- A2 : PC3
- A3 : PC1
- A4 : PC4
- A5 : PC5
- D4 : PE3
- D5 : PE11
- D6 : PE9
- D9 : PD15
- D10 : PA4
- D11 : PA7
- D12 : PA6
- D13 : PA5
- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- UART\_2\_TX : PA2
- UART\_2\_RX : PD6
- UART\_3\_TX : PB10
- UART\_3\_RX : PB11
- LPUART\_TX : PG7
- LPUART\_RX : PG8
- I2C\_1\_SCL : PB6
- I2C\_1\_SDA : PB7
- I2C\_2\_SCL : PF1
- I2C\_2\_SDA : PF0
- I2C\_3\_SCL : PC0
- I2C\_3\_SDA : PC9
- SPI\_1\_NSS : PA4
- SPI\_1\_SCK : PA5
- SPI\_1\_MISO : PA6
- SPI\_1\_MOSI : PA7
- SPI\_2\_NSS : PD0
- SPI\_2\_SCK : PD1
- SPI\_2\_MISO : PB14
- SPI\_2\_MOSI : PB15
- SPI\_3\_NSS : PA15
- SPI\_3\_SCK : PC10
- SPI\_3\_MISO : PC11
- SPI\_3\_MOSI : PC12
- PWM\_2\_CH1 : PA0
- USER\_PB : PC13
- LD1 : PE2
- USB DM : PA11
- USB DP : PA12
- ADC1 : PA1

#### System Clock

Swan System Clock could be driven by internal or external
oscillator, as well as main PLL clock. By default, the System clock is
driven by the PLL clock at 80MHz, driven by a 16MHz high speed
internal oscillator.

#### Serial Port

Swan has 4 U(S)ARTs. The Zephyr console output is
assigned to LPUART. Default settings are 115200 8N1.

## Programming and Debugging

Connect Swan to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Swan:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b swan_r5 samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! arm
```

## References

[[1](#id3)]

[https://blues.io/products/swan](https://blues.io/products/swan)

[[2](#id5)]

[https://dev.blues.io/start/swan/swan-quickstart](https://dev.blues.io/start/swan/swan-quickstart)

[[3](#id7)]

[https://dev.blues.io/hardware/swan-datasheet/](https://dev.blues.io/hardware/swan-datasheet/)

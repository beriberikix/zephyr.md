---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_u5a5zj_q/doc/index.html
original_path: boards/st/nucleo_u5a5zj_q/doc/index.html
---

# Nucleo U5A5ZJ Q

Board Overview

Name:
:   `nucleo_u5a5zj_q`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32u5a5xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_u5a5zj_q/doc/index.rst/../..)

## Overview

The Nucleo U5A5ZJ Q board, featuring an ARM Cortex-M33 based STM32U5A5ZJ MCU,
provides an affordable and flexible way for users to try out new concepts and
build prototypes by choosing from the various combinations of performance and
power consumption features. Here are some highlights of the Nucleo U5A5ZJ Q
board:

- STM32U5A5ZJ microcontroller in LQFP144 package
- Internal SMPS to generate V core logic supply
- Two types of extension resources:

  - Arduino Uno V3 connectivity
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V3E debugger/programmer
- Flexible board power supply:

  - USB VBUS or external source(3.3V, 5V, 7 - 12V)
  - ST-Link V3E
- Three users LEDs
- Two push-buttons: USER and RESET
- USB Type-C ™ Sink device FS

## Hardware

The STM32U5A5xx devices are an ultra-low-power microcontrollers family (STM32U5
Series) based on the high-performance Arm® Cortex®-M33 32-bit RISC core.
They operate at a frequency of up to 160 MHz.

- Includes ST state-of-the-art patented technology
- Ultra-low-power with FlexPowerControl:

  - 1.71 V to 3.6 V power supply
  - -40 °C to +85/125 °C temperature range
  - Low-power background autonomous mode (LPBAM): autonomous peripherals with
    DMA, functional down to Stop 2 mode
  - VBAT mode: supply for RTC, 32 x 32-bit backup registers and 2-Kbyte backup SRAM
  - 150 nA Shutdown mode (24 wake-up pins)
  - 195 nA Standby mode (24 wake-up pins)
  - 480 nA Standby mode with RTC
  - 2 µA Stop 3 mode with 40-Kbyte SRAM
  - 8.2 µA Stop 3 mode with 2.5-Mbyte SRAM
  - 4.65 µA Stop 2 mode with 40-Kbyte SRAM
  - 17.5 µA Stop 2 mode with 2.5-Mbyte SRAM
  - 18.5 µA/MHz Run mode at 3.3 V
- Core:

  - Arm® 32-bit Cortex®-M33 CPU with TrustZone®, MPU, DSP,
    and FPU ART Accelerator
  - 32-Kbyte ICACHE allowing 0-wait-state execution from flash and external
    memories: frequency up to 160 MHz, 240 DMIPS
  - 16-Kbyte DCACHE1 for external memories
- Power management:

  - Embedded regulator (LDO) and SMPSstep-down converter supporting switch
    on-the-fly and voltage scaling
- Benchmarks:

  - 1.5 DMIPS/MHz (Drystone 2.1)
  - 655 CoreMark® (4.09 CoreMark®/MHz)
  - 369 ULPMark™-CP
  - 89 ULPMark™-PP
  - 47.2 ULPMark™-CM
  - 120000 SecureMark™-TLS
- Memories:

  - 4-Mbyte flash memory with ECC, 2 banks readwhile-write, including 512 Kbytes
    with 100 kcycles
  - With SRAM3 ECC off: 2514-Kbyte RAM including 66 Kbytes with ECC
  - With SRAM3 ECC on: 2450-Kbyte RAMincluding 322 Kbytes with ECC
  - External memory interface supporting SRAM,PSRAM, NOR, NAND, and FRAM memories
  - 2 Octo-SPI memory interfaces
  - 16-bit HSPI memory interface up to 160 MHz
- Rich graphic features:

  - Neo-Chrom GPU (GPU2D) accelerating any angle rotation, scaling, and
    perspective correct texture mapping
  - 16-Kbyte DCACHE2
  - Chrom-ART Accelerator (DMA2D) for smoothmotion and transparency effects
  - Chrom-GRC (GFXMMU) allowing up to 20 % of graphic resources optimization
  - MIPI® DSI host controller with two DSI lanes running at up to 500 Mbit/s each
  - LCD-TFT controller (LTDC)
  - Digital camera interface
- General-purpose input/outputs:

  - Up to 156 fast I/Os with interrupt capability most 5V-tolerant and
    up to 14 I/Os with independent supply down to 1.08 V
- Clock management:

  - 4 to 50 MHz crystal oscillator
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC (± 1 %)
  - Internal low-power 32 kHz RC (± 5 %)
  - 2 internal multispeed 100 kHz to 48 MHz oscillators, including one
    autotrimmed by LSE (better than ± 0.25 % accuracy)
  - Internal 48 MHz
  - 5 PLLs for system clock, USB, audio, ADC, DSI
- Security and cryptography:

  - SESIP3 and PSA Level 3 Certified Assurance Target
  - Arm® TrustZone® and securable I/Os, memories, and peripherals
  - Flexible life cycle scheme with RDP andpassword-protected debug
  - Root of trust thanks to unique boot entry and secure hide-protection area (HDP)
  - Secure firmware installation (SFI) thanks to embedded root secure services (RSS)
  - Secure data storage with hardware unique key (HUK)
  - Secure firmware upgrade support with TF-M
  - 2 AES coprocessors including one with DPA resistance
  - Public key accelerator, DPA resistant
  - On-the-fly decryption of Octo-SPI external memories
  - HASH hardware accelerator
  - True random number generator, NIST SP800-90B compliant
  - 96-bit unique ID
  - 512-byte OTP (one-time programmable)
  - Active tampers
- Up to 17 timers, 2 watchdogs and RTC:

  - 19 timers: 2 16-bit advanced motor-control, 4 32-bit, 3 16-bit general
    purpose, 2 16-bit basic, 4 low-power 16-bit (available in Stop mode),
    2 SysTick timers, and 2 watchdogs
  - RTC with hardware calendar, alarms, and calibration
- Up to 25 communication peripherals:

  - 1 USB Type-C®/USB power delivery controller
  - 1 USB OTG high-speed with embedded PHY
  - 2 SAIs (serial audio interface)
  - 6 I2C FM+(1 Mbit/s), SMBus/PMBus™
  - 7 USARTs (ISO 7816, LIN, IrDA, modem)
  - 3 SPIs (6x SPIs with OCTOSPI/HSPI)
  - 1 CAN FD controller
  - 2 SDMMC interfaces
  - 1 multifunction digital filter (6 filters) + 1 audio digital filter
    with sound-activity detection
  - Parallel synchronous slave interface
- Mathematical coprocessor:

  - CORDIC for trigonometric functions acceleration
  - FMAC (filter mathematical accelerator)
- Rich analog peripherals (independent supply):

  - 2 14-bit ADC 2.5-Msps with hardware oversampling
  - 1 12-bit ADC 2.5-Msps, with hardware oversampling, autonomous in Stop 2 mode
  - 12-bit DAC (2 channels), low-power sample, and hold, autonomous in Stop 2 mode
  - 2 operational amplifiers with built-in PGA
  - 2 ultra-low-power comparators
- ECOPACK2 compliant packages

More information about STM32U5A5ZJ can be found here:

- [STM32U5A5ZJ on www.st.com](https://www.st.com/en/microcontrollers/stm32u5a5zj.html)
- [STM32U5A5 reference manual](https://www.st.com/resource/en/reference_manual/rm0456-stm32u5-series-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `nucleo_u5a5zj_q` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

Nucleo U5A5ZJ Q Board has 10 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.

For more details please refer to [STM32 Nucleo-144 board User Manual](https://www.st.com/resource/en/user_manual/um2861-stm32u5-nucleo144-board-mb1549-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

- CAN/CANFD\_TX: PD1
- CAN/CANFD\_RX: PD0
- DAC1\_OUT1 : PA4
- I2C\_1\_SCL : PB8
- I2C\_1\_SDA : PB9
- I2C\_2\_SCL : PF1
- I2C\_2\_SDA : PF0
- LD1 : PC7
- LD2 : PB7
- LD3 : PG2
- LPUART\_1\_TX : PG7
- LPUART\_1\_RX : PG8
- SPI\_1 nCS (GPIO) : PD14
- SPI\_1\_SCK : PA5
- SPI\_1\_MISO : PA6
- SPI\_1\_MOSI : PA7
- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- UART\_2\_TX : PD5
- UART\_2\_RX : PD6
- USER\_PB : PC13
- USB\_DM : PA11
- USB\_DP : PA12

#### System Clock

Nucleo U5A5ZJ Q System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
160MHz, driven by the 16MHz high speed oscillator.

#### Serial Port

Nucleo U5A5ZJ Q board has 6 U(S)ARTs. The Zephyr console output is assigned to
USART1. Default settings are 115200 8N1.

#### Backup SRAM

In order to test backup SRAM you may want to disconnect VBAT from VDD. You can
do it by removing `SB50` jumper on the back side of the board.

#### Using USB

USB 2.0 high speed (HS) operation requires the HSE clock source to be populated
and enabled. The Nucleo U5A5ZJ-Q includes the 16MHz oscillator and required
jumper settings.

## Programming and Debugging

Nucleo U5A5ZJ-Q board includes an ST-LINK/V3 embedded debug tool interface.
This probe allows to flash the board using various tools.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD, JLink, or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
$ west flash --runner pyocd
```

For pyOCD, additional target information needs to be installed.
This can be done by executing the following commands.

```shell
$ pyocd pack --update
$ pyocd pack --install stm32u5
```

#### Flashing an application to Nucleo U5A5ZJ Q

Connect the Nucleo U5A5ZJ Q to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b nucleo_u5a5zj_q samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! arm
```

### Debugging

Default flasher for this board is openocd. It could be used in the usual way.
Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_u5a5zj_q samples/basic/blinky
west debug
```

Note: Check the `build/tfm` directory to ensure that the commands required by these scripts
(`readlink`, etc.) are available on your system. Please also check `STM32_Programmer_CLI`
(which is used for initialization) is available in the PATH.

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/microchip/mec1501modular_assy6885/doc/index.html
original_path: boards/microchip/mec1501modular_assy6885/doc/index.html
---

# MEC1501 Modular card ASSY6885

Board Overview

[![../../../../_images/mec1501modular_assy6885.jpg](https://docs.zephyrproject.org/4.1.0/_images/mec1501modular_assy6885.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/mec1501modular_assy6885.jpg)

MEC1501 Modular card ASSY6885

Name:
:   `mec1501modular_assy6885`

Vendor:
:   Microchip Technology Inc.

Architecture:
:   arm

SoC:
:   mec1501\_hsz

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/mec1501modular_assy6885/doc/index.rst/../..)

## Overview

The MEC1501 Modular card ASSY6885 is a development board to evaluate the Microchip
MEC152X series microcontrollers. This board can work standalone or be mated with
any platform that complies with MECC specification.

## Hardware

- MEC1521HA0SZ ARM Cortex-M4 Processor
- 256 KB RAM and 64 KB boot ROM
- GPIO headers
- UART1 using microUSB
- PECI interface 3.0
- 10 SMBUS instances
- FAN, PMW and TACHO pins
- VCI interface
- Independent Hardware Driven PS/2 Ports

At difference from MEC15xx evaluation board, modular MEC1521 exposes the pins
in 2 different ways:

1. Standalone mode via headers

   - GPIOs
   - PWM5
   - JTAG/SWD, ETM and MCHP Trace ports
   - eSPI bus
   - SMB0
2. Mated mode with another platform that has a high density MECC connector.

   - FAN0, PWM0, SMB0, SMB1, SMB4 and SMB5
   - eSPI bus
   - Breathing/Blinking LEDs

The board is powered through the +5V USB Micro A connector or from the MECC connector.

For more information about the SOC please see the [MEC152x Reference Manual](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC152x/MEC152x_Datasheet.pdf) [[1]](#id2)

### Supported Features

The `mec1501modular_assy6885` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mec1501modular_assy6885/mec1501_hsz` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L19) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | Microchip XEC ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L436) | [`microchip,xec-adc`](../../../../build/dts/api/bindings/adc/microchip%2Cxec-adc.md#std-dtcompatible-microchip-xec-adc) |
| Clock control | on-chip | Microchip XEC Power Clock Reset and VBAT register (PCR)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L63) | [`microchip,xec-pcr`](../../../../build/dts/api/bindings/clock/microchip%2Cxec-pcr.md#std-dtcompatible-microchip-xec-pcr) |
| ESPI | on-chip | Microchip ESPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L276) | [`microchip,xec-espi`](../../../../build/dts/api/bindings/espi/microchip%2Cxec-espi.md#std-dtcompatible-microchip-xec-espi) |
| on-chip | Microchip ESPI SAF controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L284) | [`microchip,xec-espi-saf`](../../../../build/dts/api/bindings/espi/microchip%2Cxec-espi-saf.md#std-dtcompatible-microchip-xec-espi-saf) |
| GPIO & Headers | on-chip | Microchip CEC/MEC GPIO node[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L98) | [`microchip,xec-gpio`](../../../../build/dts/api/bindings/gpio/microchip%2Cxec-gpio.md#std-dtcompatible-microchip-xec-gpio) |
| Hardware information | on-chip | Microchip EC Subsystem[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L59) | [`microchip,xec-ecs`](../../../../build/dts/api/bindings/hwinfo/microchip%2Cxec-ecs.md#std-dtcompatible-microchip-xec-ecs) |
| I2C | on-chip | Microchip I2C/SMB controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L211)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L237) | [`microchip,xec-i2c`](../../../../build/dts/api/bindings/i2c/microchip%2Cxec-i2c.md#std-dtcompatible-microchip-xec-i2c) |
| Input | on-chip | Microchip XEC keyboard matrix controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L447) | [`microchip,xec-kbd`](../../../../build/dts/api/bindings/input/microchip%2Cxec-kbd.md#std-dtcompatible-microchip-xec-kbd) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| Memory controller | on-chip | Microchip, XEC family Battery Backed RAM node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L165) | [`microchip,xec-bbram`](../../../../build/dts/api/bindings/memory-controllers/microchip%2Cxec-bbram.md#std-dtcompatible-microchip-xec-bbram) |
| PECI | on-chip | Microchip XEC PECI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L457) | [`microchip,xec-peci`](../../../../build/dts/api/bindings/peci/microchip%2Cxec-peci.md#std-dtcompatible-microchip-xec-peci) |
| Pin control | on-chip | Microchip XEC Pin controller Node Based on pincfg-node.yaml binding[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L92) | [`microchip,xec-pinctrl`](../../../../build/dts/api/bindings/pinctrl/microchip%2Cxec-pinctrl.md#std-dtcompatible-microchip-xec-pinctrl) |
| PS/2 | on-chip | Microchip XEC PS/2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L353) | [`microchip,xec-ps2`](../../../../build/dts/api/bindings/ps2/microchip%2Cxec-ps2.md#std-dtcompatible-microchip-xec-ps2) |
| PWM | on-chip | Microchip XEC PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L373)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L380) | [`microchip,xec-pwm`](../../../../build/dts/api/bindings/pwm/microchip%2Cxec-pwm.md#std-dtcompatible-microchip-xec-pwm) |
| RTC | on-chip | Microchip XEC basic timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L333)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L294) | [`microchip,xec-timer`](../../../../build/dts/api/bindings/rtc/microchip%2Cxec-timer.md#std-dtcompatible-microchip-xec-timer) |
| Serial controller | on-chip | Microchip XEC UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L188)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L177) | [`microchip,xec-uart`](../../../../build/dts/api/bindings/serial/microchip%2Cxec-uart.md#std-dtcompatible-microchip-xec-uart) |
| SPI | on-chip | Microchip XEC QMSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L466) | [`microchip,xec-qmspi`](../../../../build/dts/api/bindings/spi/microchip%2Cxec-qmspi.md#std-dtcompatible-microchip-xec-qmspi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L45) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Tachometer | on-chip | Microchip XEC tachometer controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L483)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L493) | [`microchip,xec-tach`](../../../../build/dts/api/bindings/tach/microchip%2Cxec-tach.md#std-dtcompatible-microchip-xec-tach) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | Microchip XEC RTOS timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L159) | [`microchip,xec-rtos-timer`](../../../../build/dts/api/bindings/timer/microchip%2Cxec-rtos-timer.md#std-dtcompatible-microchip-xec-rtos-timer) |
| Watchdog | on-chip | Microchip XEC watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec1501hsz.dtsi?plain=1#L170) | [`microchip,xec-watchdog`](../../../../build/dts/api/bindings/watchdog/microchip%2Cxec-watchdog.md#std-dtcompatible-microchip-xec-watchdog) |

### Connections and IOs

This evaluation board kit is comprised of the following HW blocks:

- MEC1501 Modular Card ASSY 6885 Rev A0 [MEC1501 Modular EC Card - Assy\_6885 Rev A0p1](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/MEC1501%20Modular%20EC%20Card%20-%20Assy_6885%20Rev%20A0p1%20-%20SCH.pdf) [[2]](#id4)

### System Clock

The MEC1501 MCU is configured to use the 48Mhz internal oscillator with the
on-chip PLL to generate a resulting EC clock rate of 12 MHz. See Processor clock
control register in chapter 4 “4.0 POWER, CLOCKS, and RESETS” of the data sheet in
the references at the end of this document.

### Serial Port

UART1 is configured for serial logs.

## Jumper settings

Please follow the jumper settings below to properly demo this
board. Advanced users may deviate from this recommendation.

### Jumper setting for MEC1501 Modular Assy 6885 Rev A1p0

#### Power-related jumpers

If you wish to power from type A/B connector `P10` set the jumper `JP35 1-2`.

If you wish to power through MECC connector `P1` and mate to external platform,
set the jumper to `JP35 3-4`.

Note

A single jumper is required in JP35.

| JP30 VTR3 | JP31 VTR\_PLL | JP32 VTR\_REG | JP33 VTR1 | JP34 VTR2 | JP40 3.3V | JP21 VREF\_ADC |
| --- | --- | --- | --- | --- | --- | --- |
| 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 |

| JP6 VBAT | JP36 VTR\_ANALOG | JP27 PECI | JP4 VREF\_VTT |
| --- | --- | --- | --- |
| 2-3 | 1-2 | 2-3 | open |

These jumpers configure nRESETI and JTAG\_STRAP respectively.

| JP22 (nRESETI) | JP29 (JTAG\_STRAP) |
| --- | --- |
| 11-12 | 1-2 |

#### Boot-ROM Straps

These jumpers configure MEC1501 Boot-ROM straps.

| JP37 (CMP\_STRAP) | J6 (CR\_STRAP) | JP41 (VTR2\_STRAP) | JP23 (BSS\_STRAP) |
| --- | --- | --- | --- |
| 1-2 | 1-2 | 1-2 | 3-4 |

`JP23 3-4` pulls SHD SPI CS0# up to VTR2. MEC1501 Boot-ROM samples
SHD SPI CS0# and if high, it loads code from SHD SPI.
This is the recommended setup.

| CR\_STRAP | BSS\_STRAP | SOURCE |
| --- | --- | --- |
| 0 | X | Use 3.3V Private SPI |
| 1 | 0 | Use eSPI Flash channel |
|  | 1 | Use 3.3V Shared channel(R) |

#### Power management

`JP20 2-3` is required so all GPIOs powered by VTR3 rail worked at 1.8V.

Note

External 1.8V needs to be connected to JP13.1

| JP20 (VTR3 selection) | JP13 (1.8V source) |
| --- | --- |
| 2-3 | 1.8V to pin 1 |

#### Jumper location map

```text
+--------------------------------------------------------------------------------------+
|                  |------------|                     +----------+ J10              || |
|  [BT1]       +   +------------+ J50                                      ++   ++  || |
|              |                                           JP38 JP43       ++   ||  || |
|              +         +      +       +-+ JP4              +    +       JP26  ||  || |
|             JP6        +      +                  +      +  + +  + +           ||  || |
|    JP31 ++            JP32   JP36     +-+ JP27   +      +    +    +           J6  || |
|                                                 JP18  JP37 JP41 JP42              ++ |
|         ++                  +   +    +--------+                                  J48 |
|         ||  JP21            +   +    +--------+ JP22    +----------+                 |
|      J2 ||   +            JP34 JP30                         J11              ++      |
|         ++   +                                                  J44          ||      |
|                            ++                         +----------------+     ||      |
|       +---------------+    ||  +        JP24          |----------------|     ++      |
|       |---------------|    ++  +    +----------+      +----------------+    J47      |
| JP20  +---------------+  JP23  JP40 +----------+                                  ++ |
|                                                     +           ++ JP29           || |
|                             +  +    +----------+    +                             || |
|    J52+---------------+     +  +    +----------+   J5   +-------------+           ++ |
|    J45+---------------+  JP33 TP57      JP25            +-------------+ J4       J49 |
|                                                                                      |
| ++                                           TP4   +----------+   ++                 |
| ++     +    +      +    +    +       +  TP61         +----------+   ++               |
| JP28   +    +      +    +    +  TP65 +  TP60            J51        JP35              |
|      TP58 JP16   JP11 JP13 JP15     JP10                                             |
| TP5                                                                                  |
| TP6                                        TP1                                       |
+--------------------------------------------------------------------------------------+
```

## Programming and Debugging

### Setup

1. Clone the [MEC152x SPI Image Gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI_image_gen) [[3]](#id6) repository or download the files within
   that directory. For the pre-production MEC150x use the [MEC150x SPI Image Gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC1501/SPI_image_gen) [[4]](#id9)
   repository.
2. Make the image generation available for Zephyr, by making the tool
   searchable by path, or by setting an environment variable
   `EVERGLADES_SPI_GEN`, for example:

   ```shell
   export EVERGLADES_SPI_GEN=<path to tool>/everglades_spi_gen_RomE
   ```

   Note that the tools for Linux and Windows have different file names.
   For the pre-production MEC1501 SOC use everglades\_spi\_gen\_lin64.
3. If needed, a custom SPI image configuration file can be specified
   to override the default one.

   ```shell
   export EVERGLADES_SPI_CFG=custom_spi_cfg.txt
   ```

### Building

1. Build [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application as you would normally do.
2. Once you have `zephyr.bin`, use the [MEC152x SPI Image Gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI_image_gen) [[3]](#id6) microchip tool
   to create the final binary. You need the output from this tool to flash
   in the SHD SPI memory.

### Flashing

1. Connect Dediprog into header `J2`.
2. Flash the SPI NOR `U3` at offset 0x0 using Dediprog SF100
   or a similar tool for flashing SPI chips.
3. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
4. Connect the MEC1501MODULAR\_ASSY6885 board to your host computer using the
   UART1 port and apply power.

   You should see `"Hello World! mec1501modular_assy6885"` in your terminal.

### Debugging

This board comes with a Cortex ETM port which facilitates tracing and debugging
using a single physical connection. In addition, it comes with sockets for
JTAG only sessions.

### HW Issues

In case you don’t see your application running, please make sure `LED1` is lit.
If is off, then check the power related jumpers again.

## References

[[1](#id3)]

[https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC152x/MEC152x\_Datasheet.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC152x/MEC152x_Datasheet.pdf)

[[2](#id5)]

[https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/MEC1501%20Modular%20EC%20Card%20-%20Assy\_6885%20Rev%20A0p1%20-%20SCH.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/MEC1501%20Modular%20EC%20Card%20-%20Assy_6885%20Rev%20A0p1%20-%20SCH.pdf)

[3]
([1](#id7),[2](#id8))

[https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI\_image\_gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI_image_gen)

[[4](#id10)]

[https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC1501/SPI\_image\_gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC1501/SPI_image_gen)

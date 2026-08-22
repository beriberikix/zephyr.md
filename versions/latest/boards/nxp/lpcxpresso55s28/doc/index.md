---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/lpcxpresso55s28/doc/index.html
original_path: boards/nxp/lpcxpresso55s28/doc/index.html
---

# LPCXpresso55S28

Board Overview

[![../../../../_images/LPC55S28-EVK.jpg](../../../../_images/LPC55S28-EVK.jpg)
](../../../../_images/LPC55S28-EVK.jpg)

LPCXpresso55S28

Name:
:   `lpcxpresso55s28`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   lpc55s28

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/lpcxpresso55s28/doc/index.rst/../..)

## Overview

The LPCXpresso55S28 development board provides the ideal platform for evaluation
of and development with the LPC552x/S2x MCU based on the Arm® Cortex®-M33
architecture. The board includes a high-performance onboard debug probe, audio
subsystem and accelerometer, with several options for adding off-the-shelf
add-on boards for networking, sensors, displays, and other interfaces.

## Hardware

- LPC55S28 Arm® Cortex®-M33 microcontroller running at up to 150 MHz
- 512 KB flash and 256 KB SRAM on-chip
- Onboard, high-speed USB, Link2 debug probe with CMSIS-DAP and SEGGER J-Link
  protocol options
- UART and SPI port bridging from LPC55S28 target to USB via the onboard debug
  probe
- Hardware support for external debug probe
- 3 x user LEDs, plus Reset, ISP (3) and user buttons
- Micro SD card slot (4-bit SDIO)
- NXP MMA8652FCR1 accelerometer
- Stereo audio codec with line in/out
- High and full speed USB ports with micro A/B connector for host or device
  functionality
- MikroEletronika Click expansion option
- LPCXpresso-V3 expansion option compatible with Arduino UNO
- PMod compatible expansion / host connector

For more information about the LPC55S28 SoC and LPCXPresso55S28 board, see:

- [LPC55S28 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc552x-s2x-mainstream-arm-cortex-m33-based-microcontroller-family:LPC552x-S2x)
- [LPC55S28 Datasheet](https://www.nxp.com/docs/en/nxp/data-sheets/LPC55S2x_LPC552x_DS.pdf)
- [LPC55S28 User Manual](https://www.nxp.com/webapp/Download?colCode=UM11126)
- [LPCXpresso55S28 Website](https://www.nxp.com/design/software/development-software/lpcxpresso55s28-development-board:LPC55S28-EVK)
- [LPCXpresso55S28 User Manual](https://www.nxp.com/webapp/Download?colCode=UM11158)
- [LPCXpresso55S28 Development Board Design Files](https://www.nxp.com/webapp/Download?colCode=LPCXpresso55S69-DS)

### Supported Features

The `lpcxpresso55s28` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `lpcxpresso55s28/lpc55s28` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L30) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L300) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp%2Clpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| ARM architecture | on-chip | LPC Flexcomm node[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L196) | [`nxp,lpc-flexcomm`](../../../../build/dts/api/bindings/arm/nxp%2Clpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L88) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp%2Clpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| DMA | on-chip | NXP LPC DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L169)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L178) | [`nxp,lpc-dma`](../../../../build/dts/api/bindings/dma/nxp%2Clpc-dma.md#std-dtcompatible-nxp-lpc-dma) |
| Flash controller | on-chip | NXP (In-Application Programming) flash memory controller for the lpc55xxx family, except lpc553x[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x.dtsi?plain=1#L21) | [`nxp,iap-fmc55`](../../../../build/dts/api/bindings/flash_controller/nxp%2Ciap-fmc55.md#std-dtcompatible-nxp-iap-fmc55) |
| GPIO & Headers | on-chip | LPC GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L134) | [`nxp,lpc-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio.md#std-dtcompatible-nxp-lpc-gpio) |
| on-chip | LPC GPIO port device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L140) | [`nxp,lpc-gpio-port`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port) |
| on-board | GPIO pins exposed on Mikro BUS headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s28/lpcxpresso55s28_common.dtsi?plain=1#L38) | [`mikro-bus`](../../../../build/dts/api/bindings/gpio/mikro-bus.md#std-dtcompatible-mikro-bus) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s28/lpcxpresso55s28_common.dtsi?plain=1#L61) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| Hardware information | on-chip | NXP LPC 128-bit Unique identifier[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L112) | [`nxp,lpc-uid`](../../../../build/dts/api/bindings/hwinfo/nxp%2Clpc-uid.md#std-dtcompatible-nxp-lpc-uid) |
| I2C | on-chip | LPC I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L223) | [`nxp,lpc-i2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpc-i2c.md#std-dtcompatible-nxp-lpc-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s28/lpcxpresso55s28.dts?plain=1#L38) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | NXP Pin interrupt and pattern match engine (PINT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L157) | [`nxp,pint`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cpint.md#std-dtcompatible-nxp-pint) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s28/lpcxpresso55s28_common.dtsi?plain=1#L19) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L36) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L105) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s28/lpcxpresso55s28.dts?plain=1#L103) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | LPC I/O Pin Configuration (IOCON)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L123) | [`nxp,lpc-iocon`](../../../../build/dts/api/bindings/pinctrl/nxp%2Clpc-iocon.md#std-dtcompatible-nxp-lpc-iocon) |
| on-chip | LPC pinctrl node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L129) | [`nxp,lpc-iocon-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Clpc-iocon-pinctrl.md#std-dtcompatible-nxp-lpc-iocon-pinctrl) |
| PWM | on-chip | NXP SCTimer PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L259) | [`nxp,sctimer-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Csctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm) |
| Reset controller | on-chip | LPC SYSCON Peripheral reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L92) | [`nxp,lpc-syscon-reset`](../../../../build/dts/api/bindings/reset/nxp%2Clpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset) |
| RNG | on-chip | LPC RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L286) | [`nxp,lpc-rng`](../../../../build/dts/api/bindings/rng/nxp%2Clpc-rng.md#std-dtcompatible-nxp-lpc-rng) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s28/lpcxpresso55s28_common.dtsi?plain=1#L108) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp%2Cfxos8700.md#std-dtcompatible-nxp-fxos8700) |
| Serial controller | on-chip | LPC USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L187) | [`nxp,lpc-usart`](../../../../build/dts/api/bindings/serial/nxp%2Clpc-usart.md#std-dtcompatible-nxp-lpc-usart) |
| SPI | on-chip | NXP LPC SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L269) | [`nxp,lpc-spi`](../../../../build/dts/api/bindings/spi/nxp%2Clpc-spi.md#std-dtcompatible-nxp-lpc-spi) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L54) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | NXP LPCIP3511 USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L316) | [`nxp,lpcip3511`](../../../../build/dts/api/bindings/usb/nxp%2Clpcip3511.md#std-dtcompatible-nxp-lpcip3511) |
| on-chip | NXP OHCI USB host controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L324) | [`nxp,uhc-ohci`](../../../../build/dts/api/bindings/usb/nxp%2Cuhc-ohci.md#std-dtcompatible-nxp-uhc-ohci) |
| on-chip | NXP IP3516HS USB host controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L332) | [`nxp,uhc-ip3516hs`](../../../../build/dts/api/bindings/usb/nxp%2Cuhc-ip3516hs.md#std-dtcompatible-nxp-uhc-ip3516hs) |
| on-chip | NXP USB High Speed PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L339) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp%2Cusbphy.md#std-dtcompatible-nxp-usbphy) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S2x_common.dtsi?plain=1#L292) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp%2Clpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |

Note

For additional features not yet supported, please also refer to the
[LPCXPRESSO55S69](../../lpcxpresso55s69/doc/index.md#lpcxpresso55s69) , which is the superset board in NXP’s LPC55xx series.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the lpcxpresso55s69 board may have additional features
already supported, which can also be re-used on this board.

### Connections and IOs

The LPC55S28 SoC has IOCON registers, which can be used to configure
the functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_26 | SPI | SPI MOSI |
| PIO0\_29 | USART | USART RX |
| PIO0\_30 | USART | USART TX |
| PIO1\_1 | SPI | SPI SSEL |
| PIO1\_2 | SPI | SPI SCK |
| PIO1\_3 | SPI | SPI MISO |
| PIO1\_4 | GPIO | RED LED |
| PIO1\_6 | GPIO | BLUE\_LED |
| PIO1\_7 | GPIO | GREEN LED |
| PIO1\_20 | I2C | I2C SCL |
| PIO1\_21 | I2C | I2C SDA |

### System Clock

The LPC55S28 SoC is configured to use PLL1 clocked from the external 24MHz
crystal, running at 144MHz as a source for the system clock. When the flash
controller is enabled, the core clock will be reduced to 96MHz. The application
may reconfigure clocks after initialization, provided that the core clock is
always set to 96MHz when flash programming operations are performed.

### Serial Port

The LPC55S28 SoC has 8 FLEXCOMM interfaces for serial communication. One is
configured as USART for the console and the remaining are not used.

## Programming and Debugging

The `lpcxpresso55s28` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ |  | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

LinkServer is the default runner for this board.
A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the integrated [MCU-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-onboard-debug-probe)
in the CMSIS-DAP mode. To use this probe with Zephyr, you need to install the
[LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your search path.
Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging) for additional
information.

The integrated MCU-Link hardware can also be used as a J-Link probe with a
firmware update, as described in [MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
The [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) should be available in this case.

### Configuring a Console

Connect a USB cable from your PC to P6, and use the serial terminal of your
choice (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s28 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v2.4.0 *****
Hello World! lpcxpresso55s28
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s28 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS zephyr-v2.4.0 *****
Hello World! lpcxpresso55s28
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

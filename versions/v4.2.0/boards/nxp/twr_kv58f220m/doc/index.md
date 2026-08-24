---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/twr_kv58f220m/doc/index.html
original_path: boards/nxp/twr_kv58f220m/doc/index.html
---

# TWR-KV58F220M

Board Overview

[![../../../../_images/twr_kv58f220m.jpg](https://docs.zephyrproject.org/4.2.0/_images/twr_kv58f220m.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/twr_kv58f220m.jpg)

TWR-KV58F220M

Name:
:   `twr_kv58f220m`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mkv58f24

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/twr_kv58f220m/doc/index.rst/../..)

## Overview

The TWR-KV58F220M is a development board for NXP Kinetis KV5x 32-bit
MCU-based platforms. The onboard OpenSDAv2 serial and debug adapter,
running an open source bootloader, offers options for serial
communication, flash programming, and run-control debugging.

## Hardware

- MKV58F1M0VLQ24 MCU (up to 240 MHz, 1 MB flash memory, 256 KB RAM,
  and 144 Low profile Quad Flat Package (LQFP))
- 1.8 V or 3.3 V MCU operation
- 6-axis FXOS8700CQ digital accelerometer and magnetometer
- Four user LEDs
- Four user push-buttons
- Potentiometer
- Two general purpose TWRPI headers
- Motor pin header

For more information about the KV5x SoC and the TWR-KV58F220M board, see
these NXP reference documents:

- [KV5x Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/general-purpose-mcus/kv-series-cortex-m4-m0-plus-m7/kinetis-kv5x-240-mhz-motor-control-and-power-conversion-ethernet-mcus-based-on-arm-cortex-m7:KV5x)
- [KV5x Datasheet](https://www.nxp.com/docs/en/data-sheet/KV5XP144M240.pdf)
- [KV5x Reference Manual](https://www.nxp.com/webapp/Download?colCode=KV5XP144M240RM)
- [TWR-KV58F220M Website](https://www.nxp.com/TWR-KV58F220M)
- [TWR-KV58F220M User Guide](https://www.nxp.com/webapp/Download?colCode=TWRKV58F220MUG)
- [TWR-KV58F220M Schematics](https://www.nxp.com/webapp/Download?colCode=TWR-KV58F220M-SCH)

### Supported Features

The `twr_kv58f220m` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `twr_kv58f220m/mkv58f24` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L23) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | Kinetis ADC16[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L99) | [`nxp,kinetis-adc16`](../../../../build/dts/api/bindings/adc/nxp,kinetis-adc16.md#std-dtcompatible-nxp-kinetis-adc16) |
| Clock control | on-chip | Kinetis System Integration Module (SIM) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L43) | [`nxp,kinetis-sim`](../../../../build/dts/api/bindings/clock/nxp,kinetis-sim.md#std-dtcompatible-nxp-kinetis-sim) |
| on-chip | Generic fixed factor clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L48) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | NXP Kinetis Multipurpose Clock generator (MCG) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L77) | [`nxp,kinetis-mcg`](../../../../build/dts/api/bindings/clock/nxp,kinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg) |
| Flash controller | on-chip | NXP Kinetis Flash Memory Module E (FTFE)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L89) | [`nxp,kinetis-ftfe`](../../../../build/dts/api/bindings/flash_controller/nxp,kinetis-ftfe.md#std-dtcompatible-nxp-kinetis-ftfe) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L107) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp,kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| I2C | on-chip | Kinetis I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L168)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L157) | [`nxp,kinetis-i2c`](../../../../build/dts/api/bindings/i2c/nxp,kinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/twr_kv58f220m/twr_kv58f220m.dts?plain=1#L61) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/twr_kv58f220m/twr_kv58f220m.dts?plain=1#L41) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | NXP System Memory Protection Unit (SYSMPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L37) | [`nxp,sysmpu`](../../../../build/dts/api/bindings/mmu_mpu/nxp,sysmpu.md#std-dtcompatible-nxp-sysmpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5xf1m0vlx24.dtsi?plain=1#L20) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/twr_kv58f220m/twr_kv58f220m.dts?plain=1#L114) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L179) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L31) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/twr_kv58f220m/twr_kv58f220m.dts?plain=1#L148) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp,fxos8700.md#std-dtcompatible-nxp-fxos8700) |
| Serial controller | on-chip | Kinetis UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L271)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L280) | [`nxp,kinetis-uart`](../../../../build/dts/api/bindings/serial/nxp,kinetis-uart.md#std-dtcompatible-nxp-kinetis-uart) |
| SPI | on-chip | NXP DSPI controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L241) | [`nxp,dspi`](../../../../build/dts/api/bindings/spi/nxp,dspi.md#std-dtcompatible-nxp-dspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5xf1m0vlx24.dtsi?plain=1#L13) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP FlexTimer Module (FTM)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kv5x.dtsi?plain=1#L209) | [`nxp,ftm`](../../../../build/dts/api/bindings/timer/nxp,ftm.md#std-dtcompatible-nxp-ftm) |

### System Clock

The KV58 SoC is configured to use the 50 MHz external oscillator on the
board with the on-chip PLL to generate a 237.5 MHz system clock.

### Serial Port

The KV58 SoC has six UARTs. UART0 is configured for the console. The
remaining UARTs are not used.

### Accelerometer and magnetometer

The TWR-KV58F220M board by default only supports polling the FXOS8700
accelerometer and magnetometer for sensor values
(`CONFIG_FXOS8700_TRIGGER_NONE=y`).

In order to support FXOS8700 triggers (interrupts), shunts must be placed on
the jumpers `J2` and `J9`. A trigger option also must be enabled in Kconfig
(either `CONFIG_FXOS8700_TRIGGER_GLOBAL_THREAD=y` or
`CONFIG_FXOS8700_TRIGGER_OWN_THREAD=y`).

## Programming and Debugging

The `twr_kv58f220m` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

This board integrates an OpenSDA debug probe. However, it can currently only be
used for flashing the KV58 SoC by copying the compiled firmware to the USB Mass
Storage Device. The board cannot be debugged using the OpenSDA probe, since
pyOCD does not support the target. The OpenSDA J-Link firmware (as of release
2019-06-03) also cannot be used, since the flash algorithm for the KV58 seems to
be broken at the time of writing.

An external J-Link debug probe connected to the JTAG header J13 is used to debug
the target.

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Using west:

```shell
# From the root of the zephyr repository
west build -b twr_kv58f220m samples/hello_world
```

Using CMake and ninja:

```shell
# From the root of the zephyr repository
# Use cmake to configure a Ninja-based buildsystem:
cmake -Bbuild -GNinja -DBOARD=twr_kv58f220m samples/hello_world

# Now run the build tool on the generated build system:
ninja -Cbuild
```

### Configuring a Console

Even though the OpenSDA probe cannot be used for debugging, we will use it as a
USB-to-serial adapter for the serial console.

Connect a USB cable from your PC to J22.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b twr_kv58f220m samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-xxx-gxxxxxxxxxxxx *****
Hello World! twr_kv58f220m
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b twr_kv58f220m samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-xxx-gxxxxxxxxxxxx *****
Hello World! twr_kv58f220m
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

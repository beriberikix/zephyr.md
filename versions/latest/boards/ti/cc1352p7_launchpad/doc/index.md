---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ti/cc1352p7_launchpad/doc/index.html
original_path: boards/ti/cc1352p7_launchpad/doc/index.html
---

# CC1352P7 LaunchPad

Board Overview

[![../../../../_images/lp-cc1352p7-top.jpg](../../../../_images/lp-cc1352p7-top.jpg)
](../../../../_images/lp-cc1352p7-top.jpg)

CC1352P7 LaunchPad

Name:
:   `cc1352p7_lp`

Vendor:
:   Texas Instruments

Architecture:
:   arm

SoC:
:   cc1352p7

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/cc1352p7_launchpad/doc/index.rst/../..)

## Overview

The Texas Instruments CC1352P7 LaunchPad™ (LP-CC1352P7) is a
development kit for the SimpleLink™ multi-Standard CC1352P7 wireless MCU.

See the [TI CC1352P7 LaunchPad Product Page](https://www.ti.com/tool/LP-CC1352P7) for details.

## Hardware

The CC1352P7 LaunchPad™ development kit features the CC1352P7 wireless MCU.
The board is equipped with two LEDs, two push buttons, antenna switch and
BoosterPack connectors for expansion. It also includes an integrated (XDS110)
debugger.

The CC1352P7 wireless MCU has a 48 MHz Arm® Cortex®-M4F SoC and an
integrated sub-1GHz and 2.4 GHz transceiver with integrated 20dBm power amplifier
(PA) supporting multiple protocols including Bluetooth® Low Energy and IEEE® 802.15.4.

See the [TI CC1352P7 Product Page](https://www.ti.com/product/CC1352P7) for additional details.

### Supported Features

The `cc1352p7_lp` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `cc1352p7_lp/cc1352p7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L23) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | TI CC13XX/CC26xx family ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L235) | [`ti,cc13xx-cc26xx-adc`](../../../../build/dts/api/bindings/adc/ti%2Ccc13xx-cc26xx-adc.md#std-dtcompatible-ti-cc13xx-cc26xx-adc) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L57) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Flash controller | on-chip | Texas Instruments CC13xx/CC26xx flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L85) | [`ti,cc13xx-cc26xx-flash-controller`](../../../../build/dts/api/bindings/flash_controller/ti%2Ccc13xx-cc26xx-flash-controller.md#std-dtcompatible-ti-cc13xx-cc26xx-flash-controller) |
| GPIO & Headers | on-chip | TI SimpleLink CC13xx / CC26xx GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L69) | [`ti,cc13xx-cc26xx-gpio`](../../../../build/dts/api/bindings/gpio/ti%2Ccc13xx-cc26xx-gpio.md#std-dtcompatible-ti-cc13xx-cc26xx-gpio) |
| on-board | TI BoosterPack GPIO header[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/cc1352p7_launchpad/../common/boosterpack_connector.dtsi?plain=1#L8) | [`ti,boosterpack-header`](../../../../build/dts/api/bindings/gpio/ti%2Cboosterpack-header.md#std-dtcompatible-ti-boosterpack-header) |
| I2C | on-chip | TI CC13xx / CC26xx I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L171) | [`ti,cc13xx-cc26xx-i2c`](../../../../build/dts/api/bindings/i2c/ti%2Ccc13xx-cc26xx-i2c.md#std-dtcompatible-ti-cc13xx-cc26xx-i2c) |
| IEEE 802.15.4 | on-chip | TI SimpleLink CC13xx / CC26xx IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L217) | [`ti,cc13xx-cc26xx-ieee802154`](../../../../build/dts/api/bindings/ieee802154/ti%2Ccc13xx-cc26xx-ieee802154.md#std-dtcompatible-ti-cc13xx-cc26xx-ieee802154) |
| on-chip | TI SimpleLink CC13xx / CC26xx IEEE 802.15.4 node (sub-GHz)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L222) | [`ti,cc13xx-cc26xx-ieee802154-subghz`](../../../../build/dts/api/bindings/ieee802154/ti%2Ccc13xx-cc26xx-ieee802154-subghz.md#std-dtcompatible-ti-cc13xx-cc26xx-ieee802154-subghz) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/cc1352p7_launchpad/../common/launchxl.dtsi?plain=1#L45) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/cc1352p7_launchpad/../common/launchxl.dtsi?plain=1#L33) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-board | Skyworks SKY13317 pHEMT GaAs SP3T Antenna Switch[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/cc1352p7_launchpad/../common/launchxl_sky13317.dtsi?plain=1#L21) | [`skyworks,sky13317`](../../../../build/dts/api/bindings/misc/skyworks%2Csky13317.md#std-dtcompatible-skyworks-sky13317) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L92) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc1352r7.dtsi?plain=1#L19) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | TI SimpleLink CC13xx / CC26xx radio[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L207) | [`ti,cc13xx-cc26xx-radio`](../../../../build/dts/api/bindings/net/wireless/ti%2Ccc13xx-cc26xx-radio.md#std-dtcompatible-ti-cc13xx-cc26xx-radio) |
| Pin control | on-chip | TI SimpleLink CC13xx / CC26xx Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L64) | [`ti,cc13xx-cc26xx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti%2Ccc13xx-cc26xx-pinctrl.md#std-dtcompatible-ti-cc13xx-cc26xx-pinctrl) |
| PWM | on-chip | TI SimpleLink CC13xx/CC26xx GPT timer PWM Controller Node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L106) | [`ti,cc13xx-cc26xx-timer-pwm`](../../../../build/dts/api/bindings/pwm/ti%2Ccc13xx-cc26xx-timer-pwm.md#std-dtcompatible-ti-cc13xx-cc26xx-timer-pwm) |
| RNG | on-chip | TI SimpleLink CC13xx / CC26xx TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L78) | [`ti,cc13xx-cc26xx-trng`](../../../../build/dts/api/bindings/rng/ti%2Ccc13xx-cc26xx-trng.md#std-dtcompatible-ti-cc13xx-cc26xx-trng) |
| RTC | on-chip | TI SimpleLink CC13xx/CC26xx RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L200) | [`ti,cc13xx-cc26xx-rtc-timer`](../../../../build/dts/api/bindings/rtc/ti%2Ccc13xx-cc26xx-rtc-timer.md#std-dtcompatible-ti-cc13xx-cc26xx-rtc-timer) |
| Serial controller | on-chip | TI SimpleLink CC13xx / CC26xx UART node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L155)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L163) | [`ti,cc13xx-cc26xx-uart`](../../../../build/dts/api/bindings/serial/ti%2Ccc13xx-cc26xx-uart.md#std-dtcompatible-ti-cc13xx-cc26xx-uart) |
| SPI | on-chip | TI SimpleLink CC13xx / CC26xx SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L181)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L190) | [`ti,cc13xx-cc26xx-spi`](../../../../build/dts/api/bindings/spi/ti%2Ccc13xx-cc26xx-spi.md#std-dtcompatible-ti-cc13xx-cc26xx-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L46) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | TI SimpleLink CC13xx/CC26xx Timer[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L99) | [`ti,cc13xx-cc26xx-timer`](../../../../build/dts/api/bindings/timer/ti%2Ccc13xx-cc26xx-timer.md#std-dtcompatible-ti-cc13xx-cc26xx-timer) |
| Watchdog | on-chip | TI CC13xx/CC26xx watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L228) | [`ti,cc13xx-cc26xx-watchdog`](../../../../build/dts/api/bindings/watchdog/ti%2Ccc13xx-cc26xx-watchdog.md#std-dtcompatible-ti-cc13xx-cc26xx-watchdog) |

### Connections and IOs

All I/O signals are accessible from the BoosterPack connectors. Pin function
aligns with the LaunchPad standard.

| Pin | Function | Usage |
| --- | --- | --- |
| DIO3 | GPIO |  |
| DIO4 | I2C\_MSSCL | I2C SCL |
| DIO5 | I2C\_MSSDA | I2C SDA |
| DIO6 | GPIO | Red LED |
| DIO7 | GPIO | Green LED |
| DIO8 | SSI0\_RX | SPI MISO |
| DIO9 | SSI0\_TX | SPI MOSI |
| DIO10 | SSI0\_CLK | SPI CLK |
| DIO11 | SSIO\_CS | SPI CS |
| DIO12 | UART0\_RX | UART RXD |
| DIO13 | UART0\_TX | UART TXD |
| DIO14 | GPIO | Button 2 |
| DIO15 | GPIO | Button 1 |
| DIO16 |  | JTAG TDO |
| DIO17 |  | JTAG TDI |
| DIO18 | UART0\_RTS | UART RTS / JTAG SWO |
| DIO19 | UART0\_CTS | UART CTS |
| DIO20 | GPIO | Flash CS |
| DIO21 | GPIO |  |
| DIO22 | GPIO |  |
| DIO23 | AUX\_IO | A0 |
| DIO24 | AUX\_IO | A1 |
| DIO25 | AUX\_IO | A2 |
| DIO26 | AUX\_IO | A3 |
| DIO27 | AUX\_IO | A4 |
| DIO28 | AUX\_IO | A5 |
| DIO29 | AUX\_IO | A6 |
| DIO30 | AUX\_IO | A7 |

## Programming and Debugging

The `cc1352p7_lp` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Before flashing or debugging ensure the RESET, TMS, TCK, TDO, and TDI jumpers
are in place. Also place jumpers on the TXD and RXD signals for a serial
console using the XDS110 application serial port.

### Prerequisites:

1. Ensure the XDS-110 emulation firmware on the board is updated.

   Download and install the latest [XDS-110 emulation package](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download).

   Follow these [xds110 firmware update directions](http://software-dl.ti.com/ccs/esd/documents/xdsdebugprobes/emu_xds110.html#updating-the-xds110-firmware)

   Note that the emulation package install may place the xdsdfu utility
   in `<install_dir>/ccs_base/common/uscif/xds110/`.
2. Install OpenOCD

   Currently, OpenOCD doesn’t support the CC1352P7.
   Until its support get merged, we have to builld a downstream version that could found [here](https://github.com/anobli/openocd).
   Please refer to OpenOCD documentation to build and install OpenOCD.

   For your convenience, we provide a [prebuilt binary](https://github.com/anobli/openocd/actions/runs/10566225265).

```shell
$ unzip openocd-810cb5b21-x86_64-linux-gnu.zip
$ chmod +x openocd-x86_64-linux-gnu/bin/openocd
$ export OPENOCD_DIST=$PWD/openocd-x86_64-linux-gnu
```

By default, zephyr will try to use the OpenOCD binary from SDK.
You will have to define `OPENOCD` and `OPENOCD_DEFAULT_PATH` to use the custom OpenOCD binary.

### Flashing

Applications for the `CC1352P7 LaunchPad` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ screen <tty_device> 115200
```

Replace `<tty_device>` with the port where the XDS110 application
serial device can be found. For example, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b cc1352p7_lp samples/hello_world -- -DOPENOCD=$OPENOCD_DIST/bin/openocd -DOPENOCD_DEFAULT_PATH=$OPENOCD_DIST/share/openocd
west flash
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b cc1352p7_lp samples/hello_world -- -DOPENOCD=$OPENOCD_DIST/bin/openocd -DOPENOCD_DEFAULT_PATH=$OPENOCD_DIST/share/openocd
west debug
```

### Bootloader

The ROM bootloader on CC13x2x7 and CC26x2x7 devices is enabled by default. The
bootloader will start if there is no valid application image in flash or the
so-called backdoor is enabled (via option
[`CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE`](../../../../kconfig.md#CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE "CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE")) and BTN-1 is held
down during reset. See the bootloader documentation in chapter 10 of the [TI
CC13x2x7 / CC26x2x7 Technical Reference Manual](https://www.ti.com/lit/ug/swcu192/swcu192.pdf) for additional information.

### Power Management and UART

System and device power management are supported on this platform, and
can be enabled via the standard Kconfig options in Zephyr, such as
[`CONFIG_PM`](../../../../kconfig.md#CONFIG_PM "CONFIG_PM"), [`CONFIG_PM_DEVICE`](../../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE").

When system power management is turned on (CONFIG\_PM=y),
sleep state 2 (standby mode) is allowed, and polling is used to retrieve input
by calling uart\_poll\_in(), it is possible for characters to be missed if the
system enters standby mode between calls to uart\_poll\_in(). This is because
the UART is inactive while the system is in standby mode. The workaround is to
disable sleep state 2 while polling:

```c
pm_policy_state_lock_get(PM_STATE_STANDBY, PM_ALL_SUBSTATES);
<code that calls uart_poll_in() and expects input at any point in time>
pm_policy_state_lock_put(PM_STATE_STANDBY, PM_ALL_SUBSTATES);
```

## References

CC1352P7 LaunchPad Quick Start Guide:
:   [https://www.ti.com/lit/pdf/swru573](https://www.ti.com/lit/pdf/swru573)

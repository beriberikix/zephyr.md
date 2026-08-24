---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/usb_kw24d512/doc/index.html
original_path: boards/nxp/usb_kw24d512/doc/index.html
---

# USB-KW24D512

Board Overview

Name:
:   `usb_kw24d512`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mkw24d5

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/usb_kw24d512/doc/index.rst/../..)

## Overview

The USB-KW24D512 is an evaluation board in a convenient USB dongle
form factor based on the NXP MKW24D512 System-in-Package (SiP) device
(KW2xD wireless MCU series).
MKW24D512 wireless MCU provides a low-power, compact device with
integrated IEEE 802.15.4 radio. The board can be used as a packet sniffer,
network node, border router or as a development board.

## Hardware

- Kinetis KW2xD-2.4 GHz 802.15.4 Wireless Radio Microcontroller
  (50 MHz, 512 KB flash memory, 64 KB RAM, low-power, crystal-less USB)
- USB Type A Connector
- Two blue LEDs
- One user push button
- One reset button
- Integrated PCB Folded F-type antenna
- 10-pin (0.05”) JTAG debug port for target MCU

For more information about the KW2xD SiP and USB-KW24D512 board:

- [KW2xD Website](https://www.nxp.com/products/wireless/thread/kinetis-kw2xd-2.4-ghz-802.15.4-wireless-radio-microcontroller-mcu-based-on-arm-cortex-m4-core:KW2xD)
- [KW2xD Datasheet](https://www.nxp.com/docs/en/data-sheet/MKW2xDxxx.pdf)
- [KW2xD Reference Manual](https://www.nxp.com/webapp/Download?colCode=MKW2XDXXXRM)
- [USB-KW24D512 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/w-serieswireless-conn.m0-plus-m4/ieee-802.15.4-packet-sniffer-usb-dongle-form-factor:USB-KW24D512)
- [USB-KW24D512 Hardware Reference Manual](https://www.nxp.com/webapp/Download?colCode=USB-KW2XHWRM)

### Supported Features

The `usb_kw24d512` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `usb_kw24d512/mkw24d5` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L28) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | Kinetis ADC16[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L324) | [`nxp,kinetis-adc16`](../../../../build/dts/api/bindings/adc/nxp,kinetis-adc16.md#std-dtcompatible-nxp-kinetis-adc16) |
| Clock control | on-chip | NXP Kinetis Multipurpose Clock generator (MCG) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L62) | [`nxp,kinetis-mcg`](../../../../build/dts/api/bindings/clock/nxp,kinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg) |
| on-chip | Kinetis System Integration Module (SIM) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L81) | [`nxp,kinetis-sim`](../../../../build/dts/api/bindings/clock/nxp,kinetis-sim.md#std-dtcompatible-nxp-kinetis-sim) |
| on-chip | Generic fixed factor clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L86) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Flash controller | on-chip | NXP Kinetis Flash Memory Module L (FTFL)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L108) | [`nxp,kinetis-ftfl`](../../../../build/dts/api/bindings/flash_controller/nxp,kinetis-ftfl.md#std-dtcompatible-nxp-kinetis-ftfl) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L208) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp,kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| I2C | on-chip | Kinetis I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L126) | [`nxp,kinetis-i2c`](../../../../build/dts/api/bindings/i2c/nxp,kinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c) |
| IEEE 802.15.4 | on-chip | NXP MCR20A 802.15.4 wireless transceiver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L280) | [`nxp,mcr20a`](../../../../build/dts/api/bindings/ieee802154/nxp,mcr20a.md#std-dtcompatible-nxp-mcr20a) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/usb_kw24d512/usb_kw24d512.dts?plain=1#L40) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/usb_kw24d512/usb_kw24d512.dts?plain=1#L28) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L118) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/usb_kw24d512/usb_kw24d512.dts?plain=1#L101) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L178) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L36) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| RNG | on-chip | Kinetis RNGA (Random Number Generator Accelerator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L341) | [`nxp,kinetis-rnga`](../../../../build/dts/api/bindings/rng/nxp,kinetis-rnga.md#std-dtcompatible-nxp-kinetis-rnga) |
| Serial controller | on-chip | Kinetis UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L148)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L158) | [`nxp,kinetis-uart`](../../../../build/dts/api/bindings/serial/nxp,kinetis-uart.md#std-dtcompatible-nxp-kinetis-uart) |
| SPI | on-chip | NXP DSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L268)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L258) | [`nxp,dspi`](../../../../build/dts/api/bindings/spi/nxp,dspi.md#std-dtcompatible-nxp-dspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L55) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP FlexTimer Module (FTM)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L297) | [`nxp,ftm`](../../../../build/dts/api/bindings/timer/nxp,ftm.md#std-dtcompatible-nxp-ftm) |
| USB | on-chip | NPX Kinetis USBFSOTG Controller in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L332) | [`nxp,kinetis-usbd`](../../../../build/dts/api/bindings/usb/nxp,kinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd) |
| Watchdog | on-chip | Kinetis watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw2xd.dtsi?plain=1#L290) | [`nxp,kinetis-wdog`](../../../../build/dts/api/bindings/watchdog/nxp,kinetis-wdog.md#std-dtcompatible-nxp-kinetis-wdog) |

### Connections and IOs

The KW2xD SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| PTA1 | UART0\_RX | UART Console |
| PTA2 | UART0\_TX | UART Console |
| PTC4 | GPIO | SW1 |
| PTD4 | GPIO | Blue LED (D2) |
| PTD5 | GPIO | Blue LED (D3) |
| PTB10 | SPI1\_PCS0 | internal connected to MCR20A |
| PTB11 | SPI1\_SCK | internal connected to MCR20A |
| PTB16 | SPI1\_SOUT | internal connected to MCR20A |
| PTB17 | SPI1\_SIN | internal connected to MCR20A |
| PTB19 | GPIO | internal connected to MCR20A (Reset) |
| PTB3 | GPIO | internal connected to MCR20A (IRQ\_B) |
| PTC0 | GPIO | internal connected to MCR20A (GPIO5) |

### System Clock

USB-KW24D512 contains 32 MHz oscillator crystal, which is connected to the
clock pins of the radio transceiver. The MCU is configured to
use the 4 MHz external clock from the transceiver with the on-chip PLL
to generate a 48 MHz system clock.

### Serial Port

The KW2xD SoC has three UARTs. One is configured and can be used for the
console, but it uses the same pins as the JTAG interface and is only
accessible via the JTAG SWD connector.

### USB

The KW2xD SoC has a USB OTG (USBOTG) controller that supports both
device and host functions. Only USB device function is supported in Zephyr
at the moment. The USB-KW24D512 board has a USB Type A connector and
can only be used in device mode.

## Programming and Debugging

The `usb_kw24d512` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe).

#### [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Attach a J-Link 10-pin connector to J1.

### Configuring a Console

The console is available using [Segger RTT](https://www.segger.com/products/debug-probes/j-link/technology/about-real-time-transfer/).

Connect a USB cable from your PC to J5.

Once you have started a debug session, run telnet:

```shell
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
SEGGER J-Link V6.44 - Real time terminal output
SEGGER J-Link ARM V10.1, SN=600111924
Process: JLinkGDBServerCLExe
```

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b usb_kw24d512 samples/hello_world
west flash
```

The Segger RTT console is only available during a debug session. Use `attach`
to start one:

```shell
# From the root of the zephyr repository
west build -b usb_kw24d512 samples/hello_world
west attach
```

Run telnet as shown earlier, and you should see the following message in the
terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! usb_kw24d512
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b usb_kw24d512 samples/hello_world
west debug
```

Run telnet as shown earlier, step through the application in your debugger, and
you should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! usb_kw24d512
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

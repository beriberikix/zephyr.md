---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/infineon/cy8cproto_062_4343w/doc/index.html
original_path: boards/infineon/cy8cproto_062_4343w/doc/index.html
---

# CY8CPROTO-062-4343W

Board Overview

[![../../../../_images/board.jpg](https://docs.zephyrproject.org/4.2.0/_images/board.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/board.jpg)

CY8CPROTO-062-4343W

Name:
:   `cy8cproto_062_4343w`

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   cy8c624abzi\_s2d44

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/cy8cproto_062_4343w/doc/index.rst/../..)

## Overview

The CY8CPROTO-062-4343W PSOC 6 Wi-Fi BT Prototyping Kit is a low-cost hardware
platform that enables design and debug of PSOC 6 MCUs. It comes with a Murata
LBEE5KL1DX module, based on the CYW4343W combo device, industry-leading CAPSENSE
for touch buttons and slider, on-board debugger/programmer with KitProg3, microSD
card interface, 512-Mb Quad-SPI NOR flash, PDM-PCM microphone, and a thermistor.

This kit is designed with a snap-away form-factor, allowing the user to separate
the different components and features that come with this kit and use independently.
In addition, support for Digilent’s Pmod interface is also provided with this kit.

## Hardware

For more information about the PSOC 62 MCU SoC and CY8CPROTO-062-4343W board:

- [PSOC 62 MCU SoC Website](https://www.cypress.com/products/32-bit-arm-cortex-m4-psoc-6)
- [PSOC 62 MCU Datasheet](https://www.cypress.com/documentation/datasheets/psoc-6-mcu-psoc-62-datasheet-programmable-system-chip-psoc-preliminary)
- [PSOC 62 MCU Architecture Reference Manual](https://www.cypress.com/documentation/technical-reference-manuals/psoc-6-mcu-psoc-62-architecture-technical-reference-manual)
- [PSOC 62 MCU Register Reference Manual](https://www.cypress.com/documentation/technical-reference-manuals/psoc-6-mcu-psoc-62-register-technical-reference-manual-trm)
- [CY8CPROTO-062-4343W PSOC 6 Wi-Fi BT Website](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-062-4343w/)
- [CY8CPROTO-062-4343W PSOC 6 Wi-Fi BT User Guide](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-062-4343w/#!?fileId=8ac78c8c7d0d8da4017d0f0118571844)
- [CY8CPROTO-062-4343W PSOC 6 Wi-Fi BT Schematics](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-062-4343w/#!?fileId=8ac78c8c7d0d8da4017d0f01126b183f)

### Kit Features:

- Support of up to 2MB Flash and 1MB SRAM
- Dedicated SDHC to interface with WICED wireless devices.
- Delivers dual-cores, with a 150-MHz Arm Cortex-M4 as the primary
  application processor and a 100-MHz Arm Cortex-M0+ as the secondary
  processor for low-power operations.
- Supports Full-Speed USB, capacitive-sensing with CAPSENSE, a PDM-PCM
  digital microphone interface, a Quad-SPI interface, 13 serial communication
  blocks, 7 programmable analog blocks, and 56 programmable digital blocks.

### Kit Contents:

- PSOC 6 Wi-Fi BT Prototyping Board
- USB Type-A to Micro-B cable
- Quick start guide

### Supported Features

The `cy8cproto_062_4343w` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `cy8cproto_062_4343w/cy8c624abzi_s2d44` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L15) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0+.md#std-dtcompatible-arm-cortex-m0) |
| on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L20) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Infineon Cat1 ADC Each ADC group Cat1 is assigned to a Zephyr device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L306) | [`infineon,cat1-adc`](../../../../build/dts/api/bindings/adc/infineon,cat1-adc.md#std-dtcompatible-infineon-cat1-adc) |
| ARM architecture | on-chip | Infineon Serial Communication Blocks (SCB) node[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L202) | [`infineon,cat1-scb`](../../../../build/dts/api/bindings/arm/infineon,cat1-scb.md#std-dtcompatible-infineon-cat1-scb) |
| Bluetooth | on-board | CYW43xxx Connectivity that uses Zephyr’s Bluetooth Host Controller Interface UART driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8cproto_062_4343w/cy8cproto_062_4343w.dts?plain=1#L64) | [`infineon,cyw43xxx-bt-hci`](../../../../build/dts/api/bindings/bluetooth/infineon,cyw43xxx-bt-hci.md#std-dtcompatible-infineon-cyw43xxx-bt-hci) |
| Clock control | on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/system_clocks.dtsi?plain=1#L13)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/system_clocks.dtsi?plain=1#L69) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Generic fixed factor clock provider[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/system_clocks.dtsi?plain=1#L21)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/system_clocks.dtsi?plain=1#L37) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Counter | on-chip | Infineon counters[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L320)[31 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L327) | [`infineon,cat1-counter`](../../../../build/dts/api/bindings/counter/infineon,cat1-counter.md#std-dtcompatible-infineon-cat1-counter) |
| DMA | on-chip | Infineon CAT1 DMA[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L552) | [`infineon,cat1-dma`](../../../../build/dts/api/bindings/dma/infineon,cat1-dma.md#std-dtcompatible-infineon-cat1-dma) |
| Flash controller | on-chip | Infineon CAT1 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L27) | [`infineon,cat1-flash-controller`](../../../../build/dts/api/bindings/flash_controller/infineon,cat1-flash-controller.md#std-dtcompatible-infineon-cat1-flash-controller) |
| GPIO & Headers | on-chip | Infineon CAT1 GPIO Port[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L66)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L75) | [`infineon,cat1-gpio`](../../../../build/dts/api/bindings/gpio/infineon,cat1-gpio.md#std-dtcompatible-infineon-cat1-gpio) |
| I2C | on-chip | Infineon CAT1 I2C driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L226) | [`infineon,cat1-i2c`](../../../../build/dts/api/bindings/i2c/infineon,cat1-i2c.md#std-dtcompatible-infineon-cat1-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8cproto_062_4343w/cy8cproto_062_4343w-common.dtsi?plain=1#L22) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8cproto_062_4343w/cy8cproto_062_4343w-common.dtsi?plain=1#L14) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L33) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Infineon CAT1 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L53) | [`infineon,cat1-pinctrl`](../../../../build/dts/api/bindings/pinctrl/infineon,cat1-pinctrl.md#std-dtcompatible-infineon-cat1-pinctrl) |
| SDHC | on-chip | Infineon CAT1 SDHC/SDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L545) | [`infineon,cat1-sdhc-sdio`](../../../../build/dts/api/bindings/sdhc/infineon,cat1-sdhc-sdio.md#std-dtcompatible-infineon-cat1-sdhc-sdio) |
| Serial controller | on-chip | Infineon CAT1 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L218) | [`infineon,cat1-uart`](../../../../build/dts/api/bindings/serial/infineon,cat1-uart.md#std-dtcompatible-infineon-cat1-uart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L47) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Infineon CAT1 Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L314) | [`infineon,cat1-watchdog`](../../../../build/dts/api/bindings/watchdog/infineon,cat1-watchdog.md#std-dtcompatible-infineon-cat1-watchdog) |
| Wi-Fi | on-board | AIROC Wi-Fi Connectivity[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8cproto_062_4343w/cy8cproto_062_4343w.dts?plain=1#L89) | [`infineon,airoc-wifi`](../../../../build/dts/api/compatibles/infineon,airoc-wifi.md#std-dtcompatible-infineon-airoc-wifi) |

### System Clock

The PSOC 62 MCU SoC is configured to use the internal IMO+FLL as a source for
the system clock. CM0+ works at 50MHz, CM4 - at 100MHz. Other sources for the
system clock are provided in the SOC, depending on your system requirements.

## Fetch Binary Blobs

cy8cproto\_062\_4343w board optionally uses binary blobs for features
(e.g WIFI/Bluetooth chip firmware, CM0p prebuilt images, etc).

To fetch Binary Blobs:

```shell
west blobs fetch hal_infineon
```

## Build blinking led sample

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

```shell
# From the root of the zephyr repository
west build -b cy8cproto_062_4343w samples/basic/blinky
```

## Programming and Debugging

The `cy8cproto_062_4343w` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

The CY8CPROTO-062-4343W includes an onboard programmer/debugger ([KitProg3](https://github.com/Infineon/KitProg3)) to provide debugging, flash programming, and serial communication over USB. Flash and debug commands use OpenOCD and require a custom Infineon OpenOCD version, that supports KitProg3, to be installed.

### Infineon OpenOCD Installation

Both the full [ModusToolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox) and the [ModusToolbox Programming Tools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools) packages include Infineon OpenOCD. Installing either of these packages will also install Infineon OpenOCD. If neither package is installed, a minimal installation can be done by downloading the [Infineon OpenOCD](https://github.com/Infineon/openocd/releases/latest) release for your system and manually extract the files to a location of your choice.

Note

Linux requires device access rights to be set up for KitProg3. This is handled automatically by the ModusToolbox and ModusToolbox Programming Tools installations. When doing a minimal installation, this can be done manually by executing the script `openocd/udev_rules/install_rules.sh`.

### West Commands

The path to the installed Infineon OpenOCD executable must be available to the `west` tool commands. There are multiple ways of doing this. The example below uses a permanent CMake argument to set the CMake variable `OPENOCD`.

> WindowsLinux
>
> ```shell
> # Run west config once to set permanent CMake argument
> west config build.cmake-args -- -DOPENOCD=path/to/infineon/openocd/bin/openocd.exe
>
> # Do a pristine build once after setting CMake argument
> west build -b cy8cproto_062_4343w -p always samples/basic/blinky
>
> west flash
> west debug
> ```
>
> ```shell
> # Run west config once to set permanent CMake argument
> west config build.cmake-args -- -DOPENOCD=path/to/infineon/openocd/bin/openocd
>
> # Do a pristine build once after setting CMake argument
> west build -b cy8cproto_062_4343w -p always samples/basic/blinky
>
> west flash
> west debug
> ```

Once the gdb console starts after executing the west debug command, you may now set breakpoints and perform other standard GDB debugging on the PSOC 6 CM4 core.

### Errata

| Problem | Solution |
| --- | --- |
| The GPIO\_INT\_TRIG\_BOTH interrupt is not raised when the associated GPIO is asserted. | This will be fixed in a future release. |
| GDB experiences a timeout error connecting to a server instance started by west debugserver. | This will be fixed in a future release. |

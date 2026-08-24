---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/infineon/cy8cproto_063_ble/doc/index.html
original_path: boards/infineon/cy8cproto_063_ble/doc/index.html
---

# CY8CPROTO-063-BLE

Board Overview

[![../../../../_images/cy8cproto-063-ble.jpg](https://docs.zephyrproject.org/4.2.0/_images/cy8cproto-063-ble.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/cy8cproto-063-ble.jpg)

CY8CPROTO-063-BLE

Name:
:   `cy8cproto_063_ble`

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   cyble\_416045\_02

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/cy8cproto_063_ble/doc/index.rst/../..)

## Overview

The PSOC 6 BLE Proto Kit (CY8CPROTO-063-BLE) is a hardware platform that
enables design and debug of the Cypress PSOC 63 BLE MCU.

## Hardware

For more information about the PSOC 63 BLE MCU SoC and CY8CPROTO-063-BLE board:

- [PSOC 63 BLE MCU SoC Website](https://www.cypress.com/products/32-bit-arm-cortex-m4-psoc-6) [[1]](#id2)
- [PSOC 63 BLE MCU Datasheet](https://www.infineon.com/dgdl/Infineon-PSOC_6_MCU_PSOC_63_with_BLE_Datasheet_Programmable_System-on-Chip_(PSOC)-DataSheet-v16_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0ee4efe46c37&utm_source=cypress&utm_medium=referral&utm_campaign=202110_globe_en_all_integration-files) [[2]](#id4)
- [PSOC 63 BLE MCU Architecture Reference Manual](https://documentation.infineon.com/html/psoc6/zrs1651212645947.html) [[3]](#id6)
- [PSOC 63 BLE MCU Register Reference Manual](https://documentation.infineon.com/html/psoc6/bnm1651211483724.html) [[4]](#id8)
- [CY8CPROTO-063-BLE Website](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/) [[5]](#id10)
- [CY8CPROTO-063-BLE User Guide](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/#!?fileId=8ac78c8c7d0d8da4017d0f00d7eb1812) [[6]](#id12)
- [CY8CPROTO-063-BLE Schematics](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/#!?fileId=8ac78c8c7d0d8da4017d0f00ea3c1821) [[7]](#id14)

### Supported Features

The `cy8cproto_063_ble` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `cy8cproto_063_ble/cyble_416045_02` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L15) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0+.md#std-dtcompatible-arm-cortex-m0) |
| on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L20) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Infineon Cat1 ADC Each ADC group Cat1 is assigned to a Zephyr device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L209) | [`infineon,cat1-adc`](../../../../build/dts/api/bindings/adc/infineon,cat1-adc.md#std-dtcompatible-infineon-cat1-adc) |
| ARM architecture | on-chip | Infineon Serial Communication Blocks (SCB) node[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L217) | [`infineon,cat1-scb`](../../../../build/dts/api/bindings/arm/infineon,cat1-scb.md#std-dtcompatible-infineon-cat1-scb) |
| Bluetooth | on-chip | Bluetooth module that uses Infineon’s Host Controller Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L310) | [`infineon,cat1-bless-hci`](../../../../build/dts/api/bindings/bluetooth/infineon,cat1-bless-hci.md#std-dtcompatible-infineon-cat1-bless-hci) |
| Clock control | on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/system_clocks.dtsi?plain=1#L13)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/system_clocks.dtsi?plain=1#L69) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Generic fixed factor clock provider[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/system_clocks.dtsi?plain=1#L21)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/system_clocks.dtsi?plain=1#L37) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Counter | on-chip | Infineon counters[32 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L316) | [`infineon,cat1-counter`](../../../../build/dts/api/bindings/counter/infineon,cat1-counter.md#std-dtcompatible-infineon-cat1-counter) |
| DMA | on-chip | Infineon CAT1 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L548) | [`infineon,cat1-dma`](../../../../build/dts/api/bindings/dma/infineon,cat1-dma.md#std-dtcompatible-infineon-cat1-dma) |
| Flash controller | on-chip | Infineon CAT1 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L27) | [`infineon,cat1-flash-controller`](../../../../build/dts/api/bindings/flash_controller/infineon,cat1-flash-controller.md#std-dtcompatible-infineon-cat1-flash-controller) |
| GPIO & Headers | on-chip | Infineon CAT1 GPIO Port[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L67) | [`infineon,cat1-gpio`](../../../../build/dts/api/bindings/gpio/infineon,cat1-gpio.md#std-dtcompatible-infineon-cat1-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8cproto_063_ble/cy8cproto_063_ble.dts?plain=1#L43) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8cproto_063_ble/cy8cproto_063_ble.dts?plain=1#L35) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L33) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Infineon CAT1 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L53) | [`infineon,cat1-pinctrl`](../../../../build/dts/api/bindings/pinctrl/infineon,cat1-pinctrl.md#std-dtcompatible-infineon-cat1-pinctrl) |
| SDHC | on-chip | Infineon CAT1 SDHC/SDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L541) | [`infineon,cat1-sdhc-sdio`](../../../../build/dts/api/bindings/sdhc/infineon,cat1-sdhc-sdio.md#std-dtcompatible-infineon-cat1-sdhc-sdio) |
| Serial controller | on-chip | Infineon CAT1 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L257) | [`infineon,cat1-uart`](../../../../build/dts/api/bindings/serial/infineon,cat1-uart.md#std-dtcompatible-infineon-cat1-uart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L47) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Infineon CAT1 Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_01/psoc6_01.dtsi?plain=1#L303) | [`infineon,cat1-watchdog`](../../../../build/dts/api/bindings/watchdog/infineon,cat1-watchdog.md#std-dtcompatible-infineon-cat1-watchdog) |

### System Clock

The PSOC 63 BLE MCU SoC is configured to use the internal IMO+FLL as a source for
the system clock. CM0+ works at 50MHz, CM4 - at 100MHz. Other sources for the
system clock are provided in the SOC, depending on your system requirements.

## Fetch Binary Blobs

cy8cproto\_063\_ble board requires fetch binary files
(e.g Bluetooth controller firmware, CM0p prebuilt images, etc).

To fetch Binary Blobs:

```shell
west blobs fetch hal_infineon
```

## Build blinking led sample

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

```shell
# From the root of the zephyr repository
west build -b cy8cproto_063_ble samples/basic/blinky
```

## Programming and Debugging

The `cy8cproto_063_ble` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

The CY8CPROTO-063-BLE includes an onboard programmer/debugger ([KitProg3](https://github.com/Infineon/KitProg3) [[11]](#id22)) to provide debugging, flash programming, and serial communication over USB. Flash and debug commands use OpenOCD and require a custom Infineon OpenOCD version, that supports KitProg3, to be installed.

### Infineon OpenOCD Installation

Both the full [ModusToolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox) [[8]](#id16) and the [ModusToolbox Programming Tools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools) [[9]](#id18) packages include Infineon OpenOCD. Installing either of these packages will also install Infineon OpenOCD. If neither package is installed, a minimal installation can be done by downloading the [Infineon OpenOCD](https://github.com/Infineon/openocd/releases/latest) [[10]](#id20) release for your system and manually extract the files to a location of your choice.

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
> west build -b cy8cproto_063_ble -p always samples/basic/blinky
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
> west build -b cy8cproto_063_ble -p always samples/basic/blinky
>
> west flash
> west debug
> ```

## References

[[1](#id3)]

[https://www.cypress.com/products/32-bit-arm-cortex-m4-psoc-6](https://www.cypress.com/products/32-bit-arm-cortex-m4-psoc-6)

[[2](#id5)]

[https://www.infineon.com/dgdl/Infineon-PSOC\_6\_MCU\_PSOC\_63\_with\_BLE\_Datasheet\_Programmable\_System-on-Chip\_(PSOC)-DataSheet-v16\_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0ee4efe46c37&utm\_source=cypress&utm\_medium=referral&utm\_campaign=202110\_globe\_en\_all\_integration-files](https://www.infineon.com/dgdl/Infineon-PSOC_6_MCU_PSOC_63_with_BLE_Datasheet_Programmable_System-on-Chip_(PSOC)-DataSheet-v16_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0ee4efe46c37&utm_source=cypress&utm_medium=referral&utm_campaign=202110_globe_en_all_integration-files)

[[3](#id7)]

[https://documentation.infineon.com/html/psoc6/zrs1651212645947.html](https://documentation.infineon.com/html/psoc6/zrs1651212645947.html)

[[4](#id9)]

[https://documentation.infineon.com/html/psoc6/bnm1651211483724.html](https://documentation.infineon.com/html/psoc6/bnm1651211483724.html)

[[5](#id11)]

[https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/)

[[6](#id13)]

[https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/#!?fileId=8ac78c8c7d0d8da4017d0f00d7eb1812](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/#!?fileId=8ac78c8c7d0d8da4017d0f00d7eb1812)

[[7](#id15)]

[https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/#!?fileId=8ac78c8c7d0d8da4017d0f00ea3c1821](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/#!?fileId=8ac78c8c7d0d8da4017d0f00ea3c1821)

[[8](#id17)]

[https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox)

[[9](#id19)]

[https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools)

[[10](#id21)]

[https://github.com/Infineon/openocd/releases/latest](https://github.com/Infineon/openocd/releases/latest)

[[11](#id23)]

[https://github.com/Infineon/KitProg3](https://github.com/Infineon/KitProg3)

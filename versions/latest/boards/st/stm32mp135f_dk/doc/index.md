---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/stm32mp135f_dk/doc/index.html
original_path: boards/st/stm32mp135f_dk/doc/index.html
---

# STM32MP135F-DK Discovery

Board Overview

[![../../../../_images/stm32mp135f_dk.webp](https://docs.zephyrproject.org/4.2.0/_images/stm32mp135f_dk.webp)
](https://docs.zephyrproject.org/4.2.0/_images/stm32mp135f_dk.webp)

STM32MP135F-DK Discovery

Name:
:   `stm32mp135f_dk`

Vendor:
:   STMicroelectronics

Architecture:

SoC:
:   stm32mp135fxx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32mp135f_dk/doc/index.rst/../..)

## Overview

The STM32MP135 Discovery kit (STM32MP135F-DK) leverages the capabilities of the
1 GHz STM32MP135 microprocessors to allow users to develop applications easily with Zephyr RTOS.

It includes an ST-LINK embedded debug tool, LEDs, push-buttons, two 10/100 Mbit/s Ethernet (RMII) connectors, one USB Type-C® connector, four USB Host Type-A connectors, and one microSD™ connector.

To expand the functionality of the STM32MP135 Discovery kit, one GPIO expansion connector is also available for third-party shields.

Additionally, the STM32MP135 Discovery kit features an LCD display with a touch panel, Wi‑Fi® and Bluetooth® Low Energy capability, and a 2-megapixel CMOS camera module.

It also provides secure boot and cryptography features.

Zephyr OS is ported to run on the Cortex®-A7 core.

- STM32MP135FAF7: Arm® Cortex®-A7 32-bit processor at 1 GHz, in a TFBGA320 package
- ST PMIC STPMIC1
- 4-Gbit DDR3L, 16 bits, 533 MHz
- 4.3” 480x272 pixels LCD display module with capacitive touch panel and RGB interface
- UXGA 2-megapixel CMOS camera module (included) with MIPI CSI-2® / SMIA CCP2 deserializer
- Wi-Fi® 802.11b/g/n
- Bluetooth® Low Energy 4.1
- Dual 10/100 Mbit/s Ethernet (RMII) compliant with IEEE-802.3u, one with Wake on LAN (WoL) support
- USB Host 4-port hub
- USB Type-C® DRP based on an STM32G0 device
- 4 user LEDs
- 4 push-buttons (2× user, tamper, and reset)
- 1 wake-up button
- Board connectors:

  - Dual-lane MIPI CSI-2® camera module expansion
  - 2x Ethernet RJ45
  - 4x USB Type-A
  - USB Micro-B
  - USB Type-C®
  - microSD™ card holder
  - GPIO expansion
  - 5 V / 3 A USB Type-C® power supply input (charger not provided)
  - VBAT for power backup
- On-board current measurement
- On-board STLINK-V3E debugger/programmer with USB re-enumeration capability:

  - mass storage
  - Virtual COM port
  - debug port

More information about the board can be found at the
[STM32P135 Discovery website](https://www.st.com/en/evaluation-tools/stm32mp135f-dk.html) [[1]](#id2).

## Hardware

More information about the STM32MP135F\_DK board hardware can be found here:

- [STM32MP135F\_DK Hardware Description](https://wiki.stmicroelectronics.cn/stm32mpu/wiki/STM32MP135x-DK_-_hardware_description) [[7]](#id15)

More information about STM32P135F microprocessor can be found here:

- [STM32MP135F on www.st.com](https://www.st.com/content/st_com/en/products/microcontrollers-microprocessors/stm32-arm-cortex-mpus/stm32mp1-series/stm32mp135/stm32mp135f.html) [[3]](#id6)
- [STM32MP135F reference manual](https://www.st.com/resource/en/reference_manual/DM00670465-.pdf) [[4]](#id8)

### Supported Features

The `stm32mp135f_dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32mp135f_dk/stm32mp135fxx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L59) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st,stm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L31) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L270) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32MP13 CPU Clock Describes the STM32MP13 CPU armv7 timer multiplexer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L282) | [`st,stm32mp13-cpu-clock-mux`](../../../../build/dts/api/bindings/clock/st,stm32mp13-cpu-clock-mux.md#std-dtcompatible-st-stm32mp13-cpu-clock-mux) |
| on-chip | PLL node binding for STM32MP13 devices[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L288)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L300) | [`st,stm32mp13-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32mp13-pll-clock.md#std-dtcompatible-st-stm32mp13-pll-clock) |
| Display | on-chip | STM32 LCD-TFT display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp135.dtsi?plain=1#L47) | [`st,stm32-ltdc`](../../../../build/dts/api/bindings/display/st,stm32-ltdc.md#std-dtcompatible-st-stm32-ltdc) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L77) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | Microchip MCP23017 I2C GPIO Expander[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp135f_dk/stm32mp135f_dk.dts?plain=1#L134) | [`microchip,mcp23017`](../../../../build/dts/api/bindings/gpio/microchip,mcp23017.md#std-dtcompatible-microchip-mcp23017) |
| on-board | GPIO pins exposed on the Raspberry Pi CSI Camera connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp135f_dk/stm32mp135f_dk.dts?plain=1#L68) | [`raspberrypi,csi-connector`](../../../../build/dts/api/bindings/gpio/raspberrypi,csi-connector.md#std-dtcompatible-raspberrypi-csi-connector) |
| I2C | on-chip | STM32 I2C V2 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L183)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L196) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp135f_dk/stm32mp135f_dk.dts?plain=1#L28) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L150) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| on-chip | ARM Generic Interrupt Controller v2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L249) | [`arm,gic-v2`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v2.md#std-dtcompatible-arm-gic-v2) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp135f_dk/stm32mp135f_dk.dts?plain=1#L38) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L71) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L64) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| Serial controller | on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L50) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L45) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp13.dtsi?plain=1#L313) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |
| Video | on-board | MIPID02 CSI to DVP interface bridge[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp135f_dk/stm32mp135f_dk.dts?plain=1#L154) | [`st,mipid02`](../../../../build/dts/api/bindings/video/st,mipid02.md#std-dtcompatible-st-mipid02) |
| on-chip | STM32 Digital Camera Memory Interface Pixel Processor (DCMIPP)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp13/stm32mp135.dtsi?plain=1#L14) | [`st,stm32-dcmipp`](../../../../build/dts/api/bindings/video/st,stm32-dcmipp.md#std-dtcompatible-st-stm32-dcmipp) |

### Connections and IOs

STM32MP135F-DK Discovery Board schematic is available here:
[STM32MP135F Discovery board schematics](https://www.st.com/resource/en/schematic_pack/mb1635-mp135f-e02-schematic.pdf) [[2]](#id4).

#### Default Zephyr Peripheral Mapping:

- USART\_4 TX/RX : PD6/PD8 (UART console)
- USER\_BUTTON : PA13
- LED\_3 : PA14
- LED\_4 : PA13

#### System Clock

The Cortex®-A7 core is configured to run at a clock speed of up to 1GHz.

#### Memory mapping

| Region | Address | Size |
| --- | --- | --- |
| SYSRAM | 0x2FFE0000-0x2FFFFFFF | 128KB |
| SRAM 1 | 0x30000000-0x30003FFF | 16KB |
| SRAM 2 | 0x30004000-0x30005FFF | 8KB |
| SRAM 3 | 0x30006000-0x30007FFF | 8KB |
| DDR | 0xC0000000-0xDFFFFFFF | 512 MB |

## Programming and Debugging

The `stm32mp135f_dk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Prerequisite

The STM32MP135 has a DDR controller that need to be initialized before loading the Zephyr example.

One method to perform this is to flash the Zephyr executable, along with the DDR initialization script, on an SD card inserted in the board. To do so, you first need to [install STM32CubeProgrammer](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) and download the [STM32CubeMP13 package](https://github.com/STMicroelectronics/STM32CubeMP13) [[6]](#id13).

### Signature and flashing

After building the Zephyr project, you need to sign your binary file using the Stm32ImageAddHeader.py with the following command:

```shell
python3 ${Path_to_STM32CubeMP13}/Utilities/ImageHeader/Python3/Stm32ImageAddHeader.py ${Path_to_build_dir}/zephyr/zephyr.bin ${STM32CubeMP13}/Projects/STM32MP135C-DK/External_Loader/Prebuild_Binaries/SD_Ext_Loader/zephyr_Signed.bin -bt 10 -la C0000000 -ep C0000000
```

Here -bt specifies the boot type, -la specifies the load address and -ep the entry point for your executable (same as the load address in this case).

Then, copy [boards/st/stm32mp135f\_dk/support/Zephyr.tsv](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp135f_dk/support/Zephyr.tsv) to `${Path_to_STM32CubeMP13}/Projects/STM32MP135C-DK/External_Loader/Prebuild_Binaries/SD_Ext_Loader/`.

Finally using the Cube Programmer select the Zephyr.tsv and flash the SD card with the following command:

```shell
${Path_to_STM32cube_Programmer}/bin/STM32_Programmer.sh -c port=${ConnectedPort} p=even br=115200 -d ${Path_to_STM32CubeMP13}/Projects/STM32MP135C-DK/External_Loader/Prebuild_Binaries/SD_Ext_Loader/Zephyr.tsv
```

Note

You can refer to this example to flash an example to the SD card:
[How to install STM32Cube software package on microSD card](https://wiki.st.com/stm32mpu/wiki/How_to_load_and_start_STM32CubeMP13_applications_via_microSD_card) [[5]](#id10)

### Debugging

You can debug an application using OpenOCD and GDB.

- Build the sample:

  ```shell
  # From the root of the zephyr repository
  west build -b stm32mp135f_dk samples/hello_world
  ```
- Flash the SD card using:
  [How to install STM32Cube software package on microSD card](https://wiki.st.com/stm32mpu/wiki/How_to_load_and_start_STM32CubeMP13_applications_via_microSD_card) [[5]](#id10)
- Run the application from the SD card
- Attach to the target:

  ```shell
  west attach
  ```

Note

The `run` command of GDB isn’t supported at the moment for this board.

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/stm32mp135f-dk.html](https://www.st.com/en/evaluation-tools/stm32mp135f-dk.html)

[[2](#id5)]

[https://www.st.com/resource/en/schematic\_pack/mb1635-mp135f-e02-schematic.pdf](https://www.st.com/resource/en/schematic_pack/mb1635-mp135f-e02-schematic.pdf)

[[3](#id7)]

[https://www.st.com/content/st\_com/en/products/microcontrollers-microprocessors/stm32-arm-cortex-mpus/stm32mp1-series/stm32mp135/stm32mp135f.html](https://www.st.com/content/st_com/en/products/microcontrollers-microprocessors/stm32-arm-cortex-mpus/stm32mp1-series/stm32mp135/stm32mp135f.html)

[[4](#id9)]

[https://www.st.com/resource/en/reference\_manual/DM00670465-.pdf](https://www.st.com/resource/en/reference_manual/DM00670465-.pdf)

[5]
([1](#id11),[2](#id12))

[https://wiki.st.com/stm32mpu/wiki/How\_to\_load\_and\_start\_STM32CubeMP13\_applications\_via\_microSD\_card](https://wiki.st.com/stm32mpu/wiki/How_to_load_and_start_STM32CubeMP13_applications_via_microSD_card)

[[6](#id14)]

[https://github.com/STMicroelectronics/STM32CubeMP13](https://github.com/STMicroelectronics/STM32CubeMP13)

[[7](#id16)]

[https://wiki.stmicroelectronics.cn/stm32mpu/wiki/STM32MP135x-DK\_-\_hardware\_description](https://wiki.stmicroelectronics.cn/stm32mpu/wiki/STM32MP135x-DK_-_hardware_description)

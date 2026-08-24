---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/quicklogic/quick_feather/doc/index.html
original_path: boards/quicklogic/quick_feather/doc/index.html
---

# QuickFeather

Board Overview

[![../../../../_images/feather-board.jpg](https://docs.zephyrproject.org/4.1.0/_images/feather-board.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/feather-board.jpg)

QuickFeather

Name:
:   `quick_feather`

Vendor:
:   QuickLogic Corp.

Architecture:
:   arm

SoC:
:   quicklogic\_eos\_s3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/quicklogic/quick_feather/doc/index.rst/../..)

## Overview

The QuickFeather development board is a platform with an on-board QuickLogic
EOS S3 Sensor Processing Platform.

## Hardware

- QuickLogic EOS S3 MCU Platform
- mCube MC3635 accelerometer
- Infineon DPS310 pressure sensor
- Infineon IM69D130 MEMS microphone
- 16 Mbit of on-board flash memory
- User button
- RGB LED
- Integrated battery charger

Detailed information about the board can be found in a [QuickFeather repository](https://github.com/QuickLogic-Corp/quick-feather-dev-board) [[1]](#id2).

### Supported Features

The `quick_feather` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `quick_feather/quicklogic_eos_s3` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L16) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L35) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| GPIO & Headers | on-chip | EOS S3 GPIO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L56) | [`quicklogic,eos-s3-gpio`](../../../../build/dts/api/bindings/gpio/quicklogic,eos-s3-gpio.md#std-dtcompatible-quicklogic-eos-s3-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/quicklogic/quick_feather/quick_feather.dts?plain=1#L48) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/quicklogic/quick_feather/quick_feather.dts?plain=1#L30) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L23) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| Pin control | on-chip | Quicklogic EOS S3 IO MUX binding covers the 46 IOMUX\_PAD\_x\_CTRL registers that can be used to set the direction and the function of a pad[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L67) | [`quicklogic,eos-s3-pinctrl`](../../../../build/dts/api/bindings/pinctrl/quicklogic,eos-s3-pinctrl.md#std-dtcompatible-quicklogic-eos-s3-pinctrl) |
| Serial controller | on-chip | ARM PL011 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L42) | [`arm,pl011`](../../../../build/dts/api/bindings/serial/arm,pl011.md#std-dtcompatible-arm-pl011) |
| on-chip | QuickLogic USBserialport\_S3B serial interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L50) | [`quicklogic,usbserialport-s3b`](../../../../build/dts/api/bindings/serial/quicklogic,usbserialport-s3b.md#std-dtcompatible-quicklogic-usbserialport-s3b) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L30) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

### Connections and IOs

Detailed information about pinouts is available in the [schematics document](https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/quickfeather-board.pdf) [[2]](#id4).

## Programming and Debugging

### Flashing

The QuickFeather platform by default boots from flash. Currently
the Zephyr port only enables loading the program directly to SRAM using either
OpenOCD and a SWD programmer or SEGGER JLink.

#### OpenOCD

In order to connect to the target a SWD programmer supported in
OpenOCD is needed. To connect to the board run:

```shell
openocd -f /path/to/swd-programmer.cfg -f tcl/board/quicklogic_quickfeather.cfg -c "init" -c "reset halt"
```

[The QuickFeather OpenOCD config](https://sourceforge.net/p/openocd/code/ci/master/tree/tcl/board/quicklogic_quickfeather.cfg) [[3]](#id6) can be found in the OpenOCD mainline repository.

#### JLink

To connect to the QuickFeather board with JLink please follow instructions
in the [QuickFeather User Guide](https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/QuickFeather_UserGuide.pdf) [[4]](#id8).

### Debugging

To debug the QuickFeather board please connect to the target with either
OpenOCD or JLink and use GDB distributed in Zephyr’s SDK in *arm-zephyr-eabi/bin*
directory.

To load basic sample via GDB:

- Build the sample in an usual way:

```shell
# From the root of the zephyr repository
west build -b quick_feather samples/hello_world
```

- Connect to the target using either OpenOCD or JLink
- Connect via GDB and load an ELF file:

```shell
/path/to/zephyr-sdk/arm-zephyr-eabi/bin/arm-zephyr-eabi-gdb
target remote <port_number>
file </path/to/zephyr.elf>
load
continue
```

## References

[[1](#id3)]

[https://github.com/QuickLogic-Corp/quick-feather-dev-board](https://github.com/QuickLogic-Corp/quick-feather-dev-board)

[[2](#id5)]

[https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/quickfeather-board.pdf](https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/quickfeather-board.pdf)

[[3](#id7)]

[https://sourceforge.net/p/openocd/code/ci/master/tree/tcl/board/quicklogic\_quickfeather.cfg](https://sourceforge.net/p/openocd/code/ci/master/tree/tcl/board/quicklogic_quickfeather.cfg)

[[4](#id9)]

[https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/QuickFeather\_UserGuide.pdf](https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/QuickFeather_UserGuide.pdf)

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/amd/versalnet_rpu/doc/index.html
original_path: boards/amd/versalnet_rpu/doc/index.html
---

# Versal NET RPU development board

Board Overview

Name:
:   `versalnet_rpu`

Vendor:
:   Advanced Micro Devices (AMD), Inc.

Architecture:
:   arm

SoC:
:   amd\_versalnet\_rpu

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/amd/versalnet_rpu/doc/index.rst/../..)

## Overview

This configuration provides support for the RPU(R52), real-time processing unit on Xilinx
Versal Net SOC, it can operate as following:

- Two independent R52 cores with their own TCMs (tightly coupled memories)
- Or as a single dual lock step unit with the TCM.

This processing unit is based on an ARM Cortex-R52 CPU, it also enables the following devices:

- ARM GIC v3 Interrupt Controller
- Global Timer Counter
- SBSA UART

## Hardware

### Supported Features

The `versalnet_rpu` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `versalnet_rpu/amd_versalnet_rpu` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R52 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/versalnet_r52.dtsi?plain=1#L20) | [`arm,cortex-r52`](../../../../build/dts/api/bindings/cpu/arm,cortex-r52.md#std-dtcompatible-arm-cortex-r52) |
| Clock control | on-board | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/amd/versalnet_rpu/versalnet_rpu.dts?plain=1#L18) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/versalnet_r52.dtsi?plain=1#L41) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| SDHC | on-chip | Xilinx SD/EMMC host controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versalnet.dtsi?plain=1#L32) | [`xlnx,versal-8.9a`](../../../../build/dts/api/bindings/sdhc/xlnx,sdhc.md#std-dtcompatible-xlnx-versal-8.9a) |
| Serial controller | on-chip | ARM SBSA UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versalnet.dtsi?plain=1#L16) | [`arm,sbsa-uart`](../../../../build/dts/api/bindings/serial/arm,sbsa-uart.md#std-dtcompatible-arm-sbsa-uart) |
| SRAM | on-board | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/amd/versalnet_rpu/versalnet_rpu.dts?plain=1#L30) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/versalnet_r52.dtsi?plain=1#L27) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

### Devices

#### System Timer

This board configuration uses a system timer tick frequency of 100 MHz.

#### Serial Port

This board configuration uses a single serial communication channel with the
on-chip UART0.

#### Memories

Although Flash, DDR and OCM memory regions are defined in the DTS file,
all the code plus data of the application will be loaded in the sram0 region,
which points to the DDR memory. The ocm0 memory area is currently available
for usage, although nothing is placed there by default.

### Known Problems or Limitations

The following platform features are unsupported:

- Only the first core of the R52 subsystem is supported.

## Programming and Debugging

The `versalnet_rpu` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **simulate** | **rtt** | **robot** | **debugserver** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **xsdb** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ | ✅ | ✅ |

Build and flash in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b versalnet_rpu samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World!
```

## References

1. ARMv8-R Architecture Reference Manual (ARM DDI 0568A.c ID110520)
2. Cortex-R52 and Cortex-R52F Technical Reference Manual (ARM DDI r1p4 100026\_0104\_01\_en)

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/arm/mps4/doc/index.html
original_path: boards/arm/mps4/doc/index.html
---

# MPS4

Board Overview

Name:
:   `mps4`

Vendor:
:   ARM Ltd.

Architecture:
:   arm

SoC:
:   corstone315, corstone320

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arm/mps4/doc/index.rst/../..)

## Overview

The MPS4 board configuration is used by Zephyr applications that run
on the MPS4 board.

[Corstone-315 FVP](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)/[Corstone-320 FVP](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps) are Arm reference subsystem for
secure System on Chips containing an Armv8.1-M Cortex-M85 processor,
LCM, KMU and SAM IPs. Corstone-320 FVP have Ethos-U85 while
Corstone-315 FVP have a Ethos-U65 neural network processor.
They are available free of charge for Linux and Windows systems.
The FVPs have been selected for simulation since they provide access to the
Ethos-U65/Ethos-U85 NPU, which is unavailable in QEMU or other simulation platforms.

### Zephyr board options

MPS4 Corstone-315 (FVP)MPS4 Corstone-320 (FVP)

The MPS4 FVP is an SoC with Cortex-M85 architecture. Zephyr provides support
for building for both Secure and Non-Secure firmware.

The BOARD options are summarized below:

| BOARD | Description |
| --- | --- |
| `mps4/corstone315/fvp` | For building Secure (or Secure-only) firmware |
| `mps4/corstone315/fvp/ns` | For building Non-Secure firmware |

FPGA Usage:
:   - N/A.

FVP Usage:
:   - To run with the FVP, first set environment variable `ARMFVP_BIN_PATH` before using it. Then you can run it with `west build -t run`.

    ```shell
    export ARMFVP_BIN_PATH=/path/to/fvp/directory
    west build -b {BOARD qualifier from table above} samples/hello_world -t run
    ```

To run the Fixed Virtual Platform simulation tool you must download “FVP model
for the Corstone-315 MPS4” from Arm and install it on your host PC.

QEMU Usage:
:   - N/A.

The MPS4 FVP is an SoC with Cortex-M85 architecture. Zephyr provides support
for building for both Secure and Non-Secure firmware.

The BOARD options are summarized below:

| BOARD | Description |
| --- | --- |
| `mps4/corstone320/fvp` | For building Secure (or Secure-only) firmware |
| `mps4/corstone320/fvp/ns` | For building Non-Secure firmware |

FPGA Usage:
:   - N/A.

FVP Usage:
:   - To run with the FVP, first set environment variable `ARMFVP_BIN_PATH` before using it. Then you can run it with `west build -t run`.

    ```shell
    export ARMFVP_BIN_PATH=/path/to/fvp/directory
    west build -b {BOARD qualifier from table above} samples/hello_world -t run
    ```

To run the Fixed Virtual Platform simulation tool you must download “FVP model
for the Corstone-320 MPS4” from Arm and install it on your host PC. This board
has been tested with version 11.27.25 (Sep 24 2024).

QEMU Usage:
:   - N/A.

Note

- Board qualifier must include the variant name as mentioned above.
  `mps4/corstone315`/ `mps4/corstone320` without the variant name is not a valid qualifier.
- `mps4/corstone315/fvp/ns`/ `mps4/corstone320/fvp/ns` variant needs latest upstream TF-M release since Zephyr’s current
  TF-M doesn’t support Corstone-315 FVP yet.

## Hardware

No H/W available yet, only ARMFVP simulated board variants are supported for now.

### Supported Features

The `mps4` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mps4/corstone315/fvp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-board | ARM Cortex-M85 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_corstone315_fvp.dts?plain=1#L30) | [`arm,cortex-m85`](../../../../build/dts/api/bindings/cpu/arm,cortex-m85.md#std-dtcompatible-arm-cortex-m85) |
| ARM architecture | on-board | The Arm Ethos-U is a micro NPU that enables neural networks to be hardware accelerated on embedded devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_corstone315_fvp.dts?plain=1#L49) | [`arm,ethos-u`](../../../../build/dts/api/bindings/arm/arm,ethos-u.md#std-dtcompatible-arm-ethos-u) |
| Clock control | on-board | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L7) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Ethernet | on-board | SMSC (now Microchip) LAN9220 Ethernet controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L45) | [`smsc,lan9220`](../../../../build/dts/api/bindings/ethernet/smsc,lan9220.md#std-dtcompatible-smsc-lan9220) |
| GPIO & Headers | on-board | ARM CMSDK GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L13) | [`arm,cmsdk-gpio`](../../../../build/dts/api/bindings/gpio/arm,cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio) |
| on-board | ARM MMIO32 GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L131) | [`arm,mmio32-gpio`](../../../../build/dts/api/bindings/gpio/arm,mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio) |
| I2C | on-board | ARM SBCon two-wire serial bus interface[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L53) | [`arm,versatile-i2c`](../../../../build/dts/api/bindings/i2c/arm,versatile-i2c.md#std-dtcompatible-arm-versatile-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common.dtsi?plain=1#L77) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8.1-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17) | [`arm,v8.1m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8.1m-nvic.md#std-dtcompatible-arm-v8.1m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common.dtsi?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-board | ARMv8.1-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_corstone315_fvp.dts?plain=1#L37) | [`arm,armv8.1m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu) |
| Pin control | on-board | The Arm Mps4 pin controller is a node responsible for controlling pin function selection and pin properties, such as routing a UART3 TX to pin 1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L215) | [`arm,mps4-pinctrl`](../../../../build/dts/api/bindings/pinctrl/arm,mps4-pinctrl.md#std-dtcompatible-arm-mps4-pinctrl) |
| Serial controller | on-board | ARM CMSDK UART[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L156)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L205) | [`arm,cmsdk-uart`](../../../../build/dts/api/bindings/serial/arm,cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart) |
| SPI | on-board | ARM PL022 SPI[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L69) | [`arm,pl022`](../../../../build/dts/api/bindings/spi/arm,pl022.md#std-dtcompatible-arm-pl022) |
| Timer | on-chip | ARMv8.1-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25) | [`arm,armv8.1m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8.1m-systick.md#std-dtcompatible-arm-armv8.1m-systick) |

#### `mps4/corstone320/fvp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-board | ARM Cortex-M85 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_corstone320_fvp.dts?plain=1#L30) | [`arm,cortex-m85`](../../../../build/dts/api/bindings/cpu/arm,cortex-m85.md#std-dtcompatible-arm-cortex-m85) |
| ARM architecture | on-board | The Arm Ethos-U is a micro NPU that enables neural networks to be hardware accelerated on embedded devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_corstone320_fvp.dts?plain=1#L49) | [`arm,ethos-u`](../../../../build/dts/api/bindings/arm/arm,ethos-u.md#std-dtcompatible-arm-ethos-u) |
| Clock control | on-board | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L7) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Ethernet | on-board | SMSC (now Microchip) LAN9220 Ethernet controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L45) | [`smsc,lan9220`](../../../../build/dts/api/bindings/ethernet/smsc,lan9220.md#std-dtcompatible-smsc-lan9220) |
| GPIO & Headers | on-board | ARM CMSDK GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L13) | [`arm,cmsdk-gpio`](../../../../build/dts/api/bindings/gpio/arm,cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio) |
| on-board | ARM MMIO32 GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L131) | [`arm,mmio32-gpio`](../../../../build/dts/api/bindings/gpio/arm,mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio) |
| I2C | on-board | ARM SBCon two-wire serial bus interface[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L53) | [`arm,versatile-i2c`](../../../../build/dts/api/bindings/i2c/arm,versatile-i2c.md#std-dtcompatible-arm-versatile-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common.dtsi?plain=1#L77) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8.1-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17) | [`arm,v8.1m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8.1m-nvic.md#std-dtcompatible-arm-v8.1m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common.dtsi?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-board | ARMv8.1-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_corstone320_fvp.dts?plain=1#L37) | [`arm,armv8.1m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu) |
| Pin control | on-board | The Arm Mps4 pin controller is a node responsible for controlling pin function selection and pin properties, such as routing a UART3 TX to pin 1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L215) | [`arm,mps4-pinctrl`](../../../../build/dts/api/bindings/pinctrl/arm,mps4-pinctrl.md#std-dtcompatible-arm-mps4-pinctrl) |
| Serial controller | on-board | ARM CMSDK UART[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L156)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L205) | [`arm,cmsdk-uart`](../../../../build/dts/api/bindings/serial/arm,cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart) |
| SPI | on-board | ARM PL022 SPI[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L69) | [`arm,pl022`](../../../../build/dts/api/bindings/spi/arm,pl022.md#std-dtcompatible-arm-pl022) |
| Timer | on-chip | ARMv8.1-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25) | [`arm,armv8.1m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8.1m-systick.md#std-dtcompatible-arm-armv8.1m-systick) |

### Serial Port

The MPS4 has six UARTs. The Zephyr console output by default, uses
UART0.

Serial port 0 on the Debug USB interface is the MCC board control console.

Serial port 1 on the Debug USB interface is connected to UART 0.

Serial port 2 on the Debug USB interface is connected to UART 1.

Serial port 3 on the Debug USB interface is connected to UART 2.

## Programming and Debugging

### Flashing

- N/A since the only support available is FVP.

#### Building an application with Corstone-315

You can build applications in the usual way. Here is an example for
the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application with Corstone-315.

```shell
# From the root of the zephyr repository
west build -b mps4/corstone315/fvp samples/hello_world
west build -t run
```

Run with FVP and you should see the following message:

```shell
Hello World! mps4
```

#### Building an application with Corstone-320

You can build applications in the usual way. Here is an example for
the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application with Corstone-320.

```shell
# From the root of the zephyr repository
west build -b mps4/corstone320/fvp samples/hello_world
west build -t run
```

Run with FVP and you should see the following message:

```shell
Hello World! mps4
```

For more details refer to:
:   - [Corstone SSE-315 Reference Guide](https://developer.arm.com/documentation/109395/0000)
    - [Corstone SSE-320 Reference Guide](https://developer.arm.com/documentation/109760/0000/)
    - [Cortex M85 Generic User Guide](https://developer.arm.com/documentation/101924/latest)
    - [Arm Corstone-320 Reference Package Technical Overview](https://developer.arm.com/documentation/109761/0000/)
    - [Arm MPS4 FPGA Prototyping Board Technical Reference Manual](https://developer.arm.com/documentation/102577/0000/)

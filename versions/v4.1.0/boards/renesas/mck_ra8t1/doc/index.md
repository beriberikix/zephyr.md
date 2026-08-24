---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/renesas/mck_ra8t1/doc/index.html
original_path: boards/renesas/mck_ra8t1/doc/index.html
---

# RA8T1 Motor Control Kit

Board Overview

[![../../../../_images/mck_ra8t1.jpg](https://docs.zephyrproject.org/4.1.0/_images/mck_ra8t1.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/mck_ra8t1.jpg)

RA8T1 Motor Control Kit

Name:
:   `mck_ra8t1`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7fa8t1ahecbd

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/mck_ra8t1/doc/index.rst/../..)

## Overview

The **MCK-RA8T1** is a development kit that enables easy evaluation of motor control using permanent magnet synchronous
motors (brushless DC motors). More detailed information about the features of this toolkit and it’s applications can be
found here: [MCK-RA8T1 Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/rtk0ema5k0s00020bj-mck-ra8t1-renesas-flexible-motor-control-kit-ra8t1-mcu-group)

MCK-RA8T1 kit includes the items below:

- RA8T1 CPU board ([MCB-RA8T1](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/rtk0ema5k0c00000bj-mcb-ra8t1-cpu-board-ra8t1-mcu-group))
- Inverter board ([MCI-LV-1](https://www.renesas.com/us/en/products/power-power-management/fet-motor-drivers/rtk0em0000s04020bj-mci-lv-1-renesas-flexible-motor-control-inverter-board-low-voltage-48v10a-three-phase-bldcpmsm-motor))
- Communication board ([MC-COM](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/rtk0emxc90s00000bj-mc-com-renesas-flexible-motor-control-communication-board))
- Permanent magnet synchronous motors
- Accessories (cables, standoffs, etc.)

![RA8T1 Motor Control Kit](https://docs.zephyrproject.org/4.1.0/_images/mck_ra8t1_product_contents.jpg)

MCK-RA8T1 product contents (Credit: Renesas Electronics Corporation)

**MCB-RA8T1** is a CPU board for motor control equipped with RA8T1. Motor control using RA8T1 can be easily realized by
using it in combination with a supported inverter board. The RA8T1 MCU can be evaluated using this board alone.

By using a supported communication board, the CPU board can be electrically isolated from the PC for safe motor control
evaluation and debugging.

The specifications of the CPU board are shown below:

**MCU specifications**

- 480MHz Arm Cortex-M85 based RA8T1 MCU in 224 pins, BGA package
- ROM/RAM size: 2MB/1MB
- MCU input clock: 24MHz (Generate with external crystal oscillator)
- Power supply: DC 5V, select one way automatically from the below:

  - Power is supplied from compatible inverter board
  - Power is supplied from USB connector

**Connector**

- Inverter board connector (2 pair)
- USB connector for J-Link OB
- USB connector for RA8T1
- SCI connector for Renesas Motor Workbench communication
- Through hole for CAN communication
- 20 pin through hole for Arm debugger
- Pmod connectors (Type6A + Type2A/3A)
- Ethrnet connector
- microSD card connector

**Onboard debugger**

This product has the onboard debugger circuit, J-Link On-Board (hereinafter called “J-Link-OB”). You can
write a program (firmware) of RA8T1 with it.

## Hardware

Detailed Hardware features for the RA8T1 MCU group can be found at [RA8T1 Group User’s Manual Hardware](https://www.renesas.com/us/en/document/mah/ra8t1-group-users-manual-hardware?r=25463106)

[![RA8T1 MCU group feature](https://docs.zephyrproject.org/4.1.0/_images/ra8t1_block_diagram.png)
](https://docs.zephyrproject.org/4.1.0/_images/ra8t1_block_diagram.png)

RA8T1 Block diagram (Credit: Renesas Electronics Corporation)

Detailed Hardware features for the MCB-RA8T1 board can be found at [MCB-RA8T1 - User’s Manual](https://www.renesas.com/us/en/document/mat/mcb-ra8t1-users-manual?r=25466356)

### Supported Features

The `mck_ra8t1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mck_ra8t1/r7fa8t1ahecbd` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M85 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L19) | [`arm,cortex-m85`](../../../../build/dts/api/bindings/cpu/arm,cortex-m85.md#std-dtcompatible-arm-cortex-m85) |
| ADC | on-chip | Renesas RA ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L286)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L298) | [`renesas,ra-adc`](../../../../build/dts/api/bindings/adc/renesas,ra-adc.md#std-dtcompatible-renesas-ra-adc) |
| CAN | on-chip | Renesas RA CANFD controller global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L556) | [`renesas,ra-canfd-global`](../../../../build/dts/api/bindings/can/renesas,ra-canfd-global.md#std-dtcompatible-renesas-ra-canfd-global) |
| on-chip | Renesas RA CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L577)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L567) | [`renesas,ra-canfd`](../../../../build/dts/api/bindings/can/renesas,ra-canfd.md#std-dtcompatible-renesas-ra-canfd) |
| Clock control | on-chip | Renesas RA Clock Generation Circuit external clock configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L15) | [`renesas,ra-cgc-external-clock`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L22) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Renesas RA Sub-Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L40) | [`renesas,ra-cgc-subclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L47)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L80) | [`renesas,ra-cgc-pll`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock out line[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L54)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L87) | [`renesas,ra-cgc-pll-out`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pll-out.md#std-dtcompatible-renesas-ra-cgc-pll-out) |
| on-chip | Renesas RA Clock Control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L113) | [`renesas,ra-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block) |
| on-chip | Renesas RA Clock Control Peripheral Clock[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L123)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L193) | [`renesas,ra-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk) |
| on-chip | Renesas RA External Bus Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L176) | [`renesas,ra-cgc-busclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-busclk.md#std-dtcompatible-renesas-ra-cgc-busclk) |
| Counter | on-chip | Renesas RA AGT as Counter[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L533) | [`renesas,ra-agt-counter`](../../../../build/dts/api/bindings/counter/renesas,ra-agt-counter.md#std-dtcompatible-renesas-ra-agt-counter) |
| DAC | on-chip | Renesas RA DAC Controller Global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L310) | [`renesas,ra-dac-global`](../../../../build/dts/api/bindings/dac/renesas,ra-dac-global.md#std-dtcompatible-renesas-ra-dac-global) |
| on-chip | Renesas RA DAC Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L316)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L323) | [`renesas,ra-dac`](../../../../build/dts/api/bindings/dac/renesas,ra-dac.md#std-dtcompatible-renesas-ra-dac) |
| Ethernet | on-chip | Renesas RA Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L588) | [`renesas,ra-ethernet`](../../../../build/dts/api/bindings/ethernet/renesas,ra-ethernet.md#std-dtcompatible-renesas-ra-ethernet) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/mck_ra8t1/mck_ra8t1.dts?plain=1#L181) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | Renesas RA family flash high-performance controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L273) | [`renesas,ra-flash-hp-controller`](../../../../build/dts/api/bindings/flash_controller/renesas,ra-flash-hp-controller.md#std-dtcompatible-renesas-ra-flash-hp-controller) |
| GPIO & Headers | on-chip | Renesas RA GPIO IO port[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L83)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L53) | [`renesas,ra-gpio-ioport`](../../../../build/dts/api/bindings/gpio/renesas,ra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport) |
| I2C | on-chip | Renesas RA I2C Master controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L174) | [`renesas,ra-iic`](../../../../build/dts/api/bindings/i2c/renesas,ra-iic.md#std-dtcompatible-renesas-ra-iic) |
| Interrupt controller | on-chip | ARMv8.1-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17) | [`arm,v8.1m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8.1m-nvic.md#std-dtcompatible-arm-v8.1m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/mck_ra8t1/mck_ra8t1.dts?plain=1#L27) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | Renesas RA External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L597) | [`renesas,ra-mdio`](../../../../build/dts/api/bindings/mdio/renesas,ra-mdio.md#std-dtcompatible-renesas-ra-mdio) |
| Miscellaneous | on-chip | Renesas RA SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L231)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L189) | [`renesas,ra-sci`](../../../../build/dts/api/bindings/misc/renesas,ra-sci.md#std-dtcompatible-renesas-ra-sci) |
| on-chip | Renesas RA AGT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L522) | [`renesas,ra-agt`](../../../../build/dts/api/bindings/misc/renesas,ra-agt.md#std-dtcompatible-renesas-ra-agt) |
| on-chip | Renesas RA External Interrupt[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L604) | [`renesas,ra-external-interrupt`](../../../../build/dts/api/bindings/misc/renesas,ra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt) |
| MMU / MPU | on-chip | ARMv8.1-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L26) | [`arm,armv8.1m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu) |
| MTD | on-chip | Flash memory binding of Renesas RA family[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1ahecbd.dtsi?plain=1#L12) | [`renesas,ra-nv-flash`](../../../../build/dts/api/bindings/mtd/renesas,ra-nv-flash.md#std-dtcompatible-renesas-ra-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/mck_ra8t1/mck_ra8t1.dts?plain=1#L132) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L793) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | The Renesas RA pin controller is a node responsible for controlling pin function selection and pin properties, such as routing a SCI0 RXD to P610[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L47) | [`renesas,ra-pinctrl-pfs`](../../../../build/dts/api/bindings/pinctrl/renesas,ra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs) |
| PWM | on-chip | Renesas RA Pulse Width Modulation[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L381)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L361) | [`renesas,ra-pwm`](../../../../build/dts/api/bindings/pwm/renesas,ra-pwm.md#std-dtcompatible-renesas-ra-pwm) |
| RNG | on-chip | Renesas RA RSIP-E51A TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L331) | [`renesas,ra-rsip-e51a-trng`](../../../../build/dts/api/bindings/rng/renesas,ra-rsip-e51a-trng.md#std-dtcompatible-renesas-ra-rsip-e51a-trng) |
| SDHC | on-chip | Renesas RA SDHC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L748)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L763) | [`renesas,ra-sdhc`](../../../../build/dts/api/bindings/sdhc/renesas,ra-sdhc.md#std-dtcompatible-renesas-ra-sdhc) |
| Serial controller | on-chip | Renesas RA SCI\_B UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L238)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L196) | [`renesas,ra8-uart-sci-b`](../../../../build/dts/api/bindings/serial/renesas,ra8-uart-sci-b.md#std-dtcompatible-renesas-ra8-uart-sci-b) |
| SPI | on-chip | Renesas RA8 SPI\_B controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L335)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L348) | [`renesas,ra8-spi-b`](../../../../build/dts/api/bindings/spi/renesas,ra8-spi-b.md#std-dtcompatible-renesas-ra8-spi-b) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L36) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8.1-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25) | [`arm,armv8.1m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8.1m-systick.md#std-dtcompatible-arm-armv8.1m-systick) |
| USB | on-chip | Renesas RA USB full-speed controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L776) | [`renesas,ra-usbfs`](../../../../build/dts/api/bindings/usb/renesas/renesas,ra-usbfs.md#std-dtcompatible-renesas-ra-usbfs) |
| on-chip | Renesas RA USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L786) | [`renesas,ra-udc`](../../../../build/dts/api/bindings/usb/renesas/renesas,ra-udc.md#std-dtcompatible-renesas-ra-udc) |

Note

For using SDHC module on EK-RA8M1, Connect microSD Card to microSD Socket (CN12)

## Programming and Debugging

Applications for the `mcb_ra8t1` board configuration can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

**Note:** Only support from SDK v0.16.6 in which GCC for Cortex Arm-M85 was available.
To build for EK-RA8M1 user need to get and install GNU Arm Embedded toolchain from [https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.6](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.6)

### Flashing

Program can be flashed to MCB-RA8T1 via the on-board SEGGER J-Link debugger.
SEGGER J-link’s drivers are available at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

To flash the program to board

1. Connect to J-Link OB via USB port to host PC
2. Make sure J-Link OB jumper is in default configuration as describe in [MCB-RA8T1 - User’s Manual](https://www.renesas.com/us/en/document/mat/mcb-ra8t1-users-manual?r=25466356)
3. Execute west command

   > ```shell
   > west flash -r jlink
   > ```

### Debugging

You can use Segger Ozone ([Segger Ozone Download](https://www.segger.com/downloads/jlink#Ozone)) for a visual debug interface

Once downloaded and installed, open Segger Ozone and configure the debug project
like so:

- Target Device: R7FA8T1AH
- Target Interface: SWD
- Target Interface Speed: 4 MHz
- Host Interface: USB
- Program File: <path/to/your/build/zephyr.elf>

**Note:** It’s verified that debug is OK on Segger Ozone v3.30d so please use this or later
version of Segger Ozone

## References

- [MCB-RA8T1 Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/rtk0ema5k0c00000bj-mcb-ra8t1-cpu-board-ra8t1-mcu-group)
- [RA8T1 MCU group Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra8t1-480-mhz-arm-cortex-m85-based-motor-control-microcontroller-helium-and-trustzone)

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/telink/tlsr9518adk80d/doc/index.html
original_path: boards/telink/tlsr9518adk80d/doc/index.html
---

# TLSR9518ADK80D

Board Overview

[![../../../../_images/tlsr9518adk80d.jpg](../../../../_images/tlsr9518adk80d.jpg)
](../../../../_images/tlsr9518adk80d.jpg)

TLSR9518ADK80D

Name:
:   `tlsr9518adk80d`

Vendor:
:   Telink Semiconductor

Architecture:
:   riscv

SoC:
:   tlsr9518

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/telink/tlsr9518adk80d/doc/index.rst/../..)

## Overview

The TLSR9518A Generic Starter Kit is a hardware platform which
can be used to verify the [Telink TLSR951x series chipset](https://wiki.telink-semi.cn/wiki/chip-series/TLSR951x-Series/) [[1]](#id2) and develop applications
for several 2.4 GHz air interface standards including Bluetooth 5.2 (Basic data
rate, Enhanced data rate, LE, Indoor positioning and BLE Mesh),
Zigbee 3.0, Homekit, 6LoWPAN, Thread and 2.4 Ghz proprietary.

More information about the board can be found at the [Telink B91 Generic Starter Kit Hardware Guide](https://wiki.telink-semi.cn/wiki/Hardware/B91_Generic_Starter_Kit_Hardware_Guide/) [[2]](#id4) website.

## Hardware

The TLSR9518A SoC integrates a powerful 32-bit RISC-V MCU, DSP, AI Engine, 2.4 GHz ISM Radio, 256
KB SRAM (128 KB of Data Local Memory and 128 KB of Instruction Local Memory), external Flash memory,
stereo audio codec, 14 bit AUX ADC, analog and digital Microphone input, PWM, flexible IO interfaces,
and other peripheral blocks required for advanced IoT, hearable, and wearable devices.

![TLSR9518ADK80D_SOC](../../../../_images/tlsr9518_block_diagram.jpg)

The TLSR9518ADK80D default board configuration provides the following hardware components:

- RF conducted antenna
- 1 MB External Flash memory with reset button
- Chip reset button
- Mini USB interface
- 4-wire JTAG
- 4 LEDs, Key matrix up to 4 keys
- 2 line-in function (Dual Analog microphone supported when switching jumper from microphone path)
- Dual Digital microphone
- Stereo line-out

### Supported Features

The `tlsr9518adk80d` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `tlsr9518adk80d/tlsr9518` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Telink RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L22) | [`telink,b91`](../../../../build/dts/api/bindings/cpu/telink%2Cb91.md#std-dtcompatible-telink-b91) |
| ADC | on-chip | Telink B91 ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L211) | [`telink,b91-adc`](../../../../build/dts/api/bindings/adc/telink%2Cb91-adc.md#std-dtcompatible-telink-b91-adc) |
| Flash controller | on-chip | Telink B91 Flash Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L57) | [`telink,b91-flash-controller`](../../../../build/dts/api/bindings/flash_controller/telink%2Cb91-flash-controller.md#std-dtcompatible-telink-b91-flash-controller) |
| GPIO & Headers | on-chip | Telink B91 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L88)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L78) | [`telink,b91-gpio`](../../../../build/dts/api/bindings/gpio/telink%2Cb91-gpio.md#std-dtcompatible-telink-b91-gpio) |
| I2C | on-chip | Telink B91 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L202) | [`telink,b91-i2c`](../../../../build/dts/api/bindings/i2c/telink%2Cb91-i2c.md#std-dtcompatible-telink-b91-i2c) |
| IEEE 802.15.4 | on-chip | Telink B91 IEEE802154 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L156) | [`telink,b91-zb`](../../../../build/dts/api/bindings/ieee802154/telink%2Cb91-zb.md#std-dtcompatible-telink-b91-zb) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/telink/tlsr9518adk80d/tlsr9518adk80d.dts?plain=1#L61) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | RISC-V CPU interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L27) | [`riscv,cpu-intc`](../../../../build/dts/api/bindings/interrupt-controller/riscv%2Ccpu-intc.md#std-dtcompatible-riscv-cpu-intc) |
| on-chip | SiFive RISCV-V platform-local interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L128) | [`sifive,plic-1.0.0`](../../../../build/dts/api/bindings/interrupt-controller/sifive%2Cplic-1.0.0.md#std-dtcompatible-sifive-plic-1.0.0) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/telink/tlsr9518adk80d/tlsr9518adk80d.dts?plain=1#L28) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/telink/tlsr9518adk80d/tlsr9518adk80d.dts?plain=1#L52) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L64) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/telink/tlsr9518adk80d/tlsr9518adk80d.dts?plain=1#L97) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | The Telink B91 pin controller is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L218) | [`telink,b91-pinctrl`](../../../../build/dts/api/bindings/pinctrl/telink%2Cb91-pinctrl.md#std-dtcompatible-telink-b91-pinctrl) |
| Power management | on-chip | Telink B91 power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L70) | [`telink,b91-power`](../../../../build/dts/api/bindings/power/telink%2Cb91-power.md#std-dtcompatible-telink-b91-power) |
| PWM | on-chip | Telink B91 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L170) | [`telink,b91-pwm`](../../../../build/dts/api/bindings/pwm/telink%2Cb91-pwm.md#std-dtcompatible-telink-b91-pwm) |
| RNG | on-chip | Telink B91 RNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L164) | [`telink,b91-trng`](../../../../build/dts/api/bindings/rng/telink%2Cb91-trng.md#std-dtcompatible-telink-b91-trng) |
| Serial controller | on-chip | Telink B91 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L140)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L148) | [`telink,b91-uart`](../../../../build/dts/api/bindings/serial/telink%2Cb91-uart.md#std-dtcompatible-telink-b91-uart) |
| SPI | on-chip | Telink B91 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L178) | [`telink,b91-spi`](../../../../build/dts/api/bindings/spi/telink%2Cb91-spi.md#std-dtcompatible-telink-b91-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L42) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | RISC-V Machine Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/telink/telink_b91.dtsi?plain=1#L50) | [`riscv,machine-timer`](../../../../build/dts/api/bindings/timer/riscv%2Cmachine-timer.md#std-dtcompatible-riscv-machine-timer) |

Note

To support “button” example project PC3-KEY3 (J20-19, J20-20) jumper needs to be removed and KEY3 (J20-19) should be connected to VDD3\_DCDC (J51-13) externally.

For the rest example projects use the default jumpers configuration.

#### Limitations

- Maximum 3 GPIO pins could be configured to generate interrupts simultaneously. All pins must be related to different ports and use different IRQ numbers.
- DMA mode is not supported by I2C, SPI and Serial Port.
- UART hardware flow control is not implemented.
- SPI Slave mode is not implemented.
- I2C Slave mode is not implemented.

### Default configuration and IOs

#### System Clock

The TLSR9518ADK80D board is configured to use the 24 MHz external crystal oscillator
with the on-chip PLL/DIV generating the 48 MHz system clock.
The following values also could be assigned to the system clock in the board DTS file
[boards/telink/tlsr9518adk80d/tlsr9518adk80d.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/telink/tlsr9518adk80d/tlsr9518adk80d.dts):

- 16000000
- 24000000
- 32000000
- 48000000
- 64000000
- 96000000

```text
&cpu0 {
    clock-frequency = <48000000>;
};
```

#### PINs Configuration

The TLSR9518A SoC has five GPIO controllers (PORT\_A to PORT\_E), but only two are
currently enabled (PORT\_B for LEDs control and PORT\_C for buttons) in the board DTS file:

- LED0 (blue): PB4, LED1 (green): PB5, LED2 (white): PB6, LED3 (red): PB7
- Key Matrix SW0: PC2\_PC3, SW1: PC2\_PC1, SW2: PC0\_PC3, SW3: PC0\_PC1

Peripheral’s pins on the SoC are mapped to the following GPIO pins in the
[boards/telink/tlsr9518adk80d/tlsr9518adk80d.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/telink/tlsr9518adk80d/tlsr9518adk80d.dts) file:

- UART0 TX: PB2, RX: PB3
- UART1 TX: PC6, RX: PC7
- PWM Channel 0: PB4
- PSPI CS0: PC4, CLK: PC5, MISO: PC6, MOSI: PC7
- HSPI CS0: PA1, CLK: PA2, MISO: PA3, MOSI: PA4
- I2C SCL: PE1, SDA: PE3

#### Serial Port

The TLSR9518A SoC has 2 UARTs. The Zephyr console output is assigned to UART0.
The default settings are 115200 8N1.

## Programming and debugging

The `tlsr9518adk80d` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |
| **spi\_burn** | ✅ (default) | ✅ (default) |

### Building

Important

These instructions assume you’ve set up a development environment as
described in the [Getting Started Guide](../../../../develop/getting_started/index.md#getting-started).

To build applications using the default RISC-V toolchain from Zephyr SDK, just run the west build command.
Here is an example for the “hello\_world” application.

```shell
# From the root of the zephyr repository
west build -b tlsr9518adk80d samples/hello_world
```

To use [Telink RISC-V Linux Toolchain](https://wiki.telink-semi.cn/tools_and_sdk/Tools/IDE/telink_riscv_linux_toolchain.zip) [[3]](#id6), `ZEPHYR_TOOLCHAIN_VARIANT` and `CROSS_COMPILE` variables need to be set.
In addition `CONFIG_FPU=y` must be selected in [boards/telink/tlsr9518adk80d/tlsr9518adk80d\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/telink/tlsr9518adk80d/tlsr9518adk80d_defconfig) file since this
toolchain is compatible only with the float point unit usage.

```shell
# Set Zephyr toolchain variant to cross-compile
export ZEPHYR_TOOLCHAIN_VARIANT=cross-compile
# Specify the Telink RISC-V Toolchain location
export CROSS_COMPILE=~/toolchains/nds32le-elf-mculib-v5f/bin/riscv32-elf-
# From the root of the zephyr repository
west build -b tlsr9518adk80d samples/hello_world
```

[Telink RISC-V Linux Toolchain](https://wiki.telink-semi.cn/tools_and_sdk/Tools/IDE/telink_riscv_linux_toolchain.zip) [[3]](#id6) is available on the [Burning and Debugging Tools for TLSR9 Series in Linux](https://wiki.telink-semi.cn/wiki/IDE-and-Tools/BDT_for_TLSR9_Series_in_Linux/) [[6]](#id14) page.

Open a serial terminal with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Flash the board, reset and observe the following messages on the selected
serial port:

```shell
*** Booting Zephyr OS version 2.5.0  ***
Hello World! tlsr9518adk80d
```

### Flashing

To flash the TLSR9518ADK80D board see the sources below:

- [Burning and Debugging Tools for all Series](https://wiki.telink-semi.cn/wiki/IDE-and-Tools/Burning-and-Debugging-Tools-for-all-Series/) [[4]](#id10)
- [Burning and Debugging Tools for TLSR9 Series](https://wiki.telink-semi.cn/wiki/IDE-and-Tools/Burning-and-Debugging-Tools-for-TLSR9-Series/) [[5]](#id12)
- [Burning and Debugging Tools for TLSR9 Series in Linux](https://wiki.telink-semi.cn/wiki/IDE-and-Tools/BDT_for_TLSR9_Series_in_Linux/) [[6]](#id14)

It is also possible to use the west flash command, but additional steps are required to set it up:

- Download [Telink RISC-V Linux Toolchain](https://wiki.telink-semi.cn/tools_and_sdk/Tools/IDE/telink_riscv_linux_toolchain.zip) [[3]](#id6). The toolchain contains tools for the board flashing as well.
- Since the ICEman tool is created for the 32-bit OS version it is necessary to install additional packages in case of the 64-bit OS version.

```shell
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386
```

- Run the “ICEman.sh” script.

```shell
# From the root of the {path to the Telink RISC-V Linux Toolchain}/ice repository
sudo ./ICEman.sh
```

- Now you should be able to run the west flash command with the toolchain path specified (TELINK\_TOOLCHAIN\_PATH).

```shell
west flash --telink-tools-path=$TELINK_TOOLCHAIN_PATH
```

- You can also run the west flash command without toolchain path specification if add SPI\_burn and ICEman to PATH.

```shell
export PATH=$TELINK_TOOLCHAIN_PATH/flash/bin:"$PATH"
export PATH=$TELINK_TOOLCHAIN_PATH/ice:"$PATH"
```

### Debugging

This port supports UART debug and OpenOCD+GDB. The `west debug` command also supported. You may run
it in a simple way, like:

```shell
west debug
```

Or with additional arguments, like:

```shell
west debug --gdb-port=<port_number> --gdb-ex=<additional_ex_arguments>
```

Example:

```shell
west debug --gdb-port=1111 --gdb-ex="-ex monitor reset halt -ex b main -ex continue"
```

## References

[[1](#id3)]

[https://wiki.telink-semi.cn/wiki/chip-series/TLSR951x-Series/](https://wiki.telink-semi.cn/wiki/chip-series/TLSR951x-Series/)

[[2](#id5)]

[https://wiki.telink-semi.cn/wiki/Hardware/B91\_Generic\_Starter\_Kit\_Hardware\_Guide/](https://wiki.telink-semi.cn/wiki/Hardware/B91_Generic_Starter_Kit_Hardware_Guide/)

[3]
([1](#id7),[2](#id8),[3](#id9))

[https://wiki.telink-semi.cn/tools\_and\_sdk/Tools/IDE/telink\_riscv\_linux\_toolchain.zip](https://wiki.telink-semi.cn/tools_and_sdk/Tools/IDE/telink_riscv_linux_toolchain.zip)

[[4](#id11)]

[https://wiki.telink-semi.cn/wiki/IDE-and-Tools/Burning-and-Debugging-Tools-for-all-Series/](https://wiki.telink-semi.cn/wiki/IDE-and-Tools/Burning-and-Debugging-Tools-for-all-Series/)

[[5](#id13)]

[https://wiki.telink-semi.cn/wiki/IDE-and-Tools/Burning-and-Debugging-Tools-for-TLSR9-Series/](https://wiki.telink-semi.cn/wiki/IDE-and-Tools/Burning-and-Debugging-Tools-for-TLSR9-Series/)

[6]
([1](#id15),[2](#id16))

[https://wiki.telink-semi.cn/wiki/IDE-and-Tools/BDT\_for\_TLSR9\_Series\_in\_Linux/](https://wiki.telink-semi.cn/wiki/IDE-and-Tools/BDT_for_TLSR9_Series_in_Linux/)

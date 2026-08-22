---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/others/neorv32/doc/index.html
original_path: boards/others/neorv32/doc/index.html
---

# NEORV32

Board Overview

[![../../../../_images/neorv32.png](../../../../_images/neorv32.png)
](../../../../_images/neorv32.png)

NEORV32

Name:
:   `neorv32`

Vendor:
:   Other/Unknown

Architecture:
:   riscv

SoC:
:   neorv32

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/neorv32/doc/index.rst/../..)

## Overview

The NEORV32 is an open-source RISC-V compatible processor system intended as a
ready-to-go auxiliary processor within larger SoC designs or as a stand-alone
customizable microcontroller.

For more information about the NEORV32, see the following websites:

- [The NEORV32 RISC-V Processor GitHub](https://github.com/stnolting/neorv32)
- [The NEORV32 RISC-V Processor Datasheet](https://stnolting.github.io/neorv32/)
- [The NEORV32 RISC-V Processor User Guide](https://stnolting.github.io/neorv32/ug/)

The currently supported version is NEORV32 v1.11.6.

### Supported Board Targets

The following NEORV32 board targets are supported by Zephyr:

- `neorv32/neorv32/minimalboot`
- `neorv32/neorv32/up5kdemo`

Each of these match one of the NEORV32 processor templates provided alongside the NEORV32 RTL.
These board targets can be customized out-of-tree to match custom NEORV32 implementations using
[board extensions](../../../../hardware/porting/board_porting.md#extend-board) or [devicetree overlays](../../../../build/dts/howtos.md#use-dt-overlays).

The `neorv32` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `neorv32/neorv32/minimalboot` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | NEORV32 RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L22) | [`neorv32,cpu`](../../../../build/dts/api/bindings/cpu/neorv32%2Ccpu.md#std-dtcompatible-neorv32-cpu) |
| Counter | on-chip | NEORV32 General Purpose Timer (GPTMR)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L91) | [`neorv32,gptmr`](../../../../build/dts/api/bindings/counter/neorv32%2Cgptmr.md#std-dtcompatible-neorv32-gptmr) |
| GPIO & Headers | on-chip | NEORV32 GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L139) | [`neorv32,gpio`](../../../../build/dts/api/bindings/gpio/neorv32%2Cgpio.md#std-dtcompatible-neorv32-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32_neorv32_minimalboot.dts?plain=1#L63) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | RISC-V CPU interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L27) | [`riscv,cpu-intc`](../../../../build/dts/api/bindings/interrupt-controller/riscv%2Ccpu-intc.md#std-dtcompatible-riscv-cpu-intc) |
| on-chip | SiFive RISC-V Core-Local Interruptor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L99) | [`sifive,clint0`](../../../../build/dts/api/bindings/interrupt-controller/sifive%2Cclint0.md#std-dtcompatible-sifive-clint0) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32_neorv32_minimalboot.dts?plain=1#L39) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32_neorv32_minimalboot.dts?plain=1#L91) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L67) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| PWM | on-chip | NEORV32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L83) | [`neorv32,pwm`](../../../../build/dts/api/bindings/pwm/neorv32%2Cpwm.md#std-dtcompatible-neorv32-pwm) |
| RNG | on-chip | NEORV32 True Random Number Generator (TRNG)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L132) | [`neorv32,trng`](../../../../build/dts/api/bindings/rng/neorv32%2Ctrng.md#std-dtcompatible-neorv32-trng) |
| Serial controller | on-chip | NEORV32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L114)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L123) | [`neorv32,uart`](../../../../build/dts/api/bindings/serial/neorv32%2Cuart.md#std-dtcompatible-neorv32-uart) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L72) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| System controller | on-chip | System Controller Registers R/W[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L150) | [`syscon`](../../../../build/dts/api/bindings/syscon/syscon.md#std-dtcompatible-syscon) |
| Timer | on-chip | RISC-V Machine Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L106) | [`riscv,machine-timer`](../../../../build/dts/api/bindings/timer/riscv%2Cmachine-timer.md#std-dtcompatible-riscv-machine-timer) |

#### `neorv32/neorv32/up5kdemo` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | NEORV32 RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L22) | [`neorv32,cpu`](../../../../build/dts/api/bindings/cpu/neorv32%2Ccpu.md#std-dtcompatible-neorv32-cpu) |
| Counter | on-chip | NEORV32 General Purpose Timer (GPTMR)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L91) | [`neorv32,gptmr`](../../../../build/dts/api/bindings/counter/neorv32%2Cgptmr.md#std-dtcompatible-neorv32-gptmr) |
| GPIO & Headers | on-chip | NEORV32 GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L139) | [`neorv32,gpio`](../../../../build/dts/api/bindings/gpio/neorv32%2Cgpio.md#std-dtcompatible-neorv32-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32_neorv32_up5kdemo.dts?plain=1#L63) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | RISC-V CPU interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L27) | [`riscv,cpu-intc`](../../../../build/dts/api/bindings/interrupt-controller/riscv%2Ccpu-intc.md#std-dtcompatible-riscv-cpu-intc) |
| on-chip | SiFive RISC-V Core-Local Interruptor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L99) | [`sifive,clint0`](../../../../build/dts/api/bindings/interrupt-controller/sifive%2Cclint0.md#std-dtcompatible-sifive-clint0) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32_neorv32_up5kdemo.dts?plain=1#L39) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32_neorv32_up5kdemo.dts?plain=1#L91) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L67) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| PWM | on-chip | NEORV32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L83) | [`neorv32,pwm`](../../../../build/dts/api/bindings/pwm/neorv32%2Cpwm.md#std-dtcompatible-neorv32-pwm) |
| RNG | on-chip | NEORV32 True Random Number Generator (TRNG)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L132) | [`neorv32,trng`](../../../../build/dts/api/bindings/rng/neorv32%2Ctrng.md#std-dtcompatible-neorv32-trng) |
| Serial controller | on-chip | NEORV32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L114)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L123) | [`neorv32,uart`](../../../../build/dts/api/bindings/serial/neorv32%2Cuart.md#std-dtcompatible-neorv32-uart) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L72) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| System controller | on-chip | System Controller Registers R/W[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L150) | [`syscon`](../../../../build/dts/api/bindings/syscon/syscon.md#std-dtcompatible-syscon) |
| Timer | on-chip | RISC-V Machine Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L106) | [`riscv,machine-timer`](../../../../build/dts/api/bindings/timer/riscv%2Cmachine-timer.md#std-dtcompatible-riscv-machine-timer) |

## Supported Features

The following NEORV32 features are supported by Zephyr. These are pre-configured for the supported
board targets, but can be customized to match custom NEORV32 implementations.

### System Clock

The default board configuration reads the system clock frequency from the NEORV32 SYSINFO module,
which results in a small run-time overhead. If the clock frequency is known at build time, this
behavior can be overridden by setting the `clock-frequency` property of the `cpu0` devicetree
node.

### CPU

The SoC configuration assumes the NEORV32 CPU implementation has the following RISC-V ISA extensions
enabled:

- Zicntr (Extension for Base Counters and Timers)
- Zicsr (Control and Status Register (CSR) Instructions, always enabled)
- Zifencei (Instruction-fetch fence, always enabled)

Other supported RISC-V ISA extensions must be enabled via Kconfig on the board level, and the
`riscv,isa` devicetree property of the `cpu0` node must be set accordingly.

### Core Local Interruptor

The NEORV32 Core Local Interruptor (CLINT) and its machine timer (MTIMER) are supported but disabled
by default. For NEORV32 SoC implementations supporting these, support can be enabled by setting
the `status` properties of the `clint` and `mtimer` devicetree node to `okay`.

### Internal Instruction Memory

The internal instruction memory (IMEM) for code execution is supported but disabled by default. For
NEORV32 SoC implementations supporting IMEM, support can be enabled by setting the size via the
`reg` property of the `imem` devicetree node and setting its `status` property to `okay`.

### Internal Data Memory

The internal data memory (DMEM) is supported but disabled by default. For NEORV32 SoC
implementations supporting DMEM, support can be enabled by setting the size via the `reg` property
of the `dmem` devicetree node and setting its `status` property to `okay`.

### Serial Port

The NEORV32 serial ports (UART0 and UART1) are supported but disabled by default. For NEORV32 SoC
implementations supporting either of the UARTs, support can be enabled by setting the `status`
properties of the `uart0` and/or `uart1` devicetree node to `okay`.

Note

The board targets provide a console on UART0 with a baud rate of 19200 to match that of the
standard NEORV32 bootloader. The baudrate can be changed by modifying the `current-speed`
property of the `uart0` devicetree node.

### General Purpose Input/Output

The NEORV32 GPIO port is supported but disabled by default. For NEORV32 SoC implementations
supporting the GPIOs, support can be enabled by setting the `status` property of the `gpio`
devicetree node to `okay`. The number of supported GPIOs can be set via the `ngpios` devicetree
property.

### Pulse-Width Modulation

The NEORV32 PWM controller is supported but disabled by default. For NEORV32 SoC implementations
supporting PWM, support can be enabled by setting the `status` property of the `pwm` devicetree
node to `okay`.

### True Random-Number Generator

The True Random-Number Generator (TRNG) of the NEORV32 is supported, but disabled by default. For
NEORV32 SoC implementations supporting the TRNG, support can be enabled by setting the `status`
property of the `trng` devicetree node to `okay`.

### General Purpose Timer

The General Purpose Timer (GPTMR) of the NEORV32 is supported, but disabled by default. For NEORV32
SoC implementations supporting the GPTMR, support can be enabled by setting the `status` property
of the `gptmr` devicetree node to `okay` and selecting the desired GPTMR clock prescaler using
the node’s `prescaler` property.

## Programming and Debugging

The `neorv32` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

First, configure the FPGA with the NEORV32 bitstream as described in the NEORV32
user guide.

Next, build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Console

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 19200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing via JTAG

Here is an example for building and flashing the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application
for the NEORV32 via JTAG. Flashing via JTAG requires a NEORV32 SoC
implementation with the On-Chip Debugger (OCD) and bootloader enabled.

Note

If the bootloader is not enabled, the internal instruction memory (IMEM) is
configured as ROM which cannot be modified via JTAG.

```shell
# From the root of the zephyr repository
west build -b neorv32/neorv32/<variant> samples/hello_world
west flash
```

The default board configuration uses an [OpenOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#openocd-debug-host-tools)
configuration similar to the example provided by the NEORV32 project. Other
JTAGs can be used by providing further arguments when flashing. Here is an
example for using the Flyswatter JTAG @ 2 kHz:

```shell
# From the root of the zephyr repository
west build -b neorv32/neorv32/<variant> samples/hello_world
west flash --config interface/ftdi/flyswatter.cfg --config neorv32.cfg --cmd-pre-init 'adapter speed 2000'
```

After flashing, you should see message similar to the following in the terminal:

```shell
*** Booting Zephyr OS build zephyr-vn.n.nn  ***
Hello World! neorv32/neorv32/<variant>
```

Note, however, that the application was not persisted in flash memory by the
above steps. It was merely written to internal block RAM in the FPGA. It will
revert to the application stored in the block RAM within the FPGA bitstream
the next time the FPGA is configured.

The steps to persist the application within the FPGA bitstream are covered by
the NEORV32 user guide. If the [`CONFIG_BUILD_OUTPUT_BIN`](../../../../kconfig.md#CONFIG_BUILD_OUTPUT_BIN "CONFIG_BUILD_OUTPUT_BIN") is enabled and
the NEORV32 `image_gen` binary is available, the build system will
automatically generate a `zephyr.vhd` file suitable for initialising the
internal instruction memory of the NEORV32.

In order for the build system to automatically detect the `image_gen` binary
it needs to be in the [`PATH`](../../../../develop/env_vars.md#envvar-PATH) environment variable. If not, the path
can be passed at build time:

```shell
# From the root of the zephyr repository
west build -b neorv32/neorv32/<variant> samples/hello_world -- -DCMAKE_PROGRAM_PATH=<path/to/neorv32/sw/image_gen/>
```

### Uploading via UART

If the [`CONFIG_BUILD_OUTPUT_BIN`](../../../../kconfig.md#CONFIG_BUILD_OUTPUT_BIN "CONFIG_BUILD_OUTPUT_BIN") is enabled and the NEORV32
`image_gen` binary is available, the build system will automatically generate
a `zephyr_exe.bin` file suitable for uploading to the NEORV32 via the
built-in bootloader as described in the NEORV32 user guide.

### Debugging via JTAG

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b neorv32/neorv32/<variant> samples/hello_world
west debug
```

Step through the application in your debugger, and you should see a message
similar to the following in the terminal:

```shell
*** Booting Zephyr OS build zephyr-vn.n.nn  ***
Hello World! neorv32/neorv32/<variant>
```

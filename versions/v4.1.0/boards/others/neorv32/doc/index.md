---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/others/neorv32/doc/index.html
original_path: boards/others/neorv32/doc/index.html
---

# NEORV32

Board Overview

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

The currently supported version is 1.8.6.

### Supported Features

The `neorv32` board target can be used a generic definition for NEORV32
based boards. Customization to fit custom NEORV32 implementations can be done
using [devicetree overlays](../../../../build/dts/howtos.md#use-dt-overlays).

The `neorv32` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `neorv32/neorv32@1.8.6` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | NEORV32 RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L21) | [`neorv32-cpu`](../../../../build/dts/api/bindings/cpu/neorv32-cpu.md#std-dtcompatible-neorv32-cpu) |
| GPIO & Headers | on-chip | NEORV32 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L102) | [`neorv32-gpio`](../../../../build/dts/api/bindings/gpio/neorv32-gpio.md#std-dtcompatible-neorv32-gpio) |
| Interrupt controller | on-chip | RISC-V CPU interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L27) | [`riscv,cpu-intc`](../../../../build/dts/api/bindings/interrupt-controller/riscv%2Ccpu-intc.md#std-dtcompatible-riscv-cpu-intc) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32.dts?plain=1#L49) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-board | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32.dts?plain=1#L33) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| RNG | on-chip | NEORV32 True Random Number Generator (TRNG)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L82) | [`neorv32-trng`](../../../../build/dts/api/bindings/rng/neorv32-trng.md#std-dtcompatible-neorv32-trng) |
| Serial controller | on-chip | NEORV32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L73)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L125) | [`neorv32-uart`](../../../../build/dts/api/bindings/serial/neorv32-uart.md#std-dtcompatible-neorv32-uart) |
| SRAM | on-board | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32.dts?plain=1#L43) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| System controller | on-chip | System Controller Registers R/W[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L134) | [`syscon`](../../../../build/dts/api/bindings/syscon/syscon.md#std-dtcompatible-syscon) |
| Timer | on-chip | RISC-V Machine Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L67) | [`riscv,machine-timer`](../../../../build/dts/api/bindings/timer/riscv%2Cmachine-timer.md#std-dtcompatible-riscv-machine-timer) |

### System Clock

The default board configuration assumes a system clock of 100 MHz. The clock
frequency can be overridden by changing the `clock-frequency` property of the
`cpu0` devicetree node.

### CPU

The default board configuration assumes the NEORV32 CPU implementation has the
following RISC-V ISA extensions enabled:

- C (Compresses Instructions)
- M (Integer Multiplication and Division)
- Zicsr (Control and Status Register (CSR) Instructions)

### Internal Instruction Memory

The default board configuration assumes the NEORV32 SoC implementation has a 64k
byte internal instruction memory (IMEM) for code execution. The size of the
instruction memory can be overridden by changing the `reg` property of the
`imem` devicetree node.

### Internal Data Memory

The default board configuration assumes the NEORV32 SoC implementation has a 32k
byte internal data memory (DMEM). The size of the data memory can be overridden
by changing the `reg` property of the `dmem` devicetree node.

### Serial Port

The default configuration assumes the NEORV32 SoC implements UART0 for use as
system console.

Note

The default configuration uses a baud rate of 19200 to match that of the
standard NEORV32 bootloader. The baudrate can be changed by modifying the
`current-speed` property of the `uart0` devicetree node.

### True Random-Number Generator

The True Random-Number Generator (TRNG) of the NEORV32 is supported, but
disabled by default. For NEORV32 SoC implementations supporting the TRNG,
support can be enabled by setting the `status` property of the `trng`
devicetree node to `okay`.

## Programming and Debugging

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
west build -b neorv32 samples/hello_world
west flash
```

The default board configuration uses an [OpenOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#openocd-debug-host-tools)
configuration similar to the example provided by the NEORV32 project. Other
JTAGs can be used by providing further arguments when building. Here is an
example for using the Flyswatter JTAG:

```shell
# From the root of the zephyr repository
west build -b neorv32 samples/hello_world -- -DBOARD_RUNNER_ARGS_openocd="--config;interface/ftdi/flyswatter.cfg;--config;neorv32.cfg;--cmd-pre-init;'adapter speed 2000'"
west flash
```

After flashing, you should see message similar to the following in the terminal:

```shell
*** Booting Zephyr OS build zephyr-vn.n.nn  ***
Hello World! neorv32
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
west build -b neorv32 samples/hello_world -- -DCMAKE_PROGRAM_PATH=<path/to/neorv32/sw/image_gen/>
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
west build -b neorv32 samples/hello_world
west debug
```

Step through the application in your debugger, and you should see a message
similar to the following in the terminal:

```shell
*** Booting Zephyr OS build zephyr-vn.n.nn  ***
Hello World! neorv32
```

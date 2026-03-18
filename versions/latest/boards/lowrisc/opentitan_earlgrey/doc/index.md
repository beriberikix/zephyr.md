---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/lowrisc/opentitan_earlgrey/doc/index.html
original_path: boards/lowrisc/opentitan_earlgrey/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# OpenTitan Earl Grey

## Overview

The OpenTitan Earl Grey chip is a low-power secure microcontroller that is
designed for several use cases requiring hardware security. The [OpenTitan
Github](https://github.com/lowRISC/opentitan) [[2]](#id3) page contains HDL code, utilities, and documentation relevant to the
chip.

## Hardware

- RV32IMCB RISC-V “Ibex” core
- 128kB main SRAM
- Fixed-frequency and AON timers
- 32 x GPIO
- 4 x UART
- 3 x I2C
- 2 x SPI host
- 1 x SPI device
- Various security peripherals

Detailed specification is on the [OpenTitan Earl Grey Chip Datasheet](https://opentitan.org/book/hw/top_earlgrey/doc/specification.html) [[1]](#id1).

### Supported Features

The `opentitan_earlgrey` board configuration is designed and tested to run on
the Earl Grey chip simulated in Verilator, a cycle-accurate HDL simulation tool.

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| Timer | on-chip | RISC-V Machine Timer |
| UART | on-chip | serial port-polling |
| SPI | on-chip | SPI host |
| WDT | on-chip | Always-On Timer (Watchdog) |

Other hardware features are not yet supported on Zephyr porting.

## Programming and Debugging

First, build and install Verilator as described in the [OpenTitan Verilator
Setup](https://opentitan.org/guides/getting_started/setup_verilator.html) [[3]](#id5) guide .

### Building and Flashing

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello-world) application. The
following steps were tested on OpenTitan master branch @ 6a3c2e98.

```shell
# From the root of the zephyr repository
west build -b opentitan_earlgrey samples/hello_world
```

The OpenTitan Vchip\_sim\_tb tool can take the Zephyr .elf as input and place it
in simulated flash. The OpenTitan test ROM will then run in simulation, read
the manifest header from simulated flash, and begin executing Zephyr from the
entry point.

```shell
$OT_HOME/bazel-bin/hw/build.verilator_real/sim-verilator/Vchip_sim_tb --verbose-mem-load \
-r $OT_HOME/bazel-out/k8-fastbuild-ST-2cc462681f62/bin/sw/device/lib/testing/test_rom/test_rom_sim_verilator.39.scr.vmem \
--meminit=otp,$OT_HOME/bazel-out/k8-fastbuild/bin/hw/ip/otp_ctrl/data/img_rma.24.vmem \
--meminit=flash,$ZEPHYR_PATH/build/zephyr/zephyr.elf
```

UART output:

```shell
I00000 test_rom.c:135] Version: earlgrey_silver_release_v5-9599-g6a3c2e988, Build Date: 2023-01-17 16:02:09
I00001 test_rom.c:237] Test ROM complete, jumping to flash (addr: 20000384)!
*** Booting Zephyr OS build zephyr-v3.2.0-3494-gf0729b494b98 ***
Hello World! opentitan_earlgrey
```

## References

[[1](#id2)]

[https://opentitan.org/book/hw/top\_earlgrey/doc/specification.html](https://opentitan.org/book/hw/top_earlgrey/doc/specification.html)

[[2](#id4)]

[https://github.com/lowRISC/opentitan](https://github.com/lowRISC/opentitan)

[[3](#id6)]

[https://opentitan.org/guides/getting\_started/setup\_verilator.html](https://opentitan.org/guides/getting_started/setup_verilator.html)

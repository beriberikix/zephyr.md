---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nxp/mimxrt700_evk/doc/index.html
original_path: boards/nxp/mimxrt700_evk/doc/index.html
---

# MIMXRT700-EVK

Board Overview

Name:
:   `mimxrt700_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimxrt798s

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt700_evk/doc/index.rst/../..)

## Overview

The new i.MX RT700 CPU architecture is composed of a high-performance main compute subsystem,
a secondary “always-on” sense-compute subsystem and specialized coprocessors.

The main compute subsystem uses a 325 MHz capable Arm® Cortex®-M33 (CM33).
Similar to the i.MX RT600 crossover MCU, the i.MX RT700 includes a Cadence Tensilica® HiFi 4 DSP.
The HiFi 4 is a high performance DSP core based upon a Very Long Instruction Word (VLIW) architecture,
which is capable of processing up to eight 32x16 MACs per instruction cycle. It can be used for offloading
high-performance numerical tasks such as audio and image processing and supports both fixed-point and
floating-point operations.

## Hardware

- Main Compute Subsystem:

  > - Arm Cortex-M33 up to 325 MHz
  > - HiFi 4 DSP up to 325 MHz
  > - eIQ Neutron NPU up to 325 MHz
- Sense Compute Subsystem:

  > - Arm Cortex-M33 up to 250 MHz
  > - HiFi 1 DSP up to 250 MHz
- 7.5 MB on-chip SRAM
- Three xSPI interfaces for off-chip memory expansion, supporting up to 16b wide external memories up to 250 MHz DDR
- eUSB support with integrated PHY
- Two SD/eMMC memory card interfaces—one supporting eMMC 5.0 with HS400/DDR operation
- USB high-speed host/device controller with on-chip PHY
- A digital microphone interface supporting up to 8 channels
- Serial peripherals (UART/I²C/I3C/SPI/HSPI/SAI)
- 2.5D GPU with vector graphics acceleration and frame buffer compression
- EZH-V using RISC-V core with additional SIMD/DSP instructions
- Full openVG 1.1 support
- Up to [720p@60FPS](mailto:720p%4060FPS) from on-chip SRAM
- LCD Interface + MIPI DSI
- Integrated JPEG and PNG support
- CSI 8/10/16-bit parallel (via FlexIO)

For more information about the MIMXRT798 SoC and MIMXRT700-EVK board, see
these references:

- [i.MX RT700 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt700-crossover-mcu-with-arm-cortex-m33-npu-dsp-and-gpu-cores:i.MX-RT700)

### Supported Features

NXP considers the MIMXRT700-EVK as a superset board for the i.MX RT7xx
family of MCUs. This board is a focus for NXP’s Full Platform Support for
Zephyr, to better enable the entire RT7xx family. NXP prioritizes enabling
this board with new support for Zephyr features. The `mimxrt700_evk/mimxrt798s
/cm33_cpu0` and `mimxrt700_evk/mimxrt798s/cm33_cpu1` board targets support
the hardware features below.

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| CTIMER | on-chip | counter |
| NVIC | on-chip | nested vector interrupt controller |
| SPI | on-chip | spi |
| SYSTICK | on-chip | systick |
| IOCON | on-chip | pinmux |
| I2C | on-chip | i2c |
| GPIO | on-chip | gpio |
| UART | on-chip | serial port-polling; serial port-interrupt |
| CLOCK | on-chip | clock\_control |
| MRT | on-chip | counter |
| ADC | on-chip | adc |
| OS\_TIMER | on-chip | os timer |

The default configuration can be found in the defconfig file:

> [boards/nxp/mimxrt700\_evk/mimxrt700\_evk\_mimxrt798s\_cm33\_cpu0\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0_defconfig)
> [boards/nxp/mimxrt700\_evk/mimxrt700\_evk\_mimxrt798s\_cm33\_cpu1\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu1_defconfig)

Other hardware features are not currently supported by the port.

### Connections and IOs

The MIMXRT798 SoC has IOCON registers, which can be used to configure the
functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_6 | I2C | I2C SDA |
| PIO0\_7 | I2C | I2C SCL |
| PIO0\_31 | UART0 | UART RX |
| PIO1\_0 | UART0 | UART TX |
| PIO0\_18 | GPIO | GREEN LED |
| PIO0\_9 | GPIO | SW5 |
| PIO8\_14 | UART19 | UART TX |
| PIO8\_15 | UART19 | UART RX |
| PIO3\_0 | SPI | SPI MOSI |
| PIO3\_1 | SPI | SPI SCK |
| PIO3\_2 | SPI | SPI MISO |
| PIO3\_3 | SPI | SPI SSEL |

### System Clock

The MIMXRT700 EVK is configured to use the Systick
as a source for the system clock.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the MCU-Link CMSIS-DAP Onboard Debug Probe.

LinkServerJLink External

1. Install the [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your search path.
2. To put the board in `DFU mode` to program the firmware, short jumper J20.
3. To update the debug firmware, please follow the instructions on MIMXRT700-EVK Debug Firmware

1. Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search path.
2. To disconnect the SWD signals from onboard debug circuit, **short** jumpers JP18.
3. Connect the J-Link probe to J18 20-pin header.

See [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) for more information.

### Configuring a Console

Connect a USB cable from your PC to J54, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu0 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS v3.7.0 ***
Hello World! mimxrt700_evk/mimxrt798s/cm33_cpu0
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu0 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS v3.7.0 ***
Hello World! mimxrt700_evk/mimxrt798s/cm33_cpu0
```

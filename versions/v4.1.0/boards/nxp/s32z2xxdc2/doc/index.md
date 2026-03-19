---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nxp/s32z2xxdc2/doc/index.html
original_path: boards/nxp/s32z2xxdc2/doc/index.html
---

# X-S32Z27X-DC (DC2)

Board Overview

Name:
:   `s32z2xxdc2`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   s32z270

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/s32z2xxdc2/doc/index.rst/../..)

## Overview

The X-S32Z27X-DC (DC2) board is based on the NXP S32Z2 Real-Time Processor,
which includes two Real-Time Units (RTU) composed of four ARM Cortex-R52 cores
each, with flexible split/lock configurations.

There is one Zephyr board per SoC/RTU:

- `s32z2xxdc2/s32z270/rtu0`, for S32Z270/RTU0
- `s32z2xxdc2/s32z270/rtu1`, for S32Z270/RTU1.

## Hardware

Information about the hardware and design resources can be found at
[NXP S32Z2 Real-Time Processors website](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32z-and-s32e-real-time-processors/s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2) [[1]](#id1).

### Supported Features

The boards support the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| Arm GIC | on-chip | interrupt\_controller |
| Arm Timer | on-chip | timer |
| LINFlexD | on-chip | serial |
| MRU | on-chip | mbox |
| NETC | on-chip | ethernet  mdio |
| SIUL2 | on-chip | pinctrl  gpio  external interrupt controller |
| SPI | on-chip | spi |
| SWT | on-chip | watchdog |
| CANEXCEL | on-chip | can |
| FLEXCAN | on-chip | can |
| SAR\_ADC | on-chip | adc |
| LPI2C | on-chip | i2c |
| EDMA | on-chip | dma |
| DSPI | on-chip | spi |
| eMIOS | on-chip | pwm |
| QSPI | on-chip | flash |
| STM | on-chip | counter |
| PIT | on-chip | counter |

Other hardware features are not currently supported by the port.

### Connections and IOs

The SoC’s pads are grouped into ports and pins for consistency with GPIO driver
and the HAL drivers used by this Zephyr port. The following table summarizes
the mapping between pads and ports/pins. This must be taken into account when
using GPIO driver or configuring the pinmuxing for the device drivers.

| Pads | Port/Pins |
| --- | --- |
| PAD\_000 - PAD\_015 | PA0 - PA15 |
| PAD\_016 - PAD\_030 | PB0 - PB14 |
| PAD\_031 | PC15 |
| PAD\_032 - PAD\_047 | PD0 - PD15 |
| PAD\_048 - PAD\_063 | PE0 - PE15 |
| PAD\_064 - PAD\_079 | PF0 - PF15 |
| PAD\_080 - PAD\_091 | PG0 - PG11 |
| PAD\_092 - PAD\_095 | PH12 - PH15 |
| PAD\_096 - PAD\_111 | PI0 - PI15 |
| PAD\_112 - PAD\_127 | PJ0 - PJ15 |
| PAD\_128 - PAD\_143 | PK0 - PK15 |
| PAD\_144 - PAD\_145 | PL0 - PL1 |
| PAD\_146 - PAD\_159 | PM2 - PM15 |
| PAD\_160 - PAD\_169 | PN0 - PN9 |
| PAD\_170 - PAD\_173 | PO10 - PO13 |

This board does not include user LED’s or switches, which are needed for some
of the samples such as [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") or [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.").
Follow the steps described in the sample description to enable support for this
board.

### System Clock

The Cortex-R52 cores are configured to run at 1 GHz.

### Serial Port

The SoC has 12 LINFlexD instances that can be used in UART mode. The console can
be accessed by default on the USB micro-B connector J119.

### Watchdog

The watchdog driver only supports triggering an interrupt upon timer expiration.
Zephyr is currently running from SRAM on this board, thus system reset is not
supported.

### Ethernet

NETC driver supports to manage the Physical Station Interface (PSI0) and/or a
single Virtual SI (VSI). The rest of the VSI’s shall be assigned to different
cores of the system. Refer to [S32 Network Controller (NETC)](../../../../samples/boards/nxp/s32/netc/README.md#nxp_s32_netc "Configure NXP S32 Network Controller (NETC)") to learn how to
configure the Ethernet network controller.

### Controller Area Network

#### CANEXCEL

CANEXCEL supports CAN Classic (CAN 2.0) and CAN FD modes. Remote transmission
request is not supported.

Note that this board does not currently come with CAN transceivers installed for
the CANEXCEL ports. To facilitate external traffic, you will need to add a CAN
transceiver. Any transceiver pin-compatible with CAN 2.0 and CAN FD protocols
can be used.

#### FlexCAN

FlexCAN supports CAN Classic (CAN 2.0) and CAN FD modes.

### ADC

ADC is provided through ADC SAR controller with 2 instances. Each ADC SAR instance has
12-bit resolution. ADC channels are divided into 2 groups (precision and internal/standard).

Note

All channels of an instance only run on 1 group channel at the same time.

### EDMA

The EDMA modules feature four EDMA3 instances: Instance 0 with 32 channels,
and instances 1, 4, and 5, each with 16 channels.

### External Flash

The on-board S26HS512T 512M-bit HyperFlash memory is connected to the QSPI controller
port A1. This board configuration selects it as the default flash controller.

## Programming and Debugging

Applications for the `s32z2xxdc2` boards can be built in the usual way as
documented in [Building an Application](../../../../develop/application/index.md#build-an-application).

Currently is only possible to load and execute a Zephyr application binary on
this board from the core internal SRAM.

This board supports West runners for the following debug tools:

- [NXP S32 Debug Probe](../../../../develop/flash_debug/probes.md#nxp-s32-debug-probe) (default)
- [Lauterbach TRACE32](../../../../develop/flash_debug/host-tools.md#lauterbach-trace32-debug-host-tools)

Follow the installation steps of the debug tool you plan to use before loading
your firmware.

### Set-up the Board

Connect the external debugger probe to the board’s JTAG connector (`J134`)
and to the host computer via USB or Ethernet, as supported by the probe.

For visualizing the serial output, connect the board’s USB/UART port (`J119`) to
the host computer and run your favorite terminal program to listen for output.
For example, using the cross-platform [pySerial miniterm](https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm) [[2]](#id3) terminal:

```shell
python -m serial.tools.miniterm <port> 115200
```

Replace `<port>` with the port where the board can be found. For example,
under Linux, `/dev/ttyUSB0`.

### Debugging

You can build and debug the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample for the board
`s32z2xxdc2/s32z270/rtu0` with:

```shell
# From the root of the zephyr repository
west build -b s32z2xxdc2/s32z270/rtu0 samples/hello_world
west debug
```

In case you are using a newer PCB revision, you have to use an adapted board
definition as the default PCB revision is B. For example, if using revision D:

```shell
west build -b s32z2xxdc2@D/s32z270/rtu0 samples/hello_world
west debug
```

At this point you can do your normal debug session. Set breakpoints and then
`c` to continue into the program. You should see the following message in
the terminal:

```shell
Hello World! s32z2xxdc2
```

To debug with Lauterbach TRACE32 software run instead:

```shell
west debug -r trace32
```

### Flashing

Follow these steps if you just want to download the application to the board
SRAM and run.

`flash` command is supported only by the Lauterbach TRACE32 runner:

```shell
west build -b s32z2xxdc2/s32z270/rtu0 samples/hello_world
west flash -r trace32
```

Note

Currently, the Lauterbach start-up scripts executed with `flash` and
`debug` commands perform the same steps to initialize the SoC and
load the application to SRAM. The difference is that `flash` hides the
Lauterbach TRACE32 interface, executes the application and exits.

To imitate a similar behavior using NXP S32 Debug Probe runner, you can run the
`debug` command with GDB in batch mode:

```shell
west debug --tool-opt='--batch'
```

### RTU and Core Configuration

This Zephyr port can only run single core in any of the Cortex-R52 cores,
either in lock-step or split-lock mode. By default, Zephyr runs on the first
core of the RTU chosen and in lock-step mode (which is the reset
configuration).

To build for split-lock mode, the [`CONFIG_DCLS`](../../../../kconfig.md#CONFIG_DCLS "CONFIG_DCLS") must be
disabled from your application Kconfig file.

By default the board configuration will set the runner arguments according to
the build configuration. To debug for a core different than the default use:

lockstep configurationsplit-lock configuration

```shell
west debug --core-name='R52_<rtu_id>_<core_id>_LS'
```

```shell
west debug --core-name='R52_<rtu_id>_<core_id>'
```

Where:

- `<rtu_id>` is the zero-based RTU index
- `<core_id>` is the zero-based core index relative to the RTU on which to
  run the Zephyr application (0, 1, 2 or 3)

For example, to build the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample for the board
`s32z2xxdc2/s32z270/rtu0` with split-lock core configuration:

```shell
west build -b s32z2xxdc2/s32z270/rtu0 samples/hello_world -- -DCONFIG_DCLS=n
```

To execute this sample in the second core of RTU0 in split-lock mode:

```shell
west debug --core-name='R52_0_1'
```

If using Lauterbach TRACE32, all runner parameters must be overridden from command
line:

```shell
west debug -r trace32 --startup-args elfFile=<elf_path> rtu=<rtu_id> core=<core_id> lockstep=<yes/no>
```

Where `<elf_path>` is the path to the Zephyr application ELF in the output
directory.

## References

[[1](#id2)]

[https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32z-and-s32e-real-time-processors/s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32z-and-s32e-real-time-processors/s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2)

[[2](#id4)]

[https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm](https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm)

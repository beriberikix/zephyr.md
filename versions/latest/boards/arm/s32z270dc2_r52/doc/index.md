---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/s32z270dc2_r52/doc/index.html
original_path: boards/arm/s32z270dc2_r52/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# NXP X-S32Z27X-DC (DC2)

## Overview

The X-S32Z27X-DC (DC2) board is based on the NXP S32Z270 Real-Time Processor,
which includes two Real-Time Units (RTU) composed of four ARM Cortex-R52 cores
each, with flexible split/lock configurations.

There is one Zephyr board per RTU:

- `s32z270dc2_rtu0_r52`, for RTU0
- `s32z270dc2_rtu1_r52`, for RTU1.

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

The Cortex-R52 cores are configured to run at 800 MHz.

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
cores of the system. Refer to [NXP S32 NETC Sample Application](../../../../samples/boards/nxp_s32/netc/README.md#nxp-s32-netc-samples) to learn how to
configure the Ethernet network controller.

### Controller Area Network (CAN)

Currently, the CANXL transceiver is not populated in this board. So CAN transceiver
connection is required for running external traffic. We can use any CAN transceiver,
which supports CAN 2.0 and CAN FD protocol.

CAN driver supports classic (CAN 2.0) and CAN FD mode. Remote transmission request is
not supported as this feature is not available on NXP S32 CANXL HAL.

## Programming and Debugging

Applications for the `s32z270dc2_rtu0_r52` and `s32z270dc2_rtu1_r52` boards
can be built in the usual way as documented in [Building an Application](../../../../develop/application/index.md#build-an-application).

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

You can build and debug the [Hello World](../../../../samples/hello_world/README.md#hello-world) sample for the board
`s32z270dc2_rtu0_r52` with:

```shell
# From the root of the zephyr repository
west build -b s32z270dc2_rtu0_r52 samples/hello_world
west debug
```

In case you are using a newer PCB revision, you have to use an adapted board
definition as the default PCB revision is B. For example, if using revision D:

```shell
west build -b s32z270dc2_rtu0_r52@D samples/hello_world
west debug
```

At this point you can do your normal debug session. Set breakpoints and then
`c` to continue into the program. You should see the following message in
the terminal:

```shell
Hello World! s32z270dc2_rtu0_r52
```

To debug with Lauterbach TRACE32 softare run instead:

```shell
west build -b s32z270dc2_rtu0_r52 samples/hello_world
west debug
west build -t -r
west build -t trace32
```

### Flashing

Follow these steps if you just want to download the application to the board
SRAM and run.

`flash` command is supported only by the Lauterbach TRACE32 runner:

```shell
west build -b s32z270dc2_rtu0_r52 samples/hello_world
west flash
west build -t -r
west build -t trace32
```

Note

Currently, the Lauterbach start-up scripts executed with `flash` and
`debug` commands perform the same steps to initialize the SoC and
load the application to SRAM. The difference is that `flash` hides the
Lauterbach TRACE32 interface, executes the application and exits.

To imitate a similar behavior using NXP S32 Debug Probe runner, you can run the
`debug` command with GDB in batch mode:

```shell
west build -b s32z270dc2_rtu0_r52 samples/hello_world
west debug
west build -t --tool-opt='--batch'
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

- `<rtu_id>` is the zero-based RTU index (0 for `s32z270dc2_rtu0_r52`
  and 1 for `s32z270dc2_rtu1_r52`)
- `<core_id>` is the zero-based core index relative to the RTU on which to
  run the Zephyr application (0, 1, 2 or 3)

For example, to build the [Hello World](../../../../samples/hello_world/README.md#hello-world) sample for the board
`s32z270dc2_rtu0_r52` with split-lock core configuration:

```shell
west build -b s32z270dc2_rtu0_r52 samples/hello_world -- -DCONFIG_DCLS=n
```

To execute this sample in the second core of RTU0 in split-lock mode:

```shell
west debug --core-name='R52_0_1'
```

If using Lauterbach TRACE32, all runner parameters must be overridden from command
line:

```shell
west debug --startup-args elfFile=<elf_path> rtu=<rtu_id> core=<core_id> lockstep=<yes/no>
```

Where `<elf_path>` is the path to the Zephyr application ELF in the output
directory.

## References

[[1](#id2)]

[https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32z-and-s32e-real-time-processors/s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32z-and-s32e-real-time-processors/s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2)

[[2](#id4)]

[https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm](https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm)

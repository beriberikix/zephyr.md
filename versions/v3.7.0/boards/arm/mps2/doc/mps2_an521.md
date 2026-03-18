---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/arm/mps2/doc/mps2_an521.html
original_path: boards/arm/mps2/doc/mps2_an521.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ARM MPS2+ AN521

## Overview

The mps2/an521 board configuration is used by Zephyr applications that run
on the MPS2+ AN521 board. It provides support for the MPS2+ AN521 ARM Cortex-M33
CPU and the following devices:

- Nested Vectored Interrupt Controller (NVIC)
- System Tick System Clock (SYSTICK)
- Cortex-M System Design Kit GPIO
- Cortex-M System Design Kit UART

![ARM MPS2+ AN521](../../../../_images/mps2_an521.jpg)

In addition to enabling actual hardware usage, this board configuration can
also use QEMU to emulate the AN521 platform running on the MPS2+.

More information about the board can be found at the [MPS2 FPGA Website](https://developer.arm.com/tools-and-software/development-boards/fpga-prototyping-boards/mps2).

Note

This board configuration makes no claims about its suitability for use
with actual MPS2 hardware systems using AN521, or any other hardware
system. It has been tested on actual hardware, but its primary purpose is
for use with QEMU and unit tests for the ARM Cortex-M33.

### Zephyr board options

The MPS2+ AN521 is a dual core SoC with Cortex-M33 architecture on both cores
(CPU0 and CPU1). Zephyr provides support for building firmware
images for both CPU0 and CPU1. For CPU0 supporting ARM Security Extensions
both Secure and Non-Secure firmware images may be built.

The BOARD options are summarized below:

| BOARD | Description |
| --- | --- |
| mps2/an521/cpu0 | For building Secure (or Secure-only) firmware on CPU0 |
| mps2/an521/cpu0/ns | For building Non-Secure firmware for CPU0 |
| mps2/an521/cpu1 | For building firmware on CPU1 |

### Memory Partitioning

The AN521 has 4MB allocated for code space, and 4MB for SRAM. These memory
regions are shared across both cores, and are aliased in both secure and
non-secure regions, where the secure memory alias has an offset of
0x10000000 relative to non-secure.

The following memory map and partitioning schemes are used by default, where
the offset value is the offset from the base of the 4MB code or SRAM block,
ignoring the S/NS alias difference.

| Board | CPU | Code (Offset) | SRAM (Offset) | S/NS Alias |
| --- | --- | --- | --- | --- |
| mps2/an521/cpu0 | 0 | 4MB (0) | 4MB (0) | S |
| mps2/an521/cpu0/ns | 0 | 512KB (1MB) | 512KB (1MB) | NS |
| mps2/an521/cpu1 | 1 | 468KB (3628KB) | 512KB (1.5MB) | NS |

The `mps2/an521/cpu0/ns` board target is intended to be used with TF-M, with the
Zephyr memory map matching the AN521 memory map defined upstream in TF-M. TF-M
boots the secure processing environment before initialising Zephyr in the
non-secure processing environment. The non-secure Zephyr image is offset to
make room for the secure bootloader, and the secure firmware (TF-M), resulting
in a starting address of 0x00100000. SRAM begins with a 1MB offset at
0x28100000.

The `mps2/an521/cpu1` board target is setup for the second core on the
AN521, using the final 468KB code memory in the 4MB code block. This value
is chosen to maintain compatibility with TF-M, which marks that final 468KB
code region as `Unused`. Code memory thus starts with an offset of
3628KB (address 0x0038B000), and sram starts with an offset of 1.5MB
(address 0x28180000).

This memory map enables the two alternative board targets to be used together
if required, at the cost of reducing the amount of code memory available on
the second core to the worst-case scenario from TF-M.

When using one of the alternative board targets (`mps2/an521/cpu0/ns` or
`mps2/an521/cpu1`), care needs to be taken with the amount of code or
SRAM memory used on the primary board target (`mps2/an521`) since there is
some overlap in the memory maps.

## Hardware

ARM MPS2+ AN521 provides the following hardware components:

- Dual core ARM Cortex-M33
- Soft Macro Model (SMM) implementation of SSE-200 subsystem
- Memory

  - 4MB of code memory (SSRAM1)
  - 4MB of SRAM (SSRAM2 and SSRAM3)
  - 16MB of parallel SRAM (PSRAM, non-secure only)
  - 8KB of NVM code
- Debug

  - P-JTAG, SWD & 16-bit TRACE
  - UART port
- Interface

  - AHB GPIO connected to the EXP port
  - UART
  - SPI
  - I2C
  - I2S
  - Color LCD serial interface
  - Ethernet
  - VGA
- On-board Peripherals

  - Color LCD
  - 8 LEDs
  - 8 Switches
  - External SSRAM1, SSRAM2 & SSRAM3
  - SMSC9220
  - CS42L52

### User push buttons

The mps2/an521 board provides the following user push buttons:

- ON power on
- nSRST: Cortex-M33 system reset and CoreSight debug reset
- USERPB0 and USERPB1: User defined buttons

### Supported Features

The mps2/an521 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| WATCHDOG | on-chip | watchdog |
| TIMER | on-chip | timer |

Other hardware features are not currently supported by the port.
See the [MPS2 FPGA Website](https://developer.arm.com/tools-and-software/development-boards/fpga-prototyping-boards/mps2) for a complete list of MPS2+ AN521 board hardware
features.

The default configuration can be found in
[boards/arm/mps2/mps2\_an521\_cpu0\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521_cpu0_defconfig).

### Interrupt Controller

MPS2+ AN521 is a Cortex-M33 based SoC and has 15 fixed exceptions and 77 IRQs.

A Cortex-M33-based board uses vectored exceptions. This means each exception
calls a handler directly from the vector table.

Zephyr provides handlers for exceptions 1-7, 11, 12, 14, and 15, as listed
in the following table:

| Exc# | Name | Remarks | Used by Zephyr Kernel |
| --- | --- | --- | --- |
| 1 | Reset |  | system initialization |
| 2 | NMI |  | system fatal error |
| 3 | Hard fault |  | system fatal error |
| 4 | MemManage | MPU fault | system fatal error |
| 5 | Bus |  | system fatal error |
| 6 | Usage fault | Undefined instruction, or switch attempt to ARM mode | system fatal error |
| 7 | SecureFault | Unauthorized access to secure region from ns space | system fatal error |
| 8 | Reserved |  | not handled |
| 9 | Reserved |  | not handled |
| 10 | Reserved |  | not handled |
| 11 | SVC |  | system calls, kernel run-time exceptions, and IRQ offloading |
| 12 | Debug monitor |  | system fatal error |
| 13 | Reserved |  | not handled |
| 14 | PendSV |  | context switch |
| 15 | SYSTICK |  | system clock |
| 16 | Reserved |  | not handled |
| 17 | Reserved |  | not handled |
| 18 | Reserved |  | not handled |

### Pin Mapping

The ARM MPS2+ AN521 Board has 4 CMSDK AHB GPIO controllers. Each providing 16
bits of IO. These controllers are responsible for pin-muxing, input/output,
pull-up, etc.

All GPIO controller pins are exposed via the following sequence of pin numbers:

- Pins 0 - 15 are for GPIO0
- Pins 16 - 31 are for GPIO1
- Pins 32 - 47 are for GPIO2
- Pins 48 - 51 are for GPIO3

Mapping from the ARM MPS2+ AN521 Board pins to GPIO controllers:

- D0 : EXT\_0
- D1 : EXT\_4
- D2 : EXT\_2
- D3 : EXT\_3
- D4 : EXT\_1
- D5 : EXT\_6
- D6 : EXT\_7
- D7 : EXT\_8
- D8 : EXT\_9
- D9 : EXT\_10
- D10 : EXT\_12
- D11 : EXT\_13
- D12 : EXT\_14
- D13 : EXT\_11
- D14 : EXT\_15
- D15 : EXT\_5
- D16 : EXT\_16
- D17 : EXT\_17
- D18 : EXT\_18
- D19 : EXT\_19
- D20 : EXT\_20
- D21 : EXT\_21
- D22 : EXT\_22
- D23 : EXT\_23
- D24 : EXT\_24
- D25 : EXT\_25
- D26 : EXT\_26
- D27 : EXT\_30
- D28 : EXT\_28
- D29 : EXT\_29
- D30 : EXT\_27
- D31 : EXT\_32
- D32 : EXT\_33
- D33 : EXT\_34
- D34 : EXT\_35
- D35 : EXT\_36
- D36 : EXT\_38
- D37 : EXT\_39
- D38 : EXT\_40
- D39 : EXT\_44
- D40 : EXT\_41
- D41 : EXT\_31
- D42 : EXT\_37
- D43 : EXT\_42
- D44 : EXT\_43
- D45 : EXT\_45
- D46 : EXT\_46
- D47 : EXT\_47
- D48 : EXT\_48
- D49 : EXT\_49
- D50 : EXT\_50
- D51 : EXT\_51

Peripheral Mapping:

- UART\_3\_RX : D0
- UART\_3\_TX : D1
- SPI\_3\_CS : D10
- SPI\_3\_MOSI : D11
- SPI\_3\_MISO : D12
- SPI\_3\_SCLK : D13
- I2C\_3\_SDA : D14
- I2C\_3\_SCL : D15
- UART\_4\_RX : D26
- UART\_4\_TX : D30
- SPI\_4\_CS : D36
- SPI\_4\_MOSI : D37
- SPI\_4\_MISO : D38
- SPI\_4\_SCK : D39
- I2C\_4\_SDA : D40
- I2C\_4\_SCL : D41

For more details refer to [MPS2+ AN521 Technical Reference Manual (TRM)](https://developer.arm.com/documentation/dai0521/latest/).

### LED

MPS2+ has 8 built-in LEDs connected to Serial Configuration Controller (SCC).

Note

The SCC register CFG\_REG1 Bits [7:0] for LEDa, 0 = OFF 1 = ON.

### System Clock

MPS2+ AN521 has several clocks connected:

- MAINCLK : 20MHz
- SYSCLK : 20MHz
- S32KCLK : 32kHz
- TRACECLK : 20MHz
- SWCLKTCK : 20MHz
- TRACECLKIN : 20MHz

### Serial Port

The MPS2+ AN521 has five UARTs. The Zephyr console output by default, uses
UART0, which is J10 on the board.

UART2 is reserved. And UART 1, 3 and 4 are alt-functions on the EXP ports.

### Security components

- Implementation Defined Attribution Unit ([IDAU](https://developer.arm.com/documentation/100690/latest/Attribution-units--SAU-and-IDAU-)). The IDAU is used to define
  secure and non-secure memory maps. By default, all of the memory space is
  defined to be secure accessible only
- Secure and Non-secure peripherals via the Peripheral Protection Controller
  (PPC). Peripherals can be assigned as secure or non-secure accessible
- Secure boot
- Secure [AMBA®](https://developer.arm.com/products/architecture/system-architectures/amba) interconnect

### Serial Configuration Controller (SCC)

The MPS2+ AN521 implements a Serial Configuration Control (SCC) register.
The purpose of this register is to allow individual control of clocks,
reset-signals and interrupts to peripherals, and pin-muxing, and the LEDs and
switches.

## Programming and Debugging

MPS2+ AN521 (CPU0) supports the Armv8m Security Extension.
Applications built for the mps2/an521 board by default
boot in the Secure state.

MPS2+ AN521 (CPU1) does not support the Armv8m Security Extension.

### Building Secure/Non-Secure Zephyr applications with Arm® TrustZone®

Applications on the MPS2+ AN521 (CPU0) may contain a Secure and a Non-Secure
firmware image. The Secure image can be built using either Zephyr
or [Trusted Firmware M](https://tf-m-user-guide.trustedfirmware.org/building/tfm_build_instruction.html) (TF-M). Non-Secure firmware images are always built
using Zephyr. The two alternatives are described below.

Note

By default the Secure image for the MPS2+ AN521 (CPU0) is built
using TF-M.

#### Building the Secure firmware with TF-M

The process to build the Secure firmware image using TF-M and the Non-Secure
firmware image using Zephyr requires the following steps:

1. Build the Non-Secure Zephyr application
   for MPS2+ AN521 (CPU0) using `-DBOARD=mps2/an521/cpu0/ns`.
   To invoke the building of TF-M the Zephyr build system requires the
   Kconfig option `BUILD_WITH_TFM` to be enabled, which is done by
   default when building Zephyr as a Non-Secure application.
   The Zephyr build system will perform the following steps automatically:

   > - Build the Non-Secure firmware image as a regular Zephyr application
   > - Build a TF-M (secure) firmware image
   > - Merge the output image binaries together
   > - Optionally build a bootloader image (MCUboot)

Note

Depending on the TF-M configuration, an application DTS overlay may be
required, to adjust the Non-Secure image Flash and SRAM starting address
and sizes.

#### Building the Secure firmware using Zephyr

The process to build the Secure and the Non-Secure firmware images
using Zephyr requires the following steps:

1. Build the Secure Zephyr application for MPS2+ AN521 (CPU0)
   using `-DBOARD=mps2/an521` and
   `CONFIG_TRUSTED_EXECUTION_SECURE=y` and `CONFIG_BUILD_WITH_TFM=n`
   in the application project configuration file.
2. Build the Non-Secure Zephyr application for MPS2+ AN521 (CPU0)
   using `-DBOARD=mps2/an521/cpu0/ns`.
3. Merge the two binaries together.

### Building a Secure only application on MPS2+ AN521 (CPU0)

Build the Zephyr app in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run)), using `-DBOARD=mps2/an521` for
the firmware running on the MPS2+ AN521 (CPU0).

When building a Secure/Non-Secure application for the MPS2+ AN521 (CPU0),
the Secure application will have to set the SAU/IDAU configuration to allow
Non-Secure access to all CPU resources utilized by the Non-Secure application
firmware. SAU/IDAU configuration shall take place before jumping to the
Non-Secure application.

The following system components are required to be properly configured during the
secure firmware:

- AHB5 TrustZone Memory Protection Controller (MPC)
- AHB5 TrustZone Peripheral Protection Controller (PPC)
- Implementation-Defined Attribution Unit (IDAU)

For more details refer to [Corelink SSE-200 Subsystem](https://developer.arm.com/documentation/dto0051/latest/subsystem-overview/about-the-sse-200).

### Building standalone applications on MPS2+ AN521 CPU1

Applications may be built for the second Cortex-M33
(remote) core of MPS2+ AN521. The core is referred to as CPU1.

Build the Zephyr app in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run)), using `-DBOARD=mps2/an521/cpu1` for
the firmware running on the MPS2+ AN521 (CPU1).

The Zephyr build will automatically trigger building a minimal (empty)
secure-only firmware for CPU0, which will be used to boot the remote
core (CPU1).

### Flashing

MPS2+ AN521 provides:

- A USB connection to the host computer, which exposes a Mass Storage
- A Serial Port which is J10 on MPS2+ board

Build applications as described above.
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application built as
a secure-only application for CPU0.

```shell
# From the root of the zephyr repository
west build -b mps2/an521 samples/hello_world
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board, and you should see the following message on the corresponding
serial port:

```shell
Hello World! mps2_an521
```

#### Uploading an application to MPS2+ AN521

Applications can be in elf, hex or bin format. The binaries are flashed when
the board boots up, using files stored on the on-board Micro SD card. The
Motherboard Configuration Controller (MCC) is responsible for loading the FPGA
image and binaries.

Connect the MPS2+ to your host computer using the USB port. You should see a
USB connection exposing a Mass Storage (`V2M_MPS2` by default).

The update requires 3 steps:

1. Copy application files to `<MPS2 device name>/SOFTWARE/`.
2. Open `<MPS2 device name>/MB/HBI0263C/AN521/images.txt`.
3. Update the `AN521/images.txt` file as follows:

```shell
TITLE: Versatile Express Images Configuration File

[IMAGES]
TOTALIMAGES: 1 ;Number of Images (Max: 32)

IMAGE0ADDRESS: 0x10000000 ;Please select the required executable program

IMAGE0FILE: \SOFTWARE\zephyr.bin
```

Reset the board, and you should see the following message on the corresponding
serial port:

```shell
Hello World! mps2_an521
```

Note

Refer to the tfm\_integration sample for more details about integrating with TF-M and multiple images scenario.

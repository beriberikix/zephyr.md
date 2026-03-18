---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/udoo_neo_full_m4/doc/index.html
original_path: boards/arm/udoo_neo_full_m4/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# UDOO Neo Full

## Overview

UDOO Neo Full is an open source Arduino Uno compatible single board computer.
It is equipped with an NXP® i.MX 6SoloX hybrid multicore processor
composed of one ARM® Cortex-A9 core running up to 1 GHz and one Cortex-M4
core running up to 227 MHz for high CPU performance and real-time response.
Zephyr was ported to run on the Cortex-M4 core only. In a future release, it
will also communicate with the Cortex-A9 core (running Linux) via OpenAMP.

![UDOO-Neo-Full](../../../../_images/udoo_neo_full_m4.jpg)

UDOO Neo Full (Credit: udoo.org)

## Hardware

- MCIMX6X MCU with a single Cortex-A9 (1 GHz) core and single Cortex-M4 (227 MHz) core
- Memory

  - 1 GB RAM
  - 128 KB OCRAM
  - 256 KB L2 cache (can be switched into OCRAM instead)
  - 16 KB OCRAM\_S
  - 32 KB TCML
  - 32 KB TCMU
  - 32 KB CAAM (secure RAM)
- A9 Boot Devices

  - NOR flash
  - NAND flash
  - OneNAND flash
  - SD/MMC
  - Serial (I2C/SPI) NOR flash and EEPROM
  - QuadSPI (QSPI) flash
- Display

  - Micro HDMI connector
  - LVDS display connector
  - Touch (I2C signals)
- Multimedia

  - Integrated 2d/3d graphics controller
  - 8-bit parallel interface for analog camera supporting NTSC and PAL
  - HDMI audio transmitter
  - S/PDIF
  - I2S
- Connectivity

  - USB 2.0 Type A port
  - USB OTG (micro-AB connector)
  - 10/100 Mbit/s Ethernet PHY
  - Wi-Fi 802.11 b/g/n
  - Bluetooth 4.0 Low Energy
  - 3x UART ports
  - 2x CAN Bus interfaces
  - 8x PWM signals
  - 3x I2C interface
  - 1x SPI interface
  - 6x multiplexable signals
  - 32x GPIO (A9)
  - 22x GPIO (M4)
- Other

  - MicroSD card slot (8-bit SDIO interface)
  - Power status LED (green)
  - 2x user LED (red and orange)
- Power

  - 5 V DC Micro USB
  - 6-15 V DC jack
  - RTC battery connector
- Debug

  - pads for soldering of JTAG 14-pin connector
- Sensor

  - 3-Axis Accelerometer
  - 3-Axis Magnetometer
  - 3-Axis Digital Gyroscope
  - 1x Sensor Snap-In I2C connector
- Expansion port

  - Arduino interface

For more information about the MCIMX6X SoC and UDOO Neo Full board,
see these references:

- [NXP i.MX 6SoloX Website](https://www.nxp.com/products/processors-and-microcontrollers/applications-processors/i.mx-applications-processors/i.mx-6-processors/i.mx-6solox-processors-heterogeneous-processing-with-arm-cortex-a9-and-cortex-m4-cores:i.MX6SX) [[8]](#id17)
- [NXP i.MX 6SoloX Datasheet](https://www.nxp.com/docs/en/data-sheet/IMX6SXCEC.pdf) [[9]](#id19)
- [NXP i.MX 6SoloX Reference Manual](https://www.nxp.com/docs/en/reference-manual/IMX6SXRM.pdf) [[10]](#id21)
- [UDOO Neo Website](https://www.udoo.org/udoo-neo/) [[1]](#id3)
- [UDOO Neo Getting Started](https://www.udoo.org/get-started-neo/) [[2]](#id5)
- [UDOO Neo Documentation](https://www.udoo.org/docs-neo) [[3]](#id7)
- [UDOO Neo Datasheet](https://www.udoo.org/download/files/datasheets/datasheet_udoo_neo.pdf) [[4]](#id9)
- [UDOO Neo Schematics](https://www.udoo.org/download/files/schematics/UDOO_NEO_schematics.pdf) [[5]](#id11)

### Supported Features

The UDOO Neo Full board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| UART | on-chip | serial port-polling; serial port-interrupt |
| GPIO | on-chip | general purpose input/output |
| COUNTER | on-chip | counter |

The default configuration can be found in the defconfig file:

> `boards/arm/udoo_neo_full_m4/udoo_neo_full_m4_defconfig`

Other hardware features are not currently supported by the port.

### Connections and IOs

The UDOO Neo Full board was tested with the following pinmux
controller configuration.

| Board Name | SoC Name | Usage |
| --- | --- | --- |
| J4 RX | UART5\_RX\_DATA | UART Console |
| J4 TX | UART5\_TX\_DATA | UART Console |

### System Clock

The MCIMX6X SoC is configured to use the 24 MHz external oscillator
on the board with the on-chip PLL to generate core clock.
PLL settings for M4 core are set via code running on the A9 core.

### Serial Port

The MCIMX6X SoC has six UARTs. UART5 is configured for the M4 core and the
remaining are used by the A9 core or not used.

## Programming and Debugging

The M4 core does not have a flash memory and is not provided a clock
at power-on-reset. Therefore it needs to be started by the A9 core.
The A9 core is responsible to load the M4 binary application into the RAM,
put the M4 in reset, set the M4 Program Counter and Stack Pointer, and get
the M4 out of reset. The A9 can perform these steps at the bootloader level
or after the Linux system has booted.

The M4 core can use up to 5 different RAMs (some other types of memory like
a secure RAM are not currently implemented in Zephyr).
These are the memory mappings for A9 and M4:

| Region | Cortex-A9 | Cortex-M4 | Size |
| --- | --- | --- | --- |
| TCML | 0x007F8000-0x007FFFFF | 0x1FFF8000-0x1FFFFFFF | 32 KB |
| TCMU | 0x00800000-0x00807FFF | 0x20000000-0x20007FFF | 32 KB |
| OCRAM\_S | 0x008F8000-0x008FBFFF | 0x208F8000-0x208FBFFF | 16 KB |
| OCRAM | 0x00900000-0x0091FFFF | 0x20900000-0x2091FFFF | 128 KB |
| DDR | 0x80000000-0xFFFFFFFF | 0x80000000-0xDFFFFFFF | 2048 MB (1536 for M4) |

### References

- [NXP i.MX 6SoloX Reference Manual](https://www.nxp.com/docs/en/reference-manual/IMX6SXRM.pdf) [[10]](#id21) Chapter 2 - Memory Maps

You have to choose which RAM will be used at compilation time. This configuration
is done in the file `boards/arm/udoo_neo_full_m4/udoo_neo_full_m4.dts`.

If you want to have the code placed in the subregion of a memory, which will
likely be the case when using DDR, select “zephyr,flash=&flash” and set the
DT\_FLASH\_SIZE macro to determine the region size and DT\_FLASH\_ADDR to determine
the address where the region begins.

If you want to have the data placed in the subregion of a memory, which will
likely be the case when using DDR, select “zephyr,sram = &sram”, which sets the
CONFIG\_SRAM\_SIZE macro to determine the region size and
CONFIG\_SRAM\_BASE\_ADDRESS to determine the address where the region begins.

Otherwise set “zephyr,flash” and/or “zephyr,sram” to one of the predefined
regions:

```text
"zephyr,flash"
- &tcml
- &ocram_s
- &ocram
- &ddr

"zephyr,sram"
- &tcmu
- &ocram_s
- &ocram
- &ddr
```

Below you will find the instructions how a Linux user space application running
on the A9 core can be used to load and run Zephyr application on the M4 core.

The UDOOBuntu Linux distribution contains a [udooneo-m4uploader](https://github.com/ektor5/udooneo-m4uploader) [[6]](#id13) utility,
but its purpose is to load UDOO Neo “Arduino-like” sketches, so it doesn’t
work with Zephyr applications in most cases. The reason is that there is
an exchange of information between this utility and the program running on the
M4 core using hardcoded shared memory locations. The utility writes a flag which
is read by the program running on the M4 core. The program is then supposed to
end safely and write the status to the shared memory location for the main core.
The utility then loads the new application and reads its status from the shared
memory location to determine if it has successfully launched. Since this
functionality is specific for the UDOO Neo “Arduino-like” sketches, it is not
implemented in Zephyr. However Zephyr applications can support it on their own
if planned to be used along with the UDOOBuntu Linux running on the A9 core.
The udooneo-uploader utility calls another executable named
mqx\_upload\_on\_m4SoloX which can be called directly to load Zephyr applications.
Copy the Zephyr binary image into the Linux filesystem and invoke the utility
as a root user:

```shell
mqx_upload_on_m4SoloX zephyr.bin
```

If the output looks like below, the mqx\_upload\_on\_m4SoloX could not read
the status of the stopped application. This is expected if the previously
loaded application is not a UDOO Neo “Arduino-like” sketch and ignores the
shared memory communication:

```shell
UDOONeo - mqx_upload_on_m4SoloX 1.1.0
UDOONeo - Waiting M4 Stop, m4TraceFlags: 00000000
UDOONeo - Waiting M4 Stop, m4TraceFlags: 00000000
UDOONeo - Waiting M4 Stop, m4TraceFlags: 00000000
UDOONeo - Waiting M4 Stop, m4TraceFlags: 00000000
UDOONeo - Failed to Stop M4 sketch: reboot system !
```

In such situation, the mqx\_upload\_on\_m4SoloX utility has reset the trace flags,
so it will succeed when called again. Then it can have this output below:

```shell
UDOONeo - mqx_upload_on_m4SoloX 1.1.0
UDOONeo - FILENAME = zephyr.bin; loadaddr = 0x84000000
UDOONeo - start - end (0x84000000 - 0x84080000)
UDOONeo - Waiting M4 Run, m4TraceFlags: 000001E0
UDOONeo - M4 sketch is running
```

Or the one below, if the utility cannot read the status flag that the M4 core
applications has started. It can be ignored as the application should be
running, the utility just doesn’t know it:

```shell
UDOONeo - mqx_upload_on_m4SoloX 1.1.0
UDOONeo - FILENAME = zephyr.bin; loadaddr = 0x84000000
UDOONeo - start - end (0x84000000 - 0x84080000)
UDOONeo - Waiting M4 Run, m4TraceFlags: 00000000
UDOONeo - Waiting M4 Run, m4TraceFlags: 00000000
UDOONeo - Waiting M4 Run, m4TraceFlags: 00000000
UDOONeo - Waiting M4 Run, m4TraceFlags: 00000000
UDOONeo - Failed to Start M4 sketch: reboot system !
```

The stack pointer and the program counter values are read from the binary.
The memory address where binary will be placed is calculated from the program
counter as its value aligned to 64 KB down, or it can be provided as a second
command line argument:

```shell
mqx_upload_on_m4SoloX zephyr.bin 0x84000000
```

It is necessary to provide the address if the binary is copied into a memory
region which has different mapping between the A9 and the M4 core. The address
calculated from the stack pointer value in the binary file would be wrong.

It is possible to modify the mqx\_upload\_on\_m4SoloX utility source code
to not exchange the information with the M4 core application using shared
memory.

It is also possible to use the [imx-m4fwloader](https://github.com/codeauroraforum/imx-m4fwloader) [[7]](#id15) utility to load the M4 core
application.

One option applicable in UDOOBuntu Linux is to copy the binary file into the
file /var/opt/m4/m4last.fw in the Linux filesystem. The next time the system is
booted, Das U-Boot will load it from there.

Another option is to directly use Das U-Boot to load the code.

### Debugging

The UDOO Neo Full board includes pads for soldering the 14-pin JTAG
connector. Zephyr applications running on the M4 core have only been
tested by observing UART console output.

### References

[[1](#id4)]

[https://www.udoo.org/udoo-neo/](https://www.udoo.org/udoo-neo/)

[[2](#id6)]

[https://www.udoo.org/get-started-neo/](https://www.udoo.org/get-started-neo/)

[[3](#id8)]

[https://www.udoo.org/docs-neo](https://www.udoo.org/docs-neo)

[[4](#id10)]

[https://www.udoo.org/download/files/datasheets/datasheet\_udoo\_neo.pdf](https://www.udoo.org/download/files/datasheets/datasheet_udoo_neo.pdf)

[[5](#id12)]

[https://www.udoo.org/download/files/schematics/UDOO\_NEO\_schematics.pdf](https://www.udoo.org/download/files/schematics/UDOO_NEO_schematics.pdf)

[[6](#id14)]

[https://github.com/ektor5/udooneo-m4uploader](https://github.com/ektor5/udooneo-m4uploader)

[[7](#id16)]

[https://github.com/codeauroraforum/imx-m4fwloader](https://github.com/codeauroraforum/imx-m4fwloader)

[[8](#id18)]

[https://www.nxp.com/products/processors-and-microcontrollers/applications-processors/i.mx-applications-processors/i.mx-6-processors/i.mx-6solox-processors-heterogeneous-processing-with-arm-cortex-a9-and-cortex-m4-cores:i.MX6SX](https://www.nxp.com/products/processors-and-microcontrollers/applications-processors/i.mx-applications-processors/i.mx-6-processors/i.mx-6solox-processors-heterogeneous-processing-with-arm-cortex-a9-and-cortex-m4-cores:i.MX6SX)

[[9](#id20)]

[https://www.nxp.com/docs/en/data-sheet/IMX6SXCEC.pdf](https://www.nxp.com/docs/en/data-sheet/IMX6SXCEC.pdf)

[10]
([1](#id22),[2](#id23))

[https://www.nxp.com/docs/en/reference-manual/IMX6SXRM.pdf](https://www.nxp.com/docs/en/reference-manual/IMX6SXRM.pdf)

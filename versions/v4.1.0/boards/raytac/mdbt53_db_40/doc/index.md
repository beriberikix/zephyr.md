---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/raytac/mdbt53_db_40/doc/index.html
original_path: boards/raytac/mdbt53_db_40/doc/index.html
---

# MDBT53-DB-40

Board Overview

[![../../../../_images/MDBT53-DB-40.jpg](../../../../_images/MDBT53-DB-40.jpg)
](../../../../_images/MDBT53-DB-40.jpg)

MDBT53-DB-40

Name:
:   `raytac_mdbt53_db_40`

Vendor:
:   Raytac Corporation

Architecture:
:   arm

SoC:
:   nrf5340

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/raytac/mdbt53_db_40/doc/index.rst/../..)

## Overview

Raytac MDBT53-DB-40 demo board is a development board based on the Raytac MDBT53-1M module,
using Nordic Semiconductor nRF5340 ARM Cortex-M33 SoC. Its design concept is to connect all
of the module’s pins to 2.54mm pin headers. It is convenient for developers to verify whether
the modules are connected to other peripheral devices or sensors as a tool for software development.

The nRF5340 inside the MDBT53-1M module is a
dual-core SoC based on the Arm® Cortex®-M33 architecture, with:

- a full-featured Arm Cortex-M33F core with DSP instructions, FPU, and
  Armv8-M Security Extension, running at up to 128 MHz, referred to as
  the **application core**
- a secondary Arm Cortex-M33 core, with a reduced feature set, running
  at a fixed 64 MHz, referred to as the **network core**.

The `raytac_mdbt53_db_40/nrf5340/cpuapp` build target provides support for the application
core on the nRF5340 SoC. The `raytac_mdbt53_db_40/nrf5340/cpuapp` build target provides
support for the network core on the nRF5340 SoC.

nRF5340 SoC provides support for the following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- IDAU
- I2C
- MPU
- NVIC
- PWM
- QSPI
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- Segger RTT (RTT Console)
- SPI
- UARTE
- WDT

More information about the board can be found at the [MDBT53-DB-40 website](https://www.raytac.com/product/ins.php?index_id=139) [[2]](#id4).
The [MDBT53-DB-40 Specification](https://www.raytac.com/download/index.php?index_id=60) [[3]](#id7) contains the demo board’s datasheet.
The [MDBT53-DB-40 Schematic](https://www.raytac.com/upload/catalog_b/8b5e364600a9cc8c53a869733e97f07e.jpg) [[4]](#id10) contains the demo board’s schematic.

## Hardware

- Module Demo Board build by MDBT53-1M
- Nordic nRF5340 SoC Solution
- A recommended 3rd-party module by Nordic Semiconductor.
- Dual-core Arm® Cortex® M33
- 1MB/256KB Flash Memory; 512kB/ 64kB RAM
- Supports BT5 Long Range Features
- Bluetooth specification v5.2
- Supports Bluetooth Direction Finding & Mesh
- Supports Bluetooth low energy audio
- Certifications: FCC, IC, CE, Telec (MIC), KC, SRRC, NCC, RCM, WPC
- RoHs & Reach Compiant.
- 48 GPIO
- Chip Antenna
- Interfaces: SPI, UART, I2C, I2S, PWM, ADC, NFC, and USB
- Highly flexible multiprotocol SoC ideally suited for Bluetooth® Low Energy, ANT+, Zigbee, Thread (802.15.4) ultra low-power wireless applications.
- 4 User LEDs
- 4 User buttons
- 1 Mini USB connector for power supply
- SWD connector for FW programming
- J-Link interface for FW programming
- UART interface for UART communication

### Supported Features

The `raytac_mdbt53_db_40` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

See [MDBT53-DB-40 website](https://www.raytac.com/product/ins.php?index_id=139) [[2]](#id4) and [MDBT53-DB-40 Specification](https://www.raytac.com/download/index.php?index_id=60) [[3]](#id7)
for a complete list of Raytac MDBT53-DB-40 board hardware features.

### Connections and IOs

#### LED

- LED1 (green) = P0.28
- LED2 (red) = P0.30
- LED3 = P0.31
- LED4 = P0.29

#### Push buttons

- BUTTON1 = SW1 = P0.24
- BUTTON2 = SW2 = P0.08
- BUTTON3 = SW3 = P0.23
- BUTTON4 = SW4 = P0.09

#### UART

- RX = P0.22
- TX = P0.20
- RTS = P0.19
- CTS = P0.21

### Security components

- Implementation Defined Attribution Unit ([IDAU](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau) [[1]](#id2)) on the application core.
  The IDAU is implemented with the System Protection Unit and is used to
  define secure and non-secure memory maps. By default, all of the memory
  space (Flash, SRAM, and peripheral address space) is defined to be secure
  accessible only.
- Secure boot.

## Programming and Debugging

nRF5340 application core supports the Armv8-M Security Extension.
Applications built for the `raytac_mdbt53_db_40/nrf5340/cpuapp` board by
default boot in the Secure state.

nRF5340 network core does not support the Armv8-M Security Extension.
nRF5340 IDAU may configure bus accesses by the nRF5340 network core
to have Secure attribute set; the latter allows to build and run
Secure only applications on the nRF5340 SoC.

Applications for the `raytac_mdbt53_db_40_nrf5340` board configuration can be
built, flashed, and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

Note

Flashing and Debugging Zephyr onto the raytac\_mdbt53\_db\_40\_nrf5340 board
requires an external J-Link programmer. The programmer is attached to the J1
or J9 SWD connector.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Warning

The nRF5340 has a flash read-back protection feature. When flash read-back
protection is active, you will need to recover the chip before reflashing.
If you are flashing with [west](../../../../develop/west/build-flash-debug.md#west-build-flash-debug), run
this command for more details on the related `--recover` option:

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Use a USB to TTL converter to connect the computer and raytac\_mdbt53\_db\_40\_nrf5340
J10 connector. Then run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the USB to TTL converter
can be found. For example, under Linux, `/dev/ttyUSB0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b raytac_mdbt53_db_40_nrf5340 samples/hello_world
west flash
```

### Debugging

The `raytac_mdbt53_db_40_nrf5340` board does not have an on-board-J-Link debug IC,
however, instructions from the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page also apply to this board.
Use the Debug out connector of nRF52x DK to connect to the J1 connector, and use SEGGER
J-Link OB IF to debug.

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic
boards with a Segger IC.

## References

[[1](#id3)]

[https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau)

[2]
([1](#id5),[2](#id6))

[https://www.raytac.com/product/ins.php?index\_id=139](https://www.raytac.com/product/ins.php?index_id=139)

[3]
([1](#id8),[2](#id9))

[https://www.raytac.com/download/index.php?index\_id=60](https://www.raytac.com/download/index.php?index_id=60)

[[4](#id11)]

[https://www.raytac.com/upload/catalog\_b/8b5e364600a9cc8c53a869733e97f07e.jpg](https://www.raytac.com/upload/catalog_b/8b5e364600a9cc8c53a869733e97f07e.jpg)

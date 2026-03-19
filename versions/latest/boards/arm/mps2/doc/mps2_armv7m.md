---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/arm/mps2/doc/mps2_armv7m.html
original_path: boards/arm/mps2/doc/mps2_armv7m.html
---

# ARM V2M MPS2 Armv7-m (AN385/AN386/AN500)

## Overview

The `mps2/an385`, `mps2/an386`, and `mps2/an500` board targets are three of
the mps2 Armv7-m based board targets supported in Zephyr. This document
provides details about the support provided for these three Armv7-m mps2 board targets
(**AN385**, **AN386**, **AN500**) and the following devices:

- Nested Vectored Interrupt Controller (NVIC)
- System Tick System Clock (SYSTICK)
- Cortex-M System Design Kit UART

![ARM V2M MPS2](../../../../_images/mps21.jpg)

In addition to enabling actual hardware usage, these board targets can
also use [FVP](https://developer.arm.com/downloads/view/FMFVP) to emulate the platforms running on the MPS2+.

More information about the board can be found at the [V2M MPS2 Website](https://developer.mbed.org/platforms/ARM-MPS2/).

The application note for each of the board can be found as follows:

- AN385 can be found at [Application Note AN385](https://documentation-service.arm.com/static/5ed107a5ca06a95ce53f89e3)
- AN386 can be found at [Application Note AN386](https://documentation-service.arm.com/static/5ed1094dca06a95ce53f8a9f)
- AN500 can be found at [Application Note AN500](https://documentation-service.arm.com/static/5ed112fcca06a95ce53f8eb3)

AN385 is also supported to run with QEMU, and is set to run with QEMU by default.

Note

These board targets makes no claims about its suitability for use
with actual MPS2 hardware systems, or any other hardware
system.

## Hardware

ARM V2M MPS2 provides the following hardware components:

- ARM Cortex-M Chip
- ARM IoT Subsystem for Cortex-M
- Form factor: 140x120cm
- ZBTSRAM: 8MB single cycle SRAM, 16MB PSRAM
- Video: QSVGA touch screen panel, 4bit RGB VGA connector
- Audio: Audio Codec
- Debug:

  - ARM JTAG20 connector
  - ARM parallel trace connector (MICTOR38)
  - 20 pin Cortex debug connector
  - 10 pin Cortex debug connector
  - ILA connector for FPGA debug
- Expansion

  - GPIO
  - SPI

Note

4 MB of flash memory (in ZBTSRAM 1, starting at address 0x00400000) and 4 MB of RAM
(in ZBTSRAM 2 & 3, starting at address 0x20000000) are available.

### Supported Features

The `mps2/an385`, `mps2/an386`, and `mps2/an500` board targets support the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| UART | on-chip | serial port-polling; serial port-interrupt |
| GPIO | on-chip | gpio |
| WATCHDOG | on-chip | watchdog |
| TIMER | on-chip | counter |
| DUALTIMER | on-chip | counter |

Other hardware features are not currently supported by the port.
See the [V2M MPS2 Website](https://developer.mbed.org/platforms/ARM-MPS2/) for a complete list of V2M MPS2 board hardware
features.

The default configuration can be found in
[boards/arm/mps2/mps2\_an385\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an385_defconfig)
or similarly in `mps2_anxxx_defconfig` for the other applicable boards.

### Interrupt Controller

MPS2 is a Cortex-M based SoC and has 15 fixed exceptions and 45 IRQs.

A Cortex-M3/4/7-based board uses vectored exceptions. This means each exception
calls a handler directly from the vector table.

Handlers are provided for exceptions 1-6, 11-12, and 14-15. The table here
identifies the handlers used for each exception.

| Exc# | Name | Remarks | Used by Zephyr Kernel |
| --- | --- | --- | --- |
| 1 | Reset |  | system initialization |
| 2 | NMI |  | system fatal error |
| 3 | Hard fault |  | system fatal error |
| 4 | MemManage | MPU fault | system fatal error |
| 5 | Bus |  | system fatal error |
| 6 | Usage fault | undefined instruction, or switch attempt to ARM mode | system fatal error |
| 11 | SVC |  | system calls, kernel run-time exceptions, and IRQ offloading |
| 12 | Debug monitor |  | system fatal error |
| 14 | PendSV |  | context switch |
| 15 | SYSTICK |  | system clock |

### Pin Mapping

The ARM V2M MPS2 Board has 4 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.

All GPIO controller pins are exposed via the following sequence of pin numbers:

- Pins 0 - 15 are for GPIO 0
- Pins 16 - 31 are for GPIO 1
- Pins 32 - 47 are for GPIO 2
- Pins 48 - 51 are for GPIO 3

Mapping from the ARM MPS2 Board pins to GPIO controllers:

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

For more details please refer to [MPS2 Technical Reference Manual (TRM)](https://developer.arm.com/documentation/100112/0200/).

### System Clock

The V2M MPS2 main clock is 24 MHz.

### Serial Port

The V2M MPS2 processor has five UARTs. Both the UARTs have only two wires for
RX/TX and no flow control (CTS/RTS) or FIFO. The Zephyr console output, by
default, is utilizing UART0.

## Programming and Debugging

### Flashing

V2M MPS2 provides:

- A USB connection to the host computer, which exposes a Mass Storage and an
  USB Serial Port.
- A Serial Flash device, which implements the USB flash disk file storage.
- A physical UART connection which is relayed over interface USB Serial port.

#### Flashing an application to V2M MPS2

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application with AN385.

```shell
# From the root of the zephyr repository
west build -b mps2/an385 samples/hello_world
```

Connect the V2M MPS2 to your host computer using the USB port and you should
see a USB connection which exposes a Mass Storage and a USB Serial Port.
Copy the generated zephyr.bin in the exposed drive.
Reset the board and you should be able to see on the corresponding Serial Port
the following message:

```shell
Hello World! arm
```

#### Running an applicatoin with FVP

Here is the same example for running with FVP.
Set the `ARMFVP_BIN_PATH` environemnt variable to the location of your FVP you have downloaded from [here](https://developer.arm.com/downloads/view/FMFVP)

```shell
export ARMFVP_BIN_PATH=/home/../FVP_MPS2/
```

Then build with the same command you would use normally, and run with `west build -t run_armfvp`.

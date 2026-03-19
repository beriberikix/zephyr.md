---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32n6570_dk/doc/index.html
original_path: boards/st/stm32n6570_dk/doc/index.html
---

# STM32N6570-DK

Board Overview

[![../../../../_images/stm32n6570_dk.webp](../../../../_images/stm32n6570_dk.webp)
](../../../../_images/stm32n6570_dk.webp)

STM32N6570-DK

Name:
:   `stm32n6570_dk`

Vendor:
:   STMicroelectronics

Architecture:

SoC:
:   stm32n657xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32n6570_dk/doc/index.rst/../..)

## Overview

The STM32N6570\_DK Discovery kit is a complete demonstration and development platform
for the Arm® Cortex®‑M55 core‑based STM32N657X0H3Q microcontroller.

The STM32N6570\_DK Discovery kit includes a full range of hardware features that help
the user evaluate many peripherals, such as USB Type-C®, Octo‑SPI flash memory and
Hexadeca‑SPI PSRAM devices, Ethernet, camera module, LCD, microSD™, audio codec,
digital microphones, ADC, flexible extension connectors, and user button.
The four flexible extension connectors feature easy and unlimited expansion capabilities
for specific applications such as wireless connectivity, analog applications, and sensors.

The STM32N657X0H3Q microcontroller features one USB 2.0 high‑speed/full‑speed
Device/Host/OTG controller, one USB 2.0 high‑speed/full‑speed Device/Host/OTG controller
with UCPD (USB Type-C® Power Delivery), one Ethernet with TSN (time-sensitive networking),
four I2Cs, two I3Cs, six SPIs (of which four I2S‑capable), two SAIs, with four DMIC support,
five USARTs, five UARTs (ISO78916 interface, LIN, IrDA, up to 12.5 Mbit/s), one LPUART,
two SDMMCs (MMC version 4.0, CE-ATA version 1.0, and SD version 1.0.1), three CAN FD
with TTCAN capability, JTAG and SWD debugging support, and Embedded Trace Macrocell™ (ETM).

The STM32N6570\_DK Discovery kit integrates an STLINK-V3EC embedded in-circuit debugger and
programmer for the STM32 MCU, with a USB Virtual COM port bridge and the comprehensive MCU Package.

## Hardware

- STM32N657X0H3Q Arm® Cortex®‑M55‑based microcontroller featuring ST Neural-ART Accelerator,
  H264 encoder, NeoChrom 2.5D GPU, and 4.2 Mbytes of contiguous SRAM, in a VFBGA264 package
- 5” LCD module with capacitive touch panel
- USB Type-C® with USB 2.0 HS interface, dual‑role‑power (DRP)
- USB Type-A with USB 2.0 HS interface, host, 0.5 A max
- 1‑Gbit Ethernet with TSN (time-sensitive networking) compliant with IEEE‑802.3‑2002
- SAI audio codec
- One MEMS digital microphone
- 1‑Gbit Octo‑SPI flash memory
- 256-Mbit Hexadeca‑SPI PSRAM
- Two user LEDs
- User, tamper, and reset push-buttons
- Board connectors:

  - USB Type-C®
  - USB Type-A
  - Ethernet RJ45
  - Camera module
  - microSD™ card
  - LCD
  - Stereo headset jack including analog microphone input
  - Audio MEMS daughterboard expansion connector
  - ARDUINO® Uno R3 expansion connector
  - STMod+ expansion connector
- On-board STLINK-V3EC debugger/programmer with USB re-enumeration capability:
  Virtual COM port, and debug port

For more details, please refer to:

- [STM32N6570\_DK website](https://www.st.com/en/evaluation-tools/stm32n6570-dk.html)
- [STM32N657X0 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32n657x0.html)
- [STM32N657 reference manual](https://www.st.com/resource/en/reference_manual/rm0486-stm32n647657xx-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `stm32n6570_dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

STM32N6570\_DK Board has 12 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.

For more details please refer to [STM32N6570\_DK User Manual](https://www.st.com/resource/en/user_manual/um3300-discovery-kit-with-stm32n657x0-mcu-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

- ADC1\_INP10 : PA9
- ADC1\_INP11 : PA10
- FDCAN1\_TX : PH2
- FDCAN1\_RX : PD0
- I2C1\_SCL : PH9
- I2C1\_SDA : PC1
- I2C4\_SCL : PE13
- I2C4\_SDA : PE14
- LD1 : PO1
- LD2 : PG10
- SPI5\_SCK : PE15
- SPI5\_MOSI : PG2
- SPI5\_MISO : PH8
- SPI5\_NSS : PA3
- USART\_1\_TX : PE5
- USART\_1\_RX : PE6
- USART\_2\_TX : PD5
- USART\_2\_RX : PF6

#### System Clock

STM32N6570\_DK System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
400MHz, driven by 64MHz high speed internal oscillator.

#### Serial Port

STM32N6570\_DK board has 10 U(S)ARTs. The Zephyr console output is assigned to
USART1. Default settings are 115200 8N1.

## Programming and Debugging

STM32N6570\_DK board includes an ST-LINK/V3 embedded debug tool interface.
This probe allows to flash and debug the board using various tools.

### Flashing or loading

The board is configured to be programmed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is needed.
Version 2.18.0 or later of [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) is required.

Note

Firmware is run in secure mode of execution, which requires a signature.
After build, the build system will automatically generate a signed version of the
binary using [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) utility `STM32_SigningTool_CLI`.
This utility is installed along with [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html), but make sure it is
available in your `PATH` variable.

To program the board, there are two options:

- Program the firmware in external flash. At boot, it will then be loaded on RAM
  and executed from there.
- Optionally, it can also be taken advantage from the serial boot interface provided
  by the boot ROM. In that case, firmware is directly loaded in RAM and executed from
  there. It is not retained.

#### Programming an application to STM32N6570\_DK

Here is an example to build and run [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, connect the STM32N6570\_DK to your host computer using the ST-Link USB port.

> ST-LinkSerial Boot Loader (USB)
>
> Build and flash an application using `stm32n6570_dk` target.
>
> ```shell
> # From the root of the zephyr repository
> west build -b stm32n6570_dk samples/hello_world
> west flash
> ```
>
> Note
>
> For flashing, before powering the board, set the boot pins in the following configuration:
>
> - BOOT0: 0
> - BOOT1: 1
>
> After flashing, to run the application, set the boot pins in the following configuration:
>
> - BOOT1: 0
>
> Power off and on the board again.
>
> Additionally, connect the STM32N6570\_DK to your host computer using the USB port.
> In this configuration, ST-Link is used to power the board and for serial communication
> over the Virtual COM Port.
>
> Note
>
> Before powering the board, set the boot pins in the following configuration:
>
> - BOOT0: 1
> - BOOT1: 0
>
> Build and load an application using `stm32n6570_dk/stm32n657xx/sb` target (you
> can also use the shortened form: `stm32n6570_dk//sb`)
>
> ```shell
> # From the root of the zephyr repository
> west build -b stm32n6570_dk//sb samples/hello_world
> west flash
> ```

Run a serial host program to connect with your Disco board:

```shell
$ minicom -D /dev/ttyACM0
```

You should see the following message on the console:

```shell
Hello World! stm32n6570_dk/stm32n657xx
```

### Debugging

For now debugging is only available through STM32CubeIDE:

- Go to File > Import and select C/C++ > STM32 Cortex-M Executable.
- In Executable field, browse to your <ZEPHYR\_PATH>/build/zephyr/zephyr.elf.
- In MCU field, select STM32N657X0HxQ.
- Click on Finish.
- Finally, click on Debug to start the debugging session.

Note

For debugging, before powering on the board, set the boot pins in the following configuration:

- BOOT0: 0
- BOOT1: 1

### Running tests with twister

Due to the BOOT switches manipulation required when flashing the board using `stm32n6570_dk`
board target, it is only possible to run twister tests campaign on `stm32n6570_dk/stm32n657xx/sb`
board target which doesn’t require BOOT pins changes to load and execute binaries.
To do so, it is advised to use Twister’s hardware map feature with the following settings:

```yaml
- platform: stm32n6570_dk/stm32n657xx/sb
  product: BOOT-SERIAL
  pre_script: <path_to_zephyr>/boards/st/common/scripts/board_power_reset.sh
  runner: stm32cubeprogrammer
```

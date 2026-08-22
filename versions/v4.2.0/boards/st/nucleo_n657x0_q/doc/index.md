---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/nucleo_n657x0_q/doc/index.html
original_path: boards/st/nucleo_n657x0_q/doc/index.html
---

# Nucleo N657X0-Q

Board Overview

[![../../../../_images/nucleo_n657x0_q.webp](../../../../_images/nucleo_n657x0_q.webp)
](../../../../_images/nucleo_n657x0_q.webp)

Nucleo N657X0-Q

Name:
:   `nucleo_n657x0_q`

Vendor:
:   STMicroelectronics

Architecture:

SoC:
:   stm32n657xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_n657x0_q/doc/index.rst/../..)

## Overview

The NUCLEO-N657X0-Q board provides an affordable and flexible way for users to try out
new concepts and build prototypes by choosing from the various combinations of performance
and power consumption features, provided by the STM32 microcontroller. For the compatible boards,
the internal or external SMPS significantly reduces power consumption in Run mode.

The ST Zio connector, which extends the ARDUINO® Uno V3 connectivity, and the ST morpho headers
provide an easy means of expanding the functionality of the Nucleo open development platform with
a wide choice of specialized shields.

The NUCLEO-N657X0-Q board does not require any separate probe as it integrates the ST-LINK
debugger/programmer.

The STM32 Nucleo-144 board comes with the STM32 comprehensive free software libraries and
examples available with the STM32Cube MCU Package.

## Hardware

- Common features:

  - STM32 microcontroller in an LQFP144, TFBGA225, or VFBGA264 package
  - 3 user LEDs
  - 1 user push-button and 1 reset push-button
  - 32.768 kHz crystal oscillator
  - Board connectors:

    - SWD
    - ST morpho expansion connector
  - Flexible power-supply options: ST-LINK USB VBUS, USB connector, or external sources
- Features specific to some of the boards (refer to the ordering information section
  of the data brief for details);

  - External or internal SMPS to generate Vcore logic supply
  - Ethernet compliant with IEEE-802.3-2002
  - USB Device only, USB OTG full speed, or SNK/UFP (full-speed or high-speed mode)
  - Board connectors:

    - ARDUINO® Uno V3 connector or ST Zio expansion connector including ARDUINO® Uno V3
    - Camera module FPC
    - MIPI20 compatible connector with trace signals
    - USB with Micro-AB or USB Type-C®
    - Ethernet RJ45
  - On-board ST-LINK (STLINK/V2-1, STLINK-V3E, or STLINK-V3EC) debugger/programmer with
    USB re-enumeration capability: mass storage, Virtual COM port, and debug port

For more details, please refer to:

- [NUCLEO-N657X0-Q website](https://www.st.com/en/evaluation-tools/nucleo-n657x0-q.html)
- [STM32N657X0 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32n657x0.html)
- [STM32N657 reference manual](https://www.st.com/resource/en/reference_manual/rm0486-stm32n647657xx-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `nucleo_n657x0_q` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### USB

The USB pin assignments on the STM32N657XX microcontroller are immutable. This means that the specific
pins designated for USB functionality are fixed and cannot be changed or reassigned to other functions,
ensuring consistent and reliable USB communication.

### USB PIN (IOs)

| Name | Description |
| --- | --- |
| OTG1\_HSDM | USB OTG1 High-Speed Data- (negative) |
| OTG1\_HSDP | USB OTG1 High-Speed Data+ (positive) |
| OTG1\_ID | USB OTG1 ID Pin |
| OTG1\_TXRTUNE | USB OTG1 Transmit Retune |
| OTG2\_HSDM | USB OTG2 High-Speed Data- (negative) |
| OTG2\_HSDP | USB OTG2 High-Speed Data+ (positive) |
| OTG2\_ID | USB OTG2 ID Pin |
| OTG2\_TXRTUNE | USB OTG2 Transmit Retune |

### Connections and IOs

NUCLEO-N657X0-Q Board has 12 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.

For more details please refer to [NUCLEO-N657X0-Q User Manual](https://www.st.com/resource/en/user_manual/um3417-stm32n6-nucleo144-board-mb1940-stmicroelectronics.pdf).

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
- SPI5\_MISO : PG1
- SPI5\_NSS : PA3
- USART\_1\_TX : PE5
- USART\_1\_RX : PE6
- USART\_3\_TX : PD8
- USART\_3\_RX : PD9
- XSPI2\_NCS1 : PN1
- XSPI2\_DQS0 : PN0
- XSPI2\_CLK : PN6
- XSPI2\_IO0 : PN2
- XSPI2\_IO1 : PN3
- XSPI2\_IO2 : PN4
- XSPI2\_IO3 : PN5
- XSPI2\_IO4 : PN8
- XSPI2\_IO5 : PN9
- XSPI2\_IO6 : PN10
- XSPI2\_IO7 : PN11

#### System Clock

NUCLEO-N657X0-Q System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
400MHz, driven by 64MHz high speed internal oscillator.

#### Serial Port

NUCLEO-N657X0-Q board has 10 U(S)ARTs. The Zephyr console output is assigned to
USART1. Default settings are 115200 8N1.

## Programming and Debugging

The `nucleo_n657x0_q` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

NUCLEO-N657X0-Q board includes an ST-LINK/V3 embedded debug tool interface.
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

#### Programming an application to NUCLEO-N657X0-Q

Here is an example to build and run [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, connect the NUCLEO-N657X0-Q to your host computer using the ST-Link USB port.

> ST-LinkSerial Boot Loader (USB)
>
> Build and flash an application using `nucleo_n657x0_q` target.
>
> ```shell
> # From the root of the zephyr repository
> west build -b nucleo_n657x0_q samples/hello_world
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
> Additionally, connect the NUCLEO-N657X0-Q to your host computer using the USB port.
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
> Build and load an application using `nucleo_n657x0_q/stm32n657xx/sb` target (you
> can also use the shortened form: `nucleo_n657x0_q//sb`)
>
> ```shell
> # From the root of the zephyr repository
> west build -b nucleo_n657x0_q samples/hello_world
> west flash
> ```

Run a serial host program to connect to your board:

```shell
$ minicom -D /dev/ttyACM0
```

You should see the following message on the console:

```shell
Hello World! nucleo_n657x0_q/stm32n657xx
```

### Debugging

You can debug an application in the usual way using the [ST-LINK GDB Server](../../../../develop/flash_debug/host-tools.md#runner-stlink-gdbserver).
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_n657x0_q samples/hello_world
west debug
```

Note

To enable debugging, before powering on the board, set the boot pins in the following configuration:

- BOOT0: 0
- BOOT1: 1

Another solution for debugging is to use STM32CubeIDE:

- Go to File ‣ Import and select C/C++ ‣ STM32 Cortex-M Executable.
- In the Executable field, browse to your `<ZEPHYR_PATH>/build/zephyr/zephyr.elf`.
- In MCU field, select `STM32N657X0HxQ`.
- Click on Finish.
- Finally, click on Debug to start the debugging session.

### Running tests with twister

Due to the BOOT switches manipulation required when flashing the board using `nucleo_n657x0_q`
board target, it is only possible to run twister tests campaign on `nucleo_n657x0_q/stm32n657xx/sb`
board target which doesn’t require BOOT pins changes to load and execute binaries.
To do so, it is advised to use Twister’s hardware map feature with the following settings:

```yaml
- platform: nucleo_n657x0_q/stm32n657xx/sb
  product: BOOT-SERIAL
  pre_script: <path_to_zephyr>/boards/st/common/scripts/board_power_reset.sh
  runner: stm32cubeprogrammer
```

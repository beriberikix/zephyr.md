---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_n657x0_q/doc/index.html
original_path: boards/st/nucleo_n657x0_q/doc/index.html
---

# Nucleo N657X0-Q

Board Overview

[![../../../../_images/nucleo_n657x0_q.webp](https://docs.zephyrproject.org/4.1.0/_images/nucleo_n657x0_q.webp)
](https://docs.zephyrproject.org/4.1.0/_images/nucleo_n657x0_q.webp)

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

#### `nucleo_n657x0_q/stm32n657xx/sb` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M55 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L23) | [`arm,cortex-m55`](../../../../build/dts/api/bindings/cpu/arm,cortex-m55.md#std-dtcompatible-arm-cortex-m55) |
| ADC | on-chip | STM32N6 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L368)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L384) | [`st,stm32n6-adc`](../../../../build/dts/api/bindings/adc/st,stm32n6-adc.md#std-dtcompatible-st-stm32n6-adc) |
| CAN | on-chip | STM32H7 series FDCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L400)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L411) | [`st,stm32h7-fdcan`](../../../../build/dts/api/bindings/can/st,stm32h7-fdcan.md#std-dtcompatible-st-stm32h7-fdcan) |
| Clock control | on-chip | STM32N6 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L232) | [`st,stm32n6-rcc`](../../../../build/dts/api/bindings/clock/st,stm32n6-rcc.md#std-dtcompatible-st-stm32n6-rcc) |
| on-chip | STM32N6 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L46) | [`st,stm32n6-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32n6-hse-clock.md#std-dtcompatible-st-stm32n6-hse-clock) |
| on-chip | STM32 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L52) | [`st,stm32h7-hsi-clock`](../../../../build/dts/api/bindings/clock/st,stm32h7-hsi-clock.md#std-dtcompatible-st-stm32h7-hsi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L59) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L67) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32N6 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L74)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L80) | [`st,stm32n6-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32n6-pll-clock.md#std-dtcompatible-st-stm32n6-pll-clock) |
| on-chip | STM32N6 CPU Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L98) | [`st,stm32n6-cpu-clock-mux`](../../../../build/dts/api/bindings/clock/st,stm32n6-cpu-clock-mux.md#std-dtcompatible-st-stm32n6-cpu-clock-mux) |
| on-chip | STM32 Clock multiplexer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L104) | [`st,stm32-clock-mux`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mux.md#std-dtcompatible-st-stm32-clock-mux) |
| on-chip | STM32N6 Divider IC multiplexer[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L110)[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L122) | [`st,stm32n6-ic-clock-mux`](../../../../build/dts/api/bindings/clock/st,stm32n6-ic-clock-mux.md#std-dtcompatible-st-stm32n6-ic-clock-mux) |
| DMA | on-chip | STM32U5 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L631) | [`st,stm32u5-dma`](../../../../build/dts/api/bindings/dma/st,stm32u5-dma.md#std-dtcompatible-st-stm32u5-dma) |
| GPIO & Headers | on-chip | STM32 GPIO controller[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L271) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_n657x0_q/arduino_r3_connector.dtsi?plain=1#L7) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L523)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L535) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_n657x0_q/nucleo_n657x0_q_common.dtsi?plain=1#L39) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8.1-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17) | [`arm,v8.1m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8.1m-nvic.md#std-dtcompatible-arm-v8.1m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L244) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_n657x0_q/nucleo_n657x0_q_common.dtsi?plain=1#L20) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv8.1-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L30) | [`arm,armv8.1m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L265) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L238) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L433)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L442) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L611)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L571) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st,stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/n6/stm32n6.dtsi?plain=1#L37) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8.1-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25) | [`arm,armv8.1m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8.1m-systick.md#std-dtcompatible-arm-armv8.1m-systick) |

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

#### System Clock

NUCLEO-N657X0-Q System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
400MHz, driven by 64MHz high speed internal oscillator.

#### Serial Port

NUCLEO-N657X0-Q board has 10 U(S)ARTs. The Zephyr console output is assigned to
USART1. Default settings are 115200 8N1.

## Programming and Debugging

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

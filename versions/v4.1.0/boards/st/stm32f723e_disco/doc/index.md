---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32f723e_disco/doc/index.html
original_path: boards/st/stm32f723e_disco/doc/index.html
---

# STM32F723E Discovery

Board Overview

[![../../../../_images/stm32f723e_disco.jpg](https://docs.zephyrproject.org/4.1.0/_images/stm32f723e_disco.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/stm32f723e_disco.jpg)

STM32F723E Discovery

Name:
:   `stm32f723e_disco`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f723xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32f723e_disco/doc/index.rst/../..)

## Overview

The discovery kit enables a wide diversity of applications taking benefit
from audio, multi-sensor support, graphics, security, security, video,
and high-speed connectivity features. Important board features include:

- STM32F723IEK6 microcontroller featuring 512 Kbytes of Flash memory and 256+16+4 Kbytes of RAM, in BGA176 package
- On-board ST-LINK/V2-1 supporting USB re-enumeration capability
- TFT LCD 240x240 pixels with touch panel
- SAI audio codec
- Audio line in and line out jack
- Stereo speaker outputs
- Four ST MEMS microphones
- Two pushbuttons (user and reset)
- 512-Mbit Quad-SPI Flash memory
- 8-Mbit external PSRAM
- USB OTG HS with Micro-AB connectors
- USB OTG FS with Micro-AB connectors

More information about the board can be found at the [32F723E-DISCO website](https://www.st.com/en/evaluation-tools/32f723ediscovery.html).

## Hardware

The STM32F723E Discovery kit provides the following hardware components:

- STM32F723IEK6 in BGA176 package
- ARM® 32-bit Cortex® -M7 CPU with FPU
- 216 MHz max CPU frequency
- VDD from 1.8 V to 3.6 V
- 1 MB Flash
- 256+16+4 KB SRAM including 64KB of tightly coupled memory
- GPIO with external interrupt capability
- 3x12-bit ADC with 24 channels
- 2x12-bit D/A converters
- RTC
- Advanced-control Timer (2)
- General Purpose Timers (13)
- Watchdog Timers (2)
- USART/UART (8)
- I2C (3)
- SPI (5)
- 2xSAI (serial audio interface)
- SDIO (2)
- CAN
- USB 2.0 OTG FS with on-chip PHY
- USB 2.0 OTG HS/FS with dedicated DMA, on-chip full-speed PHY and on-chip hi-speed PHY
- CRC calculation unit
- True random number generator
- DMA Controller

More information about STM32F723IEK6 can be found here:

- [STM32F723IEK6 on www.st.com](https://www.st.com/en/microcontrollers/stm32f723ie.html)
- [STM32F72xxx reference manual](https://www.st.com/resource/en/reference_manual/dm00305990.pdf)

### Supported Features

The `stm32f723e_disco` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32f723e_disco/stm32f723xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L34) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | STM32F4 ADC[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L752) | [`st,stm32f4-adc`](../../../../build/dts/api/bindings/adc/st,stm32f4-adc.md#std-dtcompatible-st-stm32f4-adc) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L412) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st,stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L135) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st,stm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L56) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L62) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L69) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32F7 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L84) | [`st,stm32f7-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32f7-pll-clock.md#std-dtcompatible-st-stm32f7-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L92) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L454) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L803) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V1)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L811) | [`st,stm32-dma-v1`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L118) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| on-board | STM32 QSPI Flash controller supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f723e_disco/stm32f723e_disco.dts?plain=1#L126) | [`st,stm32-qspi-nor`](../../../../build/dts/api/bindings/flash_controller/st,stm32-qspi-nor.md#std-dtcompatible-st-stm32-qspi-nor) |
| GPIO & Headers | on-chip | STM32 GPIO controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L167) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f723e_disco/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L326) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f723e_disco/stm32f723e_disco.dts?plain=1#L41) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L146) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f723e_disco/stm32f723e_disco.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L104) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| on-chip | STM32 Flexible Memory Controller (SDRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L110) | [`st,stm32-fmc-sdram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc-sdram.md#std-dtcompatible-st-stm32-fmc-sdram) |
| on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L745) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MMC | on-chip | STM32 SDMMC Disk Access[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L839) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L41) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L126) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | STM32 USB HS PHY controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f723.dtsi?plain=1#L13) | [`st,stm32-usbphyc`](../../../../build/dts/api/bindings/phy/st,stm32-usbphyc.md#std-dtcompatible-st-stm32-usbphyc) |
| on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L899) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L161) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L431) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| QSPI | on-chip | STM32 QSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L857) | [`st,stm32-qspi`](../../../../build/dts/api/bindings/qspi/st,stm32-qspi.md#std-dtcompatible-st-stm32-qspi) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L140) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L830) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L735) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L868) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L879) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L887) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L263)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L254) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L281) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L904) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L362)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L372) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st,stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L421) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L707) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| on-chip | STM32 OTGHS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L721) | [`st,stm32-otghs`](../../../../build/dts/api/bindings/usb/st,stm32-otghs.md#std-dtcompatible-st-stm32-otghs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L240) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L246) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Pin Mapping

STM32F723E Discovery kit has 7 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [32F723E-DISCO board User Manual](https://www.st.com/resource/en/user_manual/dm00342318.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_2 TX/RX : PA2/PA3 (Arduino Serial)
- UART\_6 TX/RX : PC6/PC7 (ST-Link Virtual Port Com)
- I2C1 SCL/SDA : PB8/PB9
- I2C2 SCL/SDA : PH4/PH5 (Arduino I2C)
- I2C3 SCL/SDA : PA8/PH8
- SPI1 SCK/MISO/MOSI : PA5/PB4/PB5 (Arduino SPI)
- LD1 : PA5
- LD5 : PA7
- LD6 : PB1
- OTG\_FS\_DM : PA11
- OTG\_FS\_DP : PA12

### System Clock

The STM32F723E System Clock can be driven by an internal or external oscillator,
as well as by the main PLL clock. By default, the System clock is driven by the PLL
clock at 216MHz, driven by a 25MHz high speed external clock.

### Serial Port

The STM32F723E Discovery kit has up to 8 UARTs. The Zephyr console output is assigned to UART6
which connected to the onboard ST-LINK/V2 Virtual COM port interface. Default communication
settings are 115200 8N1.

## Programming and Debugging

STM32F723E Discovery kit includes an ST-LINK/V2 embedded debug tool interface.

Applications for the `stm32f723e_disco` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to STM32F723E-DISCO

First, connect the STM32F723E Discovery kit to your host computer using
the USB port to prepare it for flashing. Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f723e_disco samples/hello_world
west flash
```

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyACM0
```

You should see the following message on the console:

```shell
Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f723e_disco samples/hello_world
west debug
```

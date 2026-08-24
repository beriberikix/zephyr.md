---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/seco/stm32f3_seco_d23/doc/index.html
original_path: boards/seco/stm32f3_seco_d23/doc/index.html
---

# SECO SBC-3.5-PX30 (JUNO - D23) (STM32F302)

Board Overview

[![../../../../_images/stm32f3_seco_d23.jpg](https://docs.zephyrproject.org/4.1.0/_images/stm32f3_seco_d23.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/stm32f3_seco_d23.jpg)

SECO SBC-3.5-PX30 (JUNO - D23) (STM32F302)

Name:
:   `stm32f3_seco_d23`

Vendor:
:   SECO S.p.A.

Architecture:
:   arm

SoC:
:   stm32f302xc

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/seco/stm32f3_seco_d23/doc/index.rst/../..)

## Overview

SBC-3.5-PX30 (JUNO - D23) is a Single Board Computer based on embedded Rockchip PX30
Processor, featuring Quad-Core ARM Cortex-A35 processor. The processor
integrates a Mali-G31 GPU with High performance dedicated 2D processor,
supporting OpenGL ES 1.1 / 2.0 / 3.2, Vulkan 1.0, OpenCL 2.0 and Open VG 1.1.
Embedded VPU is able to support video decoding of the most common coding
standard (MPEG-4, H.265/HEVC, H.264, VP8, VC-1). The board is completed with up
to 4GB LPDDR4-3200 32-bit bus memory directly soldered on board and one eMMC
5.1 Flash Drive with up to 64GB of capacity. LVDS Single Channel interface and
HDMI are supported. The RMII interface and Micrel KSZ8091 Ethernet Transceiver
allow the implementation of a Fast Ethernet interface. The networking
capabilities can be extended by WiFi+BT M.2 module and external modem module.
The audio functionalities are managed by the AudioCodec embedded in the RK-809
PMIC. SBC-3.5-PX30 board is completed by a series of connectors with various
interfaces (UART, SPI, I2C) managed by the microcontroller STM32F302VCT6.

## Hardware

SECO SBC-3.5-PX30 provides the following hardware components:

- STM32F302VCT6
  - ARM® 32-bit Cortex® -M4 CPU with FPU
  - 256 KB Flash
  - 40 KB SRAM
  - 72 MHz max CPU frequency
- 2 User LEDs
- 16 GPI
- 16 GPO
- 4 U(S)ART
  - Modbus
  - RS485
  - TTL Serial Debug
  - TTL Serial
- 8-channel General Purpose Timers
- USB 2.0 full speed interface
- CAN
- I2C (up to 2)
- SPI

More information about STM32F302VC can be found here:

- [STM32F302VC on www.st.com](https://www.st.com/en/microcontrollers/stm32f302vc.html)
- [STM32F302xC reference manual](https://www.st.com/resource/en/reference_manual/rm0365-stm32f302xbcde-and-stm32f302x68-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `stm32f3_seco_d23` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32f3_seco_d23/stm32f302xc` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L29) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f302.dtsi?plain=1#L105) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L419) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32F3 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L97) | [`st,stm32f3-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32f3-rcc.md#std-dtcompatible-st-stm32f3-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L42) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L63)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L48) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L55) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32F0/F3 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L70) | [`st,stm32f0-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32f0-pll-clock.md#std-dtcompatible-st-stm32f0-pll-clock) |
| Counter | on-chip | STM32 counters[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L282) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L246) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2bis) for the stm32F0, stm32F1 and stm32L1 soc families[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L428) | [`st,stm32-dma-v2bis`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2bis.md#std-dtcompatible-st-stm32-dma-v2bis) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L78) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L129) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L220)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f302.dtsi?plain=1#L19) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L108) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seco/stm32f3_seco_d23/stm32f3_seco_d23.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L87) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seco/stm32f3_seco_d23/stm32f3_seco_d23.dts?plain=1#L185) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L464) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| on-board | Simple GPIO controlled CAN transceiver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seco/stm32f3_seco_d23/stm32f3_seco_d23.dts?plain=1#L69) | [`can-transceiver-gpio`](../../../../build/dts/api/bindings/phy/can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L123) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f302.dtsi?plain=1#L81)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L276) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Regulator | on-board | Fixed voltage regulators[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seco/stm32f3_seco_d23/stm32f3_seco_d23.dts?plain=1#L36) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L102) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L408) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L438) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L449) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L457) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L184)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L193) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L211) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L469) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L236)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f302.dtsi?plain=1#L61) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L36) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f302.dtsi?plain=1#L71)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L266) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L254) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L170) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L176) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Pin Mapping

SBC-3.5-PX30 has 6 GPIO controllers. These controllers are
responsible for pin muxing, input/output, pull-up, etc.

For more details please refer to [SECO SBC-3.5-PX30 board User Manual](https://www.seco.com/Manuals/SBC-D23_Manual.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PA9 (debug config for UART\_1)
- UART\_1\_RX : PA10 (debug config for UART\_1)
- UART\_1\_TX : PC4 (alternate config for UART\_1)
- UART\_1\_RX : PC5 (alternate config for UART\_1)
- UART\_2\_TX : PD5
- UART\_2\_RX : PD6
- UART\_2\_CLK : PD7
- UART\_2\_CTS : PD3
- UART\_2\_RTS/DE : PD4
- UART\_3\_TX : PC10
- UART\_3\_RX : PC11
- UART\_3\_CLK : PD10
- UART\_3\_CTS : PD11
- UART\_3\_RTS/DE : PD12
- UART\_5\_TX : PC12
- UART\_5\_RX : PD2
- I2C1\_SCL : PB6
- I2C1\_SDA : PB7
- I2C2\_SCL : PA9 (alternate config for UART\_1)
- I2C2\_SDA : PA10 (alternate config for UART\_1)
- SPI1\_NSS : PA4
- SPI1\_SCK : PB3
- SPI1\_MISO : PB4
- SPI1\_MOSI : PB5
- SPI2\_NSS : PB12
- SPI2\_SCK : PB13
- SPI2\_MISO : PB14
- SPI2\_MOSI : PB15
- CAN1\_RX : PB8
- CAN1\_TX : PB9
- USB\_DM : PA11
- USB\_DP : PA12
- LD1 : PD8
- LD2 : PD9
- PWM : PA8

### System Clock

SECO SBC-3.5-PX30 System Clock could be driven by internal or external
oscillator, as well as main PLL clock. By default System clock is driven
by PLL clock at 72 MHz, driven by an external oscillator at 8 MHz.

### Serial Port

SECO SBC-3.5-PX30 has up to 4 U(S)ARTs. The Zephyr console output
is assigned to UART1. Default settings are 115200 8N1.
In debug configuration UART1 is connected to the flashing connector CN56.

UART2 provides Modbus interface to connector CN28.
UART3 provides RS-485 interface to connectors CN57 and CN48.
In alternative config, USART2 and USART3 are exposed to connector J2.

UART1 (in alternate config) and UART5 are connected to CN32.

### I2C

SECO SBC-3.5-PX30 has up to 2 I2Cs. Both are present in connector CN33.
I2C2 is available only on boards where DEBUG serial is not connected.

### USB

SECO SBC-3.5-PX30 has a USB 2.0 full-speed device interface available through
its connector CN31.

### CAN

SECO SBC-3.5-PX30 has an onboard CAN transceiver (TJA1051T), and it is
connected to both CN29 and CN30. PD0 is connected to EC\_CAN\_STBY.

### SPI

SECO SBC-3.5-PX30 has two SPI lines: SPI1 is an internal SPI line connected to the
main processor (Rockchip PX30) and SPI2 is connected to CN39.

## Programming and Debugging

### Flashing

Applications for the `stm32f3_seco_d23` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

#### Flashing an application to SECO SBC-3.5-PX30

First, connect the SECO SBC-3.5-PX30 to your host computer using
CN56 connector to an ST-Link.

The pinout is (1-8):

- VDD
- UART1\_TX
- UART1\_RX
- BOOT\_0
- SWDIO\_JTMS
- SWCLK\_JTCK
- EC\_RST#
- GND

Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f3_seco_d23 samples/hello_world
west flash
```

Run a serial host program to connect with your board.

```shell
$ minicom -D /dev/<tty device>
```

Replace <tty\_device> with the port where the SBC-3.5-PX30 board can be
found.

You should see the following message on the console:

```shell
Hello World! stm32f3_seco_d23
```

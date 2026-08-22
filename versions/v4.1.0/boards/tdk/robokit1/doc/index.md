---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/tdk/robokit1/doc/index.html
original_path: boards/tdk/robokit1/doc/index.html
---

# RoboKit 1

Board Overview

[![../../../../_images/tdk_robokit1.jpg](../../../../_images/tdk_robokit1.jpg)
](../../../../_images/tdk_robokit1.jpg)

RoboKit 1

Name:
:   `robokit1`

Vendor:
:   TDK Corporation.

Architecture:
:   arm

SoC:
:   same70q21b

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/tdk/robokit1/doc/index.rst/../..)

## Overview

The TDK RoboKit1 is a development board for use primarily with ROS2 and provides a large
number of small ground robotics useful sensors including chirp sensors for time of flight
(e.g. ultrasonic obstacle detection).

It pairs a 300MHz Cortex-M7 ATSAME70Q21 with an array of TDK sensors and pin headers useful for robotics.

## Hardware

- ATSAME70Q21 ARM Cortex-M7 Processor
- 12 MHz crystal oscillator (Pres)
- 32.768 kHz crystal oscillator
- Micro-AB USB device
- Micro-AB USB debug (Microchip EDBG) interface supporting CMSIS-DAP, Virtual COM Port and Data
- JTAG interface connector
- One reset pushbutton
- One red user LED
- TDK ICM 42688-P 6-Axis 32KHz IMU
- TDK ICP-10111 Pressure Sensor
- TDK NTC Thermistor for Temperature
- AKM AK09918C Magnetometer
- 2 TDK HVCi-4223 Cortex-M3 Dedicated Motor Controller
- 3 TDK ICS-43434 Stereo Microphones
- Connector for Industrial Dual IMU (TDK IIM-46230)
- TDK CH101 Ultrasonic Range Sensor Array (9 Connectors, comes with 3)

### Supported Features

The `robokit1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `robokit1/same70q21b` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L30) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-board | Texas Instrument Single Channel SPI ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/tdk/robokit1/robokit1-common.dtsi?plain=1#L115) | [`ti,ads7052`](../../../../build/dts/api/bindings/adc/ti%2Cads7052.md#std-dtcompatible-ti-ads7052) |
| on-chip | Atmel SAM family AFEC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L210)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L297) | [`atmel,sam-afec`](../../../../build/dts/api/bindings/adc/atmel%2Csam-afec.md#std-dtcompatible-atmel-sam-afec) |
| ARM architecture | on-chip | Atmel SAM SSC (Synchronous Serial Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L49) | [`atmel,sam-ssc`](../../../../build/dts/api/bindings/arm/atmel%2Csam-ssc.md#std-dtcompatible-atmel-sam-ssc) |
| CAN | on-chip | Specialization of Bosch m\_can CAN FD controller for Atmel SAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L175) | [`atmel,sam-can`](../../../../build/dts/api/bindings/can/atmel%2Csam-can.md#std-dtcompatible-atmel-sam-can) |
| Clock control | on-chip | Atmel Power Management Controller (PMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L323) | [`atmel,sam-pmc`](../../../../build/dts/api/bindings/clock/atmel%2Csam-pmc.md#std-dtcompatible-atmel-sam-pmc) |
| Counter | on-chip | Atmel SAM Timer Counter (TC) node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L67) | [`atmel,sam-tc`](../../../../build/dts/api/bindings/counter/atmel%2Csam-tc.md#std-dtcompatible-atmel-sam-tc) |
| DAC | on-chip | Atmel SAM family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L219) | [`atmel,sam-dac`](../../../../build/dts/api/bindings/dac/atmel%2Csam-dac.md#std-dtcompatible-atmel-sam-dac) |
| DMA | on-chip | Atmel SAM XDMAC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L314) | [`atmel,sam-xdmac`](../../../../build/dts/api/bindings/dma/atmel%2Csam-xdmac.md#std-dtcompatible-atmel-sam-xdmac) |
| Ethernet | on-chip | Atmel SAM-family GMAC Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L228) | [`atmel,sam-gmac`](../../../../build/dts/api/bindings/ethernet/atmel%2Csam-gmac.md#std-dtcompatible-atmel-sam-gmac) |
| Flash controller | on-chip | Atmel SAM Enhanced Embedded Flash Controller (EEFC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L347) | [`atmel,sam-flash-controller`](../../../../build/dts/api/bindings/flash_controller/atmel%2Csam-flash-controller.md#std-dtcompatible-atmel-sam-flash-controller) |
| GPIO & Headers | on-chip | SAM GPIO PORT node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L370) | [`atmel,sam-gpio`](../../../../build/dts/api/bindings/gpio/atmel%2Csam-gpio.md#std-dtcompatible-atmel-sam-gpio) |
| Hardware information | on-chip | ATMEL SAM Reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L421) | [`atmel,sam-rstc`](../../../../build/dts/api/bindings/hwinfo/atmel%2Csam-rstc.md#std-dtcompatible-atmel-sam-rstc) |
| I2C | on-chip | Atmel SAM Family I2C (TWIHS)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L118) | [`atmel,sam-i2c-twihs`](../../../../build/dts/api/bindings/i2c/atmel%2Csam-i2c-twihs.md#std-dtcompatible-atmel-sam-i2c-twihs) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/tdk/robokit1/robokit1-common.dtsi?plain=1#L26) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | Atmel SAM Family MDIO Driver node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L239) | [`atmel,sam-mdio`](../../../../build/dts/api/bindings/mdio/atmel%2Csam-mdio.md#std-dtcompatible-atmel-sam-mdio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L37) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | This binding describes the Atmel SAM flash area layout[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L357) | [`atmel,sam-flash`](../../../../build/dts/api/bindings/mtd/atmel%2Csam-flash.md#std-dtcompatible-atmel-sam-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/tdk/robokit1/robokit1-common.dtsi?plain=1#L194) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Atmel SAM Pinctrl container node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L364) | [`atmel,sam-pinctrl`](../../../../build/dts/api/bindings/pinctrl/atmel%2Csam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl) |
| Power management | on-chip | Atmel SAM SUPC (Supply-Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L428) | [`atmel,sam-supc`](../../../../build/dts/api/bindings/power/atmel%2Csam-supc.md#std-dtcompatible-atmel-sam-supc) |
| PWM | on-chip | Atmel SAM PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L140)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L275) | [`atmel,sam-pwm`](../../../../build/dts/api/bindings/pwm/atmel%2Csam-pwm.md#std-dtcompatible-atmel-sam-pwm) |
| RNG | on-chip | Atmel SAM RNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L306) | [`atmel,sam-trng`](../../../../build/dts/api/bindings/rng/atmel%2Csam-trng.md#std-dtcompatible-atmel-sam-trng) |
| RTC | on-chip | Atmel SAM family RTC device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L443) | [`atmel,sam-rtc`](../../../../build/dts/api/bindings/rtc/atmel%2Csam-rtc.md#std-dtcompatible-atmel-sam-rtc) |
| Sensors | on-board | ICM-42688 motion tracking device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/tdk/robokit1/robokit1-common.dtsi?plain=1#L103) | [`invensense,icm42688`](../../../../build/dts/api/bindings/sensor/invensense%2Cicm42688.md#std-dtcompatible-invensense-icm42688) |
| on-chip | Atmel SAM Timer Counter (TC) QDEC mode[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L78) | [`atmel,sam-tc-qdec`](../../../../build/dts/api/bindings/sensor/atmel%2Csam-tc-qdec.md#std-dtcompatible-atmel-sam-tc-qdec) |
| on-board | Asahi Kasei AKM09918C Magnetometer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/tdk/robokit1/robokit1-common.dtsi?plain=1#L86) | [`asahi-kasei,akm09918c`](../../../../build/dts/api/bindings/sensor/asahi-kasei%2Cakm09918c.md#std-dtcompatible-asahi-kasei-akm09918c) |
| on-board | EPCOS B57861S0103A039 thermistor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/tdk/robokit1/robokit1-common.dtsi?plain=1#L46) | [`epcos,b57861s0103a039`](../../../../build/dts/api/bindings/sensor/epcos%2Cb57861s0103a039.md#std-dtcompatible-epcos-b57861s0103a039) |
| Serial controller | on-chip | Atmel SAM family USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L167)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L151) | [`atmel,sam-usart`](../../../../build/dts/api/bindings/serial/atmel%2Csam-usart.md#std-dtcompatible-atmel-sam-usart) |
| on-chip | SAM family UART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L331)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L460) | [`atmel,sam-uart`](../../../../build/dts/api/bindings/serial/atmel%2Csam-uart.md#std-dtcompatible-atmel-sam-uart) |
| SPI | on-chip | Atmel SAM SPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L57) | [`atmel,sam-spi`](../../../../build/dts/api/bindings/spi/atmel%2Csam-spi.md#std-dtcompatible-atmel-sam-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L44) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Atmel SAM Family USB (USBHS) in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L199) | [`atmel,sam-usbhs`](../../../../build/dts/api/bindings/usb/atmel%2Csam-usbhs.md#std-dtcompatible-atmel-sam-usbhs) |
| Watchdog | on-chip | ATMEL SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L435) | [`atmel,sam-watchdog`](../../../../build/dts/api/bindings/watchdog/atmel%2Csam-watchdog.md#std-dtcompatible-atmel-sam-watchdog) |

### Connections and IOs

The TDK RoboKit Hardware Guide has detailed information about board connections.

### System Clock

The SAM E70 MCU is configured to use the 12 MHz external oscillator on the board
with the on-chip PLL to generate a 300 MHz system clock.

### Serial Port

The ATSAME70Q21 MCU has five UARTs and three USARTs. One of the UARTs is
configured for the console and is available as a Virtual COM Port via the USB2 connector.

## Programming and Debugging

Flashing the Zephyr project onto SAM E70 MCU requires the [OpenOCD tool](http://openocd.org/).
Both west flash and west debug commands should correctly work with both USB0 and USB1
connected and the board powered.

### Flashing

1. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
2. Connect the TDK RoboKit1 board to your host computer using the
   USB debug port (USB1), USB2 for a serial console, and remaining micro USB for
   power. Then build and flash the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

   ```shell
   # From the root of the zephyr repository
   west build -b robokit1 samples/hello_world
   west flash
   ```

   You should see “Hello World! robokit1” in your terminal.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b robokit1 samples/hello_world
west debug
```

## References

TDK RoboKit1 Product Page:
:   [https://invensense.tdk.com/products/robokit1-dk/](https://invensense.tdk.com/products/robokit1-dk/)

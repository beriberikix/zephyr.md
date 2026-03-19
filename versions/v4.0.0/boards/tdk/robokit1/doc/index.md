---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/tdk/robokit1/doc/index.html
original_path: boards/tdk/robokit1/doc/index.html
---

# RoboKit 1

Board Overview

[![../../../../_images/tdk_robokit1.jpg](../../../../_images/tdk_robokit1.jpg)
](../../../../_images/tdk_robokit1.jpg)

RoboKit 1

Vendor:
:   TDK Corporation.

Architecture:
:   arm

SoC:
:   same70q21b

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

The TDK RoboKit1 board supports the following hardware
features:

: header-rows: 1

| Peripheral | Kconfig option | Devicetree compatible |
| --- | --- | --- |
| GPIO | [`CONFIG_GPIO_SAM`](../../../../kconfig.md#CONFIG_GPIO_SAM "CONFIG_GPIO_SAM") | [`atmel,sam-gpio`](../../../../build/dts/api/bindings/gpio/atmel%2Csam-gpio.md#std-dtcompatible-atmel-sam-gpio) |
| USART | [`CONFIG_USART_SAM`](../../../../kconfig.md#CONFIG_USART_SAM "CONFIG_USART_SAM") | [`atmel,sam-usart`](../../../../build/dts/api/bindings/serial/atmel%2Csam-usart.md#std-dtcompatible-atmel-sam-usart) |
| UART | [`CONFIG_UART_SAM`](../../../../kconfig.md#CONFIG_UART_SAM "CONFIG_UART_SAM") | [`atmel,sam-uart`](../../../../build/dts/api/bindings/serial/atmel%2Csam-uart.md#std-dtcompatible-atmel-sam-uart) |
| SPI | [`CONFIG_SPI_SAM`](../../../../kconfig.md#CONFIG_SPI_SAM "CONFIG_SPI_SAM") | [`atmel,sam-spi`](../../../../build/dts/api/bindings/spi/atmel%2Csam-spi.md#std-dtcompatible-atmel-sam-spi) |
| I2C | [`CONFIG_I2C_SAM_TWIHS`](../../../../kconfig.md#CONFIG_I2C_SAM_TWIHS "CONFIG_I2C_SAM_TWIHS") | [`atmel,sam-i2c-twihs`](../../../../build/dts/api/bindings/i2c/atmel%2Csam-i2c-twihs.md#std-dtcompatible-atmel-sam-i2c-twihs) |
| I2S | [`CONFIG_I2S_SAM_SSC`](../../../../kconfig.md#CONFIG_I2S_SAM_SSC "CONFIG_I2S_SAM_SSC") | [`atmel,sam-ssc`](../../../../build/dts/api/bindings/arm/atmel%2Csam-ssc.md#std-dtcompatible-atmel-sam-ssc) |
| ADC | [`CONFIG_ADC_SAM_AFEC`](../../../../kconfig.md#CONFIG_ADC_SAM_AFEC "CONFIG_ADC_SAM_AFEC") | [`atmel,sam-afec`](../../../../build/dts/api/bindings/adc/atmel%2Csam-afec.md#std-dtcompatible-atmel-sam-afec) |
| DAC | [`CONFIG_DAC_SAM`](../../../../kconfig.md#CONFIG_DAC_SAM "CONFIG_DAC_SAM") | [`atmel,sam-dac`](../../../../build/dts/api/bindings/dac/atmel%2Csam-dac.md#std-dtcompatible-atmel-sam-dac) |
| PWM | [`CONFIG_PWM_SAM`](../../../../kconfig.md#CONFIG_PWM_SAM "CONFIG_PWM_SAM") | [`atmel,sam-pwm`](../../../../build/dts/api/bindings/pwm/atmel%2Csam-pwm.md#std-dtcompatible-atmel-sam-pwm) |
| CAN | [`CONFIG_CAN_SAM`](../../../../kconfig.md#CONFIG_CAN_SAM "CONFIG_CAN_SAM") | [`atmel,sam-can`](../../../../build/dts/api/bindings/can/atmel%2Csam-can.md#std-dtcompatible-atmel-sam-can) |
| USB | [`CONFIG_USB_DC_SAM_USBHS`](../../../../kconfig.md#CONFIG_USB_DC_SAM_USBHS "CONFIG_USB_DC_SAM_USBHS") | [`atmel,sam-usbhs`](../../../../build/dts/api/bindings/usb/atmel%2Csam-usbhs.md#std-dtcompatible-atmel-sam-usbhs) |
| WATCHDOG | [`CONFIG_WDT_SAM`](../../../../kconfig.md#CONFIG_WDT_SAM "CONFIG_WDT_SAM") | [`atmel,sam-watchdog`](../../../../build/dts/api/bindings/watchdog/atmel%2Csam-watchdog.md#std-dtcompatible-atmel-sam-watchdog) |
| NVIC | N/A | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| SYSTICK | N/A | N/A |
| COUNTER | [`CONFIG_COUNTER_SAM_TC`](../../../../kconfig.md#CONFIG_COUNTER_SAM_TC "CONFIG_COUNTER_SAM_TC") | [`atmel,sam-tc`](../../../../build/dts/api/bindings/timer/atmel%2Csam-tc.md#std-dtcompatible-atmel-sam-tc) |
| DMA | [`CONFIG_DMA_SAM_XDMAC`](../../../../kconfig.md#CONFIG_DMA_SAM_XDMAC "CONFIG_DMA_SAM_XDMAC") | [`atmel,sam-xdmac`](../../../../build/dts/api/bindings/dma/atmel%2Csam-xdmac.md#std-dtcompatible-atmel-sam-xdmac) |
| ENTROPY | [`CONFIG_ENTROPY_SAM_RNG`](../../../../kconfig.md#CONFIG_ENTROPY_SAM_RNG "CONFIG_ENTROPY_SAM_RNG") | [`atmel,sam-trng`](../../../../build/dts/api/bindings/rng/atmel%2Csam-trng.md#std-dtcompatible-atmel-sam-trng) |
| HWINFO (reset cause) | [`CONFIG_HWINFO_SAM_RSTC`](../../../../kconfig.md#CONFIG_HWINFO_SAM_RSTC "CONFIG_HWINFO_SAM_RSTC") | [`atmel,sam-rstc`](../../../../build/dts/api/bindings/hwinfo/atmel%2Csam-rstc.md#std-dtcompatible-atmel-sam-rstc) |
| HWINFO (device id) | [`CONFIG_HWINFO_SAM`](../../../../kconfig.md#CONFIG_HWINFO_SAM "CONFIG_HWINFO_SAM") | N/A |

The default configuration can be found in the Kconfig
[boards/tdk/robokit1/robokit1\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/tdk/robokit1/robokit1_defconfig).

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

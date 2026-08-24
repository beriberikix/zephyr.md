---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/dev_kits/sltb004a/doc/index.html
original_path: boards/silabs/dev_kits/sltb004a/doc/index.html
---

# EFR32MG12 Thunderboard (SLTB004A)

Board Overview

[![../../../../../_images/sltb004a.jpg](https://docs.zephyrproject.org/4.2.0/_images/sltb004a.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/sltb004a.jpg)

EFR32MG12 Thunderboard (SLTB004A)

Name:
:   `sltb004a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32mg12p332f1024gl125

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/dev_kits/sltb004a/doc/index.rst/../..)

## Overview

The EFR32MG12 Thunderboard (a.k.a Thunderboard Sense 2) contains an MCU
from the EFR32MG12 family built on ARM® Cortex®-M4F processor with low
power capabilities.

## Hardware

- EFR32MG12 Mighty Gecko Wireless SoC with 38.4 MHz operating frequency
- ARM® Cortex® M4 core with 256 kB RAM and 1024 kB Flash
- Macronix ultra low power 8-Mbit SPI flash (MX25R8035F)
- 2.4 GHz ceramic antenna for wireless transmission
- Silicon Labs Si7021 relative humidity and temperature sensor
- Silicon Labs Si1133 UV index and ambient light sensor
- Silicon Labs Si7210 hall effect sensor
- Bosch Sensortec BMP280 barometric pressure sensor
- ams CCS811 indoor air quality gas sensor
- TDK InvenSense ICM-20648 6-axis inertial sensor
- TDK InvenSense ICS-43434 MEMS microphone
- Four high brightness RGB LEDs from Broadcom Limited (ASMT-YTB7-0AA02)
- One bi-color LED and two push buttons
- Power enable signals for fine grained power-control
- On-board SEGGER J-Link debugger for easy programming and debugging, which
  includes a USB virtual COM port
- Mini Simplicity connector for access to energy profiling and advanced wireless
  network debugging
- Breakout pads for GPIO access and connection to external hardware
- Reset button
- Automatic switch-over between USB and battery power
- CR2032 coin cell holder and external battery connector

For more information about the EFR32MG12 SoC and Thunderboard Sense 2 board:

- [EFR32MG12 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg12-datasheet.pdf)
- [EFR32MG12 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efr32xg12-rm.pdf)
- [SLTB004A User Guide](https://www.silabs.com/documents/public/user-guides/ug309-sltb004a-user-guide.pdf)
- [SLTB004A Schematics](https://www.silabs.com/documents/public/schematic-files/BRD4166A-D00-schematic.pdf)

### Supported Features

The `sltb004a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sltb004a/efr32mg12p332f1024gl125` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L19) | [`arm,cortex-m4f`](../../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Bluetooth | on-chip | Silicon Labs Series 2 Bluetooth HCI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L237) | [`silabs,bt-hci-efr32`](../../../../../build/dts/api/bindings/bluetooth/silabs,bt-hci-efr32.md#std-dtcompatible-silabs-bt-hci-efr32) |
| Flash controller | on-chip | Silicon Labs Gecko flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L30) | [`silabs,gecko-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs,gecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L118) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs,gecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L128)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L137) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs,gecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L89) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs,gecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb004a/sltb004a.dts?plain=1#L49) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb004a/sltb004a.dts?plain=1#L35) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb004a/sltb004a.dts?plain=1#L67) | [`pwm-leds`](../../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L38) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb004a/sltb004a.dts?plain=1#L221) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb004a/sltb004a.dts?plain=1#L101) | [`jedec,spi-nor`](../../../../../build/dts/api/bindings/mtd/jedec,spi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Pin control | on-chip | Silabs Gecko Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L242) | [`silabs,gecko-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs,gecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl) |
| PWM | on-chip | Silabs Gecko PWM port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L222) | [`silabs,gecko-pwm`](../../../../../build/dts/api/bindings/pwm/silabs,gecko-pwm.md#std-dtcompatible-silabs-gecko-pwm) |
| RNG | on-chip | GECKO TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L229) | [`silabs,gecko-trng`](../../../../../build/dts/api/bindings/rng/silabs,gecko-trng.md#std-dtcompatible-silabs-gecko-trng) |
| RTC | on-chip | Silabs Gecko RTCC (Real-Time Counter)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L109) | [`silabs,gecko-rtcc`](../../../../../build/dts/api/bindings/rtc/silabs,gecko-rtcc.md#std-dtcompatible-silabs-gecko-rtcc) |
| Sensors | on-board | CCS811 digital air quality sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb004a/sltb004a.dts?plain=1#L155) | [`ams,ccs811`](../../../../../build/dts/api/bindings/sensor/ams,ccs811.md#std-dtcompatible-ams-ccs811) |
| Serial controller | on-chip | Gecko USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L45)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L54) | [`silabs,gecko-usart`](../../../../../build/dts/api/bindings/serial/silabs,gecko-usart.md#std-dtcompatible-silabs-gecko-usart) |
| on-chip | Gecko LEUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L81) | [`silabs,gecko-leuart`](../../../../../build/dts/api/bindings/serial/silabs,gecko-leuart.md#std-dtcompatible-silabs-gecko-leuart) |
| SPI | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L63) | [`silabs,usart-spi`](../../../../../build/dts/api/bindings/spi/silabs,usart-spi.md#std-dtcompatible-silabs-usart-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L25) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32mg.dtsi?plain=1#L201) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs,gecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### Connections and IOs

The EFR32MG12 SoC has eight gpio controllers (PORTA, PORTB, PORTC, PORTD,
PORTF, PORTI, PORTJ and PORTK).

In the following table, the column Name contains Pin names. For example, PE2
means Pin number 2 on PORTE and #27 represents the location bitfield , as used
in the board’s and microcontroller’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PD8 | GPIO | LED0 (RED) |
| PD9 | GPIO | LED1 (GREEN) |
| PD14 | GPIO | SW0 Push Button PB0 |
| PD15 | GPIO | Push Button PB1 |
| PA0 | UART\_TX | UART TX Console VCOM\_TX US0\_TX #0 |
| PA1 | UART\_RX | UART RX Console VCOM\_RX US0\_RX #0 |
| PF3 | UART\_TX | EXP12\_UART\_TX LEU0\_TX #27 |
| PF4 | UART\_RX | EXP14\_UART\_RX LEU0\_RX #27 |
| PC10 | I2C\_SDA | EXP16\_I2C\_SDA I2C0\_SDA #15 |
| PC11 | I2C\_SCL | EXP15\_I2C\_SCL I2C0\_SCL #15 |
| PB6 | I2C\_SDA | CCS811\_I2C\_SDA I2C1\_SDA #6 |
| PB7 | I2C\_SCL | CCS811\_I2C\_SCL I2C1\_SCL #6 |
| PK0 | SPI\_MOSI | Flash MOSI US2\_TX #29 |
| PK2 | SPI\_MISO | Flash MISO US2\_RX #30 |
| PF7 | SPI\_SCLK | Flash SCLK US2\_CLK #18 |
| PK1 | SPI\_CS | Flash Chip Select (GPIO) |

### System Clock

The EFR32MG12 SoC is configured to use the 38.4 MHz external oscillator on the
board.

### Serial Port

The EFR32MG12 SoC has four USARTs and one Low Energy UARTs (LEUART with 9600
maximum baudrate). USART0 is configured as the Zephyr console and is connected
to the On-Board J-Link Debugger that presents a virtual COM port for general
purpose application serial data transfer with this interface.

## Programming and Debugging

The `sltb004a` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Note

Before using the kit the first time, you should update the J-Link firmware
in Simplicity Studio.

### Flashing

The SLTB004A includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer, which exposes a Mass Storage and a
  USB Serial Port.
- A Serial Flash device, which implements the USB flash disk file storage.
- A physical UART connection which is relayed over interface USB Serial port.

#### Flashing an application to SLTB004A

The sample application [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b sltb004a samples/hello_world
```

Connect the SLTB004A to your host computer using the USB port and you
should see a USB connection which exposes a Mass Storage (TB004) and a
USB Serial Port. Copy the generated zephyr.bin in the SLTB004A drive.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should be able to see on the corresponding Serial Port
the following message:

```shell
Hello World! sltb004a
```

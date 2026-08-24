---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max32666fthr/doc/index.html
original_path: boards/adi/max32666fthr/doc/index.html
---

# MAX32666FTHR

Board Overview

[![../../../../_images/max32666fthr_img2.jpg](https://docs.zephyrproject.org/4.2.0/_images/max32666fthr_img2.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/max32666fthr_img2.jpg)

MAX32666FTHR

Name:
:   `max32666fthr`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32666

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32666fthr/doc/index.rst/../..)

## Overview

The MAX32666FTHR board is a rapid development platform to help engineers quickly implement battery
optimized Bluetooth® 5 solutions with the MAX32666 Arm® Cortex®-M4 processor with FPU. The board
also includes the MAX1555 1-Cell Li+ battery charger for battery management. The form factor is
a small 0.9in by 2.0in dualrow header footprint that is compatible with breadboards and
off-the-shelf peripheral expansion boards. The board also includes a variety of peripherals,
such as a micro SD card connector, 6-axis accelerometer/gyro, RGB indicator LED, and pushbutton.
This platform provides poweroptimized flexible for quick proof-of-concepts and early software
development to enhance time to market.

The Zephyr port is running on the MAX32666 MCU.

![MAX32666FTHR Front](https://docs.zephyrproject.org/4.2.0/_images/max32666fthr_img1.jpg)
![MAX32666FTHR Back](https://docs.zephyrproject.org/4.2.0/_images/max32666fthr_img21.jpg)

## Hardware

- MAX32666 MCU:

  - High-Efficiency Microcontroller and Audio DSP for Wearable and Hearable Devices

    - Arm Cortex-M4 with FPU Up to 96MHz
    - Optional Second Arm Cortex-M4 with FPU Optimized for Data Processing
    - Low-Power 7.3728MHz System Clock Option
    - 1MB Flash, Organized into Dual Banks 2 x 512KB
    - 560KB (448KB ECC) SRAM; 3 x 16KB Cache
    - Optional Error Correction Code (ECC-SEC-DED)for Cache, SRAM, and Internal Flash
  - Bluetooth 5 Low Energy Radio

    - 1Mbps and 2Mbps Data Throughput
    - Long Range (125kbps and 500kbps)
    - Advertising Extension
    - Rx Sensitivity: -95dbm; Tx Power Up to +4.5dbm
    - On-Chip Matching with Single-Ended Antenna Port
  - Power Management Maximizes Operating Time for Battery Applications

    - Integrated SIMO SMPS for Coin-Cell Operation
    - Dynamic Voltage Scaling Minimizes Active Core Power Consumption
    - 27.3μA/MHz at 3.3V Executing from Cache
    - Selectable SRAM Retention in Low Power Modes with RTC Enabled
  - Multiple Peripherals for System Control

    - Three QSPI Master/Slave with Three Chip Selects Each
    - Three 4-Wire UARTs
    - Three I2C Master/Slave
    - Up to 50 GPIO
    - QSPI (SPIXF) with Real-Time Flash Decryption
    - QSPI (SPIXR) RAM Interface Provides SRAMExpansion
    - 8-Input 10-Bit Delta-Sigma ADC 7.8ksps
    - USB 2.0 HS Engine with Internal Transceiver
    - PDM Interface Supports Two Digital Microphones
    - I2S with TDM
    - Six 32-Bit Timers
    - Two High-Speed Timers
    - 1-Wire Master
    - Sixteen Pulse Trains (PWM)
    - Secure Digital Interface Supports SD3.0/SDIO3.0/eMMC4.51
  - Secure Valuable IP/Data with Hardware Security

    - Trust Protection Unit (TPU) with MAA SupportsFast ECDSA and Modular Arithmetic
    - AES128/192/256, DES, 3DES, Hardware Accelerator
    - TRNG Seed Generator
    - SHA-2 Accelerator•Secure Bootloader
- External devices connected to the MAX32666FTHR:

  - MAX1555 1-Cell Li+ Battery Charger
  - Breadboard Compatible Headers
  - 10-Pin Cortex Debug Header
  - Micro USB Connector
  - Micro SD Card Connector
  - RGB Indicator LED and One General Purpose Push Button Switch
  - 6-Axis Accelerometer/Gyro
  - Bluetooth Surface Mount Antenna

### Supported Features

The `max32666fthr` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max32666fthr/max32666/cpu0` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC 10-Bits[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-10b`](../../../../build/dts/api/bindings/adc/adi%2Cmax32-adc-10b.md#std-dtcompatible-adi-max32-adc-10b) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi%2Cmax32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L60) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L318) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L100)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L110) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi%2Cmax32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi%2Cmax32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi%2Cmax32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| on-board | GPIO pins exposed on Adafruit Feather headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32666fthr/max32666fthr_max32666_cpu0.dts?plain=1#L62) | [`adafruit-feather-header`](../../../../build/dts/api/bindings/gpio/adafruit-feather-header.md#std-dtcompatible-adafruit-feather-header) |
| I2C | on-chip | ADI MAX32 I2C[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi%2Cmax32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32666fthr/max32666fthr_max32666_cpu0.dts?plain=1#L42) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32666fthr/max32666fthr_max32666_cpu0.dts?plain=1#L26) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi%2Cmax32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi%2Cmax32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi%2Cmax32-trng.md#std-dtcompatible-adi-max32-trng) |
| SDHC | on-chip | ADI MAX32 SDHC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L178) | [`adi,max32-sdhc`](../../../../build/dts/api/bindings/sdhc/adi%2Cmax32-sdhc.md#std-dtcompatible-adi-max32-sdhc) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi%2Cmax32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L130)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L120) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi%2Cmax32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi%2Cmax32-timer.md#std-dtcompatible-adi-max32-timer) |
| 1-Wire | on-chip | ADI MAX32xxx MCUs 1-Wire Master[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L170) | [`adi,max32-w1`](../../../../build/dts/api/bindings/w1/adi%2Cmax32-w1.md#std-dtcompatible-adi-max32-w1) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi%2Cmax32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

## JH3 Pinout

| Pin | Name | Description |
| --- | --- | --- |
| 1 | GND | Ground |
| 2 | P0\_9 | UART0 Tx |
| 3 | P0\_10 | UART0 Rx |
| 4 | P0\_26 | QSPI2 MISO |
| 5 | P0\_25 | QSPI2 MOSI |
| 6 | P0\_27 | QSPI2 SCK |
| 7 | AIN\_5 | ADC Analog Input. Alternatively, AIN2N or P0\_21 |
| 8 | AIN\_4 | ADC Analog Input. Alternatively, AIN2P or P0\_20 |
| 9 | AIN\_3 | ADC Analog Input. Alternatively, AIN1N or P0\_19 |
| 10 | AIN\_2 | ADC Analog Input. Alternatively, AIN1P or P0\_18 |
| 11 | AIN\_1 | ADC Analog Input. Alternatively, AIN0N or P0\_17 |
| 12 | AIN\_0 | ADC Analog Input. Alternatively, AIN0P or P0\_16 |
| 13 | GND | Ground |
| 14 | NC | No Connection |
| 15 | 3V3 | 3.3V Output. Typically used to provide 3.3V to peripherals connected to the expansion headers |
| 16 | RSTN | Master Reset Signal |

## JH4 Pinout

| Pin | Name | Description |
| --- | --- | --- |
| 1 | SYS | SYS switched connection to the Battery. This is the primary system power supply and automatically switches between the battery voltage and the USB supply when available. |
| 2 | PWREN | Power Enable. This is connected to the ON pin of the MAX4995 LDO. It turns off the LDO if shorted to GND. |
| 3 | VBUS | USB VBUS Signal. This can be used as a 5V supply when connected to USB. This pin can also be used as an input to power the board, but this should only be done when not using the USB connector since there is no circuitry to prevent current from flowing back into the USB connector. |
| 4 | P0\_12 | 1-Wire master signal |
| 5 | P0\_3 | SPIXF SCK |
| 6 | P0\_5 | SPIXF SDIO3 |
| 7 | P0\_4 | SPIXF SDIO2 |
| 8 | P0\_2 | SPIXF SDIO1/MISO |
| 9 | P0\_1 | SPIXF SDIO0/MOSI |
| 10 | P0\_0 | SPIXF SS0 |
| 11 | P0\_6 | I2CM0 SCL. Pulled to MAX32666 VDDIOH, connected to BMI160. |
| 12 | P0\_7 | I2CM0 SDA. Pulled to MAX32666 VDDIOH, connected to BMI160. |

## Programming and Debugging

The `max32666fthr` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX32666 MCU can be flashed by connecting an external debug probe to the SWD port.
SWD debug can be accessed through the Cortex 10-pin connector, JH2.
Logic levels are fixed to VDDIO (1.8V).

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash. To perform a full erase,
pass the `--erase` option when executing `west flash`.

Note

This board uses OpenOCD as the default debug interface. You can also use
a Segger J-Link with Segger’s native tooling by overriding the runner,
appending `--runner jlink` to your `west` command(s). The J-Link should
be connected to the standard 2\*5 pin debug connector (JH2) using an
appropriate adapter board and cable.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX32666FTHR web page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/MAX32666FTHR.html)

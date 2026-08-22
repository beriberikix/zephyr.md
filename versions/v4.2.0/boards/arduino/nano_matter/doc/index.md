---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/arduino/nano_matter/doc/index.html
original_path: boards/arduino/nano_matter/doc/index.html
---

# Arduino Nano Matter

Board Overview

[![../../../../_images/nano_matter.webp](../../../../_images/nano_matter.webp)
](../../../../_images/nano_matter.webp)

Arduino Nano Matter

Name:
:   `arduino_nano_matter`

Vendor:
:   Arduino

Architecture:
:   arm

SoC:
:   mgm240sd22vna

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arduino/nano_matter/doc/index.rst/../..)

## Overview

The Nano Matter merges the well-known Arduino way of making complex technology more accessible with the
powerful MGM240S from Silicon Labs, to bring Matter closer to the maker world, in one of the
smallest form factors in the market.

It enables 802.15.4 (Thread®) and Bluetooth® Low Energy connectivity, to interact with Matter-compatible devices
with a user-friendly software layer ready for quick prototyping.

The Nano Matter features a compact and efficient architecture powered by the
MGM240S (32-bit Arm® Cortex®-M33) from Silicon Labs, a high-performance wireless module optimized for
the needs of battery and line-powered IoT devices for 2.4 GHz mesh networks.

## Hardware

- MGM240SD22VNA2 Mighty Gecko SiP
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 1536 kB
- RAM: 256 kB
- Transmit power: up to +20 dBm
- Operation frequency: 2.4 GHz
- Crystals for LFXO (32.768 kHz) and HFXO (39 MHz).
- User RGB LED
- User button

For more information about the EFR32MG24 SoC and the Arduino Nano Matter, refer to these
documents:

- [MGM240S Website](https://www.silabs.com/wireless/zigbee/efr32mg24-series-2-modules/device.mgm240sd22vna)
- [EFR32MG24 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg24-datasheet.pdf)
- [EFR32xG24 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/brd4187c-rm.pdf)
- [Nano Matter User Manual](https://docs.arduino.cc/tutorials/nano-matter/user-manual/)

### Supported Features

The `arduino_nano_matter` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `arduino_nano_matter/mgm240sd22vna` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L138) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Silicon Labs Series 2 IADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L524) | [`silabs,gecko-iadc`](../../../../build/dts/api/bindings/adc/silabs%2Cgecko-iadc.md#std-dtcompatible-silabs-gecko-iadc) |
| Bluetooth | on-chip | Silicon Labs Series 2 Bluetooth HCI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L24) | [`silabs,bt-hci-efr32`](../../../../build/dts/api/bindings/bluetooth/silabs%2Cbt-hci-efr32.md#std-dtcompatible-silabs-bt-hci-efr32) |
| Clock control | on-chip | Silicon Labs Series 2 CMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L195) | [`silabs,series-clock`](../../../../build/dts/api/bindings/clock/silabs%2Cseries-clock.md#std-dtcompatible-silabs-series-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L204) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Silicon Labs Series 2 HFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L211) | [`silabs,hfxo`](../../../../build/dts/api/bindings/clock/silabs%2Chfxo.md#std-dtcompatible-silabs-hfxo) |
| on-chip | Silicon Labs Series 2 LFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L223) | [`silabs,series2-lfxo`](../../../../build/dts/api/bindings/clock/silabs%2Cseries2-lfxo.md#std-dtcompatible-silabs-series2-lfxo) |
| on-chip | Silicon Labs Series 2 HFRCODPLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L234) | [`silabs,series2-hfrcodpll`](../../../../build/dts/api/bindings/clock/silabs%2Cseries2-hfrcodpll.md#std-dtcompatible-silabs-series2-hfrcodpll) |
| on-chip | Silicon Labs Series 2 HFRCOEM23[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L241) | [`silabs,series2-hfrcoem23`](../../../../build/dts/api/bindings/clock/silabs%2Cseries2-hfrcoem23.md#std-dtcompatible-silabs-series2-hfrcoem23) |
| on-chip | Silicon Labs Series 2 LFRCO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L248) | [`silabs,series2-lfrco`](../../../../build/dts/api/bindings/clock/silabs%2Cseries2-lfrco.md#std-dtcompatible-silabs-series2-lfrco) |
| on-chip | Generic fixed factor clock provider[20 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L22) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Comparator | on-chip | Silicon Labs Series 2 ACMP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L540) | [`silabs,acmp`](../../../../build/dts/api/bindings/comparator/silabs%2Cacmp.md#std-dtcompatible-silabs-acmp) |
| Cryptographic accelerator | on-chip | Silicon Labs Series 2 SE Mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L399) | [`silabs,gecko-semailbox`](../../../../build/dts/api/bindings/crypto/silabs%2Cgecko-semailbox.md#std-dtcompatible-silabs-gecko-semailbox) |
| Debug | on-chip | Silicon Labs Packet Trace Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L29) | [`silabs,pti`](../../../../build/dts/api/bindings/debug/silabs%2Cpti.md#std-dtcompatible-silabs-pti) |
| on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L150) | [`arm,armv8m-itm`](../../../../build/dts/api/bindings/debug/arm%2Carmv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| DMA | on-chip | Silicon Labs Series 2 LDMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L483) | [`silabs,ldma`](../../../../build/dts/api/bindings/dma/silabs%2Cldma.md#std-dtcompatible-silabs-ldma) |
| Flash controller | on-chip | Silicon Labs Series 2 MSC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L269) | [`silabs,series2-flash-controller`](../../../../build/dts/api/bindings/flash_controller/silabs%2Cseries2-flash-controller.md#std-dtcompatible-silabs-series2-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L429) | [`silabs,gecko-gpio`](../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L440) | [`silabs,gecko-gpio-port`](../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L407) | [`silabs,gecko-i2c`](../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nano_matter/arduino_nano_matter.dts?plain=1#L79) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nano_matter/arduino_nano_matter.dts?plain=1#L41) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nano_matter/arduino_nano_matter.dts?plain=1#L60) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L277) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nano_matter/arduino_nano_matter.dts?plain=1#L212) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Silicon Labs Series 2 Radio Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L11) | [`silabs,series2-radio`](../../../../build/dts/api/bindings/net/wireless/silabs%2Cseries2-radio.md#std-dtcompatible-silabs-series2-radio) |
| Pin control | on-chip | Silicon Labs Series 2 DBUS Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L477) | [`silabs,dbus-pinctrl`](../../../../build/dts/api/bindings/pinctrl/silabs%2Cdbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl) |
| PWM | on-chip | Silicon Labs TIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L293)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L309) | [`silabs,timer-pwm`](../../../../build/dts/api/bindings/pwm/silabs%2Ctimer-pwm.md#std-dtcompatible-silabs-timer-pwm) |
| on-chip | Silicon Labs LETIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L517) | [`silabs,letimer-pwm`](../../../../build/dts/api/bindings/pwm/silabs%2Cletimer-pwm.md#std-dtcompatible-silabs-letimer-pwm) |
| Regulator | on-chip | Silicon Labs Series 2 DC-DC converter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L533) | [`silabs,series2-dcdc`](../../../../build/dts/api/bindings/regulator/silabs%2Cseries2-dcdc.md#std-dtcompatible-silabs-series2-dcdc) |
| RTC | on-chip | Silicon Labs Series 2 Sleeptimer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L418) | [`silabs,gecko-stimer`](../../../../build/dts/api/bindings/rtc/silabs%2Cgecko-stimer.md#std-dtcompatible-silabs-gecko-stimer) |
| Serial controller | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L364) | [`silabs,usart-uart`](../../../../build/dts/api/bindings/serial/silabs%2Cusart-uart.md#std-dtcompatible-silabs-usart-uart) |
| on-chip | Silicon Labs Series 2 EUSART [1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L373) | [`silabs,eusart-uart`](../../../../build/dts/api/bindings/serial/silabs%2Ceusart-uart.md#std-dtcompatible-silabs-eusart-uart) |
| SPI | on-chip | Silicon Labs Series 2 EUSART [1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L382) | [`silabs,eusart-spi`](../../../../build/dts/api/bindings/spi/silabs%2Ceusart-spi.md#std-dtcompatible-silabs-eusart-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L189) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Silicon Labs TIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L284)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L300) | [`silabs,series2-timer`](../../../../build/dts/api/bindings/timer/silabs%2Cseries2-timer.md#std-dtcompatible-silabs-series2-timer) |
| on-chip | Silicon Labs Series 2 BURTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L391) | [`silabs,gecko-burtc`](../../../../build/dts/api/bindings/timer/silabs%2Cgecko-burtc.md#std-dtcompatible-silabs-gecko-burtc) |
| on-chip | Silicon Labs LETIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L510) | [`silabs,series2-letimer`](../../../../build/dts/api/bindings/timer/silabs%2Cseries2-letimer.md#std-dtcompatible-silabs-series2-letimer) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L492)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L501) | [`silabs,gecko-wdog`](../../../../build/dts/api/bindings/watchdog/silabs%2Cgecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### Connections and IOs

In the following table, the column **Name** contains Pin names. For example, PA2
means Pin number 2 on PORTA, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PC1 | GPIO | LED0 |
| PC2 | GPIO | LED1 |
| PC3 | GPIO | LED2 |
| PA0 | GPIO | Button |
| PC4 | USART0\_TX | UART Console TX |
| PC5 | USART0\_RX | UART Console RX |

### System Clock

The MGM240S SiP is configured to run at 78 MHz using DPLL and the 39 MHz internal oscillator.

### Serial Port

The MGM240S SiP has one USART and two EUSARTs.
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

The Arduino Nano Matter contains an SAMD11 with CMSIS-DAP, allowing flashing, debugging, logging, etc. over
the USB port. Doing so requires a version of OpenOCD that includes support for the flash on the MG24
MCU. Until those changes are included in stock OpenOCD, the version bundled with Arduino can be
used, or can be installed from the [OpenOCD Arduino Fork](https://github.com/facchinm/OpenOCD/tree/arduino-0.12.0-rtx5). When flashing, debugging, etc. you may
need to include `--openocd=/usr/local/bin/openocd
--openocd-search=/usr/local/share/openocd/scripts/` options to the command.

### Flashing

Connect the Arduino Nano Matter board to your host computer using the USB port. A USB CDC ACM serial port
should appear on the host, that can be used to view logs from the flashed application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b arduino_nano_matter samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) connecting to the UCB CDC ACM serial port.

Reset the board and you should see the following message in the terminal:

```shell
Hello World! arduino_nano_matter
```

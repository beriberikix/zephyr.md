---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/seeed/xiao_mg24/doc/index.html
original_path: boards/seeed/xiao_mg24/doc/index.html
---

# XIAO MG24

Board Overview

[![../../../../_images/xiao_mg24.webp](https://docs.zephyrproject.org/4.2.0/_images/xiao_mg24.webp)
](https://docs.zephyrproject.org/4.2.0/_images/xiao_mg24.webp)

XIAO MG24

Name:
:   `xiao_mg24`

Vendor:
:   Seeed Technology Co., Ltd

Architecture:
:   arm

SoC:
:   efr32mg24b220f1536im48

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/seeed/xiao_mg24/doc/index.rst/../..)

## Overview

Seeed Studio XIAO MG24 is a mini development board based on Silicon Labs’ MG24. XIAO MG24 is based
on ARM Cortex-M33 core, 32-bit RISC architecture with a maximum clock speed of 78MHz, supporting DSP
instructions and FPU floating-point operations, possessing powerful computing power, and built-in
AL/ML hardware accelerator MVP, which can efficiently process AI/machine learning algorithms.
Secondly, it has excellent RF performance, with a transmission power of up to+19.5 dBm and a
reception sensitivity as low as -105.4 dBm. It supports multiple IoT and wireless transmission
protocols such as Matter, Thread, Zigbee, Bluetooth LE 5.3,Bluetooth mesh etc.

## Hardware

- EFR32MG24B220F1536IM48 Mighty Gecko SoC
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 1536 kB
- RAM: 256 kB
- Transmit power: up to +20 dBm
- Operation frequency: 2.4 GHz
- Crystals for LFXO (32.768 kHz) and HFXO (39 MHz).
- 3.7v LiPo power and charge support
- User and battery charge LEDs

For more information about the EFR32MG24 SoC and XIAO MG24 board, refer to these
documents:

- [EFR32MG24 Website](https://www.silabs.com/wireless/zigbee/efr32mg24-series-2-socs)
- [EFR32MG24 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg24-datasheet.pdf)
- [EFR32xG24 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/brd4187c-rm.pdf)
- [XIAO MG24 Wiki](https://wiki.seeedstudio.com/xiao_mg24_getting_started/)

### Supported Features

The `xiao_mg24` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `xiao_mg24/efr32mg24b220f1536im48` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L138) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Silicon Labs Series 2 IADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L524) | [`silabs,gecko-iadc`](../../../../build/dts/api/bindings/adc/silabs,gecko-iadc.md#std-dtcompatible-silabs-gecko-iadc) |
| Bluetooth | on-chip | Silicon Labs Series 2 Bluetooth HCI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L24) | [`silabs,bt-hci-efr32`](../../../../build/dts/api/bindings/bluetooth/silabs,bt-hci-efr32.md#std-dtcompatible-silabs-bt-hci-efr32) |
| Clock control | on-chip | Silicon Labs Series 2 CMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L195) | [`silabs,series-clock`](../../../../build/dts/api/bindings/clock/silabs,series-clock.md#std-dtcompatible-silabs-series-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L204) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Silicon Labs Series 2 HFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L211) | [`silabs,hfxo`](../../../../build/dts/api/bindings/clock/silabs,hfxo.md#std-dtcompatible-silabs-hfxo) |
| on-chip | Silicon Labs Series 2 LFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L223) | [`silabs,series2-lfxo`](../../../../build/dts/api/bindings/clock/silabs,series2-lfxo.md#std-dtcompatible-silabs-series2-lfxo) |
| on-chip | Silicon Labs Series 2 HFRCODPLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L234) | [`silabs,series2-hfrcodpll`](../../../../build/dts/api/bindings/clock/silabs,series2-hfrcodpll.md#std-dtcompatible-silabs-series2-hfrcodpll) |
| on-chip | Silicon Labs Series 2 HFRCOEM23[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L241) | [`silabs,series2-hfrcoem23`](../../../../build/dts/api/bindings/clock/silabs,series2-hfrcoem23.md#std-dtcompatible-silabs-series2-hfrcoem23) |
| on-chip | Silicon Labs Series 2 LFRCO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L248) | [`silabs,series2-lfrco`](../../../../build/dts/api/bindings/clock/silabs,series2-lfrco.md#std-dtcompatible-silabs-series2-lfrco) |
| on-chip | Generic fixed factor clock provider[20 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L22) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Comparator | on-chip | Silicon Labs Series 2 ACMP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L540) | [`silabs,acmp`](../../../../build/dts/api/bindings/comparator/silabs,acmp.md#std-dtcompatible-silabs-acmp) |
| Cryptographic accelerator | on-chip | Silicon Labs Series 2 SE Mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L399) | [`silabs,gecko-semailbox`](../../../../build/dts/api/bindings/crypto/silabs,gecko-semailbox.md#std-dtcompatible-silabs-gecko-semailbox) |
| Debug | on-chip | Silicon Labs Packet Trace Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L29) | [`silabs,pti`](../../../../build/dts/api/bindings/debug/silabs,pti.md#std-dtcompatible-silabs-pti) |
| on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L150) | [`arm,armv8m-itm`](../../../../build/dts/api/bindings/debug/arm,armv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| DMA | on-chip | Silicon Labs Series 2 LDMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L483) | [`silabs,ldma`](../../../../build/dts/api/bindings/dma/silabs,ldma.md#std-dtcompatible-silabs-ldma) |
| Flash controller | on-chip | Silicon Labs Series 2 MSC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L269) | [`silabs,series2-flash-controller`](../../../../build/dts/api/bindings/flash_controller/silabs,series2-flash-controller.md#std-dtcompatible-silabs-series2-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L429) | [`silabs,gecko-gpio`](../../../../build/dts/api/bindings/gpio/silabs,gecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L440) | [`silabs,gecko-gpio-port`](../../../../build/dts/api/bindings/gpio/silabs,gecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| on-board | GPIO pins exposed on Seeeduino Xiao (and compatible devices) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/xiao_mg24/seeed_xiao_connector.dtsi?plain=1#L8) | [`seeed,xiao-gpio`](../../../../build/dts/api/bindings/gpio/seeed-xiao-header.md#std-dtcompatible-seeed-xiao-gpio) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L407) | [`silabs,gecko-i2c`](../../../../build/dts/api/bindings/i2c/silabs,gecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/xiao_mg24/xiao_mg24.dts?plain=1#L35) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/xiao_mg24/xiao_mg24.dts?plain=1#L44) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L277) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/xiao_mg24/xiao_mg24.dts?plain=1#L189) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Silicon Labs Series 2 Radio Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L11) | [`silabs,series2-radio`](../../../../build/dts/api/bindings/net/wireless/silabs,series2-radio.md#std-dtcompatible-silabs-series2-radio) |
| Pin control | on-chip | Silicon Labs Series 2 DBUS Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L477) | [`silabs,dbus-pinctrl`](../../../../build/dts/api/bindings/pinctrl/silabs,dbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl) |
| PWM | on-chip | Silicon Labs TIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L293)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L309) | [`silabs,timer-pwm`](../../../../build/dts/api/bindings/pwm/silabs,timer-pwm.md#std-dtcompatible-silabs-timer-pwm) |
| on-chip | Silicon Labs LETIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L517) | [`silabs,letimer-pwm`](../../../../build/dts/api/bindings/pwm/silabs,letimer-pwm.md#std-dtcompatible-silabs-letimer-pwm) |
| Regulator | on-chip | Silicon Labs Series 2 DC-DC converter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L533) | [`silabs,series2-dcdc`](../../../../build/dts/api/bindings/regulator/silabs,series2-dcdc.md#std-dtcompatible-silabs-series2-dcdc) |
| RTC | on-chip | Silicon Labs Series 2 Sleeptimer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L418) | [`silabs,gecko-stimer`](../../../../build/dts/api/bindings/rtc/silabs,gecko-stimer.md#std-dtcompatible-silabs-gecko-stimer) |
| Serial controller | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L364) | [`silabs,usart-uart`](../../../../build/dts/api/bindings/serial/silabs,usart-uart.md#std-dtcompatible-silabs-usart-uart) |
| on-chip | Silicon Labs Series 2 EUSART [1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L373) | [`silabs,eusart-uart`](../../../../build/dts/api/bindings/serial/silabs,eusart-uart.md#std-dtcompatible-silabs-eusart-uart) |
| SPI | on-chip | Silicon Labs Series 2 EUSART [1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L382) | [`silabs,eusart-spi`](../../../../build/dts/api/bindings/spi/silabs,eusart-spi.md#std-dtcompatible-silabs-eusart-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L189) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Silicon Labs TIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L284)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L300) | [`silabs,series2-timer`](../../../../build/dts/api/bindings/timer/silabs,series2-timer.md#std-dtcompatible-silabs-series2-timer) |
| on-chip | Silicon Labs Series 2 BURTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L391) | [`silabs,gecko-burtc`](../../../../build/dts/api/bindings/timer/silabs,gecko-burtc.md#std-dtcompatible-silabs-gecko-burtc) |
| on-chip | Silicon Labs LETIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L510) | [`silabs,series2-letimer`](../../../../build/dts/api/bindings/timer/silabs,series2-letimer.md#std-dtcompatible-silabs-series2-letimer) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L492)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L501) | [`silabs,gecko-wdog`](../../../../build/dts/api/bindings/watchdog/silabs,gecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### Connections and IOs

In the following table, the column **Name** contains Pin names. For example, PA2
means Pin number 2 on PORTA, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PA7 | GPIO | LED0 |
| PA8 | USART0\_TX | UART Console TX |
| PA9 | USART0\_RX | UART Console RX |

The default configuration can be found in
[boards/seeed/xiao\_mg24/xiao\_mg24\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/xiao_mg24/xiao_mg24_defconfig)

### System Clock

The EFR32MG24 SoC is configured to use the 39 MHz external oscillator on the
board.

### Serial Port

The EFR32MG24 SoC has one USART and two EUSARTs.
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

The XIAO MG24 contains an SAMD11 with CMSIS-DAP, allowing flashing, debugging, logging, etc. over
the USB port. Doing so requires a version of OpenOCD that includes support for the flash on the MG24
MCU. Until those changes are included in stock OpenOCD, the version bundled with Arduino can be
used, or can be installed from the [OpenOCD Arduino Fork](https://github.com/facchinm/OpenOCD/tree/arduino-0.12.0-rtx5). When flashing, debugging, etc. you may
need to include `--openocd=/usr/local/bin/openocd
--openocd-search=/usr/local/share/openocd/scripts/` options to the command.

### Flashing

Connect the XIAO MG24 board to your host computer using the USB port. A USB CDC ACM serial port
should appear on the host, that can be used to view logs from the flashed application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b xiao_mg24 samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) connecting to the UCB CDC ACM serial port.

Reset the board and you should see the following message in the terminal:

```shell
Hello World! xiao_mg24
```

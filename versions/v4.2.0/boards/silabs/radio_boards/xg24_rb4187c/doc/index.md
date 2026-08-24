---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/radio_boards/xg24_rb4187c/doc/index.html
original_path: boards/silabs/radio_boards/xg24_rb4187c/doc/index.html
---

# EFR32xG24 2.4 GHz 20 dBm (xG24-RB4187C)

Board Overview

[![../../../../../_images/efr32mg24-xg24-rb4187c.jpg](https://docs.zephyrproject.org/4.2.0/_images/efr32mg24-xg24-rb4187c.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/efr32mg24-xg24-rb4187c.jpg)

EFR32xG24 2.4 GHz 20 dBm (xG24-RB4187C)

Name:
:   `xg24_rb4187c`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32mg24b220f1536im48

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/xg24_rb4187c/doc/index.rst/../..)

## Overview

The EFR32MG24 Mighty Gecko Radio Board is one of the two
radio boards delivered with [xG24-PK6010A Website](https://www.silabs.com/development-tools/wireless/efr32xg24-pro-kit-20-dbm). It contains
a Wireless System-On-Chip from the EFR32MG24 family built on an
ARM Cortex®-M33F processor with excellent low power capabilities.

The BRD4187C a.k.a. xG24-RB4187C radio board plugs into the Wireless Pro Kit
Mainboard BRD4002A and is supported as one of [Radio Boards](../../index.md#silabs-radio-boards).

## Hardware

- EFR32MG24B220F1536IM48 Mighty Gecko SoC
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 1536 kB
- RAM: 256 kB
- Transmit power: up to +20 dBm
- Operation frequency: 2.4 GHz
- Crystals for LFXO (32.768 kHz) and HFXO (39 MHz).

For more information about the EFR32MG24 SoC and BRD4187C board, refer to these
documents:

- [EFR32MG24 Website](https://www.silabs.com/wireless/zigbee/efr32mg24-series-2-socs)
- [EFR32MG24 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg24-datasheet.pdf)
- [EFR32xG24 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/brd4187c-rm.pdf)
- [xG24-PK6010A Website](https://www.silabs.com/development-tools/wireless/efr32xg24-pro-kit-20-dbm)
- [BRD4187C User Guide](https://www.silabs.com/documents/public/user-guides/ug526-brd4187c-user-guide.pdf)

### Supported Features

The `xg24_rb4187c` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `xg24_rb4187c/efr32mg24b220f1536im48` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L138) | [`arm,cortex-m33`](../../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Silicon Labs Series 2 IADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L524) | [`silabs,gecko-iadc`](../../../../../build/dts/api/bindings/adc/silabs,gecko-iadc.md#std-dtcompatible-silabs-gecko-iadc) |
| Bluetooth | on-chip | Silicon Labs Series 2 Bluetooth HCI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L24) | [`silabs,bt-hci-efr32`](../../../../../build/dts/api/bindings/bluetooth/silabs,bt-hci-efr32.md#std-dtcompatible-silabs-bt-hci-efr32) |
| Clock control | on-chip | Silicon Labs Series 2 CMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L195) | [`silabs,series-clock`](../../../../../build/dts/api/bindings/clock/silabs,series-clock.md#std-dtcompatible-silabs-series-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L204) | [`fixed-clock`](../../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Silicon Labs Series 2 HFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L211) | [`silabs,hfxo`](../../../../../build/dts/api/bindings/clock/silabs,hfxo.md#std-dtcompatible-silabs-hfxo) |
| on-chip | Silicon Labs Series 2 LFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L223) | [`silabs,series2-lfxo`](../../../../../build/dts/api/bindings/clock/silabs,series2-lfxo.md#std-dtcompatible-silabs-series2-lfxo) |
| on-chip | Silicon Labs Series 2 HFRCODPLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L234) | [`silabs,series2-hfrcodpll`](../../../../../build/dts/api/bindings/clock/silabs,series2-hfrcodpll.md#std-dtcompatible-silabs-series2-hfrcodpll) |
| on-chip | Silicon Labs Series 2 HFRCOEM23[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L241) | [`silabs,series2-hfrcoem23`](../../../../../build/dts/api/bindings/clock/silabs,series2-hfrcoem23.md#std-dtcompatible-silabs-series2-hfrcoem23) |
| on-chip | Silicon Labs Series 2 LFRCO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L248) | [`silabs,series2-lfrco`](../../../../../build/dts/api/bindings/clock/silabs,series2-lfrco.md#std-dtcompatible-silabs-series2-lfrco) |
| on-chip | Generic fixed factor clock provider[20 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L22) | [`fixed-factor-clock`](../../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Comparator | on-chip | Silicon Labs Series 2 ACMP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L540) | [`silabs,acmp`](../../../../../build/dts/api/bindings/comparator/silabs,acmp.md#std-dtcompatible-silabs-acmp) |
| Cryptographic accelerator | on-chip | Silicon Labs Series 2 SE Mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L399) | [`silabs,gecko-semailbox`](../../../../../build/dts/api/bindings/crypto/silabs,gecko-semailbox.md#std-dtcompatible-silabs-gecko-semailbox) |
| Debug | on-chip | Silicon Labs Packet Trace Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L29) | [`silabs,pti`](../../../../../build/dts/api/bindings/debug/silabs,pti.md#std-dtcompatible-silabs-pti) |
| on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L150) | [`arm,armv8m-itm`](../../../../../build/dts/api/bindings/debug/arm,armv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| Display | on-board | Sharp LS0XX memory display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg24_rb4187c/xg24_rb4187c.dts?plain=1#L149) | [`sharp,ls0xx`](../../../../../build/dts/api/bindings/display/sharp,ls0xx.md#std-dtcompatible-sharp-ls0xx) |
| DMA | on-chip | Silicon Labs Series 2 LDMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L483) | [`silabs,ldma`](../../../../../build/dts/api/bindings/dma/silabs,ldma.md#std-dtcompatible-silabs-ldma) |
| Flash controller | on-chip | Silicon Labs Series 2 MSC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L269) | [`silabs,series2-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs,series2-flash-controller.md#std-dtcompatible-silabs-series2-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L429) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs,gecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L440) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs,gecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L407) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs,gecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg24_rb4187c/xg24_rb4187c.dts?plain=1#L52) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg24_rb4187c/xg24_rb4187c.dts?plain=1#L38) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L277) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg24_rb4187c/xg24_rb4187c.dts?plain=1#L232) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg24_rb4187c/xg24_rb4187c.dts?plain=1#L160) | [`jedec,spi-nor`](../../../../../build/dts/api/bindings/mtd/jedec,spi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Networking | on-chip | Silicon Labs Series 2 Radio Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L11) | [`silabs,series2-radio`](../../../../../build/dts/api/bindings/net/wireless/silabs,series2-radio.md#std-dtcompatible-silabs-series2-radio) |
| Pin control | on-chip | Silicon Labs Series 2 DBUS Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L477) | [`silabs,dbus-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs,dbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl) |
| PWM | on-chip | Silicon Labs TIMER PWM[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L293) | [`silabs,timer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs,timer-pwm.md#std-dtcompatible-silabs-timer-pwm) |
| on-chip | Silicon Labs LETIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L517) | [`silabs,letimer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs,letimer-pwm.md#std-dtcompatible-silabs-letimer-pwm) |
| Regulator | on-chip | Silicon Labs Series 2 DC-DC converter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L533) | [`silabs,series2-dcdc`](../../../../../build/dts/api/bindings/regulator/silabs,series2-dcdc.md#std-dtcompatible-silabs-series2-dcdc) |
| on-board | Fixed voltage regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg24_rb4187c/xg24_rb4187c.dts?plain=1#L68) | [`regulator-fixed`](../../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| RTC | on-chip | Silicon Labs Series 2 Sleeptimer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L418) | [`silabs,gecko-stimer`](../../../../../build/dts/api/bindings/rtc/silabs,gecko-stimer.md#std-dtcompatible-silabs-gecko-stimer) |
| Sensors | on-board | Silicon Labs Si7006/13/20/21 RHT Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg24_rb4187c/xg24_rb4187c.dts?plain=1#L178) | [`silabs,si7006`](../../../../../build/dts/api/bindings/sensor/silabs,si7006.md#std-dtcompatible-silabs-si7006) |
| Serial controller | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L364) | [`silabs,usart-uart`](../../../../../build/dts/api/bindings/serial/silabs,usart-uart.md#std-dtcompatible-silabs-usart-uart) |
| SPI | on-chip | Silicon Labs Series 2 EUSART [1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L382)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L373) | [`silabs,eusart-spi`](../../../../../build/dts/api/bindings/spi/silabs,eusart-spi.md#std-dtcompatible-silabs-eusart-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L189) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Silicon Labs TIMER[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L284) | [`silabs,series2-timer`](../../../../../build/dts/api/bindings/timer/silabs,series2-timer.md#std-dtcompatible-silabs-series2-timer) |
| on-chip | Silicon Labs Series 2 BURTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L391) | [`silabs,gecko-burtc`](../../../../../build/dts/api/bindings/timer/silabs,gecko-burtc.md#std-dtcompatible-silabs-gecko-burtc) |
| on-chip | Silicon Labs LETIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L510) | [`silabs,series2-letimer`](../../../../../build/dts/api/bindings/timer/silabs,series2-letimer.md#std-dtcompatible-silabs-series2-letimer) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L492)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L501) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs,gecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### System Clock

The EFR32MG24 SoC is configured to use the HFRCODPLL oscillator at 78 MHz as the system clock,
locked to the 39 MHz external crystal oscillator on the board.

### Serial Port

The EFR32MG24 SoC has one USART and two EUSARTs.
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

The `xg24_rb4187c` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[openocd](../../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

### Flashing

Connect the BRD4002A board with a mounted BRD4187C radio module to your host
computer using the USB port.

Here is an example for the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b xg24_rb4187c samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! xg24_rb4187c
```

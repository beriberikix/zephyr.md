---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/radio_boards/xg23_rb4210a/doc/index.html
original_path: boards/silabs/radio_boards/xg23_rb4210a/doc/index.html
---

# EFR32xG23 868-915 MHz 20 dBm (xG23-RB4210A)

Board Overview

[![../../../../../_images/efr32zg23-xg23-rb4210a.jpg](../../../../../_images/efr32zg23-xg23-rb4210a.jpg)
](../../../../../_images/efr32zg23-xg23-rb4210a.jpg)

EFR32xG23 868-915 MHz 20 dBm (xG23-RB4210A)

Name:
:   `xg23_rb4210a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32zg23b020f512im48

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/xg23_rb4210a/doc/index.rst/../..)

## Overview

The EFR32ZG23 Radio Board is the radio board delivered with
[xG23-PK6068A Website](https://www.silabs.com/development-tools/wireless/efr32xg23-pro-kit-20-dbm). It contains a Wireless System-On-Chip from the
EFR32ZG23 family built on an ARM Cortex®-M33 processor with excellent low
power capabilities.

The BRD4210A a.k.a. xG23-RB4210A radio board plugs into the Wireless Pro Kit
Mainboard BRD4002A and is supported as one of [Radio Boards](../../index.md#silabs-radio-boards).

## Hardware

- EFR32ZG23B020F512IM48 SoC
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 512 kB
- RAM: 64 kB
- Transmit power: up to +20 dBm
- Operation frequency: 868-915 MHz
- Crystals for LFXO (32.768 kHz) and HFXO (39 MHz).
- Silicon Labs Si7021 relative humidity and temperature sensor
- Low-power 128x128 pixel Memory LCD
- Macronix ultra low power 8-Mbit SPI flash (MX25R8035F)

For more information about the EFR32ZG23 SoC and BRD4210A board, refer to these
documents:

- [EFR32ZG23 Website](https://www.silabs.com/wireless/z-wave/800-series-modem-soc)
- [EFR32ZG23 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32zg23-datasheet.pdf)
- [EFR32xG23 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efr32xg23-rm.pdf)
- [xG23-PK6068A Website](https://www.silabs.com/development-tools/wireless/efr32xg23-pro-kit-20-dbm)
- [BRD4210A User Guide](https://www.silabs.com/documents/public/user-guides/ug507-brd4210a-user-guide.pdf)

### Supported Features

The `xg23_rb4210a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `xg23_rb4210a/efr32zg23b020f512im48` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L148) | [`arm,cortex-m33`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Silicon Labs Series 2 IADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L554) | [`silabs,gecko-iadc`](../../../../../build/dts/api/bindings/adc/silabs%2Cgecko-iadc.md#std-dtcompatible-silabs-gecko-iadc) |
| Clock control | on-chip | Silicon Labs Series 2 CMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L205) | [`silabs,series-clock`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries-clock.md#std-dtcompatible-silabs-series-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L214) | [`fixed-clock`](../../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Silicon Labs Series 2 HFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L221) | [`silabs,hfxo`](../../../../../build/dts/api/bindings/clock/silabs%2Chfxo.md#std-dtcompatible-silabs-hfxo) |
| on-chip | Silicon Labs Series 2 LFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L233) | [`silabs,series2-lfxo`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-lfxo.md#std-dtcompatible-silabs-series2-lfxo) |
| on-chip | Silicon Labs Series 2 HFRCODPLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L244) | [`silabs,series2-hfrcodpll`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-hfrcodpll.md#std-dtcompatible-silabs-series2-hfrcodpll) |
| on-chip | Silicon Labs Series 2 HFRCOEM23[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L251) | [`silabs,series2-hfrcoem23`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-hfrcoem23.md#std-dtcompatible-silabs-series2-hfrcoem23) |
| on-chip | Silicon Labs Series 2 LFRCO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L258) | [`silabs,series2-lfrco`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-lfrco.md#std-dtcompatible-silabs-series2-lfrco) |
| on-chip | Generic fixed factor clock provider[22 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L22) | [`fixed-factor-clock`](../../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Comparator | on-chip | Silicon Labs Series 2 ACMP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L570) | [`silabs,acmp`](../../../../../build/dts/api/bindings/comparator/silabs%2Cacmp.md#std-dtcompatible-silabs-acmp) |
| Cryptographic accelerator | on-chip | Silicon Labs Series 2 SE Mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L418) | [`silabs,gecko-semailbox`](../../../../../build/dts/api/bindings/crypto/silabs%2Cgecko-semailbox.md#std-dtcompatible-silabs-gecko-semailbox) |
| Debug | on-chip | Silicon Labs Packet Trace Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/efr32xg23.dtsi?plain=1#L24) | [`silabs,pti`](../../../../../build/dts/api/bindings/debug/silabs%2Cpti.md#std-dtcompatible-silabs-pti) |
| on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L160) | [`arm,armv8m-itm`](../../../../../build/dts/api/bindings/debug/arm%2Carmv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| Display | on-board | Sharp LS0XX memory display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg23_rb4210a/xg23_rb4210a.dts?plain=1#L147) | [`sharp,ls0xx`](../../../../../build/dts/api/bindings/display/sharp%2Cls0xx.md#std-dtcompatible-sharp-ls0xx) |
| DMA | on-chip | Silicon Labs Series 2 LDMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L513) | [`silabs,ldma`](../../../../../build/dts/api/bindings/dma/silabs%2Cldma.md#std-dtcompatible-silabs-ldma) |
| Flash controller | on-chip | Silicon Labs Series 2 MSC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L279) | [`silabs,series2-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Cseries2-flash-controller.md#std-dtcompatible-silabs-series2-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L459) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L470) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L426)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L437) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg23_rb4210a/xg23_rb4210a.dts?plain=1#L50) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg23_rb4210a/xg23_rb4210a.dts?plain=1#L36) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L287) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg23_rb4210a/xg23_rb4210a.dts?plain=1#L229) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg23_rb4210a/xg23_rb4210a.dts?plain=1#L158) | [`jedec,spi-nor`](../../../../../build/dts/api/bindings/mtd/jedec%2Cspi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Networking | on-chip | Silicon Labs Series 2 Radio Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/efr32xg23.dtsi?plain=1#L11) | [`silabs,series2-radio`](../../../../../build/dts/api/bindings/net/wireless/silabs%2Cseries2-radio.md#std-dtcompatible-silabs-series2-radio) |
| Pin control | on-chip | Silicon Labs Series 2 DBUS Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L507) | [`silabs,dbus-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Cdbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl) |
| PWM | on-chip | Silicon Labs TIMER PWM[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L303) | [`silabs,timer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Ctimer-pwm.md#std-dtcompatible-silabs-timer-pwm) |
| on-chip | Silicon Labs LETIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L547) | [`silabs,letimer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Cletimer-pwm.md#std-dtcompatible-silabs-letimer-pwm) |
| Regulator | on-chip | Silicon Labs Series 2 DC-DC converter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L563) | [`silabs,series2-dcdc`](../../../../../build/dts/api/bindings/regulator/silabs%2Cseries2-dcdc.md#std-dtcompatible-silabs-series2-dcdc) |
| on-board | Fixed voltage regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg23_rb4210a/xg23_rb4210a.dts?plain=1#L66) | [`regulator-fixed`](../../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| RTC | on-chip | Silicon Labs Series 2 Sleeptimer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L448) | [`silabs,gecko-stimer`](../../../../../build/dts/api/bindings/rtc/silabs%2Cgecko-stimer.md#std-dtcompatible-silabs-gecko-stimer) |
| Sensors | on-board | Silicon Labs Si7006/13/20/21 RHT Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg23_rb4210a/xg23_rb4210a.dts?plain=1#L176) | [`silabs,si7006`](../../../../../build/dts/api/bindings/sensor/silabs%2Csi7006.md#std-dtcompatible-silabs-si7006) |
| Serial controller | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L374) | [`silabs,usart-uart`](../../../../../build/dts/api/bindings/serial/silabs%2Cusart-uart.md#std-dtcompatible-silabs-usart-uart) |
| on-chip | Silicon Labs Series 2 EUSART [1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L383) | [`silabs,eusart-uart`](../../../../../build/dts/api/bindings/serial/silabs%2Ceusart-uart.md#std-dtcompatible-silabs-eusart-uart) |
| SPI | on-chip | Silicon Labs Series 2 EUSART [1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L392)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L401) | [`silabs,eusart-spi`](../../../../../build/dts/api/bindings/spi/silabs%2Ceusart-spi.md#std-dtcompatible-silabs-eusart-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L199) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Silicon Labs TIMER[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L294) | [`silabs,series2-timer`](../../../../../build/dts/api/bindings/timer/silabs%2Cseries2-timer.md#std-dtcompatible-silabs-series2-timer) |
| on-chip | Silicon Labs Series 2 BURTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L410) | [`silabs,gecko-burtc`](../../../../../build/dts/api/bindings/timer/silabs%2Cgecko-burtc.md#std-dtcompatible-silabs-gecko-burtc) |
| on-chip | Silicon Labs LETIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L540) | [`silabs,series2-letimer`](../../../../../build/dts/api/bindings/timer/silabs%2Cseries2-letimer.md#std-dtcompatible-silabs-series2-letimer) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L522)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg23/xg23.dtsi?plain=1#L531) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs%2Cgecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### Connections and IOs

In the following table, the column **Name** contains Pin names. For example, PA2
means Pin number 2 on PORTA, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PA8 | EUSART0\_TX | UART Console TX |
| PA9 | EUSART0\_RX | UART Console RX |
| PB0 | GPIO | Board Controller Enable |
| PB1 | GPIO | Push Button 0 |
| PB2 | GPIO | LED0 |
| PB3 | GPIO | Push Button 1 |
| PC1 | EUSART1\_TX | Display/Flash SPI MOSI |
| PC2 | EUSART1\_RX | Flash SPI MISO |
| PC3 | EUSART1\_CLK | Display/Flash SPI Clock |
| PC4 | GPIO | Flash SPI Chip Select |
| PC5 | I2C0\_SCL | Si7021 I2C Clock |
| PC6 | GPIO | Display COM Inversion |
| PC7 | I2C0\_SDA | Si7021 I2C Data |
| PC8 | GPIO | Display SPI Chip Select |
| PC9 | GPIO | Display/Si7021 Enable |
| PD3 | GPIO | LED1 |

The default configuration can be found in
[boards/silabs/radio\_boards/xg23\_rb4210a/xg23\_rb4210a\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg23_rb4210a/xg23_rb4210a_defconfig)

### System Clock

The EFR32ZG23 SoC is configured to use the 39 MHz external oscillator on the
board.

### Serial Port

The EFR32ZG23 SoC has one USART and three EUSARTs.
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

The `xg23_rb4210a` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[openocd](../../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **silabs\_commander** | ✅ |  |  |  |  |

### Flashing

Connect the BRD4002A board with a mounted BRD4210A radio module to your host
computer using the USB port.

Here is an example for the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b xg23_rb4210a samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! xg23_rb4210a/efr32zg23b020f512im48
```

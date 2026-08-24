---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/radio_boards/siwx917_rb4342a/doc/index.html
original_path: boards/silabs/radio_boards/siwx917_rb4342a/doc/index.html
---

# SiWx917 Wi-Fi 6 and Bluetooth LE 8 MB Flash + 8 MB ext PSRAM Radio Board (SLWRB4342A)

Board Overview

[![../../../../../_images/siwx917_rb4342a.webp](https://docs.zephyrproject.org/4.2.0/_images/siwx917_rb4342a.webp)
](https://docs.zephyrproject.org/4.2.0/_images/siwx917_rb4342a.webp)

SiWx917 Wi-Fi 6 and Bluetooth LE 8 MB Flash + 8 MB ext PSRAM Radio Board (SLWRB4342A)

Name:
:   `siwx917_rb4342a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   siwg917m111mgtba

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/siwx917_rb4342a/doc/index.rst/../..)

## Overview

The SiWx917-RB4342A (aka BRD4342A) radio board provides support for the Silicon
Labs SiWG917 SoC. This board cannot be used stand-alone and requires a a
[Wireless Pro Kit](https://www.silabs.com/development-tools/wireless/wireless-pro-kit-mainboard) Mainboard (Si-MB4002A aka BRD4002A), for power, debug
options etc.

SiWG917 is an ultra-low power SoC that includes hardware support for Single-Band
Wi-Fi 6 + Bluetooth LE 5.4, Matter…

## Hardware

For more information about the SiWG917 SoC and BRD4342A board, refer to these
documents:

- [SiWG917 Website](https://www.silabs.com/wireless/wi-fi/siwx917-wireless-socs)
- [SiWG917 Datasheet](https://www.silabs.com/documents/public/data-sheets/siwg917-datasheet.pdf)
- [SiWG917 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/siw917x-family-rm.pdf)
- [BRD4342A Website](https://www.silabs.com/development-tools/wireless/wi-fi/siwx91x-rb4342a-wifi-6-bluetooth-le-soc-radio-board)
- [BRD4342A User Guide](https://www.silabs.com/documents/public/user-guides/ug564-brd4342a-user-guide.pdf)

### Supported Features

The `siwx917_rb4342a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `siwx917_rb4342a/siwg917m111mgtba` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L24) | [`arm,cortex-m4f`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Silicon Labs siwx91x ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L401) | [`silabs,siwx91x-adc`](../../../../../build/dts/api/bindings/adc/silabs%2Csiwx91x-adc.md#std-dtcompatible-silabs-siwx91x-adc) |
| Bluetooth | on-chip | Bluetooth HCI on Silabs boards[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L79) | [`silabs,siwx91x-bt-hci`](../../../../../build/dts/api/bindings/bluetooth/silabs%2Csiwx91x-bt-hci.md#std-dtcompatible-silabs-siwx91x-bt-hci) |
| Clock control | on-chip | Clocks embedded on Silabs SiWx91x chips[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L91) | [`silabs,siwx91x-clock`](../../../../../build/dts/api/bindings/clock/silabs%2Csiwx91x-clock.md#std-dtcompatible-silabs-siwx91x-clock) |
| DMA | on-chip | Silabs SiWx91x DMA[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L293) | [`silabs,siwx91x-dma`](../../../../../build/dts/api/bindings/dma/silabs%2Csiwx91x-dma.md#std-dtcompatible-silabs-siwx91x-dma) |
| Flash controller | on-chip | Silicon Labs SiWx91x flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L106) | [`silabs,siwx91x-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Csiwx91x-flash-controller.md#std-dtcompatible-silabs-siwx91x-flash-controller) |
| GPIO & Headers | on-chip | Silabs SiWx91x GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L162) | [`silabs,siwx91x-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Csiwx91x-gpio.md#std-dtcompatible-silabs-siwx91x-gpio) |
| on-chip | Silabs SiWx91x GPIO Port[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L173) | [`silabs,siwx91x-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Csiwx91x-gpio-port.md#std-dtcompatible-silabs-siwx91x-gpio-port) |
| on-chip | Silabs SiWx91x UULP (ultra ultra low power) GPIO Port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L247) | [`silabs,siwx91x-gpio-uulp`](../../../../../build/dts/api/bindings/gpio/silabs%2Csiwx91x-gpio-uulp.md#std-dtcompatible-silabs-siwx91x-gpio-uulp) |
| I2C | on-chip | Synopsys DesignWare I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L260)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L271) | [`snps,designware-i2c`](../../../../../build/dts/api/bindings/i2c/snps%2Cdesignware-i2c.md#std-dtcompatible-snps-designware-i2c) |
| I2S | on-chip | Silabs siwx91x I2S (Inter-IC sound interface)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L374) | [`silabs,siwx91x-i2s`](../../../../../build/dts/api/bindings/i2s/silabs%2Csiwx91x-i2s.md#std-dtcompatible-silabs-siwx91x-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/siwx917_rb4342a/siwx917_rb4342a.dts?plain=1#L42) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/siwx917_rb4342a/siwx917_rb4342a.dts?plain=1#L34) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | Silicon Labs QSPI (Quad Serial Protocol Interface) memory controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L119) | [`silabs,siwx91x-qspi-memory`](../../../../../build/dts/api/bindings/memory-controllers/silabs%2Csiwx91x-qspi-memory.md#std-dtcompatible-silabs-siwx91x-qspi-memory) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L112) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/siwx917_rb4342a/siwx917_rb4342a.dts?plain=1#L100) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Silicon Labs SiWx91x NWP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L75) | [`silabs,siwx91x-nwp`](../../../../../build/dts/api/bindings/net/wireless/silabs%2Csiwx91x-nwp.md#std-dtcompatible-silabs-siwx91x-nwp) |
| Pin control | on-chip | Silabs SiWx91x Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L101) | [`silabs,siwx91x-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Csiwx91x-pinctrl.md#std-dtcompatible-silabs-siwx91x-pinctrl) |
| PWM | on-chip | Silabs siwx91x PWM Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L320) | [`silabs,siwx91x-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Csiwx91x-pwm.md#std-dtcompatible-silabs-siwx91x-pwm) |
| RNG | on-chip | Hardware Random Number Generator embedded on Silabs SiWx91x chips[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L157) | [`silabs,siwx91x-rng`](../../../../../build/dts/api/bindings/rng/silabs%2Csiwx91x-rng.md#std-dtcompatible-silabs-siwx91x-rng) |
| RTC | on-chip | Silabs Siwx91x RTC (Real-Time Counter)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L333) | [`silabs,siwx91x-rtc`](../../../../../build/dts/api/bindings/rtc/silabs%2Csiwx91x-rtc.md#std-dtcompatible-silabs-siwx91x-rtc) |
| on-chip | Silicon Labs Series 2 Sleeptimer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L353) | [`silabs,gecko-stimer`](../../../../../build/dts/api/bindings/rtc/silabs%2Cgecko-stimer.md#std-dtcompatible-silabs-gecko-stimer) |
| Sensors | on-board | Silicon Labs Si7006/13/20/21 RHT Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/siwx917_rb4342a/siwx917_rb4342a.dts?plain=1#L93) | [`silabs,si7006`](../../../../../build/dts/api/bindings/sensor/silabs%2Csi7006.md#std-dtcompatible-silabs-si7006) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L127)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L137) | [`ns16550`](../../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| SPI | on-chip | Silabs GSPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L363) | [`silabs,gspi`](../../../../../build/dts/api/bindings/spi/silabs%2Cgspi.md#std-dtcompatible-silabs-gspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L53) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Silabs SiWx91x Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L342) | [`silabs,siwx91x-wdt`](../../../../../build/dts/api/bindings/watchdog/silabs%2Csiwx91x-wdt.md#std-dtcompatible-silabs-siwx91x-wdt) |
| Wi-Fi | on-chip | Silabs SiWx91x SoC WiFi[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/siwg917.dtsi?plain=1#L84) | [`silabs,siwx91x-wifi`](../../../../../build/dts/api/bindings/wifi/silabs%2Csiwx91x-wifi.md#std-dtcompatible-silabs-siwx91x-wifi) |

Refer to the [SiWx917 Wi-Fi Features (Alpha)](../../common/wifi.md#siwx917-wifi-features) page for a list of supported Wi-Fi features.

## Programming and Debugging

### Flashing

Applications for the `siwx917_rb4342a` board can be built in the usual
way. The flash method requires on [Simplicity Commander](https://www.silabs.com/developer-tools/simplicity-studio/simplicity-commander) installed on the host.

Then, connect the BRD4002A board with a mounted BRD4342A radio module to your
host computer using the USB port.

Here is an example for the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b siwx917_rb4342a samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! siwx917_rb4342a
```

### Debugging

Debuggning relies on JLink tool. JLink is not able to flash the firmware. So
debug session has to be done in two steps. `west flash` will flahs the
firmware using Simplicity Commander. Then `west attach` will use JLink to
attach to the board. The Zephyr image may has already booted when user runs
`west attach`. User may execute `monitor reset` in the gdb prompt to reset
the board.

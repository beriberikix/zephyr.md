---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/radio_boards/xg29_rb4412a/doc/index.html
original_path: boards/silabs/radio_boards/xg29_rb4412a/doc/index.html
---

# EFR32xG29 2.4 GHz 8 dBm Buck (xG29-RB4412A)

Board Overview

Name:
:   `xg29_rb4412a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32mg29b140f1024im40

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/xg29_rb4412a/doc/index.rst/../..)

## Overview

The xG24-RB4412A radio board provides support for the Silicon Labs EFR32MG29 SoC.

## Hardware

- EFR32MG29B140F1024IM40 SoC
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 1024 kB
- RAM: 256 kB
- Transmit power: up to +8 dBm
- Operation frequency: 2.4 GHz
- Crystal oscillators for LFXO (32.768 kHz) and HFXO (38.4 MHz)

### Supported Features

The `xg29_rb4412a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `xg29_rb4412a/efr32mg29b140f1024im40` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L145) | [`arm,cortex-m33`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Silicon Labs Series 2 IADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L532) | [`silabs,gecko-iadc`](../../../../../build/dts/api/bindings/adc/silabs%2Cgecko-iadc.md#std-dtcompatible-silabs-gecko-iadc) |
| Bluetooth | on-chip | Silicon Labs Series 2 Bluetooth HCI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/efr32xg29.dtsi?plain=1#L24) | [`silabs,bt-hci-efr32`](../../../../../build/dts/api/bindings/bluetooth/silabs%2Cbt-hci-efr32.md#std-dtcompatible-silabs-bt-hci-efr32) |
| Clock control | on-chip | Silicon Labs Series 2 CMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L191) | [`silabs,series-clock`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries-clock.md#std-dtcompatible-silabs-series-clock) |
| on-chip | Silicon Labs Series 2 HFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L200) | [`silabs,hfxo`](../../../../../build/dts/api/bindings/clock/silabs%2Chfxo.md#std-dtcompatible-silabs-hfxo) |
| on-chip | Silicon Labs Series 2 HFRCODPLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L212) | [`silabs,series2-hfrcodpll`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-hfrcodpll.md#std-dtcompatible-silabs-series2-hfrcodpll) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L221) | [`fixed-clock`](../../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Silicon Labs Series 2 LFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L228) | [`silabs,series2-lfxo`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-lfxo.md#std-dtcompatible-silabs-series2-lfxo) |
| on-chip | Silicon Labs Series 2 LFRCO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L241) | [`silabs,series2-lfrco`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-lfrco.md#std-dtcompatible-silabs-series2-lfrco) |
| on-chip | Generic fixed factor clock provider[18 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L22) | [`fixed-factor-clock`](../../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Comparator | on-chip | Silicon Labs Series 2 ACMP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L542) | [`silabs,acmp`](../../../../../build/dts/api/bindings/comparator/silabs%2Cacmp.md#std-dtcompatible-silabs-acmp) |
| Cryptographic accelerator | on-chip | Silicon Labs Series 2 SE Mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L550) | [`silabs,gecko-semailbox`](../../../../../build/dts/api/bindings/crypto/silabs%2Cgecko-semailbox.md#std-dtcompatible-silabs-gecko-semailbox) |
| Debug | on-chip | Silicon Labs Packet Trace Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/efr32xg29.dtsi?plain=1#L29) | [`silabs,pti`](../../../../../build/dts/api/bindings/debug/silabs%2Cpti.md#std-dtcompatible-silabs-pti) |
| on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L157) | [`arm,armv8m-itm`](../../../../../build/dts/api/bindings/debug/arm%2Carmv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| Display | on-board | Sharp LS0XX memory display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg29_rb4412a/xg29_rb4412a.dts?plain=1#L172) | [`sharp,ls0xx`](../../../../../build/dts/api/bindings/display/sharp%2Cls0xx.md#std-dtcompatible-sharp-ls0xx) |
| DMA | on-chip | Silicon Labs Series 2 LDMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L330) | [`silabs,ldma`](../../../../../build/dts/api/bindings/dma/silabs%2Cldma.md#std-dtcompatible-silabs-ldma) |
| Flash controller | on-chip | Silicon Labs Series 2 MSC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L266) | [`silabs,series2-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Cseries2-flash-controller.md#std-dtcompatible-silabs-series2-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L281) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L291) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L447)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L459) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg29_rb4412a/xg29_rb4412a.dts?plain=1#L61) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg29_rb4412a/xg29_rb4412a.dts?plain=1#L39) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg29_rb4412a/xg29_rb4412a.dts?plain=1#L53) | [`pwm-leds`](../../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L274) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg29_rb4412a/xg29_rb4412a.dts?plain=1#L246) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg29_rb4412a/xg29_rb4412a.dts?plain=1#L160) | [`jedec,spi-nor`](../../../../../build/dts/api/bindings/mtd/jedec%2Cspi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Networking | on-chip | Silicon Labs Series 2 Radio Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/efr32xg29.dtsi?plain=1#L11) | [`silabs,series2-radio`](../../../../../build/dts/api/bindings/net/wireless/silabs%2Cseries2-radio.md#std-dtcompatible-silabs-series2-radio) |
| Pin control | on-chip | Silicon Labs Series 2 DBUS Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L324) | [`silabs,dbus-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Cdbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl) |
| PWM | on-chip | Silicon Labs TIMER PWM[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L349) | [`silabs,timer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Ctimer-pwm.md#std-dtcompatible-silabs-timer-pwm) |
| on-chip | Silicon Labs LETIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L525) | [`silabs,letimer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Cletimer-pwm.md#std-dtcompatible-silabs-letimer-pwm) |
| Regulator | on-chip | Silicon Labs Series 2 DC-DC converter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L471) | [`silabs,series2-dcdc`](../../../../../build/dts/api/bindings/regulator/silabs%2Cseries2-dcdc.md#std-dtcompatible-silabs-series2-dcdc) |
| on-board | Fixed voltage regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg29_rb4412a/xg29_rb4412a.dts?plain=1#L77) | [`regulator-fixed`](../../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| RTC | on-chip | Silicon Labs Series 2 Sleeptimer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L497) | [`silabs,gecko-stimer`](../../../../../build/dts/api/bindings/rtc/silabs%2Cgecko-stimer.md#std-dtcompatible-silabs-gecko-stimer) |
| Sensors | on-board | Silicon Labs Si7006/13/20/21 RHT Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg29_rb4412a/xg29_rb4412a.dts?plain=1#L144) | [`silabs,si7006`](../../../../../build/dts/api/bindings/sensor/silabs%2Csi7006.md#std-dtcompatible-silabs-si7006) |
| Serial controller | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L429)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L420) | [`silabs,usart-uart`](../../../../../build/dts/api/bindings/serial/silabs%2Cusart-uart.md#std-dtcompatible-silabs-usart-uart) |
| SPI | on-chip | Silicon Labs Series 2 EUSART [1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L488)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L479) | [`silabs,eusart-spi`](../../../../../build/dts/api/bindings/spi/silabs%2Ceusart-spi.md#std-dtcompatible-silabs-eusart-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L185) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Silicon Labs TIMER[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L340) | [`silabs,series2-timer`](../../../../../build/dts/api/bindings/timer/silabs%2Cseries2-timer.md#std-dtcompatible-silabs-series2-timer) |
| on-chip | Silicon Labs Series 2 BURTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L438) | [`silabs,gecko-burtc`](../../../../../build/dts/api/bindings/timer/silabs%2Cgecko-burtc.md#std-dtcompatible-silabs-gecko-burtc) |
| on-chip | Silicon Labs LETIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L518) | [`silabs,series2-letimer`](../../../../../build/dts/api/bindings/timer/silabs%2Cseries2-letimer.md#std-dtcompatible-silabs-series2-letimer) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg29/xg29.dtsi?plain=1#L508) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs%2Cgecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

## Programming and Debugging

The `xg29_rb4412a` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **silabs\_commander** | ✅ |  |  |  |  |

Applications for the `xg29_rb4412a` board target can be built, flashed, and debugged in the
usual way. See [Building an Application](../../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../../develop/application/index.md#application-run) for more details on
building and running.

### Flashing

As an example, this section shows how to build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

To build and program the sample to the xG24-RB4412A, complete the following steps:

First, plug the xG24-RB4412A to a compatible mainboard and connect the mainboard to your computer
using the USB port on the left side.
Next, build and flash the sample by running the following command:

```shell
# From the root of the zephyr repository
west build -b xg29_rb4412a samples/hello_world
west flash
```

`west flash` will by default use SEGGER JLink. Make sure that the JLinkExe binary is available on
the PATH. Alternatively, use `west flash -r silabs_commander` to use Simplicity Commander to flash.
In this case, make sure that the commander binary is available on PATH.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! xg29_rb4412a
```

### Bluetooth

To use the BLE function, run the command below to retrieve necessary binary
blobs from the SiLabs HAL repository.

```shell
west blobs fetch hal_silabs
```

Then build the Zephyr kernel and a Bluetooth sample with the following
command. The [Observer](../../../../../samples/bluetooth/observer/README.md#bluetooth_observer "Scan for Bluetooth devices nearby and print their information.") sample application is used in
this example.

```shell
# From the root of the zephyr repository
west build -b xg29_rb4412a samples/bluetooth/observer
```

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/sparkfun/thing_plus_matter_mgm240p/doc/index.html
original_path: boards/sparkfun/thing_plus_matter_mgm240p/doc/index.html
---

# Thing Plus Matter

Board Overview

[![../../../../_images/sparkfun_thing_plus_matter_mgm240p.jpg](https://docs.zephyrproject.org/4.2.0/_images/sparkfun_thing_plus_matter_mgm240p.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/sparkfun_thing_plus_matter_mgm240p.jpg)

Thing Plus Matter

Name:
:   `sparkfun_thing_plus_matter_mgm240p`

Vendor:
:   SparkFun Electronics

Architecture:
:   arm

SoC:
:   mgm240pb32vna

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sparkfun/thing_plus_matter_mgm240p/doc/index.rst/../..)

## Overview

The MGM240P Mighty Sparkfun Think Plus Matter contains
a Wireless System-On-Chip from the EFR32MG24 family built on an
ARM Cortex®-M33F processor with excellent low power capabilities.

## Hardware

- Based on the Series 2 EFR32MG24 SoC
- CPU core: 32-bit ARM® Cortex®-M33 core at 39 MHz
- Flash memory: 1536 kB
- RAM: 256 kB
- Supports Multiple 802.15.4 Wireless Protocols (Zigbee and OpenThread)
- Bluetooth Low Energy 5.3
- Crystals for LFXO (32 kHz) and HFXO (39 MHz).

For more information about the EFR32MG24 SoC and BRD2601B board, refer to these
documents:

- [EFR32MG24 Website](https://www.silabs.com/wireless/zigbee/efr32mg24-series-2-socs#)
- [EFR32MG24 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg24-datasheet.pdf)
- [EFR32xG24 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efr32xg24-rm.pdf)
- [MGM240P Datasheet](https://cdn.sparkfun.com/assets/1/4/5/e/5/MGM240P-Datasheet.pdf)
- [MGM240P Schematics](https://cdn.sparkfun.com/assets/0/f/8/4/9/Thing_Plus_MGM240P.pdf)

### Supported Features

The `sparkfun_thing_plus_matter_mgm240p` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sparkfun_thing_plus_matter_mgm240p/mgm240pb32vna` target

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
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L407) | [`silabs,gecko-i2c`](../../../../build/dts/api/bindings/i2c/silabs,gecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sparkfun/thing_plus_matter_mgm240p/sparkfun_thing_plus_matter_mgm240p.dts?plain=1#L36) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sparkfun/thing_plus_matter_mgm240p/sparkfun_thing_plus_matter_mgm240p.dts?plain=1#L44) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Miscellaneous | on-board | GPIO Wake Up Trigger for EFR32BG22/EFR32BG27[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sparkfun/thing_plus_matter_mgm240p/sparkfun_thing_plus_matter_mgm240p.dts?plain=1#L53) | `silabs,gecko-wake-up-trigger` |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L277) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sparkfun/thing_plus_matter_mgm240p/sparkfun_thing_plus_matter_mgm240p.dts?plain=1#L149) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Silicon Labs Series 2 Radio Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L11) | [`silabs,series2-radio`](../../../../build/dts/api/bindings/net/wireless/silabs,series2-radio.md#std-dtcompatible-silabs-series2-radio) |
| Pin control | on-chip | Silicon Labs Series 2 DBUS Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L477) | [`silabs,dbus-pinctrl`](../../../../build/dts/api/bindings/pinctrl/silabs,dbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl) |
| PWM | on-chip | Silicon Labs TIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L293)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L309) | [`silabs,timer-pwm`](../../../../build/dts/api/bindings/pwm/silabs,timer-pwm.md#std-dtcompatible-silabs-timer-pwm) |
| on-chip | Silicon Labs LETIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L517) | [`silabs,letimer-pwm`](../../../../build/dts/api/bindings/pwm/silabs,letimer-pwm.md#std-dtcompatible-silabs-letimer-pwm) |
| Regulator | on-chip | Silicon Labs Series 2 DC-DC converter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L533) | [`silabs,series2-dcdc`](../../../../build/dts/api/bindings/regulator/silabs,series2-dcdc.md#std-dtcompatible-silabs-series2-dcdc) |
| RTC | on-chip | Silicon Labs Series 2 Sleeptimer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L418) | [`silabs,gecko-stimer`](../../../../build/dts/api/bindings/rtc/silabs,gecko-stimer.md#std-dtcompatible-silabs-gecko-stimer) |
| Serial controller | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L364) | [`silabs,usart-uart`](../../../../build/dts/api/bindings/serial/silabs,usart-uart.md#std-dtcompatible-silabs-usart-uart) |
| SPI | on-chip | Silicon Labs Series 2 EUSART [1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L382)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L373) | [`silabs,eusart-spi`](../../../../build/dts/api/bindings/spi/silabs,eusart-spi.md#std-dtcompatible-silabs-eusart-spi) |
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
| PA8 | GPIO | LED0 |
| PA5 | USART0\_TX | UART Console EFM\_BC\_TX US0\_TX |
| PA6 | USART0\_RX | UART Console EFM\_BC\_RX US0\_RX |

The default configuration can be found in
[boards/sparkfun/thing\_plus\_matter\_mgm240p/sparkfun\_thing\_plus\_matter\_mgm240p\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sparkfun/thing_plus_matter_mgm240p/sparkfun_thing_plus_matter_mgm240p_defconfig)

### System Clock

The EFR32MG24 SoC is configured to use the 39 MHz external oscillator on the
board.

### Serial Port

The EFR32MG24 SoC has one USART and two EUSARTs.
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

The `sparkfun_thing_plus_matter_mgm240p` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Note

Before using the kit the first time, you should update the J-Link firmware
in Simplicity Studio.

### Flashing

The sample application [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b sparkfun_thing_plus_mgm240p samples/hello_world
```

Connect the sparkfun\_thing\_plus\_mgm240p to your host computer using the USB port and you
should see a USB connection.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you’ll see the following message on the corresponding serial port
terminal session:

```shell
Hello World! _sparkfun_thing_plus_matter_mgm240p
```

### Bluetooth

To use the BLE function, run the command below to retrieve necessary binary
blobs from the SiLabs HAL repository.

```shell
west blobs fetch silabs
```

Then build the Zephyr kernel and a Bluetooth sample with the following
command. The [Observer](../../../../samples/bluetooth/observer/README.md#bluetooth_observer "Scan for Bluetooth devices nearby and print their information.") sample application is used in
this example.

```shell
# From the root of the zephyr repository
west build -b sparkfun_thing_plus_matter_mgm240p samples/bluetooth/observer
```

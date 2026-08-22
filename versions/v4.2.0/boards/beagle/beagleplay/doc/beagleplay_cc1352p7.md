---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/beagle/beagleplay/doc/beagleplay_cc1352p7.html
original_path: boards/beagle/beagleplay/doc/beagleplay_cc1352p7.html
---

# BeaglePlay (CC1352)

Board Overview

[![../../../../_images/beagle_play.webp](../../../../_images/beagle_play.webp)
](../../../../_images/beagle_play.webp)

BeaglePlay (CC1352)

Name:
:   `beagleplay`

Vendor:
:   BeagleBoard.org Foundation

Architecture:
:   arm

SoC:
:   cc1352p7

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/beagle/beagleplay/doc/beagleplay_cc1352p7.rst/../..)

## Overview

BeagleBoard.org BeaglePlay is an open hardware single board computer based on a TI Sitara AM6254
quad-core ARM Cortex-A53 SoC with an external TI SimpleLink multi-standard CC1352P7 wireless MCU
providing long-range, low-power connectivity.

## Hardware

- Processors

  - TI Sitara AM6252 SoC

    - 4x ARM Cortex-A53
    - ARM Cortex-R5
    - ARM Cortex-M4
    - Dual-core 32-bit RISC Programmble Real-Time Unit (PRU)
  - TI SimpleLink CC1352P7 Wireless MCU

    - ARM Cortex-M4F programmable MCU
    - ARM Cortex-M0+ software-defined radio processor
- Memory

  - 2GB DDR4
  - 16GB eMMC flash
  - I2C EEPROM
- Wired connectivity

  - Gigabit Ethernet (RJ45)
  - Single-pair Ethernet with 5V/250mA PoDL output (RJ11)
  - HDMI
  - USB Type-A (host)
  - USB Type-C (client/power)
- Wireless connectivity

  - TI WL1807 2.4GHz/5GHz WiFi
  - BLE/SubG via CC1352P7
- Expansion

  - mikroBUS
  - Grove
  - QWIIC

BeaglePlay ARM Cortex-A53 CPUs typically run Linux, while the CC1352P7 Cortex-M4 typically runs Zephyr.

### Supported Features

The `beagleplay` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `beagleplay/cc1352p7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L23) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | TI CC13XX/CC26xx family ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L235) | [`ti,cc13xx-cc26xx-adc`](../../../../build/dts/api/bindings/adc/ti%2Ccc13xx-cc26xx-adc.md#std-dtcompatible-ti-cc13xx-cc26xx-adc) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L57) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Flash controller | on-chip | Texas Instruments CC13xx/CC26xx flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L85) | [`ti,cc13xx-cc26xx-flash-controller`](../../../../build/dts/api/bindings/flash_controller/ti%2Ccc13xx-cc26xx-flash-controller.md#std-dtcompatible-ti-cc13xx-cc26xx-flash-controller) |
| GPIO & Headers | on-chip | TI SimpleLink CC13xx / CC26xx GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L69) | [`ti,cc13xx-cc26xx-gpio`](../../../../build/dts/api/bindings/gpio/ti%2Ccc13xx-cc26xx-gpio.md#std-dtcompatible-ti-cc13xx-cc26xx-gpio) |
| I2C | on-chip | TI CC13xx / CC26xx I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L171) | [`ti,cc13xx-cc26xx-i2c`](../../../../build/dts/api/bindings/i2c/ti%2Ccc13xx-cc26xx-i2c.md#std-dtcompatible-ti-cc13xx-cc26xx-i2c) |
| IEEE 802.15.4 | on-chip | TI SimpleLink CC13xx / CC26xx IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L217) | [`ti,cc13xx-cc26xx-ieee802154`](../../../../build/dts/api/bindings/ieee802154/ti%2Ccc13xx-cc26xx-ieee802154.md#std-dtcompatible-ti-cc13xx-cc26xx-ieee802154) |
| on-chip | TI SimpleLink CC13xx / CC26xx IEEE 802.15.4 node (sub-GHz)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L222) | [`ti,cc13xx-cc26xx-ieee802154-subghz`](../../../../build/dts/api/bindings/ieee802154/ti%2Ccc13xx-cc26xx-ieee802154-subghz.md#std-dtcompatible-ti-cc13xx-cc26xx-ieee802154-subghz) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beagleplay/beagleplay_cc1352p7.dts?plain=1#L30) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-board | Skyworks SKY13317 pHEMT GaAs SP3T Antenna Switch[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beagleplay/beagleplay_cc1352p7.dts?plain=1#L55) | [`skyworks,sky13317`](../../../../build/dts/api/bindings/misc/skyworks%2Csky13317.md#std-dtcompatible-skyworks-sky13317) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L92) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc1352r7.dtsi?plain=1#L19) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | TI SimpleLink CC13xx / CC26xx radio[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L207) | [`ti,cc13xx-cc26xx-radio`](../../../../build/dts/api/bindings/net/wireless/ti%2Ccc13xx-cc26xx-radio.md#std-dtcompatible-ti-cc13xx-cc26xx-radio) |
| Pin control | on-chip | TI SimpleLink CC13xx / CC26xx Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L64) | [`ti,cc13xx-cc26xx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti%2Ccc13xx-cc26xx-pinctrl.md#std-dtcompatible-ti-cc13xx-cc26xx-pinctrl) |
| PWM | on-chip | TI SimpleLink CC13xx/CC26xx GPT timer PWM Controller Node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L106) | [`ti,cc13xx-cc26xx-timer-pwm`](../../../../build/dts/api/bindings/pwm/ti%2Ccc13xx-cc26xx-timer-pwm.md#std-dtcompatible-ti-cc13xx-cc26xx-timer-pwm) |
| RNG | on-chip | TI SimpleLink CC13xx / CC26xx TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L78) | [`ti,cc13xx-cc26xx-trng`](../../../../build/dts/api/bindings/rng/ti%2Ccc13xx-cc26xx-trng.md#std-dtcompatible-ti-cc13xx-cc26xx-trng) |
| RTC | on-chip | TI SimpleLink CC13xx/CC26xx RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L200) | [`ti,cc13xx-cc26xx-rtc-timer`](../../../../build/dts/api/bindings/rtc/ti%2Ccc13xx-cc26xx-rtc-timer.md#std-dtcompatible-ti-cc13xx-cc26xx-rtc-timer) |
| Serial controller | on-chip | TI SimpleLink CC13xx / CC26xx UART node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L155)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L163) | [`ti,cc13xx-cc26xx-uart`](../../../../build/dts/api/bindings/serial/ti%2Ccc13xx-cc26xx-uart.md#std-dtcompatible-ti-cc13xx-cc26xx-uart) |
| SPI | on-chip | TI SimpleLink CC13xx / CC26xx SPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L181) | [`ti,cc13xx-cc26xx-spi`](../../../../build/dts/api/bindings/spi/ti%2Ccc13xx-cc26xx-spi.md#std-dtcompatible-ti-cc13xx-cc26xx-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L46) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | TI SimpleLink CC13xx/CC26xx Timer[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L99) | [`ti,cc13xx-cc26xx-timer`](../../../../build/dts/api/bindings/timer/ti%2Ccc13xx-cc26xx-timer.md#std-dtcompatible-ti-cc13xx-cc26xx-timer) |
| Watchdog | on-chip | TI CC13xx/CC26xx watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc13xx_cc26xx.dtsi?plain=1#L228) | [`ti,cc13xx-cc26xx-watchdog`](../../../../build/dts/api/bindings/watchdog/ti%2Ccc13xx-cc26xx-watchdog.md#std-dtcompatible-ti-cc13xx-cc26xx-watchdog) |

### Connections and IOs

CC1352 reset is connected to AM62 GPIO0\_14.

| Pin | Function | Usage |
| --- | --- | --- |
| DIO5 | N/C |  |
| DIO6 | N/C |  |
| DIO7 | N/C |  |
| DIO8 | N/C |  |
| DIO9 | N/C |  |
| DIO10 | N/C |  |
| DIO11 | N/C |  |
| DIO12 | CC1352\_RX | AM62 UART6\_TXD |
| DIO13 | CC1352\_TX | AM62 UART6\_RXD |
| DIO14 | N/C |  |
| DIO15 | CC1352\_BOOT | AM62 GPIO0\_13 |
| DIO16 | CC1352\_TDO | TAG-CONNECT TDO |
| DIO17 | CC1352\_TDI | TAG-CONNECT TDI |
| DIO18 | N/C |  |
| DIO19 | N/C |  |
| DIO20 | N/C |  |
| DIO21 | N/C |  |
| DIO22 | N/C |  |
| DIO23 | N/C |  |
| DIO24 | N/C |  |
| DIO25 | N/C |  |
| DIO26 | N/C |  |
| DIO27 | LED1 | CC1352\_LED1 yellow LED9 |
| DIO28 | LED2 | CC1352\_LED2 yellow LED8 |
| DIO29 | RF\_PA | SubG/PA Antenna mux PA enable |
| DIO30 | RF\_SUB1G | SubG/PA Antenna mux SubG enable |

## Programming and Debugging

The `beagleplay` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |
| **misc-flasher** | ✅ (default) |  |

### Flashing

To flash, disable the existing driver that ties up the serial port and use
the customized BSL Python script.

1. Ensure the bcfserial or gb-beagleplay driver isn’t blocking the serial port. This can be done by
   loading :file: `/overlays/k3-am625-beagleplay-bcfserial-no-firmware.dtbo` or selecting uboot
   entry which disables bcfserial/gb-beagleplay.
2. Now reboot the board.

   ```shell
   sudo shutdown -r now
   ```
3. Install CC1352-flasher if not already installed

   ```shell
   if ! command -v cc1352_flasher &> /dev/null; then pip install cc1352-flasher; fi
   ```
4. Flash the CC1352P7

   ```shell
   west flash
   ```

### Debugging

For debugging, you can use the serial port or JTAG. You can use OpenOCD
over the Tag-Connect header on the board.

- Tagconnect JTAG

## References

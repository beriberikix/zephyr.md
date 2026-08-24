---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/atmel/sam0/same54_xpro/doc/index.html
original_path: boards/atmel/sam0/same54_xpro/doc/index.html
---

# SAM E54 Xplained Pro Evaluation Kit

Board Overview

[![../../../../../_images/atsame54_xpro.jpg](https://docs.zephyrproject.org/4.2.0/_images/atsame54_xpro.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/atsame54_xpro.jpg)

SAM E54 Xplained Pro Evaluation Kit

Name:
:   `same54_xpro`

Vendor:
:   Atmel Corporation

Architecture:
:   arm

SoC:
:   same54p20a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/atmel/sam0/same54_xpro/doc/index.rst/../..)

## Overview

The [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/en-us/development-tool/ATSAME54-XPRO) [[1]](#id2) is ideal for evaluation and
prototyping with the SAM E54 Cortex®-M4F processor-based
microcontrollers. The kit includes Atmel’s Embedded Debugger (EDBG),
which provides a full debug interface without the need for additional
hardware.

## Hardware

- SAME54P20A ARM Cortex-M4F processor at 120 MHz
- 32.768 kHz crystal oscillator
- 12 MHz crystal oscillator
- 1024 KiB flash memory and 256 KiB of RAM
- One yellow user LED
- One mechanical user push button
- One reset button
- On-board USB based EDBG unit with serial console
- One QTouch® PTC button
- 32 MiB QSPI Flash
- ATECC508 CryptoAuthentication™ device
- AT24MAC402 serial EEPROM with EUI-48™ MAC address
- Ethernet

  > - RJ45 connector with built-in magnetics
  > - KSZ8091RNA PHY
  > - 10Base-T/100Base-TX IEE 802.3 compliant Ethernet transceiver
- USB interface, host, and device
- SD/SDIO card connector

### Supported Features

The `same54_xpro` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `same54_xpro/same54p20a` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L59) | [`arm,cortex-m4f`](../../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Atmel SAM0 family ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L342)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L367) | [`atmel,sam0-adc`](../../../../../build/dts/api/bindings/adc/atmel,sam0-adc.md#std-dtcompatible-atmel-sam0-adc) |
| ARM architecture | on-chip | For locating the Device ID (serial number) on Atmel SAM0 devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L86) | [`atmel,sam0-id`](../../../../../build/dts/api/bindings/arm/atmel,sam0-id.md#std-dtcompatible-atmel-sam0-id) |
| on-chip | Atmel SAM0 multi-protocol (UART, SPI, I2C) SERCOM unit[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L177) | [`atmel,sam0-sercom`](../../../../../build/dts/api/bindings/arm/atmel,sam0-sercom.md#std-dtcompatible-atmel-sam0-sercom) |
| CAN | on-chip | Specialization of Bosch m\_can CAN FD controller for Atmel SAM0[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/same5x.dtsi?plain=1#L33) | [`atmel,sam0-can`](../../../../../build/dts/api/bindings/can/atmel,sam0-can.md#std-dtcompatible-atmel-sam0-can) |
| Clock control | on-chip | Atmel SAM0 Main Clock Controller (MCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L94) | [`atmel,sam0-mclk`](../../../../../build/dts/api/bindings/clock/atmel,sam0-mclk.md#std-dtcompatible-atmel-sam0-mclk) |
| on-chip | Atmel SAM0 32kHz Oscillator Controller (OSC32KCTRL)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L101) | [`atmel,sam0-osc32kctrl`](../../../../../build/dts/api/bindings/clock/atmel,sam0-osc32kctrl.md#std-dtcompatible-atmel-sam0-osc32kctrl) |
| on-chip | Atmel SAMD0 Generic Clock Controller (GCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L108) | [`atmel,sam0-gclk`](../../../../../build/dts/api/bindings/clock/atmel,sam0-gclk.md#std-dtcompatible-atmel-sam0-gclk) |
| Counter | on-chip | Atmel SAM0 basic timer counter (TC) operating in 32-bit wide mode[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L391) | [`atmel,sam0-tc32`](../../../../../build/dts/api/bindings/counter/atmel,sam0-tc32.md#std-dtcompatible-atmel-sam0-tc32) |
| DMA | on-chip | Atmel SAM0 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L133) | [`atmel,sam0-dmac`](../../../../../build/dts/api/bindings/dma/atmel,sam0-dmac.md#std-dtcompatible-atmel-sam0-dmac) |
| Ethernet | on-chip | Atmel SAM0-family GMAC Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/same5x.dtsi?plain=1#L13) | [`atmel,sam0-gmac`](../../../../../build/dts/api/bindings/ethernet/atmel,sam0-gmac.md#std-dtcompatible-atmel-sam0-gmac) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/same54_xpro/same54_xpro.dts?plain=1#L148) | [`ethernet-phy`](../../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | Atmel SAM0 NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L116) | [`atmel,sam0-nvmctrl`](../../../../../build/dts/api/bindings/flash_controller/atmel,sam0-nvmctrl.md#std-dtcompatible-atmel-sam0-nvmctrl) |
| GPIO & Headers | on-chip | SAM0 GPIO PORT node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L272) | [`atmel,sam0-gpio`](../../../../../build/dts/api/bindings/gpio/atmel,sam0-gpio.md#std-dtcompatible-atmel-sam0-gpio) |
| I2C | on-chip | Atmel SAM0 series SERCOM I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L254) | [`atmel,sam0-i2c`](../../../../../build/dts/api/bindings/i2c/atmel,sam0-i2c.md#std-dtcompatible-atmel-sam0-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/same54_xpro/same54_xpro.dts?plain=1#L47) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | Atmel SAM0 series External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L142) | [`atmel,sam0-eic`](../../../../../build/dts/api/bindings/interrupt-controller/atmel,sam0-eic.md#std-dtcompatible-atmel-sam0-eic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/same54_xpro/same54_xpro.dts?plain=1#L32) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/same54_xpro/same54_xpro.dts?plain=1#L40) | [`pwm-leds`](../../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MDIO | on-chip | Atmel SAM Family MDIO Driver node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/same5x.dtsi?plain=1#L24) | [`atmel,sam-mdio`](../../../../../build/dts/api/bindings/mdio/atmel,sam-mdio.md#std-dtcompatible-atmel-sam-mdio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L68) | [`arm,armv7m-mpu`](../../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L126) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam0/same54_xpro/same54_xpro.dts?plain=1#L156) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Atmel SAM0 PINMUX[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L151) | [`atmel,sam0-pinmux`](../../../../../build/dts/api/bindings/pinctrl/atmel,sam0-pinmux.md#std-dtcompatible-atmel-sam0-pinmux) |
| on-chip | Atmel SAM0 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L265) | [`atmel,sam0-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/atmel,sam0-pinctrl.md#std-dtcompatible-atmel-sam0-pinctrl) |
| PWM | on-chip | Atmel SAM0 TCC in PWM mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L435) | [`atmel,sam0-tcc-pwm`](../../../../../build/dts/api/bindings/pwm/atmel,sam0-tcc-pwm.md#std-dtcompatible-atmel-sam0-tcc-pwm) |
| RNG | on-chip | Atmel SAM RNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L322) | [`atmel,sam-trng`](../../../../../build/dts/api/bindings/rng/atmel,sam-trng.md#std-dtcompatible-atmel-sam-trng) |
| RTC | on-chip | Atmel SAM0 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L328) | [`atmel,sam0-rtc`](../../../../../build/dts/api/bindings/rtc/atmel,sam0-rtc.md#std-dtcompatible-atmel-sam0-rtc) |
| Serial controller | on-chip | Atmel SAM0 SERCOM UART driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L199) | [`atmel,sam0-uart`](../../../../../build/dts/api/bindings/serial/atmel,sam0-uart.md#std-dtcompatible-atmel-sam0-uart) |
| SPI | on-chip | Atmel SAM0 SERCOM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L221) | [`atmel,sam0-spi`](../../../../../build/dts/api/bindings/spi/atmel,sam0-spi.md#std-dtcompatible-atmel-sam0-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L76) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Atmel SAM0 USB in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L313) | [`atmel,sam0-usb`](../../../../../build/dts/api/bindings/usb/atmel,sam0-usb.md#std-dtcompatible-atmel-sam0-usb) |
| Watchdog | on-chip | Atmel SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L171) | [`atmel,sam0-watchdog`](../../../../../build/dts/api/bindings/watchdog/atmel,sam0-watchdog.md#std-dtcompatible-atmel-sam0-watchdog) |

### Pin Mapping

The SAM E54 Xplained Pro evaluation kit has 4 GPIO controllers. These
controllers are responsible for pin muxing, input/output, pull-up, etc.

For more details please refer to [SAM D5x/E5x Family Datasheet (Web)](https://onlinedocs.microchip.com/oxy/GUID-AA358083-AEED-4BA8-8511-9F986D3390A5-en-US-2/index.html) [[2]](#id4), the [SAM E54
Xplained Pro Schematic (Blue PCB)](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/BoardDesignFiles/SAM-E54-Xplained-Pro-Design-Documentation-Rev9.zip) [[3]](#id6), or [SAM E54
Xplained Pro Schematic (Red PCB)](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/BoardDesignFiles/SAM-E54-Xplained-Pro-Design-Documentation-Rev11.zip) [[4]](#id8).

![SAME54-XPRO-pinout](https://docs.zephyrproject.org/4.2.0/_images/ATSAME54-XPRO-pinout.jpg)

#### Default Zephyr Peripheral Mapping:

- SERCOM2 USART TX : PB24
- SERCOM2 USART RX : PB25
- GPIO/PWM LED0 : PC18
- GPIO SW0 : PB31
- GMAC RMII REFCK : PA14
- GMAC RMII TXEN : PA17
- GMAC RMII TXD0 : PA18
- GMAC RMII TXD1 : PA19
- GMAC RMII CRSDV : PC20
- GMAC RMII RXD0 : PA13
- GMAC RMII RXD1 : PA12
- GMAC RMII RXER : PA15
- GMAC MDIO MDC : PC11
- GMAC MDIO MDIO : PC12
- SERCOM4 SPI SCK : PB26
- SERCOM4 SPI MOSI : PB27
- SERCOM4 SPI MISO : PB29
- SERCOM7 I2C SDA : PD08
- SERCOM7 I2C SCL : PD09
- USB DP : PA25
- USB DM : PA24

### System Clock

The SAME54 MCU is configured to use the 32.768 kHz external oscillator
with the on-chip PLL generating the 48 MHz system clock.

### Serial Port

The SAME54 MCU has 8 SERCOM based USARTs with one configured as USARTs in
this BSP. SERCOM2 is the default Zephyr console.

- SERCOM2 115200 8n1 connected to the onboard Atmel Embedded Debugger (EDBG)

### PWM

The SAME54 MCU has 5 TCC based PWM units with up to 6 outputs each and a period
of 24 bits or 16 bits. If `CONFIG_PWM_SAM0_TCC` is enabled then LED0 is
driven by TCC0 instead of by GPIO.

### SPI Port

The SAME54 MCU has 8 SERCOM based SPIs.

### I2C Port

The SAME54 MCU has 8 SERCOM based I2Cs. On the SAM E54 Xplained Pro,
SERCOM7 is connected to a AT24MAC402 EEPROM and a ATECC508A Crypto
Authentication device.

## Programming and Debugging

The `same54_xpro` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

The SAM E54 Xplained Pro comes with a Atmel Embedded Debugger (EDBG). This
provides a debug interface to the SAME54 chip and is supported by
OpenOCD.

### Flashing

1. Build the Zephyr kernel and the `hello_world` sample application:

   ```shell
   west build -b same54_xpro samples/hello_world
   ```
2. Connect the SAM E54 Xplained Pro to your host computer using the USB debug
   port.
3. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
4. To flash an image:

   ```shell
   west build -b same54_xpro samples/hello_world
   west flash
   ```

   You should see “Hello World! same54\_xpro” in your terminal.

## References

[[1](#id3)]

[https://www.microchip.com/en-us/development-tool/ATSAME54-XPRO](https://www.microchip.com/en-us/development-tool/ATSAME54-XPRO)

[[2](#id5)]

[https://onlinedocs.microchip.com/oxy/GUID-AA358083-AEED-4BA8-8511-9F986D3390A5-en-US-2/index.html](https://onlinedocs.microchip.com/oxy/GUID-AA358083-AEED-4BA8-8511-9F986D3390A5-en-US-2/index.html)

[[3](#id7)]

[https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/BoardDesignFiles/SAM-E54-Xplained-Pro-Design-Documentation-Rev9.zip](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/BoardDesignFiles/SAM-E54-Xplained-Pro-Design-Documentation-Rev9.zip)

[[4](#id9)]

[https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/BoardDesignFiles/SAM-E54-Xplained-Pro-Design-Documentation-Rev11.zip](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/BoardDesignFiles/SAM-E54-Xplained-Pro-Design-Documentation-Rev11.zip)

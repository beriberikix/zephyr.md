---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/b_l072z_lrwan1/doc/index.html
original_path: boards/st/b_l072z_lrwan1/doc/index.html
---

# B-L072Z-LRWAN1 Discovery kit

Board Overview

[![../../../../_images/b_l072z_lrwan1.jpg](https://docs.zephyrproject.org/4.1.0/_images/b_l072z_lrwan1.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/b_l072z_lrwan1.jpg)

B-L072Z-LRWAN1 Discovery kit

Name:
:   `b_l072z_lrwan1`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32l072xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/b_l072z_lrwan1/doc/index.rst/../..)

## Overview

This Discovery kit features an all-in-one open module CMWX1ZZABZ-091 (by Murata).
The module is powered by an STM32L072CZ and an SX1276 transceiver.

This kit provides:

- CMWX1ZZABZ-091 LoRa\* / Sigfox\* module (Murata)

  > - Embedded ultra-low-power STM32L072CZ Series MCUs, based on
  >   Arm\* Cortex\* -M0+ core, with 192 Kbytes of Flash
  >   memory, 20 Kbytes of RAM, 6 Kbytes of EEPROM
  > - Frequency range: 860 MHz - 930 MHz
  > - USB 2.0 FS
  > - 4-channel,12-bit ADC, 2xDAC
  > - 6-bit timers, LP-UART, I2C and SPI
  > - Embedded SX1276 transceiver
  > - LoRa\* , FSK, GFSK, MSK, GMSK and OOK modulations (+ Sigfox\* compatibility)
  > - +14 dBm or +20 dBm selectable output power
  > - 157 dB maximum link budget
  > - Programmable bit rate up to 300 kbit/s
  > - High sensitivity: down to -137 dBm
  > - Bullet-proof front end: IIP3 = -12.5 dBm
  > - 89 dB blocking immunity
  > - Low Rx current of 10 mA, 200 nA register retention
  > - Fully integrated synthesizer with a resolution of 61 Hz
  > - Built-in bit synchronizer for clock recovery
  > - Sync word recognition
  > - Preamble detection
  > - 127 dB+ dynamic range RSSI
- SMA and U.FL RF interface connectors
- Including 50 ohm SMA RF antenna
- On-board ST-LINK/V2-1 supporting USB re-enumeration capability
- USB ST-LINK functions:
- Board power supply:

  > - Through USB bus or external VIN/3.3 V supply voltage or batteries
- 3xAAA-type-battery holder for standalone operation
- 7 LEDs:

  > - 4 general-purpose LEDs
  > - A 5 V-power LED
  > - An ST-LINK-communication LED
  > - A fault-power LED
  > - 2 push-buttons (user and reset)
- Arduino\* Uno V3 connectors

More information about the board can be found at the [B-L072Z-LRWAN1 website](https://www.st.com/en/evaluation-tools/b-l072z-lrwan1.html).

## Hardware

The STM32L072CZ SoC provides the following hardware IPs:

- Ultra-low-power (down to 0.29 µA Standby mode and 93 uA/MHz run mode)
- Core: ARM\* 32-bit Cortex\*-M0+ CPU, frequency up to 32 MHz
- Clock Sources:

  > - 1 to 32 MHz crystal oscillator
  > - 32 kHz crystal oscillator for RTC (LSE)
  > - Internal 16 MHz factory-trimmed RC ( ±1%)
  > - Internal low-power 37 kHz RC ( ±5%)
  > - Internal multispeed low-power 65 kHz to 4.2 MHz RC
- RTC with HW calendar, alarms and calibration
- Up to 24 capacitive sensing channels: support touchkey, linear and rotary touch sensors
- 11x timers:

  > - 2x 16-bit with up to 4 channels
  > - 2x 16-bit with up to 2 channels
  > - 1x 16-bit ultra-low-power timer
  > - 1x SysTick
  > - 1x RTC
  > - 2x 16-bit basic for DAC
  > - 2x watchdogs (independent/window)
- Up to 84 fast I/Os, most 5 V-tolerant.
- Memories

  > - Up to 192 KB Flash, 2 banks read-while-write, proprietary code readout protection
  > - Up to 20 KB of SRAM
  > - External memory interface for static memories supporting SRAM, PSRAM, NOR and NAND memories
- Rich analog peripherals (independent supply)

  > - 1x 12-bit ADC 1.14 MSPS
  > - 2x 12-bit DAC
  > - 2x ultra-low-power comparators
- 11x communication interfaces

  > - USB 2.0 full-speed device, LPM and BCD
  > - 3x I2C FM+(1 Mbit/s), SMBus/PMBus
  > - 4x USARTs (ISO 7816, LIN, IrDA, modem)
  > - 6x SPIs (4x SPIs with the Quad SPI)
- 7-channel DMA controller
- True random number generator
- CRC calculation unit, 96-bit unique ID
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell\*

More information about STM32L072CZ can be found here:

- [STM32L072CZ on www.st.com](https://www.st.com/en/microcontrollers/stm32l072cz.html)
- [STM32L0x2 reference manual](https://www.st.com/resource/en/reference_manual/DM00108281.pdf)

### Supported Features

The `b_l072z_lrwan1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `b_l072z_lrwan1/stm32l072xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L29) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L308) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L129) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L51) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L57)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L79) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32L0/L1 Multi Speed Internal Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L64) | [`st,stm32l0-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32l0-msi-clock.md#std-dtcompatible-st-stm32l0-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L71) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32L0/L1 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L86) | [`st,stm32l0-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32l0-pll-clock.md#std-dtcompatible-st-stm32l0-pll-clock) |
| Counter | on-chip | STM32 counters[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L269) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l072.dtsi?plain=1#L54) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L325) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L111) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L158) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L231)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l071.dtsi?plain=1#L23) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l072z_lrwan1/b_l072z_lrwan1.dts?plain=1#L43) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L140) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l072z_lrwan1/b_l072z_lrwan1.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| LoRa | on-board | Semtech SX1276 LoRa Modem[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l072z_lrwan1/b_l072z_lrwan1.dts?plain=1#L117) | [`semtech,sx1276`](../../../../build/dts/api/bindings/lora/semtech%2Csx1276.md#std-dtcompatible-semtech-sx1276) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L104) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32L0 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L119) | [`st,stm32l0-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32l0-nv-flash.md#std-dtcompatible-st-stm32l0-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l072z_lrwan1/b_l072z_lrwan1.dts?plain=1#L171) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-chip | STM32 on-chip EEPROM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L334) | [`st,stm32-eeprom`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-eeprom.md#std-dtcompatible-st-stm32-eeprom) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l072.dtsi?plain=1#L49) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L152) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L263) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L134) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l072.dtsi?plain=1#L40) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L94) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L340) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L351) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L213)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l071.dtsi?plain=1#L142) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L222) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L359) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L243) | [`st,stm32-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi.md#std-dtcompatible-st-stm32-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L46) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| on-chip | STM32 timers[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L253) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L297) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l072.dtsi?plain=1#L26) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L199) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L205) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

B-L072Z-LRWAN1 Discovery kit has GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Available pins:

For detailed information about available pins please refer to [B-L072Z-LRWAN1 website](https://www.st.com/en/evaluation-tools/b-l072z-lrwan1.html).

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX/RX: PA9/PA10 (Arduino Serial)
- UART\_2\_TX/RX: PA2/PA3 (ST-Link Virtual COM Port)
- SPI1 NSS/SCK/MISO/MOSI: PA15/PB3/PA6/PA7 (Semtech SX1276 LoRa\* Transceiver)
- SPI2 NSS/SCK/MISO/MOSI: PB12/PB13/PB14/PB15 (Arduino SPI)
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)

#### System Clock

B-L072Z-LRWAN1 Discovery board System Clock is at 32MHz.

#### Serial Port

B-L072Z-LRWAN1 Discovery board has 2 U(S)ARTs. The Zephyr console output is assigned to UART2.
Default settings are 115200 8N1.

#### USB device

B-L072Z-LRWAN1 Discovery board has 1 USB device controller. However,
the USB data lines are not connected to the MCU by default. To connect
the USB data lines to the MCU, short solder bridges SB15 and SB16.

## Programming and Debugging

B-L072Z-LRWAN1 Discovery board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `b_l072z_lrwan1` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to B-L072Z-LRWAN1 Discovery board

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Connect the B-L072Z-LRWAN1 Discovery board to a STLinkV2 to your host computer using the USB port, then
run a serial host program to connect with your board. For example:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application:

```shell
# From the root of the zephyr repository
west build -b b_l072z_lrwan1 samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b b_l072z_lrwan1 samples/hello_world
west debug
```

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/nucleo_wba65ri/doc/nucleo_wba65ri.html
original_path: boards/st/nucleo_wba65ri/doc/nucleo_wba65ri.html
---

# Nucleo WBA65RI

Board Overview

[![../../../../_images/nucleo_wba65ri.webp](https://docs.zephyrproject.org/4.2.0/_images/nucleo_wba65ri.webp)
](https://docs.zephyrproject.org/4.2.0/_images/nucleo_wba65ri.webp)

Nucleo WBA65RI

Name:
:   `nucleo_wba65ri`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32wba65xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_wba65ri/doc/nucleo_wba65ri.rst/../..)

## Overview

NUCLEO-WBA65RI is a Bluetooth® Low Energy, 802.15.4 and Zigbee® wireless
and ultra-low-power board embedding a powerful and ultra-low-power radio
compliant with the Bluetooth® Low Energy SIG specification v5.4
with IEEE 802.15.4-2015 and Zigbee® specifications.

The ARDUINO® Uno V3 connectivity support and the ST morpho headers allow the
easy expansion of the functionality of the STM32 Nucleo open development
platform with a wide choice of specialized shields.

- Ultra-low-power wireless STM32WBA65RI microcontroller based on the Arm®
  Cortex®‑M33 core, featuring 2 Mbyte of flash memory and 512 Kbytes of SRAM in
  a VFQFPN68 package
- MCU RF board (MB2130):

  - 2.4 GHz RF transceiver supporting Bluetooth® specification v5.4
  - Arm® Cortex® M33 CPU with TrustZone®, MPU, DSP, and FPU
  - Integrated PCB antenna
- Three user LEDs
- Three user and one reset push-buttons
- Board connectors:

  - 2 USB Type-C
  - ARDUINO® Uno V3 expansion connector
  - ST morpho headers for full access to all STM32 I/Os
- Flexible power-supply options: ST-LINK USB VBUS or external sources
- On-board STLINK-V3MODS debugger/programmer with USB re-enumeration capability:
  mass storage, Virtual COM port, and debug port

## Hardware

The STM32WBA65xx multiprotocol wireless and ultralow power devices embed a
powerful and ultralow power radio compliant with the Bluetooth® SIG Low Energy
specification 5.4. They contain a high-performance Arm Cortex-M33 32-bit RISC
core. They operate at a frequency of up to 100 MHz.

- Includes ST state-of-the-art patented technology
- Ultra low power radio:

  - 2.4 GHz radio
  - RF transceiver supporting Bluetooth® Low Energy 5.4 specification
    IEEE 802.15.4-2015 PHY and MAC, supporting Thread, Matter and Zigbee®
  - Proprietary protocols
  - RX sensitivity: -96 dBm (Bluetooth® Low Energy at 1 Mbps)
    and -100 dBm (IEEE 802.15.4 at 250 kbps)
  - Programmable output power, up to +10 dBm with 1 dB steps
  - Support for external PA
  - Integrated balun to reduce BOM
  - Suitable for systems requiring compliance with radio frequency regulations
    ETSI EN 300 328, EN 300 440, FCC CFR47 Part 15 and ARIB STD-T66
- Ultra low power platform with FlexPowerControl:

  - 1.71 to 3.6 V power supply
  - - 40 °C to 85 °C temperature range
  - Autonomous peripherals with DMA, functional down to Stop 1 mode
  - TBD nA Standby mode (16 wake-up pins)
  - TBD nA Standby mode with RTC
  - TBD µA Standby mode with 64 KB SRAM
  - TBD µA Stop 2 mode with 64 KB SRAM
  - TBD µA/MHz Run mode at 3.3 V
  - Radio: Rx TBD mA / Tx at 0 dBm TBD mA
- Core: Arm® 32-bit Cortex®-M33 CPU with TrustZone®, MPU, DSP, and FPU
- ART Accelerator™: 8-Kbyte instruction cache allowing 0-wait-state execution
  from flash memory (frequency up to 100 MHz, 150 DMIPS)
- Power management: embedded regulator LDO and SMPS step-down converter
- Supporting switch on-the-fly and voltage scaling
- Benchmarks:

  - 1.5 DMIPS/MHz (Drystone 2.1)
  - 410 CoreMark® (4.10 CoreMark/MHz)
- Clock sources:

  - 32 MHz crystal oscillator
  - 32 kHz crystal oscillator (LSE)
  - Internal low-power 32 kHz (±5%) RC
  - Internal 16 MHz factory trimmed RC (±1%)
  - PLL for system clock and ADC
- Memories:

  - 2 MB flash memory with ECC, including 256 Kbytes with 100 cycles
  - 512 KB SRAM, including 64 KB with parity check
  - 512-byte (32 rows) OTP
- Rich analog peripherals (independent supply):

  - 12-bit ADC 2.5 Msps with hardware oversampling
- Communication peripherals:

  - Four UARTs (ISO 7816, IrDA, modem)
  - Three SPIs
  - Four I2C Fm+ (1 Mbit/s), SMBus/PMBus®
- System peripherals:

  - Touch sensing controller, up to 24 sensors, supporting touch key, linear,
    :   rotary touch sensors
  - One 16-bit, advanced motor control timer
  - Three 16-bit timers
  - Two 32-bit timer
  - Two low-power 16-bit timers (available in Stop mode)
  - Two Systick timers
  - RTC with hardware calendar and calibration
  - Two watchdogs
  - 8-channel DMA controller, functional in Stop mode
- Security and cryptography:

  - Arm® TrustZone® and securable I/Os, memories, and peripherals
  - Flexible life cycle scheme with RDP and password protected debug
  - Root of trust thanks to unique boot entry and secure hide protection area (HDP)
  - SFI (secure firmware installation) thanks to embedded RSS (root secure services)
  - Secure data storage with root hardware unique key (RHUK)
  - Secure firmware upgrade support with TF-M
  - Two AES co-processors, including one with DPA resistance
  - Public key accelerator, DPA resistant
  - HASH hardware accelerator
  - True random number generator, NIST SP800-90B compliant
  - 96-bit unique ID
  - Active tampers
  - CRC calculation unit
- Up to 86 I/Os (most of them 5 V-tolerant) with interrupt capability
- Development support:

  - Serial wire debug (SWD), JTAG
- ECOPACK2 compliant package

More information about STM32WBA series can be found here:

- [STM32WBA Series on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32wba-series.html)

### Supported Features

The `nucleo_wba65ri` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_wba65ri/stm32wba65xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L33) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L420) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Bluetooth | on-chip | Bluetooth HCI driver for ST STM32WBA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L494) | [`st,hci-stm32wba`](../../../../build/dts/api/bindings/bluetooth/st,hci-stm32wba.md#std-dtcompatible-st-hci-stm32wba) |
| Clock control | on-chip | STM32WBA RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L147) | [`st,stm32wba-rcc`](../../../../build/dts/api/bindings/clock/st,stm32wba-rcc.md#std-dtcompatible-st-stm32wba-rcc) |
| on-chip | STM32WBA HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L85) | [`st,stm32wba-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32wba-hse-clock.md#std-dtcompatible-st-stm32wba-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L92)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L107) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L99) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32WBA PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L114) | [`st,stm32wba-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32wba-pll-clock.md#std-dtcompatible-st-stm32wba-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L122) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L322) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DMA | on-chip | STM32U5 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L472) | [`st,stm32u5-dma`](../../../../build/dts/api/bindings/dma/st,stm32u5-dma.md#std-dtcompatible-st-stm32u5-dma) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L129) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L185) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-chip | Serial Wire - JTAG Connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L499) | [`swj-connector`](../../../../build/dts/api/bindings/gpio/swj-connector.md#std-dtcompatible-swj-connector) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wba65ri/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L288)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L300) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wba65ri/nucleo_wba65ri.dts?plain=1#L47) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L159) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wba65ri/nucleo_wba65ri.dts?plain=1#L28) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L42) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L137) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wba65ri/nucleo_wba65ri.dts?plain=1#L163) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L179) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L327) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L153) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L461) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L218) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L485) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L241)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L250) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L259) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L509) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba65.dtsi?plain=1#L48)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L268) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st,stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L71) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | STM32 timers[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L312) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L439)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L450) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L227) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L233) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Nucleo WBA65RI Board has 4 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Default Zephyr Peripheral Mapping:

- USART\_1 TX/RX : PB12/PA8
- I2C\_1\_SCL : PB2
- I2C\_1\_SDA : PB1
- USER\_PB : PC13
- LD1 : PD8
- SPI\_2\_NSS : PB9 (arduino\_spi)
- SPI\_2\_SCK : PB10 (arduino\_spi)
- SPI\_2\_MISO : PA9 (arduino\_spi)
- SPI\_2\_MOSI : PC3 (arduino\_spi)

#### System Clock

Nucleo WBA65RI System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by HSE+PLL clock at 100MHz.

#### Serial Port

Nucleo WBA65RI board has 3 U(S)ARTs. The Zephyr console output is assigned to USART1.
Default settings are 115200 8N1.

## Programming and Debugging

The `nucleo_wba65ri` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

Nucleo WBA65RI board includes an ST-LINK/V3 embedded debug tool interface.
It could be used for flash and debug using either OpenOCD or STM32Cube ecosystem tools.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, openocd can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
```

#### Flashing an application to Nucleo WBA65RI

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_wba65ri samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

#### Debugging using OpenOCD

You can debug an application in the usual way using OpenOCD. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_wba65ri samples/basic/blinky
west debug
```

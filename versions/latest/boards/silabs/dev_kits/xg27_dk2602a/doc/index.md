---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/dev_kits/xg27_dk2602a/doc/index.html
original_path: boards/silabs/dev_kits/xg27_dk2602a/doc/index.html
---

# EFR32xG27 Dev Kit (xG27-DK2602A)

Board Overview

[![../../../../../_images/xg27_dk2602a.png](https://docs.zephyrproject.org/4.2.0/_images/xg27_dk2602a.png)
](https://docs.zephyrproject.org/4.2.0/_images/xg27_dk2602a.png)

EFR32xG27 Dev Kit (xG27-DK2602A)

Name:
:   `xg27_dk2602a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32bg27c140f768im40

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/dev_kits/xg27_dk2602a/doc/index.rst/../..)

Silicon Labs xG27-DK2602A is a Dev Kit using the EFR32BG27 SoC. The kit
consists of the EFR32BG27 +8 dBm Dev Kit Board (BRD2602A).

## Hardware

- EFR32BG27 Blue Gecko Wireless SoC with up to 76.8 MHz operating frequency
- ARM® Cortex® M33 core with 64 kB RAM and 768 kB Flash
- Macronix ultra low power 8-Mbit SPI flash (MX25R8035F)
- 2.4 GHz ceramic antenna for wireless transmission
- Silicon Labs Si7021 relative humidity and temperature sensor
- Vishay VEML6035 low power, high sensitivity ambient light Sensor
- Silicon Labs Si7210 hall effect sensor
- TDK InvenSense ICM-20689 6-axis inertial sensor
- Pair of PDM microphones
- One LED and one push button
- Power enable signals and isolation switches for ultra low power operation
- On-board SEGGER J-Link debugger for easy programming and debugging, which
  includes a USB virtual COM port and Packet Trace Interface (PTI)
- Mini Simplicity connector for access to energy profiling and advanced wireless
  network debugging
- Breakout pads for GPIO access and connection to external hardware
- Reset button
- CR2032 coin cell holder and external battery connector

For more information, refer to these documents:

- [xG27 Dev Kit User’s Guide](https://www.silabs.com/documents/public/user-guides/ug554-brd2602a-user-guide.pdf)

### Supported Features

The `xg27_dk2602a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `xg27_dk2602a/efr32bg27c140f768im40` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L123) | [`arm,cortex-m33`](../../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Silicon Labs Series 2 IADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L500) | [`silabs,gecko-iadc`](../../../../../build/dts/api/bindings/adc/silabs,gecko-iadc.md#std-dtcompatible-silabs-gecko-iadc) |
| Bluetooth | on-chip | Silicon Labs Series 2 Bluetooth HCI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/efr32xg27.dtsi?plain=1#L24) | [`silabs,bt-hci-efr32`](../../../../../build/dts/api/bindings/bluetooth/silabs,bt-hci-efr32.md#std-dtcompatible-silabs-bt-hci-efr32) |
| Clock control | on-chip | Silicon Labs Series 2 CMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L190) | [`silabs,series-clock`](../../../../../build/dts/api/bindings/clock/silabs,series-clock.md#std-dtcompatible-silabs-series-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L199) | [`fixed-clock`](../../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Silicon Labs Series 2 HFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L206) | [`silabs,hfxo`](../../../../../build/dts/api/bindings/clock/silabs,hfxo.md#std-dtcompatible-silabs-hfxo) |
| on-chip | Silicon Labs Series 2 LFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L218) | [`silabs,series2-lfxo`](../../../../../build/dts/api/bindings/clock/silabs,series2-lfxo.md#std-dtcompatible-silabs-series2-lfxo) |
| on-chip | Silicon Labs Series 2 HFRCODPLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L229) | [`silabs,series2-hfrcodpll`](../../../../../build/dts/api/bindings/clock/silabs,series2-hfrcodpll.md#std-dtcompatible-silabs-series2-hfrcodpll) |
| on-chip | Silicon Labs Series 2 LFRCO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L236) | [`silabs,series2-lfrco`](../../../../../build/dts/api/bindings/clock/silabs,series2-lfrco.md#std-dtcompatible-silabs-series2-lfrco) |
| on-chip | Generic fixed factor clock provider[17 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L23) | [`fixed-factor-clock`](../../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Comparator | on-chip | Silicon Labs Series 2 ACMP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L509) | [`silabs,acmp`](../../../../../build/dts/api/bindings/comparator/silabs,acmp.md#std-dtcompatible-silabs-acmp) |
| Debug | on-chip | Silicon Labs Packet Trace Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/efr32xg27.dtsi?plain=1#L29) | [`silabs,pti`](../../../../../build/dts/api/bindings/debug/silabs,pti.md#std-dtcompatible-silabs-pti) |
| on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L146) | [`arm,armv8m-itm`](../../../../../build/dts/api/bindings/debug/arm,armv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| DMA | on-chip | Silicon Labs Series 2 LDMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L468) | [`silabs,ldma`](../../../../../build/dts/api/bindings/dma/silabs,ldma.md#std-dtcompatible-silabs-ldma) |
| Flash controller | on-chip | Silicon Labs Series 2 MSC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L250) | [`silabs,series2-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs,series2-flash-controller.md#std-dtcompatible-silabs-series2-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L412) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs,gecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L422)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L446) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs,gecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L390)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L401) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs,gecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/xg27_dk2602a/thunderboard.dtsi?plain=1#L28) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/xg27_dk2602a/thunderboard.dtsi?plain=1#L19) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-board | GPIO Wake Up Trigger for EFR32BG22/EFR32BG27[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/xg27_dk2602a/thunderboard.dtsi?plain=1#L38) | `silabs,gecko-wake-up-trigger` |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L257) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/xg27_dk2602a/thunderboard.dtsi?plain=1#L114) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/xg27_dk2602a/thunderboard.dtsi?plain=1#L87) | [`jedec,spi-nor`](../../../../../build/dts/api/bindings/mtd/jedec,spi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Networking | on-chip | Silicon Labs Series 2 Radio Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/efr32xg27.dtsi?plain=1#L11) | [`silabs,series2-radio`](../../../../../build/dts/api/bindings/net/wireless/silabs,series2-radio.md#std-dtcompatible-silabs-series2-radio) |
| Pin control | on-chip | Silicon Labs Series 2 DBUS Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L455) | [`silabs,dbus-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs,dbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl) |
| PWM | on-chip | Silicon Labs TIMER PWM[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L273) | [`silabs,timer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs,timer-pwm.md#std-dtcompatible-silabs-timer-pwm) |
| on-chip | Silicon Labs LETIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L493) | [`silabs,letimer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs,letimer-pwm.md#std-dtcompatible-silabs-letimer-pwm) |
| Regulator | on-chip | Silicon Labs Series 2 DC-DC converter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L517) | [`silabs,series2-dcdc`](../../../../../build/dts/api/bindings/regulator/silabs,series2-dcdc.md#std-dtcompatible-silabs-series2-dcdc) |
| on-board | Fixed voltage regulators[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/xg27_dk2602a/thunderboard.dtsi?plain=1#L44) | [`regulator-fixed`](../../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| RNG | on-chip | GECKO TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L383) | [`silabs,gecko-trng`](../../../../../build/dts/api/bindings/rng/silabs,gecko-trng.md#std-dtcompatible-silabs-gecko-trng) |
| RTC | on-chip | Silicon Labs Series 2 Sleeptimer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L372) | [`silabs,gecko-stimer`](../../../../../build/dts/api/bindings/rtc/silabs,gecko-stimer.md#std-dtcompatible-silabs-gecko-stimer) |
| Sensors | on-board | Si7210 hall effect magnetic position and temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/xg27_dk2602a/thunderboard.dtsi?plain=1#L151) | [`silabs,si7210`](../../../../../build/dts/api/bindings/sensor/silabs,si7210.md#std-dtcompatible-silabs-si7210) |
| Serial controller | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L355) | [`silabs,usart-uart`](../../../../../build/dts/api/bindings/serial/silabs,usart-uart.md#std-dtcompatible-silabs-usart-uart) |
| SPI | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L344) | [`silabs,usart-spi`](../../../../../build/dts/api/bindings/spi/silabs,usart-spi.md#std-dtcompatible-silabs-usart-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L185) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Silicon Labs TIMER[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L264) | [`silabs,series2-timer`](../../../../../build/dts/api/bindings/timer/silabs,series2-timer.md#std-dtcompatible-silabs-series2-timer) |
| on-chip | Silicon Labs Series 2 BURTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L364) | [`silabs,gecko-burtc`](../../../../../build/dts/api/bindings/timer/silabs,gecko-burtc.md#std-dtcompatible-silabs-gecko-burtc) |
| on-chip | Silicon Labs LETIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L486) | [`silabs,series2-letimer`](../../../../../build/dts/api/bindings/timer/silabs,series2-letimer.md#std-dtcompatible-silabs-series2-letimer) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg27/xg27.dtsi?plain=1#L477) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs,gecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### Flashing

The xG27 Dev Kit includes an embedded [J-Link](https://www.segger.com/jlink-debug-probes.html) adapter built around
EFM32GG12 microcontroller (not user-programmable).
The adapter provides:

- SWD interface to EFR32BG27 for flashing and debugging.
- SWO trace interface to EFR32BG27 for tracing.
- UART interface to EFR32BG27 for console access.
- A USB connection to the host computer, which exposes CDC-ACM Serial Port
  endpoints for access to the console UART interface and proprietary J-Link
  endpoints for access to the SWD and SWO interfaces.

UART functionality of the adapter is accessible via standard CDC-ACM USB driver
present in most desktop operating systems and any standard serial port terminal
program e.g. [picocom](https://github.com/npat-efault/picocom).

SWD and SWO functionality is accessible via [Simplicity Commander](https://www.silabs.com/developers/mcu-programming-options).

The simplest way to flash the board is by using West, which runs Simplicity
Commander in unattended mode and passes all the necessary arguments to it.

- If Simplicity Commander is installed in the system and the directory in
  which `commander` executable is located is present in the [`PATH`](../../../../../develop/env_vars.md#envvar-PATH) environment
  variable:

  ```shell
  west flash
  ```
- Otherwise, one should specify full path to the `commander` executable:

  ```shell
  west flash --commander <path_to_commander_directory>/commander
  ```
- In case several J-Link adapters are connected, you must specify serial number
  of the adapter which should be used for flashing:

  ```shell
  west flash --dev-id <J-Link serial number>
  ```

### Programming and Debugging

The `xg27_dk2602a` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **silabs\_commander** | ✅ |  |  |  |  |

The sample application [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b xg27_dk2602a samples/hello_world
```

Connect your device to your host computer using the USB port and you
should see a USB connection. Use `west`’s flash command

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should be able to see on the corresponding Serial Port
the following message:

```shell
Hello World! xg27_dk2602a
```

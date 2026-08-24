---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/particle/nrf51_blenano/doc/index.html
original_path: boards/particle/nrf51_blenano/doc/index.html
---

# Redbear Labs Nano

Board Overview

[![../../../../_images/nrf51_blenano.jpg](https://docs.zephyrproject.org/4.1.0/_images/nrf51_blenano.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/nrf51_blenano.jpg)

Redbear Labs Nano

Name:
:   `nrf51_blenano`

Vendor:
:   Particle.io

Architecture:
:   arm

SoC:
:   nrf51822

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/particle/nrf51_blenano/doc/index.rst/../..)

## Overview

The Nano is a development board equipped with Nordic’s nRF51822 Bluetooth Low Energy SOC.
This board is available on [RedBear Store](https://redbear.cc/product/ble-nano-kit.html) [[1]](#id2).

## Hardware

nRF51 BLE Nano has two external oscillators. The frequency of the slow clock
is 32.768 kHz. The frequency of the main clock is 16 MHz.

### Supported Features

The `nrf51_blenano` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nrf51_blenano/nrf51822` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L18) | [`arm,cortex-m0`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | nRF ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L148) | [`nordic,nrf-adc`](../../../../build/dts/api/bindings/adc/nordic,nrf-adc.md#std-dtcompatible-nordic-nrf-adc) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L33) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic,nrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic nRF family MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L67) | [`nordic,nrf-mpu`](../../../../build/dts/api/bindings/arm/nordic,nrf-mpu.md#std-dtcompatible-nordic-nrf-mpu) |
| on-chip | Nordic nRF family SWI (Software Interrupt)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L256) | [`nordic,nrf-swi`](../../../../build/dts/api/bindings/arm/nordic,nrf-swi.md#std-dtcompatible-nordic-nrf-swi) |
| Clock control | on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L60) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic,nrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Comparator | on-chip | Nordic nRF LPCOMP (analog Low-Power COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L248) | [`nordic,nrf-lpcomp`](../../../../build/dts/api/bindings/comparator/nordic,nrf-lpcomp.md#std-dtcompatible-nordic-nrf-lpcomp) |
| Counter | on-chip | Nordic nRF timer node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L156) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic,nrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | Nordic ECB (AES electronic codebook mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L210) | [`nordic,nrf-ecb`](../../../../build/dts/api/bindings/crypto/nordic,nrf-ecb.md#std-dtcompatible-nordic-nrf-ecb) |
| on-chip | Nordic nRF family CCM (AES CCM mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L217) | [`nordic,nrf-ccm`](../../../../build/dts/api/bindings/crypto/nordic,nrf-ccm.md#std-dtcompatible-nordic-nrf-ccm) |
| Flash controller | on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L298) | [`nordic,nrf51-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic,nrf51-flash-controller.md#std-dtcompatible-nordic-nrf51-flash-controller) |
| GPIO & Headers | on-chip | NRF5 GPIOTE node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L140) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-chip | NRF5 GPIO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L319) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic,nrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| I2C | on-chip | Nordic nRF family TWI (TWI master)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L103) | [`nordic,nrf-twi`](../../../../build/dts/api/bindings/i2c/nordic,nrf-twi.md#std-dtcompatible-nordic-nrf-twi) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/particle/nrf51_blenano/nrf51_blenano.dts?plain=1#L29) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L26) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic,nrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic nRF family PPI (Programmable Peripheral Interconnect)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L313) | [`nordic,nrf-ppi`](../../../../build/dts/api/bindings/misc/nordic,nrf-ppi.md#std-dtcompatible-nordic-nrf-ppi) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L306) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L73) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic,nrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| Pin control | on-chip | The nRF pin controller is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L43) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic,nrf-power.md#std-dtcompatible-nordic-nrf-power) |
| PWM | on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/common/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic,nrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L51) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic,nrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RNG | on-chip | Nordic nRF family RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L203) | [`nordic,nrf-rng`](../../../../build/dts/api/bindings/rng/nordic,nrf-rng.md#std-dtcompatible-nordic-nrf-rng) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L186) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic,nrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L196) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic,nrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| on-chip | Nordic nRF quadrature decoder (QDEC) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L241) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic,nrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L85) | [`nordic,nrf-uart`](../../../../build/dts/api/bindings/serial/nordic,nrf-uart.md#std-dtcompatible-nordic-nrf-uart) |
| SPI | on-chip | Nordic nRF family SPI (SPI master)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L92) | [`nordic,nrf-spi`](../../../../build/dts/api/bindings/spi/nordic,nrf-spi.md#std-dtcompatible-nordic-nrf-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L39) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L224) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic,nrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

### Connections and IOs

BLE nano pinout

![BLE Nano](https://docs.zephyrproject.org/4.1.0/_images/nrf51_blenano1.jpg)

DAPLink board

![DAPLink](https://docs.zephyrproject.org/4.1.0/_images/daplink.jpg)

The DAPLink USB board acts as a dongle. DAPLink debug probes appear on the host computer as a USB disk.
It also regulates 5V from USB to 3.3V via the onboard LDO to power Nano.

More information about Nano and DAPLink can be found at the [RedBear Github](https://github.com/redbear/nRF5x) [[2]](#id5).

## Programming and Debugging

Applications for the `nrf51_blenano` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

To flash an application, you’ll need to connect your BLE Nano with the
DAPLink board, then attach that to your computer via USB.

Warning

Be careful to mount the BLE Nano correctly! The side of the board
with the VIN and GND pins should face **towards** the USB connector.
The [RedBear Store](https://redbear.cc/product/ble-nano-kit.html) [[1]](#id2) page links to a tutorial video that shows how to
properly solder headers and assemble the DAPLink and BLE Nano boards.

Now build and flash applications as usual. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nrf51_blenano samples/hello_world
west flash
```

### Debugging

After mounting the BLE Nano on its DAPLink board as described above,
you can debug an application in the usual way. Here is an example for
the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nrf51_blenano samples/hello_world
west debug
```

## References

[1]
([1](#id3),[2](#id4))

[https://redbear.cc/product/ble-nano-kit.html](https://redbear.cc/product/ble-nano-kit.html)

[[2](#id6)]

[https://github.com/redbear/nRF5x](https://github.com/redbear/nRF5x)

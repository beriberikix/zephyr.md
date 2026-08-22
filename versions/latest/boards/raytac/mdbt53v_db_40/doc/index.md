---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/raytac/mdbt53v_db_40/doc/index.html
original_path: boards/raytac/mdbt53v_db_40/doc/index.html
---

# MDBT53V-DB-40

Board Overview

[![../../../../_images/MDBT53V-DB-40.jpg](../../../../_images/MDBT53V-DB-40.jpg)
](../../../../_images/MDBT53V-DB-40.jpg)

MDBT53V-DB-40

Name:
:   `raytac_mdbt53v_db_40`

Vendor:
:   Raytac Corporation

Architecture:
:   arm

SoC:
:   nrf5340

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/raytac/mdbt53v_db_40/doc/index.rst/../..)

## Overview

Raytac MDBT53V-DB-40 demo board is a development board based on the Raytac MDBT53V-1M module,
using Nordic Semiconductor nRF5340 ARM Cortex-M33 SoC. Its design concept is to connect all
of the module’s pins to 2.54mm pin headers. It is convenient for developers to verify whether
the modules are connected to other peripheral devices or sensors as a tool for software development.

The nRF5340 inside the MDBT53V-1M module is a
dual-core SoC based on the Arm® Cortex®-M33 architecture, with:

- a full-featured Arm Cortex-M33F core with DSP instructions, FPU, and
  Armv8-M Security Extension, running at up to 128 MHz, referred to as
  the **application core**
- a secondary Arm Cortex-M33 core, with a reduced feature set, running
  at a fixed 64 MHz, referred to as the **network core**.

The raytac\_mdbt53v\_db\_40\_nrf5340\_cpuapp build target provides support for the application
core on the nRF5340 SoC. The raytac\_mdbt53v\_db\_40\_nrf5340\_cpuapp build target provides
support for the network core on the nRF5340 SoC.

nRF5340 SoC provides support for the following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- IDAU
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- Segger RTT (RTT Console)
- SPI
- UARTE
- WDT

More information about the board can be found at the [MDBT53V-DB-40 website](https://www.raytac.com/product/ins.php?index_id=140) [[2]](#id4).
The [MDBT53V-DB-40 Specification](https://www.raytac.com/download/index.php?index_id=62) [[3]](#id7) contains the demo board’s datasheet.
The [MDBT53V-DB-40 Schematic](https://www.raytac.com/upload/catalog_b/f2c33d52dca8cd6546c95938bc0cb295.jpg) [[4]](#id10) contains the demo board’s schematic.

## Hardware

- Module Demo Board build by MDBT53V-1M
- Nordic nRF5340 SoC Solution
- A recommended 3rd-party module by Nordic Semiconductor.
- Dual-core Arm® Cortex® M33
- 1MB/256KB Flash Memory; 512kB/ 64kB RAM
- Supports BT5 Long Range Features
- Bluetooth specification v5.2
- Supports BT5 Long Range Features
- Supports Bluetooth Direction Finding & Mesh
- Supports Bluetooth low energy audio
- Cerifications: FCC, IC, CE, Telec(MIC), KC, SRRC, NCC, RCM, WPC
- RoHs & Reach Compiant.
- 25 GPIO
- Chip Antenna
- Interfaces: SPI, UART, I2C, I2S, PWM, ADC, and NFC
- Highly flexible multiprotocol SoC ideally suited for Bluetooth® Low Energy, ANT+, Zigbee, Thread (802.15.4) ultra low-power wireless applications.
- 1 User LEDs
- 3 User buttons
- 1 Mini USB connector for power supply
- SWD connector for FW programming
- J-Link interface for FW programming

### Supported Features

The `raytac_mdbt53v_db_40` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `raytac_mdbt53v_db_40/nrf5340/cpuapp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L16) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L285) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic%2Cnrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L49) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic nRF family DCNF (Domain Configuration)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L9) | [`nordic,nrf-dcnf`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-dcnf.md#std-dtcompatible-nordic-nrf-dcnf) |
| on-chip | Nordic nRF family RESET (Reset Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L97) | [`nordic,nrf-reset`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-reset.md#std-dtcompatible-nordic-nrf-reset) |
| on-chip | Nordic nRF family CTRL-AP (Control Access Port)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L103) | [`nordic,nrf-ctrlapperi`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-ctrlapperi.md#std-dtcompatible-nordic-nrf-ctrlapperi) |
| on-chip | Nordic EGU (Event Generator Unit)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L375) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family MUTEX (Mutual Exclusive Peripheral)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L492) | [`nordic,nrf-mutex`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-mutex.md#std-dtcompatible-nordic-nrf-mutex) |
| on-chip | Nordic KMU (Key Management Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L547) | [`nordic,nrf-kmu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-kmu.md#std-dtcompatible-nordic-nrf-kmu) |
| on-chip | Nordic SPU (System Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L73) | [`nordic,nrf-spu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-spu.md#std-dtcompatible-nordic-nrf-spu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L449) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic%2Cnrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Nordic nRF53X OSCILLATORS (Oscillator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L15) | [`nordic,nrf53-oscillators`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf53-oscillators.md#std-dtcompatible-nordic-nrf53-oscillators) |
| on-chip | Nordic nRF low-frequency crystal oscillator (nRF53 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L19) | [`nordic,nrf53-lfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf53-lfxo.md#std-dtcompatible-nordic-nrf53-lfxo) |
| on-chip | Nordic nRF high-frequency crystal oscillator (nRF53 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L25) | [`nordic,nrf53-hfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf53-hfxo.md#std-dtcompatible-nordic-nrf53-hfxo) |
| on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L64) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L364) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic%2Cnrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L294) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic%2Cnrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | ARM TrustZone CryptoCell 312[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L102) | [`arm,cryptocell-312`](../../../../build/dts/api/bindings/crypto/arm%2Ccryptocell-312.md#std-dtcompatible-arm-cryptocell-312) |
| Debug | on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L23) | [`arm,armv8m-itm`](../../../../build/dts/api/bindings/debug/arm%2Carmv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| Flash controller | on-chip | Properties defining the interface for the Nordic QSPI peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L475) | [`nordic,nrf-qspi`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf-qspi.md#std-dtcompatible-nordic-nrf-qspi) |
| on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L531) | [`nordic,nrf53-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf53-flash-controller.md#std-dtcompatible-nordic-nrf53-flash-controller) |
| GPIO & Headers | on-chip | NRF5 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L560) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| on-chip | NRF5 GPIOTE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L85)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L94) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-board | This is an abstract device responsible for forwarding pins between cores[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raytac/mdbt53v_db_40/raytac_mdbt53v_db_40_nrf5340_cpuapp_common.dts?plain=1#L56) | [`nordic,nrf-gpio-forwarder`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio-forwarder.md#std-dtcompatible-nordic-nrf-gpio-forwarder) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L149)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L109) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic%2Cnrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L456) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic%2Cnrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L581) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic%2Cnrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raytac/mdbt53v_db_40/raytac_mdbt53v_db_40_nrf5340_cpuapp_common.dts?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raytac/mdbt53v_db_40/raytac_mdbt53v_db_40_nrf5340_cpuapp_common.dts?plain=1#L22) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raytac/mdbt53v_db_40/raytac_mdbt53v_db_40_nrf5340_cpuapp_common.dts?plain=1#L30) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Mailbox | on-chip | Nordic nRF family IPC (MBOX Interprocessor Communication)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L465) | [`nordic,mbox-nrf-ipc`](../../../../build/dts/api/bindings/mbox/nordic%2Cmbox-nrf-ipc.md#std-dtcompatible-nordic-mbox-nrf-ipc) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L42) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L344) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L29) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L540) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf5340_cpuapp_partition.dtsi?plain=1#L27) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-chip | Fixed subpartitions of a flash (or other nonvolatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf5340_cpuapp_partition.dtsi?plain=1#L37) | [`fixed-subpartitions`](../../../../build/dts/api/bindings/mtd/fixed-subpartitions.md#std-dtcompatible-fixed-subpartitions) |
| Networking | on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L485) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic%2Cnrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L71) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-power.md#std-dtcompatible-nordic-nrf-power) |
| on-chip | Nordic nRF family USBREG (USB Regulator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L524) | [`nordic,nrf-usbreg`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-usbreg.md#std-dtcompatible-nordic-nrf-usbreg) |
| on-chip | Nordic VMC (Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L554) | [`nordic,nrf-vmc`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-vmc.md#std-dtcompatible-nordic-nrf-vmc) |
| PWM | on-chip | nRF PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L417)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L425) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic REGULATORS (voltage regulators control module) on nRF53X[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L33) | [`nordic,nrf53x-regulators`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf53x-regulators.md#std-dtcompatible-nordic-nrf53x-regulators) |
| on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L40) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| on-chip | Nordic nRF53X regulator (high voltage stage of the main supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L56) | [`nordic,nrf53x-regulator-hv`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf53x-regulator-hv.md#std-dtcompatible-nordic-nrf53x-regulator-hv) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L80) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic%2Cnrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L324) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic%2Cnrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-chip | Nordic nRF quadrature decoder (QDEC) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L498) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L142)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L183) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L190)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L125) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic%2Cnrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp.dtsi?plain=1#L55) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Nordic nRF52 USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L512) | [`nordic,nrf-usbd`](../../../../build/dts/api/bindings/usb/nordic%2Cnrf-usbd.md#std-dtcompatible-nordic-nrf-usbd) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L350)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L357) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic%2Cnrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

#### `raytac_mdbt53v_db_40/nrf5340/cpuapp/ns` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L18) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | Nordic Semiconductor nRF family SAADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L285) | [`nordic,nrf-saadc`](../../../../build/dts/api/bindings/adc/nordic%2Cnrf-saadc.md#std-dtcompatible-nordic-nrf-saadc) |
| ARM architecture | on-chip | Nordic nRF family DCNF (Domain Configuration)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L9) | [`nordic,nrf-dcnf`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-dcnf.md#std-dtcompatible-nordic-nrf-dcnf) |
| on-chip | Nordic nRF family RESET (Reset Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L97) | [`nordic,nrf-reset`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-reset.md#std-dtcompatible-nordic-nrf-reset) |
| on-chip | Nordic nRF family CTRL-AP (Control Access Port)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L103) | [`nordic,nrf-ctrlapperi`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-ctrlapperi.md#std-dtcompatible-nordic-nrf-ctrlapperi) |
| on-chip | Nordic EGU (Event Generator Unit)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L375) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family MUTEX (Mutual Exclusive Peripheral)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L492) | [`nordic,nrf-mutex`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-mutex.md#std-dtcompatible-nordic-nrf-mutex) |
| on-chip | Nordic KMU (Key Management Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L547) | [`nordic,nrf-kmu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-kmu.md#std-dtcompatible-nordic-nrf-kmu) |
| Audio | on-chip | Nordic PDM (Pulse Density Modulation interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L449) | [`nordic,nrf-pdm`](../../../../build/dts/api/bindings/audio/nordic%2Cnrf-pdm.md#std-dtcompatible-nordic-nrf-pdm) |
| Clock control | on-chip | Nordic nRF53X OSCILLATORS (Oscillator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L15) | [`nordic,nrf53-oscillators`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf53-oscillators.md#std-dtcompatible-nordic-nrf53-oscillators) |
| on-chip | Nordic nRF low-frequency crystal oscillator (nRF53 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L19) | [`nordic,nrf53-lfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf53-lfxo.md#std-dtcompatible-nordic-nrf53-lfxo) |
| on-chip | Nordic nRF high-frequency crystal oscillator (nRF53 series)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L25) | [`nordic,nrf53-hfxo`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf53-hfxo.md#std-dtcompatible-nordic-nrf53-hfxo) |
| on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L64) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Comparator | on-chip | Nordic nRF COMP (analog COMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L364) | [`nordic,nrf-comp`](../../../../build/dts/api/bindings/comparator/nordic%2Cnrf-comp.md#std-dtcompatible-nordic-nrf-comp) |
| Counter | on-chip | Nordic nRF timer node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L294) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic%2Cnrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Flash controller | on-chip | Properties defining the interface for the Nordic QSPI peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L475) | [`nordic,nrf-qspi`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf-qspi.md#std-dtcompatible-nordic-nrf-qspi) |
| on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L531) | [`nordic,nrf53-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf53-flash-controller.md#std-dtcompatible-nordic-nrf53-flash-controller) |
| GPIO & Headers | on-chip | NRF5 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L560) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| on-chip | NRF5 GPIOTE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L59) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-board | This is an abstract device responsible for forwarding pins between cores[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raytac/mdbt53v_db_40/raytac_mdbt53v_db_40_nrf5340_cpuapp_common.dts?plain=1#L56) | [`nordic,nrf-gpio-forwarder`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio-forwarder.md#std-dtcompatible-nordic-nrf-gpio-forwarder) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L149)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L109) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic%2Cnrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| I2S | on-chip | Nordic I2S (Inter-IC sound interface)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L456) | [`nordic,nrf-i2s`](../../../../build/dts/api/bindings/i2s/nordic%2Cnrf-i2s.md#std-dtcompatible-nordic-nrf-i2s) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L581) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic%2Cnrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raytac/mdbt53v_db_40/raytac_mdbt53v_db_40_nrf5340_cpuapp_common.dts?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raytac/mdbt53v_db_40/raytac_mdbt53v_db_40_nrf5340_cpuapp_common.dts?plain=1#L22) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raytac/mdbt53v_db_40/raytac_mdbt53v_db_40_nrf5340_cpuapp_common.dts?plain=1#L30) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Mailbox | on-chip | Nordic nRF family IPC (MBOX Interprocessor Communication)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L465) | [`nordic,mbox-nrf-ipc`](../../../../build/dts/api/bindings/mbox/nordic%2Cmbox-nrf-ipc.md#std-dtcompatible-nordic-mbox-nrf-ipc) |
| Miscellaneous | on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L344) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L25) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L540) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf5340_cpuapp_partition.dtsi?plain=1#L27) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-chip | Fixed subpartitions of a flash (or other nonvolatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf5340_cpuapp_partition.dtsi?plain=1#L37) | [`fixed-subpartitions`](../../../../build/dts/api/bindings/mtd/fixed-subpartitions.md#std-dtcompatible-fixed-subpartitions) |
| Networking | on-chip | Nordic nRF family NFCT (Near Field Communication Tag)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L485) | [`nordic,nrf-nfct`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-nfct.md#std-dtcompatible-nordic-nrf-nfct) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic%2Cnrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L71) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-power.md#std-dtcompatible-nordic-nrf-power) |
| on-chip | Nordic nRF family USBREG (USB Regulator Control)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L524) | [`nordic,nrf-usbreg`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-usbreg.md#std-dtcompatible-nordic-nrf-usbreg) |
| on-chip | Nordic VMC (Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L554) | [`nordic,nrf-vmc`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-vmc.md#std-dtcompatible-nordic-nrf-vmc) |
| PWM | on-chip | nRF PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L417)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L425) | [`nordic,nrf-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-pwm.md#std-dtcompatible-nordic-nrf-pwm) |
| on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Regulator | on-chip | Nordic REGULATORS (voltage regulators control module) on nRF53X[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L33) | [`nordic,nrf53x-regulators`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf53x-regulators.md#std-dtcompatible-nordic-nrf53x-regulators) |
| on-chip | Nordic nRF5X regulator (fixed stage of the core supply)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L40) | [`nordic,nrf5x-regulator`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf5x-regulator.md#std-dtcompatible-nordic-nrf5x-regulator) |
| on-chip | Nordic nRF53X regulator (high voltage stage of the main supply)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L56) | [`nordic,nrf53x-regulator-hv`](../../../../build/dts/api/bindings/regulator/nordic%2Cnrf53x-regulator-hv.md#std-dtcompatible-nordic-nrf53x-regulator-hv) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L80) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic%2Cnrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L324) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic%2Cnrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-chip | Nordic nRF quadrature decoder (QDEC) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L498) | [`nordic,nrf-qdec`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L142)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L183) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L190)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L125) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic%2Cnrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuappns.dtsi?plain=1#L38) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Nordic nRF52 USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L512) | [`nordic,nrf-usbd`](../../../../build/dts/api/bindings/usb/nordic%2Cnrf-usbd.md#std-dtcompatible-nordic-nrf-usbd) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L350)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi?plain=1#L357) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic%2Cnrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

#### `raytac_mdbt53v_db_40/nrf5340/cpunet` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L21) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ARM architecture | on-chip | Nordic UICR (User Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L43) | [`nordic,nrf-uicr`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| on-chip | Nordic EGU (Event Generator Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L234) | [`nordic,nrf-egu`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-egu.md#std-dtcompatible-nordic-nrf-egu) |
| on-chip | Nordic nRF family SWI (Software Interrupt)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L270) | [`nordic,nrf-swi`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-swi.md#std-dtcompatible-nordic-nrf-swi) |
| on-chip | Nordic nRF family ACL (Access Control List)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L298) | [`nordic,nrf-acl`](../../../../build/dts/api/bindings/arm/nordic%2Cnrf-acl.md#std-dtcompatible-nordic-nrf-acl) |
| Clock control | on-chip | Nordic nRF clock control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L58) | [`nordic,nrf-clock`](../../../../build/dts/api/bindings/clock/nordic%2Cnrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| Counter | on-chip | Nordic nRF timer node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L136) | [`nordic,nrf-timer`](../../../../build/dts/api/bindings/counter/nordic%2Cnrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| Cryptographic accelerator | on-chip | Nordic ECB (AES electronic codebook mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L146) | [`nordic,nrf-ecb`](../../../../build/dts/api/bindings/crypto/nordic%2Cnrf-ecb.md#std-dtcompatible-nordic-nrf-ecb) |
| on-chip | Nordic nRF family CCM (AES CCM mode encryption)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L153) | [`nordic,nrf-ccm`](../../../../build/dts/api/bindings/crypto/nordic%2Cnrf-ccm.md#std-dtcompatible-nordic-nrf-ccm) |
| Flash controller | on-chip | Nordic NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L304) | [`nordic,nrf53-flash-controller`](../../../../build/dts/api/bindings/flash_controller/nordic%2Cnrf53-flash-controller.md#std-dtcompatible-nordic-nrf53-flash-controller) |
| GPIO & Headers | on-chip | NRF5 GPIOTE[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L121) | [`nordic,nrf-gpiote`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| on-chip | NRF5 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L326) | [`nordic,nrf-gpio`](../../../../build/dts/api/bindings/gpio/nordic%2Cnrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| I2C | on-chip | Nordic nRF family TWIM (TWI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L193) | [`nordic,nrf-twim`](../../../../build/dts/api/bindings/i2c/nordic%2Cnrf-twim.md#std-dtcompatible-nordic-nrf-twim) |
| IEEE 802.15.4 | on-chip | Nordic nRF IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L100) | [`nordic,nrf-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nordic%2Cnrf-ieee802154.md#std-dtcompatible-nordic-nrf-ieee802154) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| Mailbox | on-chip | Nordic nRF family IPC (MBOX Interprocessor Communication)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L183) | [`nordic,mbox-nrf-ipc`](../../../../build/dts/api/bindings/mbox/nordic%2Cmbox-nrf-ipc.md#std-dtcompatible-nordic-mbox-nrf-ipc) |
| Miscellaneous | on-chip | Nordic FICR (Factory Information Configuration Registers)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L36) | [`nordic,nrf-ficr`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| on-chip | Nordic DPPIC (Distributed Programmable Peripheral Interconnect Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L162) | [`nordic,nrf-dppic`](../../../../build/dts/api/bindings/misc/nordic%2Cnrf-dppic.md#std-dtcompatible-nordic-nrf-dppic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L28) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L313) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raytac/mdbt53v_db_40/raytac_mdbt53v_db_40_nrf5340_cpunet_common.dts?plain=1#L35) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Nordic nRF family RADIO peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L90) | [`nordic,nrf-radio`](../../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| Pin control | on-chip | Nordic nRF family Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L25) | [`nordic,nrf-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nordic%2Cnrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| Power management | on-chip | Nordic nRF power control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L65) | [`nordic,nrf-power`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-power.md#std-dtcompatible-nordic-nrf-power) |
| on-chip | Nordic VMC (Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L320) | [`nordic,nrf-vmc`](../../../../build/dts/api/bindings/power/nordic%2Cnrf-vmc.md#std-dtcompatible-nordic-nrf-vmc) |
| PWM | on-chip | nRFx S/W PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L38) | [`nordic,nrf-sw-pwm`](../../../../build/dts/api/bindings/pwm/nordic%2Cnrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| Retained memory | on-chip | Nordic GPREGRET (General Purpose Register Retention) device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L73) | [`nordic,nrf-gpregret`](../../../../build/dts/api/bindings/retained_mem/nordic%2Cnrf-gpreget.md#std-dtcompatible-nordic-nrf-gpregret) |
| RNG | on-chip | Nordic nRF family RNG (Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L114) | [`nordic,nrf-rng`](../../../../build/dts/api/bindings/rng/nordic%2Cnrf-rng.md#std-dtcompatible-nordic-nrf-rng) |
| RTC | on-chip | Nordic nRF RTC (Real-Time Counter)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L175) | [`nordic,nrf-rtc`](../../../../build/dts/api/bindings/rtc/nordic%2Cnrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| Sensors | on-chip | Nordic nRF family TEMP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L168) | [`nordic,nrf-temp`](../../../../build/dts/api/bindings/sensor/nordic%2Cnrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| Serial controller | on-chip | Nordic nRF family UARTE (UART with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L227) | [`nordic,nrf-uarte`](../../../../build/dts/api/bindings/serial/nordic%2Cnrf-uarte.md#std-dtcompatible-nordic-nrf-uarte) |
| SPI | on-chip | Nordic nRF family SPIM (SPI master with EasyDMA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L210) | [`nordic,nrf-spim`](../../../../build/dts/api/bindings/spi/nordic%2Cnrf-spim.md#std-dtcompatible-nordic-nrf-spim) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L49) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| Watchdog | on-chip | Nordic nRF family WDT (Watchdog Timer)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf5340_cpunet.dtsi?plain=1#L129) | [`nordic,nrf-wdt`](../../../../build/dts/api/bindings/watchdog/nordic%2Cnrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

See [MDBT53V-DB-40 website](https://www.raytac.com/product/ins.php?index_id=140) [[2]](#id4) and [MDBT53V-DB-40 Specification](https://www.raytac.com/download/index.php?index_id=62) [[3]](#id7)
for a complete list of Raytac MDBT53V-DB-40 board hardware features.

### Connections and IOs

#### LED

- LED1 (green) = P0.31

#### Push buttons

- BUTTON1 = SW1 = P1.13
- BUTTON2 = SW2 = P0.25
- BUTTON3 = SW3 = P0.26

#### HSPI

- MOSI = P0.9
- MISO = P0.10
- SCK = P0.8
- CSN = P0.11
- DCX = P0.12

#### QSPI

- SCK = P0.17
- CSN = P0.18
- DATA0 = P0.13
- DATA1 = P0.14
- DATA2 = P0.15
- DATA3 = P0.16

### Security components

- Implementation Defined Attribution Unit ([IDAU](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau) [[1]](#id2)) on the application core.
  The IDAU is implemented with the System Protection Unit and is used to
  define secure and non-secure memory maps. By default, all of the memory
  space (Flash, SRAM, and peripheral address space) is defined to be secure
  accessible only.
- Secure boot.

## Programming and Debugging

The `raytac_mdbt53v_db_40` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **nrfjprog** | ✅ |  |  |  |  |
| **nrfutil** | ✅ (default) |  |  |  |  |

nRF5340 application core supports the Armv8-M Security Extension.
Applications built for the raytac\_mdbt53v\_db\_40\_nrf5340\_cpuapp board by
default boot in the Secure state.

nRF5340 network core does not support the Armv8-M Security Extension.
nRF5340 IDAU may configure bus accesses by the nRF5340 network core
to have Secure attribute set; the latter allows to build and run
Secure only applications on the nRF5340 SoC.

Applications for the `raytac_mdbt53v_db_40_nrf5340` board configuration can be
built, flashed, and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

Note

Flashing and Debugging Zephyr onto the raytac\_mdbt53v\_db\_40\_nrf5340 board
requires an external J-Link programmer. The programmer is attached to the J1
or J9 SWD connector.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Use a USB to TTL converter to connect the computer and raytac\_mdbt53v\_db\_40\_nrf5340
J13 connector pin 8(RX), 9(TX) and GND. Then run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the USB to TTL converter
can be found. For example, under Linux, `/dev/ttyUSB0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b raytac_mdbt53v_db_40_nrf5340 samples/hello_world
west flash
```

### Debugging

The `raytac_mdbt53v_db_40_nrf5340` board does not have an on-board-J-Link debug IC,
however, instructions from the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page also apply to this board.
Use the Debug out connector of nRF52x DK to connect to the J1 connector, and use SEGGER
J-Link OB IF to debug.

## References

[[1](#id3)]

[https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau)

[2]
([1](#id5),[2](#id6))

[https://www.raytac.com/product/ins.php?index\_id=140](https://www.raytac.com/product/ins.php?index_id=140)

[3]
([1](#id8),[2](#id9))

[https://www.raytac.com/download/index.php?index\_id=62](https://www.raytac.com/download/index.php?index_id=62)

[[4](#id11)]

[https://www.raytac.com/upload/catalog\_b/f2c33d52dca8cd6546c95938bc0cb295.jpg](https://www.raytac.com/upload/catalog_b/f2c33d52dca8cd6546c95938bc0cb295.jpg)

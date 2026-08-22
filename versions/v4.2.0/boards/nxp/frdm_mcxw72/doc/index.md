---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_mcxw72/doc/index.html
original_path: boards/nxp/frdm_mcxw72/doc/index.html
---

# FRDM-MCXW72

Board Overview

[![../../../../_images/frdm_mcxw72.webp](../../../../_images/frdm_mcxw72.webp)
](../../../../_images/frdm_mcxw72.webp)

FRDM-MCXW72

Name:
:   `frdm_mcxw72`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mcxw727c

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_mcxw72/doc/index.rst/../..)

## Overview

The FRDM-MCXW72

The MCX W72x family features a 96 MHz Arm® Cortex®-M33 core coupled with a
multiprotocol radio subsystem supporting Matter, Thread, Zigbee and
Bluetooth LE. The independent radio subsystem, with a dedicated core and
memory, offloads the main CPU, preserving it for the primary application and
allowing firmware updates to support future wireless standards.

## Hardware

- MCXW72 Arm Cortex-M33 microcontroller running up to 96 MHz
- 2MB on-chip Flash memory unit
- 256 KB TCM RAM
- On-board MCU-Link debugger with CMSIS-DAP

For more information about the MCXW72 SoC and FRDM-MCXW72 board, see:

- [MCXW72 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w72x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W72X) [[8]](#id18)
- [FRDM-MCXW72 Website](#frdm-mcxw72-website)

### Supported Features

The `frdm_mcxw72` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `frdm_mcxw72/mcxw727c/cpu0` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L31) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L309) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp%2Clpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| ARM architecture | on-chip | NXP NBU interruption information[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L281) | [`nxp,nbu`](../../../../build/dts/api/bindings/arm/nxp%2Cnbu.md#std-dtcompatible-nxp-nbu) |
| Bluetooth | on-chip | NXP BLE HCI information[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L287) | [`nxp,hci-ble`](../../../../build/dts/api/bindings/bluetooth/nxp%2Chci-ble.md#std-dtcompatible-nxp-hci-ble) |
| CAN | on-chip | NXP FlexCAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L299) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan.md#std-dtcompatible-nxp-flexcan) |
| Clock control | on-chip | NXP K4 Generation SCG (System Clock Generator) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L116) | [`nxp,scg-k4`](../../../../build/dts/api/bindings/clock/nxp%2Cscg-k4.md#std-dtcompatible-nxp-scg-k4) |
| Counter | on-chip | NXP LPTMR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L259)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L270) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp%2Clptmr.md#std-dtcompatible-nxp-lptmr) |
| Flash controller | on-chip | NXP MSF1 Flash Memory Module (FMU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L45) | [`nxp,msf1`](../../../../build/dts/api/bindings/flash_controller/nxp%2Cmsf1.md#std-dtcompatible-nxp-msf1) |
| GPIO & Headers | on-chip | Kinetis GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L357)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L204) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Ckinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| I2C | on-chip | NXP LPI2C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L169)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L158) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| IEEE 802.15.4 | on-chip | NXP MCXW71 IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L291) | [`nxp,mcxw-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nxp%2Cmcxw-ieee802154.md#std-dtcompatible-nxp-mcxw-ieee802154) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxw72/frdm_mcxw72_mcxw727c_cpu0.dts?plain=1#L55) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxw72/frdm_mcxw72_mcxw727c_cpu0.dts?plain=1#L35) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxw72/frdm_mcxw72_mcxw727c_cpu0.dts?plain=1#L42) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L37) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L53) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxw72/frdm_mcxw72_mcxw727c_cpu0.dts?plain=1#L93) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP PORT Pin Controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L122) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L103) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | MCUX Timer/PWM Module (TPM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L219)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L229) | [`nxp,kinetis-tpm`](../../../../build/dts/api/bindings/pwm/nxp%2Ckinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm) |
| Regulator | on-chip | NXP VREF SOC peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L325) | [`nxp,vref`](../../../../build/dts/api/bindings/regulator/nxp%2Cvref.md#std-dtcompatible-nxp-vref) |
| RNG | on-chip | NXP ELE (EdgeLock secure enclave) TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L295) | [`nxp,ele-trng`](../../../../build/dts/api/bindings/rng/nxp%2Cele-trng.md#std-dtcompatible-nxp-ele-trng) |
| RTC | on-chip | NXP Real Time Clock (RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L338) | [`nxp,rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Crtc.md#std-dtcompatible-nxp-rtc) |
| Sensors | on-board | FXLS8974 3-axis accelerometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxw72/frdm_mcxw72_mcxw727c_cpu0.dts?plain=1#L153) | [`nxp,fxls8974`](../../../../build/dts/api/compatibles/nxp%2Cfxls8974.md#std-dtcompatible-nxp-fxls8974) |
| Serial controller | on-chip | NXP LPUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L142) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L192)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L180) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L64) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| Watchdog | on-chip | NXP watchdog (WDOG32)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L239)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L249) | [`nxp,wdog32`](../../../../build/dts/api/bindings/watchdog/nxp%2Cwdog32.md#std-dtcompatible-nxp-wdog32) |
| on-chip | NXP External Watchdog Monitor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxw7x_common.dtsi?plain=1#L347) | [`nxp,ewm`](../../../../build/dts/api/bindings/watchdog/nxp%2Cewm.md#std-dtcompatible-nxp-ewm) |

## Fetch Binary Blobs

To support Bluetooth, frdm\_mcxw72 requires fetching binary blobs, which can be
achieved by running the following command:

```shell
west blobs fetch hal_nxp
```

## Programming and Debugging

The `frdm_mcxw72` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **debugserver** | **rtt** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ | ✅ |  |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the MCU-Link CMSIS-DAP Onboard Debug Probe.

#### Using LinkServer

Linkserver is the default runner for this board, and supports the factory
default MCU-Link firmware. Follow the instructions in
[MCU-Link CMSIS-DAP Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-cmsis-onboard-debug-probe) to reprogram the default MCU-Link
firmware. This only needs to be done if the default onboard debug circuit
firmware was changed. To put the board in `DFU mode` to program the firmware,
short jumper JP5.

#### Using J-Link

There are two options. The onboard debug circuit can be updated with Segger
J-Link firmware by following the instructions in
[MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
To be able to program the firmware, you need to put the board in `DFU mode`
by shortening the jumper JP5.
The second option is to attach a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) to the
10-pin SWD connector (J12) of the board.
For both options use the `-r jlink` option with west to use the jlink runner.

```shell
west flash -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J14, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Application Building

#### Openthread applications

```shell
# From the root of the zephyr repository
west build -b frdm_mcxw72/mcxw727c/cpu0 samples/net/sockets/echo_server
```

```shell
# From the root of the zephyr repository
west build -b frdm_mcxw72/mcxw727c/cpu0 samples/net/sockets/echo_client
```

### Application Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxw72/mcxw727c/cpu0 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.7.0-xxx-xxxx ***
Hello World! frdm_mcxw72/mcxw727c/cpu0
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxw72/mcxw727c/cpu0 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.7.0-xxx-xxxx ***
Hello World! frdm_mcxw72/mcxw727c/cpu0
```

### NBU Flashing

BLE functionality requires to fetch binary blobs, so make sure to follow
the `Fetch Binary Blobs` section first.

Two images must be written to the board: one for the host (CM33) and one for the NBU (CM3).

- To flash the application (CM33) refer to the `Application Flashing` section above.
- To flash the `NBU Flashing`, follow the instructions below:

  > - Install `blhost` from NXP’s website. This is the tool that will allow you to flash the NBU.
  > - Enter ISP mode. To boot the MCU in ISP mode, follow these steps:
  >   :   - Disconnect the `FRDM-MCXW72` board from all power sources.
  >       - Keep the `SW4` and `SW1` buttons on the board pressed, while connecting the board to the host computer USB port.
  >       - Release the `SW4` and `SW1` buttons. The MCXW72 MCU boots in ISP mode.
  >       - Reconnect any external power supply, if needed.
  > - Use the following command to flash NBU file:

DYN NBU - WindowsDYN NBU - Linux

Flash Dynamic NBU (BLE + 15.4) on Windows

```shell
blhost.exe -p COMxx flash-erase-all 0
blhost.exe -p COMxx flash-erase-all 2
blhost.exe -p COMxx write-memory 0x48800000 <nbu-firmware.bin>
```

Flash Dynamic NBU (BLE + 15.4) on Linux

```shell
./blhost -p /dev/ttyxx flash-erase-all 0
/blhost -p /dev/ttyxx flash-erase-all 2
/blhost -p /dev/ttyxx write-memory 0x48800000 <nbu-firmware.bin>
```

Please consider changing `COMxx` on Windows or `ttyxx` on Linux to the serial port used by your board.

The NBU files can be found in : `<zephyr workspace>/modules/hal/nxp/zephyr/blobs/mcxw72/` folder.

### Troubleshooting

#### Using Segger SystemView and RTT

Note that when using SEGGER SystemView or RTT with this SOC, the RTT control
block address must be set manually within SystemView or the RTT Viewer. The
address provided to the tool should be the location of the `_SEGGER_RTT`
symbol, which can be found using a debugger or by examining the `zephyr.map`
file output by the linker.

The RTT control block address must be provided manually because this SOC
supports ECC RAM. If the SEGGER tooling searches the ECC RAM space for the
control block a fault will occur, provided that ECC is enabled and the RAM
segment being searched has not been initialized to a known value.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk) [[1]](#id4)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC) [[2]](#id6), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) [[3]](#id8) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started) [[4]](#id10)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548) [[5]](#id12)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) [[6]](#id14) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project) [[7]](#id16)

## References

[[1](#id5)]

[https://github.com/nxp-zephyr/nxp-zsdk](https://github.com/nxp-zephyr/nxp-zsdk)

[[2](#id7)]

[https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC)

[[3](#id9)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki)

[[4](#id11)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)

[[5](#id13)]

[https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)

[[6](#id15)]

[https://nxp.com/zephyr](https://nxp.com/zephyr)

[[7](#id17)]

[https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

[[8](#id19)]

[https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w72x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W72X](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w72x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W72X)

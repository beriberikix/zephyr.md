---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/ucans32k1sic/doc/index.html
original_path: boards/arm/ucans32k1sic/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# NXP UCANS32K1SIC

## Overview

[NXP UCANS32K1SIC](https://www.nxp.com/design/development-boards/analog-toolbox/can-sic-evaluation-board:UCANS32K1SIC) [[1]](#id4) is a CAN signal improvement capability (SIC) evaluation
board designed for both automotive and industrial applications. The UCANS32K1SIC
provides two CAN SIC interfaces and is based on the 32-bit Arm Cortex-M4F
[NXP S32K146](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k1-microcontrollers-for-automotive-general-purpose:S32K1) [[2]](#id7) microcontroller.

![NXP UCANS32K1SIC (TOP)](../../../../_images/ucans32k1sic_top.webp)

## Hardware

- NXP S32K146
  :   - Arm Cortex-M4F @ up to 112 Mhz
      - 1 MB Flash
      - 128 KB SRAM
      - up to 127 I/Os
      - 3x FlexCAN with 2x FD
      - eDMA, 12-bit ADC, MPU, ECC and more.
- Interfaces:
  :   - DCD-LZ debug interface with SWD + Console / UART
      - Dual CAN FD PHYs with dual connectors for daisy chain operation
      - JST-GH DroneCode compliant standard connectors and I/O headers
      - user RGB LED and button.

More information about the hardware and design resources can be found at
[NXP UCANS32K1SIC](https://www.nxp.com/design/development-boards/analog-toolbox/can-sic-evaluation-board:UCANS32K1SIC) [[1]](#id4) website.

### Supported Features

The `ucans32k1sic` board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| SYSMPU | on-chip | mpu |
| PORT | on-chip | pinctrl |
| GPIO | on-chip | gpio |
| LPUART | on-chip | serial |
| LPI2C | on-chip | i2c |
| LPSPI | on-chip | spi |
| FTM | on-chip | pwm |
| FlexCAN | on-chip | can |
| Watchdog | on-chip | watchdog |
| RTC | on-chip | counter |

The default configuration can be found in the Kconfig file
[boards/arm/ucans32k1sic/ucans32k1sic\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/ucans32k1sic/ucans32k1sic_defconfig).

### Connections and IOs

This board has 5 GPIO ports named from `gpioa` to `gpioe`.

Pin control can be further configured from your application overlay by adding
children nodes with the desired pinmux configuration to the singleton node
`pinctrl`. Supported properties are described in
[dts/bindings/pinctrl/nxp,kinetis-pinctrl.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/pinctrl/nxp,kinetis-pinctrl.yaml).

#### LEDs

The UCANS32K1SIC board has one user RGB LED that can be used either as a GPIO
LED or as a PWM LED.

RGB LED as GPIO LED

| Devicetree node | Devicetree alias | Label | Pin |
| --- | --- | --- | --- |
| led1\_red | led0 | LED1\_RGB\_RED | PTD15 |
| led1\_green | led1 | LED1\_RGB\_GREEN | PTD16 |
| led1\_blue | led2 | LED1\_RGB\_BLUE | PTD0 |

RGB LED as PWM LED

| Devicetree node | Devicetree alias | Label | Pin |
| --- | --- | --- | --- |
| led1\_red\_pwm | pwm-led0 / red-pwm-led | LED1\_RGB\_RED\_PWM | PTD15 / FTM0\_CH0 |
| led1\_green\_pwm | pwm-led1 / green-pwm-led | LED1\_RGB\_GREEN\_PWM | PTD16 / FTM0\_CH1 |
| led1\_blue\_pwm | pwm-led2 / blue-pwm-led | LED1\_RGB\_BLUE\_PWM | PTD0 / FTM0\_CH2 |

The user can control the LEDs in any way. An output of `0` illuminates the LED.

#### Buttons

The UCANS32K1SIC board has one user button:

| Devicetree node | Label | Pin |
| --- | --- | --- |
| sw0 / button\_3 | SW3 | PTD15 |

### Serial Console

The serial console is provided via `lpuart1` on the 7-pin DCD-LZ debug
connector `P6`.

| Connector | Pin | Pin Function |
| --- | --- | --- |
| P6.2 | PTC7 | LPUART1\_TX |
| P6.3 | PTC6 | LPUART1\_RX |

### System Clock

The Arm Cortex-M4F core is configured to run at 80 MHz (RUN mode).

## Programming and Debugging

Applications for the `ucans32k1sic` board can be built in the usual way as
documented in [Building an Application](../../../../develop/application/index.md#build-an-application).

This board configuration supports [Lauterbach TRACE32](https://www.lauterbach.com) [[3]](#id9) and [SEGGER J-Link](https://wiki.segger.com/S32Kxxx) [[4]](#id11)
West runners for flashing and debugging applications. Follow the steps described
in [Lauterbach TRACE32 Debug Host Tools](../../../../develop/flash_debug/host-tools.md#lauterbach-trace32-debug-host-tools) and [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools),
to setup the flash and debug host tools for these runners, respectively. The
default runner is J-Link.

### Flashing

Run the `west flash` command to flash the application using SEGGER J-Link.
Alternatively, run `west flash -r trace32` to use Lauterbach TRACE32.

The Lauterbach TRACE32 runner supports additional options that can be passed
through command line:

```shell
west flash -r trace32 --startup-args elfFile=<elf_path> loadTo=<flash/sram>
   eraseFlash=<yes/no> verifyFlash=<yes/no>
```

Where:

- `<elf_path>` is the path to the Zephyr application ELF in the output
  directory
- `loadTo=flash` loads the application to the SoC internal program flash
  ([`CONFIG_XIP`](../../../../kconfig.md#CONFIG_XIP "CONFIG_XIP") must be set), and `loadTo=sram` load the
  application to SRAM. The default is `flash`.
- `eraseFlash=yes` erases the whole content of SoC internal flash before the
  application is downloaded to either Flash or SRAM. This routine takes time to
  execute. The default is `no`.
- `verifyFlash=yes` verify the SoC internal flash content after programming
  (use together with `loadTo=flash`). The default is `no`.

For example, to erase and verify flash content:

```shell
west flash -r trace32 --startup-args elfFile=build/zephyr/zephyr.elf loadTo=flash eraseFlash=yes verifyFlash=yes
```

### Debugging

Run the `west debug` command to start a GDB session using SEGGER J-Link.
Alternatively, run `west debug -r trace32` to launch the Lauterbach TRACE32
software debugging interface.

## References

[1]
([1](#id5),[2](#id6))

[https://www.nxp.com/design/development-boards/analog-toolbox/can-sic-evaluation-board:UCANS32K1SIC](https://www.nxp.com/design/development-boards/analog-toolbox/can-sic-evaluation-board:UCANS32K1SIC)

[[2](#id8)]

[https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k1-microcontrollers-for-automotive-general-purpose:S32K1](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k1-microcontrollers-for-automotive-general-purpose:S32K1)

[[3](#id10)]

[https://www.lauterbach.com](https://www.lauterbach.com)

[[4](#id12)]

[https://wiki.segger.com/S32Kxxx](https://wiki.segger.com/S32Kxxx)

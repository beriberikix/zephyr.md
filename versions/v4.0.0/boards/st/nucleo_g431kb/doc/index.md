---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/st/nucleo_g431kb/doc/index.html
original_path: boards/st/nucleo_g431kb/doc/index.html
---

# Nucleo G431KB

Board Overview

[![../../../../_images/nucleo_g431kb.webp](../../../../_images/nucleo_g431kb.webp)
](../../../../_images/nucleo_g431kb.webp)

Nucleo G431KB

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32g431xx

## Overview

The Nucleo G431KB board features an ARM Cortex-M4 based STM32G431KB MCU
with a wide range of connectivity support and configurations.
Here are some highlights of the Nucleo G431KB board:

- STM32 microcontroller in LQFP32 package
- Arduino Nano V3 connectivity
- On-board ST-LINK/V3E debugger/programmer
- Flexible board power supply:

  - USB VBUS or external source(3.3 V, 5 V, 7 - 12 V)
  - Power management access point
- Three LEDs: USB communication (LD1), power LED (LD3), user LED (LD2)
- One push-button for RESET

More information about the board can be found at the [Nucleo G431KB website](https://www.st.com/en/evaluation-tools/nucleo-g431kb.html) [[1]](#id2).

- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell.

More information about STM32G431KB can be found here:

- [STM32G431KB on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32g431kb.html) [[3]](#id6)
- [STM32G4 reference manual](https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) [[4]](#id8)

### Supported Features

The Zephyr `nucleo_g431kb` board target supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| PWM | on-chip | pwm |
| I2C | on-chip | i2c |

Other hardware features are not yet supported on this Zephyr port.

The default configuration can be found in the defconfig file:
[boards/st/nucleo\_g431kb/nucleo\_g431kb\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_g431kb/nucleo_g431kb_defconfig)

### Connections and IOs

Nucleo G431KB Board has 6 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32G4 Nucleo-32 board User Manual](https://www.st.com/resource/en/user_manual/um2397-stm32g4-nucleo32-board-mb1430-stmicroelectronics.pdf) [[2]](#id4).

#### Default Zephyr Peripheral Mapping:

- LPUART\_1\_TX : PA2
- LPUART\_1\_RX : PA3
- LD2 : PB8
- PWM\_4\_CH\_3 : PB8
- I2C\_2\_SCL : PA9
- I2C\_2\_SDA : PA8

#### System Clock

The Nucleo G431KB System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default the external oscillator is not connected to the board. Therefore only the internal
High Speed oscillator is supported. By default System clock is driven by PLL clock at 170 MHz,
the PLL is driven by the 16 MHz high speed internal oscillator.

#### Serial Port

Nucleo G431KB board has 1 U(S)ARTs and one LPUART. The Zephyr console output is assigned to LPUART1.
Default settings are 115200 8N1.

Please note that LPUART1 baudrate is limited to 9600 if the MCU is clocked by LSE (32.768 kHz) in
low power mode.

## Programming and Debugging

Nucleo G431KB Board includes an ST-Link/V3 embedded debug tool interface.

Applications for the `nucleo_g431kb` board target can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[5]](#id10) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD, or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner pyocd
```

To enable support of the STM32G431KB SoC in pyOCD, its pack has to be installed first:

```shell
$ pyocd pack --update
$ pyocd pack --install stm32g431kb
```

#### Flashing an application to Nucleo G431KB

Connect the Nucleo G431KB to your host computer using the USB port,
then run a serial host program to connect with your Nucleo board.

```shell
$ minicom -D /dev/ttyACM0
```

Now build and flash an application. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.").

```shell
# From the root of the zephyr repository
west build -b nucleo_g431kb samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! nucleo_g431kb/stm32g431xx
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_g431kb samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/nucleo-g431kb.html](https://www.st.com/en/evaluation-tools/nucleo-g431kb.html)

[[2](#id5)]

[https://www.st.com/resource/en/user\_manual/um2397-stm32g4-nucleo32-board-mb1430-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um2397-stm32g4-nucleo32-board-mb1430-stmicroelectronics.pdf)

[[3](#id7)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32g431kb.html](https://www.st.com/en/microcontrollers-microprocessors/stm32g431kb.html)

[[4](#id9)]

[https://www.st.com/resource/en/reference\_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

[[5](#id11)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)

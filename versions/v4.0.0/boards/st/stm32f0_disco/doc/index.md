---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/st/stm32f0_disco/doc/index.html
original_path: boards/st/stm32f0_disco/doc/index.html
---

# STM32F0 Discovery

Board Overview

[![../../../../_images/stm32f0_disco.jpg](../../../../_images/stm32f0_disco.jpg)
](../../../../_images/stm32f0_disco.jpg)

STM32F0 Discovery

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f051x8

## Overview

The STM32F0 Discovery development board uses an STM32F051R8T6 MCU and
integrates the ST-LINK/V2-1 debugger and programmer. It also comes with a
comprehensive STM32 software HAL library and various packaged software
examples.

More information about the board can be found at the [STM32F0DISCOVERY website](https://www.st.com/en/evaluation-tools/stm32f0discovery.html) [[1]](#id2).

## Hardware

The STM32 Discovery board features:

- STM32F051R8T6 microcontroller featuring 64 KB Flash memory, 8 KB RAM in an
  LQFP64 package
- On-board ST-LINK/V2 with selection mode switch to use the kit as a standalone
  ST-LINK/V2 (with SWD connector for programming and debugging)
- Board power supply: through USB bus or from an external 5 V supply voltage
- External application power supply: 3 V and 5 V
- Four LEDs:

  > - LD1 (red) for 3.3 V power on
  > - LD2 (red/green) for USB communication
  > - LD3 (green) for PC9 output
  > - LD4 (blue) for PC8 output
- Two push buttons (user and reset)
- Extension header for all LQFP64 I/Os for quick connection to prototyping board
  and easy probing
- An additional board is provided which can be connected to the extension
  connector for even easier prototyping and probing.
- Comprehensive free software including a variety of examples, part of
  STM32CubeF0 package or STSW-STM32049 for legacy Standard Libraries usage

More information about STM32F051R8 can be found in the [STM32F0x8 reference manual](https://www.st.com/resource/en/reference_manual/dm00031936.pdf) [[2]](#id4).

### Supported Features

The Zephyr stm32f0\_disco board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| CLOCK | on-chip | reset and clock control |
| FLASH | on-chip | flash memory |
| WATCHDOG | on-chip | independent watchdog |

Other hardware features are not yet supported in this Zephyr port.

The default configuration can be found in
[boards/st/stm32f0\_disco/stm32f0\_disco\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f0_disco/stm32f0_disco_defconfig)

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- UART\_2\_TX : PA2
- UART\_2\_RX : PA3

For more details please refer to [STM32F0DISCOVERY board User Manual](https://www.st.com/resource/en/user_manual/dm00050135.pdf) [[3]](#id6).

## Programming and Debugging

STM32F0DISCOVERY board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `stm32f0_disco` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[4]](#id8) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to Nucleo F030R8

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f0_disco samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f0_disco samples/basic/blinky
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/stm32f0discovery.html](https://www.st.com/en/evaluation-tools/stm32f0discovery.html)

[[2](#id5)]

[https://www.st.com/resource/en/reference\_manual/dm00031936.pdf](https://www.st.com/resource/en/reference_manual/dm00031936.pdf)

[[3](#id7)]

[https://www.st.com/resource/en/user\_manual/dm00050135.pdf](https://www.st.com/resource/en/user_manual/dm00050135.pdf)

[[4](#id9)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)

---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/silabs/starter_kits/efm32wg_stk3800/doc/index.html
original_path: boards/silabs/starter_kits/efm32wg_stk3800/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# EFM32 Wonder Gecko (EFM32WG-STK3800)

## Overview

The EFM32 Wonder Gecko Starter Kit EFM32WG-STK3800 contains a MCU from the
EFM32WG family built on ARM® Cortex®-M4F processor with excellent low
power capabilities.

![EFM32WG-STK3800](../../../../../_images/efm32wg_stk3800.jpg)

EFM32WG-STK3800 (image courtesy of Silicon Labs)

## Hardware

- Advanced Energy Monitoring provides real-time information about the energy
  consumption of an application or prototype design.
- 32MByte parallel NAND Flash
- 160 segment Energy Micro LCD
- 2 user buttons, 2 LEDs and a touch slider
- Ambient Light Sensor and Inductive-capacitive metal sensor
- On-board Segger J-Link USB debugger

For more information about the EFM32WG SoC and EFM32WG-STK3800 board:

- [EFM32WG Website](http://www.silabs.com/products/mcu/32-bit/efm32-wonder-gecko)
- [EFM32WG Datasheet](http://www.silabs.com/documents/public/data-sheets/EFM32WG990.pdf)
- [EFM32WG Reference Manual](http://www.silabs.com/documents/public/reference-manuals/EFM32WG-RM.pdf)
- [EFM32WG-STK3800 Website](http://www.silabs.com/products/development-tools/mcu/32-bit/efm32-wonder-gecko-starter-kit)
- [EFM32WG-STK3800 User Guide](http://www.silabs.com/documents/public/user-guides/efm32wg-stk3800-ug.pdf)
- [EFM32WG-STK3800 Schematics](http://www.silabs.com/documents/public/schematic-files/BRD2400A_A00.pdf)

### Supported Features

The efm32wg\_stk3800 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| MPU | on-chip | memory protection unit |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| FLASH | on-chip | flash memory |
| GPIO | on-chip | gpio |
| UART | on-chip | serial port-polling; serial port-interrupt |

The default configuration can be found in
[boards/silabs/starter\_kit/efm32wg\_stk3800/efm32wg\_stk3800\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kit/efm32wg_stk3800/efm32wg_stk3800_defconfig)

Other hardware features are currently not supported by the port.

### Connections and IOs

The EFM32WG SoC has six gpio controllers (PORTA to PORTF), but only three are
currently enabled (PORTB, PORTE and PORTF) for the EFM32WG-STK3800 board.

In the following table, the column Name contains Pin names. For example, PE2
means Pin number 2 on PORTE, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PE2 | GPIO | LED0 |
| PE3 | GPIO | LED1 |
| PB9 | GPIO | Push Button PB0 |
| PB10 | GPIO | Push Button PB1 |
| PF7 | GPIO | Board Controller Enable EFM\_BC\_EN |
| PE0 | UART0\_TX | UART Console EFM\_BC\_TX U0\_TX #1 |
| PE1 | UART0\_RX | UART Console EFM\_BC\_RX U0\_RX #1 |

### System Clock

The EFM32WG SoC is configured to use the 48 MHz external oscillator on the
board.

### Serial Port

The EFM32WG SoC has three USARTs, two UARTs and two Low Energy UARTs (LEUART).
UART0 is connected to the board controller and is used for the console.

## Programming and Debugging

Note

Before using the kit the first time, you should update the J-Link firmware
from [J-Link-Downloads](https://www.segger.com/downloads/jlink)

### Flashing

The EFM32WG-STK3800 includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer, which exposes a Mass Storage and a
  USB Serial Port.
- A Serial Flash device, which implements the USB flash disk file storage.
- A physical UART connection which is relayed over interface USB Serial port.

#### Flashing an application to EFM32-STK3800

The sample application [Hello World](../../../../../samples/hello_world/README.md#hello-world) is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b efm32wg_stk3800 samples/hello_world
```

Connect the EFM32WG-STK3800 to your host computer using the USB port and you
should see a USB connection which exposes a Mass Storage (STK3800) and a
USB Serial Port. Copy the generated zephyr.bin in the STK3800 drive.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should be able to see on the corresponding Serial Port
the following message:

```shell
Hello World! efm32wg_stk3800
```

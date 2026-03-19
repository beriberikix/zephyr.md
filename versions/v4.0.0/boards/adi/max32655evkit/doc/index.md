---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/adi/max32655evkit/doc/index.html
original_path: boards/adi/max32655evkit/doc/index.html
---

# MAX32655EVKIT

Board Overview

[![../../../../_images/max32655evkit_img2.jpg](../../../../_images/max32655evkit_img2.jpg)
](../../../../_images/max32655evkit_img2.jpg)

MAX32655EVKIT

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32655

## Overview

The MAX32655 evaluation kit (EV kit) provides a platform for evaluation capabilities
of the MAX32655 microcontroller, which is an advanced system-on-chip (SoC).
It features an Arm® Cortex®-M4F CPU for efficient computation of complex functions and
algorithms, integrated power management (SIMO), and the newest generation
Bluetooth® 5.0 Low Energy (Bluetooth LE), long-range radio for wearable and hearable device applications.

The Zephyr port is running on the MAX32655 MCU.

![MAX32655 EVKIT Front](../../../../_images/max32655evkit_img1.jpg)
![MAX32655 Back](../../../../_images/max32655evkit_img21.jpg)

## Hardware

- MAX32655 MCU:

  - Ultra-Low-Power Wireless Microcontroller
    - Internal 100MHz Oscillator
    - Flexible Low-Power Modes with 7.3728MHz System Clock Option
    - 512KB Flash and 128KB SRAM (Optional ECC on One 32KB SRAM Bank)
    - 16KB Instruction Cache
  - Bluetooth 5.2 LE Radio
    - Dedicated, Ultra-Low-Power, 32-Bit RISC-V Coprocessor to Offload Timing-Critical Bluetooth Processing
    - Fully Open-Source Bluetooth 5.2 Stack Available
    - Supports AoA, AoD, LE Audio, and Mesh
    - High-Throughput (2Mbps) Mode
    - Long-Range (125kbps and 500kbps) Modes
    - Rx Sensitivity: -97.5dBm; Tx Power: +4.5dBm
    - Single-Ended Antenna Connection (50Ω)
  - Power Management Maximizes Battery Life
    - 2.0V to 3.6V Supply Voltage Range
    - Integrated SIMO Power Regulator
    - Dynamic Voltage Scaling (DVS)
    - 23.8μA/MHz Active Current at 3.0V
    - 4.4μA at 3.0V Retention Current for 32KB
    - Selectable SRAM Retention + RTC in Low-Power Modes
  - Multiple Peripherals for System Control
    - Up to Two High-Speed SPI Master/Slave
    - Up to Three High-Speed I2C Master/Slave (3.4Mbps)
    - Up to Four UART, One I2S Master/Slave
    - Up to 8-Input, 10-Bit Sigma-Delta ADC 7.8ksps
    - Up to Four Micro-Power Comparators
    - Timers: Up to Two Four 32-Bit, Two LP, TwoWatchdog Timers
    - 1-Wire® Master
    - Up to Four Pulse Train (PWM) Engines
    - RTC with Wake-Up Timer
    - Up to 52 GPIOs
  - Security and Integrity​
    - Available Secure Boot
    - TRNG Seed Generator
    - AES 128/192/256 Hardware Acceleration Engine
- External devices connected to the MAX32655 EVKIT:

  - Color TFT Display
  - Audio Stereo Codec Interface
  - Digital Microphone
  - A 128Mb QSPI flash

### Supported Features

Below are the interfaces supported by Zephyr on MAX32655EVKIT.

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| CLOCK | on-chip | clock and reset control |
| GPIO | on-chip | gpio |
| UART | on-chip | serial |
| TRNG | on-chip | entropy |
| I2C | on-chip | i2c |
| DMA | on-chip | dma controller |
| Watchdog | on-chip | watchdog |
| SPI | on-chip | spi |
| ADC | on-chip | adc |
| Timer | on-chip | counter |
| PWM | on-chip | pwm |
| W1 | on-chip | one wire master |
| Flash | on-chip | flash |

### Connections and IOs

| Name | Signal | Usage |
| --- | --- | --- |
| JP1 | VREGI | Connect/Disconnect VREGIO power |
| JP2 | P0\_24 | Enable/Disable LED1 |
| JP3 | P0\_25 | Enable/Disable LED2 |
| JP4 | P2\_6/ P2\_7 | Connect/Disconnect the USB to serial UART to GPIO P2\_6 (LPUART\_RX) |
| JP5 | P2\_7/ P0\_1 | Connect/Disconnect the USB to serial UART to GPIO P2\_7 (LPUART\_TX) |
| JP6 | P0\_2 | Connect/Disconnect the USB to serial UART to GPIO P0\_2 (UART0\_CTS) |
| JP7 | P0\_3 | Connect/Disconnect he USB to serial UART to GPIO P0\_3 (UART0\_RTS) |
| JP8 | VREGI | Select VDDIO\_EN power source (3V3 or coin cell) |
| JP9 | VDDIOH\_EN | Select VDDIOH\_EN power source 3V3/VREGI |
| JP10 | VDDIOH | Connect/Disconnect VDDIOH power |
| JP11 | VDDIO\_EN | Select VDDIO\_EN power source 1V8/VREGO\_A |
| JP12 | VDDIO | Connect/Disconnect VDDIO power |
| JP13 | VDDA\_EN | Select VDDA\_EN power source 1V8/VREGO\_A |
| JP14 | VDDA | Connect/Disconnect VDDA power |
| JP15 | VCOREA\_EN | Select VCOREA\_EN power source 1V1/VREGO\_C |
| JP16 | VCOREA | Connect/Disconnect VCOREA power |
| JP17 | VCOREB\_EN | Select VCOREB\_EN power source 1V1/VREGO\_B |
| JP18 | VCOREB | Connect/Disconnect VCOREB power |
| JP19 | BLE\_LDO | Connect/Disconnect BLE\_LDO power |
| JP20 | VREF | Select VREF power source VDDIO/VDDIOH |
| JP21 | I2C0\_PU | Select I2C0\_PU power source VDDIO/VDDIOH |
| JP22 | I2C1\_PU | Select I2C1\_PU power source VDDIO/VDDIOH |
| JP23 | BOARD RESET | Connect/Disconnect RV JTAG NRESET from the BOARD RESET circuitry |

## Programming and Debugging

### Flashing

The MAX32655 MCU can be flashed by connecting an external debug probe to the
SWD port. SWD debug can be accessed through the Cortex 10-pin connector, JH3.
Logic levels are fixed to VDDIO (1.8V).

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash.

Note

This board uses OpenOCD as the default debug interface. You can also use
a Segger J-Link with Segger’s native tooling by overriding the runner,
appending `--runner jlink` to your `west` command(s). The J-Link should
be connected to the standard 2\*5 pin debug connector (JW3) using an
appropriate adapter board and cable.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX32655EVKIT web page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max32655evkit.html#eb-overview)

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/adi/max32666evkit/doc/index.html
original_path: boards/adi/max32666evkit/doc/index.html
---

# MAX32666EVKIT

Board Overview

[![../../../../_images/max32666evkit.webp](../../../../_images/max32666evkit.webp)
](../../../../_images/max32666evkit.webp)

MAX32666EVKIT

Name:
:   `max32666evkit`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32666

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32666evkit/doc/index.rst/../..)

## Overview

The MAX32666EVKIT provides a platform for evaluating the capabilities of the MAX32665 and MAX32666
high-efficiency Arm® microcontrollers and audio DSP for wearable and hearable device applications.

The Zephyr port is running on the MAX32666 MCU.

## Hardware

- MAX32666 MCU:

  - High-Efficiency Microcontroller and Audio DSP for Wearable and Hearable Devices

    - Arm Cortex-M4 with FPU Up to 96MHz
    - Optional Second Arm Cortex-M4 with FPU Optimized for Data Processing
    - Low-Power 7.3728MHz System Clock Option
    - 1MB Flash, Organized into Dual Banks 2 x 512KB
    - 560KB (448KB ECC) SRAM; 3 x 16KB Cache
    - Optional Error Correction Code (ECC-SEC-DED)for Cache, SRAM, and Internal Flash
  - Bluetooth 5 Low Energy Radio

    - 1Mbps and 2Mbps Data Throughput
    - Long Range (125kbps and 500kbps)
    - Advertising Extension
    - Rx Sensitivity: -95dbm; Tx Power Up to +4.5dbm
    - On-Chip Matching with Single-Ended Antenna Port
  - Power Management Maximizes Operating Time for Battery Applications

    - Integrated SIMO SMPS for Coin-Cell Operation
    - Dynamic Voltage Scaling Minimizes Active Core Power Consumption
    - 27.3μA/MHz at 3.3V Executing from Cache
    - Selectable SRAM Retention in Low Power Modes with RTC Enabled
  - Multiple Peripherals for System Control

    - Three QSPI Master/Slave with Three Chip Selects Each
    - Three 4-Wire UARTs
    - Three I2C Master/Slave
    - Up to 50 GPIO
    - QSPI (SPIXF) with Real-Time Flash Decryption
    - QSPI (SPIXR) RAM Interface Provides SRAMExpansion
    - 8-Input 10-Bit Delta-Sigma ADC 7.8ksps
    - USB 2.0 HS Engine with Internal Transceiver
    - PDM Interface Supports Two Digital Microphones
    - I2S with TDM
    - Six 32-Bit Timers
    - Two High-Speed Timers
    - 1-Wire Master
    - Sixteen Pulse Trains (PWM)
    - Secure Digital Interface Supports SD3.0/SDIO3.0/eMMC4.51
  - Secure Valuable IP/Data with Hardware Security

    - Trust Protection Unit (TPU) with MAA SupportsFast ECDSA and Modular Arithmetic
    - AES128/192/256, DES, 3DES, Hardware Accelerator
    - TRNG Seed Generator
    - SHA-2 Accelerator•Secure Bootloader
- Benefits and Features of MAX32666EVKIT:

  - Bluetooth SMA connector with a 2.4GHz Hinged Whip Antenna
  - 1.28in 128 x 128 Monochrome TFT Display
  - 64MB XIP Flash
  - 1MB XIP RAM
  - Stereo Audio Codec with Line-In and Line-Out 3.5mm Jacks
  - Digital Audio Microphone
  - USB 2.0 Micro B Interface
  - USB 2.0 Micro B to Serial UARTs
  - Micro SD Card Interface
  - Select GPIOs Accessed Through a 0.1in Header
  - Access to the 8 Analog Inputs Through a 0.1in Header
  - Arm® or SWD JTAG 20-Pin Header
  - 1-Wire RJ11 Port
  - Can Be Solely Sourced by a Coin Cell Battery
  - Board Power Provided by Either USB Port
  - Individual Power Measurement on All IC Rails Through Jumpers
  - On-Board 1.8V and 3.3V Regulators
  - Two General-Purpose LEDs and Two General-Purpose Pushbutton Switches

### Supported Features

Below interfaces are supported by Zephyr on MAX32666EVKIT.

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| CLOCK | on-chip | clock and reset control |
| GPIO | on-chip | gpio |
| UART | on-chip | serial |
| TRNG | on-chip | entropy |
| Watchdog | on-chip | watchdog |
| DMA | on-chip | dma controller |
| I2C | on-chip | i2c |
| ADC | on-chip | adc |
| Timer | on-chip | counter |
| PWM | on-chip | pwm |
| W1 | on-chip | one wire master |
| Flash | on-chip | flash |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| JP1 | I2C0\_SCL/SDA | | Open | | --- | | Close | | | Disconnects I2C0 SCL and SDA 1.5K pullups from VDDIOH. | | --- | | Connects I2C0 SCL and SDA 1.5K pullups to VDDIOH. | |
| JP2 | I2C1\_SCL/SDA | | Open | | --- | | Close | | | Disconnects I2C1 SCL and SDA 1.5K pullups from VDDIOH. | | --- | | Connects I2C1 SCL and SDA 1.5K pullups to VDDIOH. | |
| JP3 | I2C2\_SCL/SDA | | Open | | --- | | Close | | | Disconnects I2C2 SCL and SDA 1.5K pullups from VDDIOH. | | --- | | Connects I2C2 SCL and SDA 1.5K pullups to VDDIOH. | |
| JP4 | P1\_14 | | Open | | --- | | Close | | | Disconnects LED D2 from P1\_14. | | --- | | Connects LED D2 to P1\_14. | |
| JP5 | P1\_15 | | Open | | --- | | Close | | | Disconnects LED D3 from P1\_15. | | --- | | Connects LED D3 to P1\_15. | |
| JP6 | VBUS | | 2-1 | | --- | | 2-3 | | | Connects VBUS to USB connector CN1 to supply board power. | | --- | | Connects VBUS to USB connector CN2 to supply board power. | |
| JP7 | N/A | N/A | N/A |
| JP8 | N/A | N/A | N/A |
| JP9 | | P0\_20 | | --- | | P0\_28 | | | 2-1 | | --- | | 2-3 | | | Connects the USB to serial UART to GPIO P0\_20 (RX1). | | --- | | Connects the USB to serial UART to GPIO P0\_28 (RX2). | |
| JP10 | | P0\_21 | | --- | | P0\_29 | | | 2-1 | | --- | | 2-3 | | | Connects the USB to serial UART to GPIO P0\_21 (TX1). | | --- | | Connects the USB to serial UART to GPIO P0\_29 (TX2). | |
| JP11 | | P0\_22 | | --- | | P0\_30 | | | 2-1 | | --- | | 2-3 | | | Connects the USB to serial UART to GPIO P0\_22 (CTS1\_N). | | --- | | Connects the USB to serial UART to GPIO P0\_30 (CTS2\_N). | |
| JP12 | | P0\_23 | | --- | | P0\_31 | | | 2-1 | | --- | | 2-3 | | | Connects the USB to serial UART to GPIO P0\_23 (RTS1\_N). | | --- | | Connects the USB to serial UART to GPIO P0\_31 (RTS2\_N). | |
| JP13 | VREGI | | 2-1 | | --- | | 2-3 | | | Connects VREGI to the coin cell battery. | | --- | | Connects VREGI to 3V3. | |
| JP14 | VDDIOH | | 1-2 | | --- | | 3-4 | | 5-6 | | | Connects VDDIOH to VREGO\_A | | --- | | Connects VDDIOH to 1V8. | | Connects VDDIOH to 3V3. | |
| JP15 | VDDIOH | | Open | | --- | | Close | | | Disconnects power from VDDIOH. | | --- | | Connects power to VDDIOH. | |
| JP16 | VDDB | | Open | | --- | | Close | | | Disconnects power from VDDB. | | --- | | Connects power to VDDB. | |
| JP17 | VDDIO | | 2-1 | | --- | | 2-3 | | | Connects VDDIO to VREGO\_A. | | --- | | Connects VDDIO to 1V8. | |
| JP18 | VDDIO | | Open | | --- | | Close | | | Disconnects power from VDDIO. | | --- | | Connects power to VDDIO. | |
| JP19 | VDDA | | Open | | --- | | Close | | | Disconnects power from VDDA. | | --- | | Connects power to VDDA. | |
| JP20 | VCORE\_A | | Open | | --- | | Close | | | Disconnects power from VCORE\_A. | | --- | | Connects power to VCORE\_A. | |
| JP21 | VCORE\_B | | Open | | --- | | Close | | | Disconnects power from VCORE\_B. | | --- | | Connects power to VCORE\_B. | |
| JP22 | VTXIN | | Open | | --- | | Close | | | Disconnects power from VTXIN. | | --- | | Connects power to VTXIN. | |
| JP23 | VRXIN | | Open | | --- | | Close | | | Disconnects power from VRXIN. | | --- | | Connects power to VRXIN. | |

## Programming and Debugging

### Flashing

The MAX32666 MCU can be flashed by connecting an external debug probe to the
SWD port. SWD debug can be accessed through the Cortex 10-pin connector, J6.
Logic levels are fixed to VDDIOH (1.8V or 3.3V).

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash. To perform a full erase,
pass the `--erase` option when executing `west flash`.

Note

This board uses OpenOCD as the default debug interface. You can also use
a Segger J-Link with Segger’s native tooling by overriding the runner,
appending `--runner jlink` to your `west` command(s). The J-Link should
be connected to the standard 20-pin connector (J7) or a Cortex® 10-pin connector (J6).

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX32666EVKIT web page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/MAX32666EVKIT.html)

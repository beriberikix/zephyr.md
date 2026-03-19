---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/m5stack/m5stack_core2/doc/index.html
original_path: boards/m5stack/m5stack_core2/doc/index.html
---

# Core2

Board Overview

[![../../../../_images/m5stack_core2.webp](../../../../_images/m5stack_core2.webp)
](../../../../_images/m5stack_core2.webp)

Core2

Vendor:
:   M5Stack

Architecture:
:   xtensa

SoC:
:   esp32

## Overview

M5Stack Core2 is an ESP32-based development board from M5Stack. It is the successor for the Core module.

M5Stack Core2 features the following integrated components:

- ESP32-D0WDQ6-V3 chip (240MHz dual core, 600 DMIPS, 520KB SRAM, Wi-Fi)
- PSRAM 8MB
- Flash 16MB
- LCD IPS TFT 2”, 320x240 px screen (ILI9342C)
- Touch screen (FT6336U)
- PMU AXP192
- Audio NS4168 amplifier (1W-092 speaker)
- Vibration motor
- RTC BM8563
- USB CP2104
- SD-Card slot
- Grove connector
- IMO 6-axis IMU MPU6886
- MIC SPM1423
- Battery 390mAh 3,7V

## Functional Description

The following table below describes the key components, interfaces, and controls
of the M5Stack Core2 board.

| Key Component | Description | Status |
| --- | --- | --- |
| ESP32-D0WDQ6-V2 module | This [MPU-ESP32](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/esp32_datasheet_en_v3.9.pdf) module provides complete Wi-Fi and Bluetooth functionalities and integrates a 16-MB SPI flash. | supported |
| 32.768 kHz RTC | External precision 32.768 kHz crystal oscillator serves as a clock with low-power consumption while the chip is in Deep-sleep mode. | supported |
| Status LED | One user LED connected to the GPIO pin. | supported |
| USB Port | USB interface. Power supply for the board as well as the communication interface between a computer and the board. Contains: TypeC x 1, GROVE(I2C+I/O+UART) x 1 | supported |
| Reset button | Reset button | supported |
| Power Switch | Power on/off button. | supported |
| LCD screen | Built-in LCD TFT display ([LCD-ILI9342C](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf), 2”, 320x240 px) controlled via SPI interface | supported |
| SD-Card slot | SD-Card connection via SPI-mode. | supported |
| 6-axis IMU MPU6886 | The [MPU-6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf) is a 6-axis motion tracker (6DOF IMU) device that combines a 3-axis gyroscope and a 3-axis accelerometer. For details please refer to [M5Stack-Core2 base shield](../../../shields/m5stack_core2_ext/doc/index.md#m5stack-core2-ext) | supported |
| Grove port | Note: Grove port requires 5V to be enabled via `bus_5v` regulator | supported |
| Built-in microphone | The [SPM-1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf) I2S driven microphone. | todo |
| Built-in speaker | 1W speaker for audio output via I2S interface. | todo |
| Battery-support | Power supply via battery is supported automatically. But there is no possibility to query current battery status. | todo |

### Power supply

M5Stack Core2 module is equipped with the feature-rich power management IC
([`x-powers,axp192-regulator`](../../../../build/dts/api/bindings/regulator/x-powers%2Caxp192-regulator.md#std-dtcompatible-x-powers-axp192-regulator)).
Following regulators are utilized on this module:

- **vdd\_mcu**:
  Main power supply for the MCU.
- **lcd\_bg**:
  Display backlight voltage.
- **v\_peri**:
  Periphal supply. This regulator controls supply for the display, SD-Card.
- **vib\_motor**:
  Vibration motor regulator.
- **bus\_5v**
  BUS\_5V supply for Grove port.
  Note: This fixed regulator supply is disabled by default.

These voltages can be controlled via regulator api.

### Supported Features

The Zephyr m5stack\_core2 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| CLOCK | on-chip | reset and clock control |
| COUNTER | on-chip | rtc |
| WATCHDOG | on-chip | independent watchdog |
| PWM | on-chip | pwm |
| ADC | on-chip | adc |
| DAC | on-chip | dac |
| die-temp | on-chip | die temperature sensor |

## Start Application Development

Before powering up your M5Stack Core2, please make sure that the board is in good
condition with no obvious signs of damage.

### System requirements

#### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order work. Run the command
below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

#### Building & Flashing

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b m5stack_core2/esp32/procpu samples/hello_world
```

The usual `flash` target will work with the `m5stack_core2` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
application.

```shell
# From the root of the zephyr repository
west build -b m5stack_core2/esp32/procpu samples/hello_world
west flash
```

The baud rate of 921600bps is set by default. If experiencing issues when flashing,
try using different values by using `--esp-baud-rate <BAUD>` option during
`west flash` (e.g. `west flash --esp-baud-rate 115200`).

You can also open the serial monitor using the following command:

```shell
west espressif monitor
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! m5stack_core2
```

#### Debugging

M5Stack Core2 debugging is not supported due to pinout limitations.

## Related Documents

- [M5Stack-Core2 schematic](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/CORE2_V1.0_SCH.pdf) (PDF)
- [ESP32-PICO-D4 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-pico-d4_datasheet_en.pdf) (PDF)
- [M5Stack-Core2 docs](https://docs.m5stack.com/en/core/core2)
- [ESP32 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) (PDF)
- [ESP32 Hardware Reference](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/index.html)

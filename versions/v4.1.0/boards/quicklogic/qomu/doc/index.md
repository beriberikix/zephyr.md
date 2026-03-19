---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/quicklogic/qomu/doc/index.html
original_path: boards/quicklogic/qomu/doc/index.html
---

# Qomu

Board Overview

[![../../../../_images/qomu-board.png](../../../../_images/qomu-board.png)
](../../../../_images/qomu-board.png)

Qomu

Name:
:   `qomu`

Vendor:
:   QuickLogic Corp.

Architecture:
:   arm

SoC:
:   quicklogic\_eos\_s3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/quicklogic/qomu/doc/index.rst/../..)

## Overview

The Qomu board is a platform with an on-board QuickLogic EOS S3 Sensor Processing Platform.

## Hardware

- QuickLogic EOS S3 MCU Platform
- 16 Mbit of on-board flash memory
- Touchpads (4)
- RGB LED
- Powered from USB

Detailed information about the board can be found in a [Qomu repository](https://github.com/QuickLogic-Corp/qomu-dev-board) [[1]](#id2) and [Qomu User Guide](https://github.com/QuickLogic-Corp/qomu-dev-board/blob/master/doc/Qomu_UserGuide.pdf) [[2]](#id4).

### Connections and IOs

Detailed information about pinouts is available in the [schematics document](https://github.com/QuickLogic-Corp/qomu-dev-board/blob/master/doc/qomu-board.pdf) [[3]](#id6).

## Programming

The Qomu platform by default boots from flash.

Below are steps to run Qomu sample application:

1. Build the sample in an usual way:

   ```shell
   # From the root of the zephyr repository
   west build -b qomu samples/boards/quicklogic/qomu
   ```
2. Remove Qomu board from USB port.
3. Insert Qomu board to USB port.
4. While the blue LED is blinking (for 5 seconds), touch the touch-pads with your finger.
   On success, the green led will start flashing.
5. Use TinyFpgaProgrammer application to load the target application:

   ```shell
   python3 /path/to/TinyFPGA-Programmer-Application/tinyfpga-programmer-gui.py --mode m4 --m4app build/zephyr/zephyr.bin --reset
   ```

   Refer to [TinyFPGA Programmer Application repo](https://github.com/QuickLogic-Corp/TinyFPGA-Programmer-Application) [[4]](#id8) for detailed information on installation
   and program usage.

## References

[[1](#id3)]

[https://github.com/QuickLogic-Corp/qomu-dev-board](https://github.com/QuickLogic-Corp/qomu-dev-board)

[[2](#id5)]

[https://github.com/QuickLogic-Corp/qomu-dev-board/blob/master/doc/Qomu\_UserGuide.pdf](https://github.com/QuickLogic-Corp/qomu-dev-board/blob/master/doc/Qomu_UserGuide.pdf)

[[3](#id7)]

[https://github.com/QuickLogic-Corp/qomu-dev-board/blob/master/doc/qomu-board.pdf](https://github.com/QuickLogic-Corp/qomu-dev-board/blob/master/doc/qomu-board.pdf)

[[4](#id9)]

[https://github.com/QuickLogic-Corp/TinyFPGA-Programmer-Application](https://github.com/QuickLogic-Corp/TinyFPGA-Programmer-Application)

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/qomu/doc/index.html
original_path: boards/arm/qomu/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Qomu

## Overview

The Qomu board is a platform with an on-board QuickLogic EOS S3 Sensor Processing Platform.

![Qomu](../../../../_images/qomu-board.png)

Qomu (Credit: QuickLogic)

## Hardware

- QuickLogic EOS S3 MCU Platform
- 16 Mbit of on-board flash memory
- Touchpads (4)
- RGB LED
- Powered from USB

Detailed information about the board can be found in a [Qomu repository](https://github.com/QuickLogic-Corp/qomu-dev-board) [[1]](#id3) and [Qomu User Guide](https://github.com/QuickLogic-Corp/qomu-dev-board/blob/master/doc/Qomu_UserGuide.pdf) [[2]](#id5).

### Connections and IOs

Detailed information about pinouts is available in the [schematics document](https://github.com/QuickLogic-Corp/qomu-dev-board/blob/master/doc/qomu-board.pdf) [[3]](#id7).

## Programming

The Qomu platform by default boots from flash.

Below are steps to run Qomu sample application:

1. Build the sample in an usual way:

   ```shell
   # From the root of the zephyr repository
   west build -b qomu samples/boards/qomu
   ```
2. Remove Qomu board from USB port.
3. Insert Qomu board to USB port.
4. While the blue LED is blinking (for 5 seconds), touch the touch-pads with your finger.
   On success, the green led will start flashing.
5. Use TinyFpgaProgrammer application to load the target application:

   ```shell
   python3 /path/to/TinyFPGA-Programmer-Application/tinyfpga-programmer-gui.py --mode m4 --m4app build/zephyr/zephyr.bin --reset
   ```

   Refer to [TinyFPGA Programmer Application repo](https://github.com/QuickLogic-Corp/TinyFPGA-Programmer-Application) [[4]](#id9) for detailed information on installation
   and program usage.

## References

[[1](#id4)]

[https://github.com/QuickLogic-Corp/qomu-dev-board](https://github.com/QuickLogic-Corp/qomu-dev-board)

[[2](#id6)]

[https://github.com/QuickLogic-Corp/qomu-dev-board/blob/master/doc/Qomu\_UserGuide.pdf](https://github.com/QuickLogic-Corp/qomu-dev-board/blob/master/doc/Qomu_UserGuide.pdf)

[[3](#id8)]

[https://github.com/QuickLogic-Corp/qomu-dev-board/blob/master/doc/qomu-board.pdf](https://github.com/QuickLogic-Corp/qomu-dev-board/blob/master/doc/qomu-board.pdf)

[[4](#id10)]

[https://github.com/QuickLogic-Corp/TinyFPGA-Programmer-Application](https://github.com/QuickLogic-Corp/TinyFPGA-Programmer-Application)

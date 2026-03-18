---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/modules/tflite-micro/magic_wand/README.html
original_path: samples/modules/tflite-micro/magic_wand/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# TensorFlow Lite Micro Magic Wand sample

## Overview

This sample application shows how to use TensorFlow Lite Micro
to run a 20 kilobyte neural network model that recognizes gestures
from an accelerometer.

Note

This README and sample have been modified from
[the TensorFlow Magic Wand sample for Zephyr](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/examples/magic_wand) and
[the Antmicro tutorial on Renode emulation for TensorFlow](https://github.com/antmicro/litex-vexriscv-tensorflow-lite-demo).

## Building and Running

The application can be built for the [LiteX VexRiscv](../../../../boards/riscv/litex_vexriscv/doc/index.md#litex-vexriscv) for
emulation in Renode as follows:

```shell
west build -b litex_vexriscv samples/modules/tflite-micro/magic_wand
```

Once the application is built, [download and install Renode 1.12 or higher as a package](https://github.com/renode/renode/releases/)
following the instructions in the [Renode GitHub README](https://github.com/renode/renode/blob/master/README.rst) and
start the emulator:

```shell
renode -e "set zephyr_elf @./build/zephyr/zephyr.elf; s @./samples/modules/tflite-micro/magic_wand/renode/litex-vexriscv-tflite.resc"
```

### Sample Output

The Renode-emulated LiteX/VexRiscv board is fed data that the
application recognizes as a series of alternating ring and slope
gestures.

```shell
Got accelerometer, label: accel-0

RING:
          *
       *     *
     *         *
    *           *
     *         *
       *     *
          *

SLOPE:
        *
       *
      *
     *
    *
   *
  *
 * * * * * * * *

RING:
          *
       *     *
     *         *
    *           *
     *         *
       *     *
          *

SLOPE:
        *
       *
      *
     *
    *
   *
  *
 * * * * * * * *
```

## Modifying Sample for Your Own Project

It is recommended that you copy and modify one of the two TensorFlow
samples when creating your own TensorFlow project. To build with
TensorFlow, you must enable the below Kconfig options in your `prj.conf`:

```kconfig
CONFIG_CPP=y
CONFIG_REQUIRES_FULL_LIBC=y
CONFIG_TENSORFLOW_LITE_MICRO=y
```

## Training

Follow the instructions in the `train/` directory to train your
own model for use in the sample.

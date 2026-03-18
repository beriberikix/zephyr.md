---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/boards/qomu/README.html
original_path: samples/boards/qomu/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Zephyr usbserial driver on Qomu

This sample demonstrates how to load bitstream on EOS-S3 FPGA and use the
usbserial driver.

## Requirements

- Zephyr RTOS with printk enabled
- [QuickLogic Qomu board](https://www.quicklogic.com/products/eos-s3/quickfeather-development-kit/)

## Building

```shell
west build -b qomu samples/boards/qomu
```

## Flashing

To load example into Qomu you can use [TinyFPGA-Programmer-Application](https://github.com/QuickLogic-Corp/TinyFPGA-Programmer-Application).

```shell
python3 /PATH/TO/BASE/DIR/TinyFPGA-Programmer-Application/tinyfpga-programmer-gui.py --mode m4 --m4app build/zephyr/zephyr.bin --reset
```

See [Qomu User Guide](https://github.com/QuickLogic-Corp/qomu-dev-board/blob/662f8841bdc1ed35c1539ac381182159d7cd5914/doc/Qomu_UserGuide.pdf) on how to load an image to the board.

## Running

After connecting to the shell console you should see the following output:

```shell
####################
I am Zephyr on Qomu!
####################
```

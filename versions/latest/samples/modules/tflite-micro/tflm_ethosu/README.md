---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/modules/tflite-micro/tflm_ethosu/README.html
original_path: samples/modules/tflite-micro/tflm_ethosu/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Arm(R) Ethos(TM)-U Tensorflow Lite for Microcontrollers test application

A sample application that demonstrates how to run an inference using the TFLM
framework and the Arm Ethos-U NPU.

The sample application runs a model that has been downloaded from the
[Arm model zoo](https://github.com/ARM-software/ML-zoo). This model has then
been optimized using the
[Vela compiler](https://git.mlplatform.org/ml/ethos-u/ethos-u-vela.git).

Vela takes a tflite file as input and produces another tflite file as output,
where the operators supported by Ethos-U have been replaced by an Ethos-U custom
operator. In an ideal case the complete network would be replaced by a single
Ethos-U custom operator.

## Building and running

This application can be built and run on any Arm Ethos-U capable platform, for
example Corstone(TM)-300. A reference implementation of Corstone-300 can be
downloaded either as a FPGA bitfile for the
[MPS3 FPGA prototyping board](https://developer.arm.com/tools-and-software/development-boards/fpga-prototyping-boards/mps3),
or as a
[Fixed Virtual Platform](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)
that can be emulated on a host machine.

Assuming that the Corstone-300 FVP has been downloaded, installed and added to
the `PATH` variable, then building and testing can be done with following
commands.

```shell
$ west build -b mps3_an547 zephyr/samples/modules/tflite-micro/tflm_ethosu
$ FVP_Corstone_SSE-300_Ethos-U55 build/zephyr/zephyr.elf
```

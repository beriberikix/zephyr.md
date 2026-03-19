---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/fxos8700/README.html
original_path: samples/sensor/fxos8700/README.html
---

# FXOS8700 Accelerometer/Magnetometer Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/fxos8700/README.rst/..)

## Overview

This sample application shows how to use the FXOS8700 driver.
The driver supports FXOS8700 accelerometer/magnetometer and
MMA8451Q, MMA8652FC, MMA8653FC accelerometers.

## Building and Running

This project outputs sensor data to the console. FXOS8700
sensor is present on the [FRDM-K64F](../../../boards/nxp/frdm_k64f/doc/index.md#frdm_k64f), [FRDM-K22F](../../../boards/nxp/frdm_k22f/doc/index.md#frdm_k22f),
[FRDM-KW41Z](../../../boards/nxp/frdm_kw41z/doc/index.md#frdm_kw41z), [Hexiwear](../../../boards/nxp/hexiwear/doc/index.md#hexiwear), and [TWR-KE18F](../../../boards/nxp/twr_ke18f/doc/index.md#twr_ke18f) boards.
Accelerometer only devices are present on the [FRDM-KL25Z](../../../boards/nxp/frdm_kl25z/doc/index.md#frdm_kl25z),
[micro:bit](../../../boards/bbc/microbit/doc/index.md#bbc_microbit), and [reel board](../../../boards/phytec/reel_board/doc/index.md#reel-board) boards. It does not work on
QEMU.

### Building and Running for FRDM-K64F

FRDM-K64F is equipped with FXOS8700CQ accelerometer and magnetometer.
Sample can be built and executed for the FRDM-K64F as follows:

```shell
west build -b frdm_k64f samples/sensor/fxos8700
west flash
```

Example building for the FRDM-K64F with motion detection support:

```shell
west build -b frdm_k64f samples/sensor/fxos8700 -- -DCONF_FILE="prj.conf overlay-motion.conf"
west flash
```

### Building and Running for FRDM-K22F

FRDM-K22F is equipped with FXOS8700CQ accelerometer and magnetometer.
Sample can be built and executed for the FRDM-K22F as follows:

```shell
west build -b frdm_k22f samples/sensor/fxos8700
west flash
```

Example building for the FRDM-K22F with motion detection support:

```shell
west build -b frdm_k22f samples/sensor/fxos8700 -- -DCONF_FILE="prj.conf overlay-motion.conf"
west flash
```

### Building and Running for TWR-KE18F

TWR-KE18F is equipped with FXOS8700CQ accelerometer and magnetometer.
The FXOS8700CQ IRQ lines, however, are not connected by default, so
motion detection is not supported.

Sample can be built and executed for the TWR-KE18F as follows:

```shell
west build -b twr_ke18f samples/sensor/fxos8700
west flash
```

### Building and Running for FRDM-KL25Z

FRDM-KL25Z is equipped with MMA8451Q accelerometer.
Sample can be built and executed for the FRDM-KL25Z as follows:

```shell
west build -b frdm_kl25z samples/sensor/fxos8700 -- -DCONF_FILE="prj_accel.conf"
west flash
```

### Building and Running for Micro Bit

Micro Bit is equipped with MMA8653FC accelerometer.
Sample can be built and executed for the Micro Bit as follows:

```shell
west build -b bbc_microbit samples/sensor/fxos8700 -- -DCONF_FILE="prj_accel.conf"
west flash
```

### Building and Running for reel board

The reel board is equipped with MMA8652FC accelerometer.
Sample can be built and executed for the reel board as follows:

```shell
west build -b reel_board samples/sensor/fxos8700 -- -DCONF_FILE="prj_accel.conf"
west flash
```

### Building and Running for MIMXRT685-EVK

MIMXRT685-EVK is equipped with FXOS8700CQ accelerometer and magnetometer.
Sample can be built and executed for the MIMXRT685-EVK as follows:

```shell
west build -b mimxrt685_evk/mimxrt685s/cm33 samples/sensor/fxos8700
west flash
```

### Building and Running for MIMXRT595-EVK

MIMXRT595-EVK is optionally equipped with FXOS8700CQ accelerometer and magnetometer.
Please confirm the FXOS8700CQ(U6) is populated on your board.
Sample can be built and executed for the MIMXRT595-EVK as follows:

```shell
west build -b mimxrt595_evk/mimxrt595s/cm33 samples/sensor/fxos8700
west flash
```

### Sample Output

```shell
AX= -0.191537 AY=  0.067037 AZ=  9.902418 MX=  0.379000 MY=  0.271000 MZ= -0.056000 T= 22.080000
AX= -0.162806 AY=  0.143652 AZ=  9.940725 MX=  0.391000 MY=  0.307000 MZ= -0.058000 T= 22.080000
AX= -0.172383 AY=  0.134075 AZ=  9.969455 MX=  0.395000 MY=  0.287000 MZ= -0.017000 T= 22.080000
AX= -0.210690 AY=  0.105344 AZ=  9.911994 MX=  0.407000 MY=  0.306000 MZ= -0.068000 T= 22.080000
AX= -0.153229 AY=  0.124498 AZ=  9.950302 MX=  0.393000 MY=  0.301000 MZ= -0.021000 T= 22.080000
AX= -0.153229 AY=  0.095768 AZ=  9.921571 MX=  0.398000 MY=  0.278000 MZ= -0.040000 T= 22.080000
AX= -0.162806 AY=  0.105344 AZ=  9.902418 MX=  0.372000 MY=  0.300000 MZ= -0.046000 T= 22.080000
```

<repeats endlessly>

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)

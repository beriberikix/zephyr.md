---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/stream_fifo/README.html
original_path: samples/sensor/stream_fifo/README.html
---

# Generic device FIFO streaming

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/stream_fifo/README.rst/..)

## Overview

This sample application demonstrates how to stream FIFO data using the [RTIO framework](../../../services/rtio/index.md#rtio).

The streaming is started using the sensor\_stream() API and it is self-sustained by the
SENSOR\_TRIG\_FIFO\_WATERMARK trigger.

Currently the sample gets/prints data for the following sensor channels:

- SENSOR\_CHAN\_ACCEL\_XYZ
- SENSOR\_CHAN\_GYRO\_XYZ
- SENSOR\_CHAN\_DIE\_TEMP
- SENSOR\_CHAN\_GAME\_ROTATION\_VECTOR
- SENSOR\_CHAN\_GRAVITY\_VECTOR
- SENSOR\_CHAN\_GBIAS\_XYZ

## Building and Running

This sample supports up to 10 FIFO streaming devices. Each device needs
to be aliased as `streamN` where `N` goes from `0` to `9`. For example:

```devicetree
/ {
    aliases {
                 stream0 = &lsm6dsv16x_6b_x_nucleo_iks4a1;
            };
    };
```

Note

Note that NUM\_SENSORS defined in main.c must match `N` and should be set accordingly.

Example devicetree overlays and configurations are already available for nucleo\_f401re and
nucleo\_h503rb in the boards directory:

- [samples/sensor/stream\_fifo/boards/nucleo\_f401re.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/stream_fifo/boards/nucleo_f401re.overlay)

  DT overlay file for the nucleo\_f401re board.
- [samples/sensor/stream\_fifo/boards/nucleo\_f401re.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/stream_fifo/boards/nucleo_f401re.conf)

  Configuration file for the nucleo\_f401re board.
- [samples/sensor/stream\_fifo/boards/nucleo\_h503rb.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/stream_fifo/boards/nucleo_h503rb.overlay)

  DT overlay file for the nucleo\_h503rb board.
- [samples/sensor/stream\_fifo/boards/nucleo\_h503rb.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/stream_fifo/boards/nucleo_h503rb.conf)

  Configuration file for the nucleo\_h503rb board.

For example, build and run sample for nucleo\_h503rb with:

```shell
west build -b nucleo_h503rb samples/sensor/stream_fifo
west flash
```

### Sample Output

The following example output is for lsm6dsv16x IMU device with accelerometer, gyroscope
and temperature sensor including also the Sensor Fusion Low Power (SFLP) information.
The FIFO watermark is set to 64. The board used is a nucleo\_h503rb
equipped with a [X-NUCLEO-IKS4A1: MEMS Inertial and Environmental Multi sensor shield](../../../boards/shields/x_nucleo_iks4a1/doc/index.md#x-nucleo-iks4a1) shield.

```shell
FIFO count - 64
XL data for lsm6dsv16x@6b 1680572433340ns (0.373229, -0.009569, 9.909734)
XL data for lsm6dsv16x@6b 1680639100006ns (0.354089, -0.023924, 9.909734)
XL data for lsm6dsv16x@6b 1680705766672ns (0.368444, 0.000000, 9.933659)
XL data for lsm6dsv16x@6b 1680772433338ns (0.373229, 0.000000, 9.924089)
XL data for lsm6dsv16x@6b 1680839100004ns (0.368444, -0.004784, 9.924089)
XL data for lsm6dsv16x@6b 1680905766670ns (0.363659, -0.009569, 9.924089)
XL data for lsm6dsv16x@6b 1680972433336ns (0.358874, -0.004784, 9.928874)
XL data for lsm6dsv16x@6b 1681039100002ns (0.363659, 0.004784, 9.928874)
GY data for lsm6dsv16x@6b 1680572433340ns (0.001524, -0.000609, 0.004269)
GY data for lsm6dsv16x@6b 1680639100006ns (-0.001219, 0.002134, 0.004879)
GY data for lsm6dsv16x@6b 1680705766672ns (0.001219, -0.001219, 0.004879)
GY data for lsm6dsv16x@6b 1680772433338ns (-0.000914, 0.001219, 0.003964)
GY data for lsm6dsv16x@6b 1680839100004ns (0.000914, -0.001219, 0.004574)
GY data for lsm6dsv16x@6b 1680905766670ns (0.001829, 0.000914, 0.005489)
GY data for lsm6dsv16x@6b 1680972433336ns (-0.000609, 0.000304, 0.004574)
GY data for lsm6dsv16x@6b 1681039100002ns (0.001829, 0.000304, 0.004879)
TP data for lsm6dsv16x@6b 1680572433340ns 24.347656 °C
TP data for lsm6dsv16x@6b 1680639100006ns 24.324218 °C
TP data for lsm6dsv16x@6b 1680705766672ns 24.316406 °C
TP data for lsm6dsv16x@6b 1680772433338ns 24.296875 °C
ROT data for lsm6dsv16x@6b 1680639100006ns (-0.000008, -0.018661, 0.021575, 0.999593)
ROT data for lsm6dsv16x@6b 1680705766672ns (-0.000139, -0.018524, 0.021606, 0.999594)
ROT data for lsm6dsv16x@6b 1680772433338ns (-0.000055, -0.018569, 0.021621, 0.999593)
ROT data for lsm6dsv16x@6b 1680839100004ns (-0.000050, -0.018539, 0.021606, 0.999594)
ROT data for lsm6dsv16x@6b 1680905766670ns (-0.000003, -0.018569, 0.021621, 0.999593)
ROT data for lsm6dsv16x@6b 1680972433336ns (0.000044, -0.018493, 0.021667, 0.999594)
ROT data for lsm6dsv16x@6b 1681039100002ns (0.000013, -0.018432, 0.021667, 0.999595)
ROT data for lsm6dsv16x@6b 1681105766668ns (0.000113, -0.018402, 0.021682, 0.999595)
GV data for lsm6dsv16x@6b 1680639100006ns (37.270999, -0.792999, 998.447998)
GV data for lsm6dsv16x@6b 1680705766672ns (36.965999, -1.037000, 998.447998)
GV data for lsm6dsv16x@6b 1680772433338ns (37.088001, -0.854000, 998.447998)
GV data for lsm6dsv16x@6b 1680839100004ns (37.027000, -0.854000, 998.447998)
GV data for lsm6dsv16x@6b 1680905766670ns (37.088001, -0.792999, 998.447998)
GV data for lsm6dsv16x@6b 1680972433336ns (36.904998, -0.670999, 998.447998)
GV data for lsm6dsv16x@6b 1681039100002ns (36.783000, -0.732000, 998.447998)
GV data for lsm6dsv16x@6b 1681105766668ns (36.722000, -0.548999, 998.447998)
GY GBIAS data for lsm6dsv16x@6b 1680572433340ns (0.000303, -0.000151, 0.004179)
GY GBIAS data for lsm6dsv16x@6b 1680639100006ns (0.000303, 0.000000, 0.004179)
GY GBIAS data for lsm6dsv16x@6b 1680705766672ns (0.000303, -0.000075, 0.004179)
GY GBIAS data for lsm6dsv16x@6b 1680772433338ns (0.000227, 0.000000, 0.004179)
GY GBIAS data for lsm6dsv16x@6b 1680839100004ns (0.000303, -0.000075, 0.004179)
GY GBIAS data for lsm6dsv16x@6b 1680905766670ns (0.000303, 0.000000, 0.004255)
GY GBIAS data for lsm6dsv16x@6b 1680972433336ns (0.000303, 0.000000, 0.004255)
GY GBIAS data for lsm6dsv16x@6b 1681039100002ns (0.000379, 0.000000, 0.004255)
XL data for lsm6dsv16x@6b 1681105766668ns (0.358874, -0.019139, 9.928874)
XL data for lsm6dsv16x@6b 1681172433334ns (0.382799, -0.004784, 9.962369)
XL data for lsm6dsv16x@6b 1681239100000ns (0.354089, 0.000000, 9.914519)
GY data for lsm6dsv16x@6b 1681105766668ns (0.000304, 0.002134, 0.004574)
GY data for lsm6dsv16x@6b 1681172433334ns (-0.000914, 0.000914, 0.004574)
GY data for lsm6dsv16x@6b 1681239100000ns (0.002744, -0.002439, 0.004879)
TP data for lsm6dsv16x@6b 1680839100004ns 24.339843 °C
TP data for lsm6dsv16x@6b 1680905766670ns 24.339843 °C
TP data for lsm6dsv16x@6b 1680972433336ns 24.289062 °C
TP data for lsm6dsv16x@6b 1681039100002ns 24.296875 °C
ROT data for lsm6dsv16x@6b 1681172433334ns (0.000049, -0.018310, 0.021697, 0.999596)
ROT data for lsm6dsv16x@6b 1681239100000ns (0.000020, -0.018371, 0.021697, 0.999595)
GV data for lsm6dsv16x@6b 1681172433334ns (36.539001, -0.670999, 998.447998)
GV data for lsm6dsv16x@6b 1681239100000ns (36.660999, -0.732000, 998.447998)
GY GBIAS data for lsm6dsv16x@6b 1681105766668ns (0.000379, 0.000000, 0.004331)
GY GBIAS data for lsm6dsv16x@6b 1681172433334ns (0.000303, 0.000075, 0.004331)
GY GBIAS data for lsm6dsv16x@6b 1681239100000ns (0.000379, 0.000000, 0.004331)
TP data for lsm6dsv16x@6b 1681105766668ns 24.289062 °C
TP data for lsm6dsv16x@6b 1681172433334ns 24.324218 °C
TP data for lsm6dsv16x@6b 1681239100000ns 24.281250 °C
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)

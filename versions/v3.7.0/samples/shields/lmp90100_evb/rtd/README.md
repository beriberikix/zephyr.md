---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/shields/lmp90100_evb/rtd/README.html
original_path: samples/shields/lmp90100_evb/rtd/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# LMP90100 Sensor AFE Evaluation Board: RTD Sample

## Overview

This sample is provided as an example of how to read the temperature
of a Resistance Temperature Detector (RTD) sensor using the LMP90100
Sensor AFE Evaluation Board shield. The sample is designed for use
with a 3-wire PT100 sensor.

Please refer to [LMP90100 Sensor AFE Evaluation Board](../../../../boards/shields/lmp90100_evb/doc/index.md#lmp90100-evb-shield) for more information on
this shield.

## Requirements

Prior to running the sample application, the LMP90100 EVB must be
connected to the development board according to Example #3 (“3-wire
RTD Application”) in the [LMP90100 Sensor AFE Evaluation Board User’s
Guide](http://www.ti.com/lit/pdf/snau028).

## Building and Running

This sample runs with the LMP90100 EVB connected to any development
board with a matching Arduino connector. For this example, we use a
[NXP FRDM-K64F](../../../../boards/nxp/frdm_k64f/doc/index.md#frdm-k64f) board.

```shell
west build -b frdm_k64f samples/shields/lmp90100_evb/rtd
```

### Sample Output

> ```shell
> R: 111.15 ohm
> T: 28.66 degC
> R: 111.14 ohm
> T: 28.64 degC
> R: 111.14 ohm
> T: 28.63 degC
> R: 111.13 ohm
> T: 28.61 degC
> ```

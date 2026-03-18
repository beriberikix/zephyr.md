---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/bq274xx/README.html
original_path: samples/sensor/bq274xx/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# BQ274XX Sensor Sample

## Overview

This sample application retrieves all the fuel gauge parameters,
- Voltage, in volts
- Average current, in amps
- Standby current, in amps
- Maximum load current, in amps
- Gauge temperature
- State of charge measurement in percentage
- Full Charge Capacity in mAh
- Remaining Charge Capacity in mAh
- Nominal Available Capacity in mAh
- Full Available Capacity in mAh
- Average power in mW
- State of health measurement in percentage

from BQ274XX sensor and prints this information to the UART console.

## Requirements

- nrf9160\_innblue22 board with BQ274XX sensor [BQ274XX Sensor](http://www.ti.com/lit/ds/symlink/bq27421-g1.pdf) [[1]](#id1)

## Building and Running

Build this sample using the following commands:

```shell
# From the root of the zephyr repository
west build -b nrf9160_innblue22 samples/sensor/bq274xx
west flash
```

## References

[[1](#id2)]

[http://www.ti.com/lit/ds/symlink/bq27421-g1.pdf](http://www.ti.com/lit/ds/symlink/bq27421-g1.pdf)

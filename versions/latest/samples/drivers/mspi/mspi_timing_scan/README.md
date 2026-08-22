---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/drivers/mspi/mspi_timing_scan/README.html
original_path: samples/drivers/mspi/mspi_timing_scan/README.html
---

# Ambiq MSPI timing scan

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/mspi/mspi_timing_scan/README.rst/..)

## Overview

This sample demonstrates the usage of ambiq timing scan utility.

## Building and Running

The application will build only for a target that has a [devicetree](../../../../build/dts/index.md#dt-guide)
`flash0` or `psram0` alias depending on the interface used.
They refers to an entry with the following bindings as a compatible:

- [`ambiq,mspi-device`](../../../../build/dts/api/bindings/mspi/ambiq%2Cmspi-device.md#std-dtcompatible-ambiq-mspi-device)

```shell
west build -b apollo5_eb samples/drivers/mspi/mspi_timing_scan
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build zephyr-v3.4.0-27775-g750ed00d564b ***
<inf> mspi_ambiq_timing_scan: TxNeg=0, RxNeg=0, RxCap=0, Turnaround=5
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 0, RxDQSDelay Scan = 0x0007FFFE, Window size = 18
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 1, RxDQSDelay Scan = 0x0007FFFF, Window size = 19
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 1, RxDQSDelay Scan = 0x0007FFFF, Window size = 19
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 2, RxDQSDelay Scan = 0x0007FFFE, Window size = 18
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 3, RxDQSDelay Scan = 0x0007FFFF, Window size = 19
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 4, RxDQSDelay Scan = 0x0007FFFE, Window size = 18
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 5, RxDQSDelay Scan = 0x0005FD54, Window size = 7
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 6, RxDQSDelay Scan = 0x00000000, Window size = 0
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 7, RxDQSDelay Scan = 0x00000000, Window size = 0
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 8, RxDQSDelay Scan = 0x00000000, Window size = 0
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 9, RxDQSDelay Scan = 0x00000000, Window size = 0
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 10, RxDQSDelay Scan = 0x00000000, Window size = 0
<inf> mspi_ambiq_timing_scan: Selected setting: TxNeg=0, RxNeg=0, RxCap=0, Turnaround=5,TxDQSDelay=2, RxDQSDelay=9
```

## See also

[FLASH Interface](../../../../doxygen/html/group__flash__interface.md)

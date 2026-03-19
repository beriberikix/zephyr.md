---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/amg88xx/README.html
original_path: samples/sensor/amg88xx/README.html
---

# AMG88XX infrared array sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/amg88xx/README.rst/..)

## Overview

This sample application periodically reads the 8x8 temperature array from
the AMG88XX sensor and displays its values to the serial console.
The sample can also be configured to be triggered when the upper threshold
of 27° Celsius has been reached.

## Building and Running

This sample requires a supported AMG88xx shield, see [Panasonic Grid-EYE Shields](../../../boards/shields/amg88xx/doc/index.md#amg88xx-shields)
for the list of supported shields and build instructions.

### Sample Output

Sample shows values in° C multiplied by 100.

```shell
new sample:
---|  00    01    02    03    04    05    06    07
000|02075 01900 02000 01925 02050 01975 01950 01900
001|02000 02000 02000 01900 02125 02000 02050 02050
002|02075 01950 01950 01925 02050 01975 02075 02000
003|02175 02000 01975 01800 02000 02125 01925 02050
004|01975 02050 02050 02000 02000 01975 01925 02000
005|02100 02100 02075 02000 02025 02050 02100 02100
006|01975 02150 02075 02025 02025 02225 02025 02375
007|02025 02075 02150 02075 02025 02050 02125 02400
```

The sensor array data is output every second.

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)

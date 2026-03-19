---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/gnss/README.html
original_path: samples/drivers/gnss/README.html
---

# GNSS

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/gnss/README.rst/..)

## Overview

This sample demonstrates how to use a GNSS device implementing the
GNSS device driver API.

## Requirements

This sample requires a board with a GNSS device present and enabled
in the devicetree.

## Sample Output

```shell
gnss: gnss_info: {satellites_cnt: 14, hdop: 0.850, fix_status: GNSS_FIX, fix_quality: GNSS_SPS}
gnss: navigation_data: {latitude: 57.162331699, longitude : 9.961104199, bearing 12.530, speed 0.25, altitude: 42.372}
gnss: gnss_time: {hour: 16, minute: 17, millisecond 36000, month_day 3, month: 10, century_year: 23}
gnss has fix!
gnss: gnss_satellite: {prn: 1, snr: 30, elevation 71, azimuth 276, system: GLONASS, is_tracked: 1}
gnss: gnss_satellite: {prn: 11, snr: 31, elevation 62, azimuth 221, system: GLONASS, is_tracked: 1}
gnss reported 2 satellites!
```

## See also

[GNSS Interface](../../../doxygen/html/group__gnss__interface.md)

[Navigation](../../../doxygen/html/group__navigation.md)

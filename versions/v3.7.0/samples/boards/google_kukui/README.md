---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/google_kukui/README.html
original_path: samples/boards/google_kukui/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Kukui general features

## Overview

This provides access to [Kukui](../../../boards/google/kukui/doc/index.md#google-kukui-board) through a serial shell
so you can try out the supported features, including I2C, GPIO and flash access.

## Building

The sample can be built as follows:

```shell
west build -b google_kukui samples/boards/google_kukui
```

### Sample Output

```shell
Welcome to Google Kukui

uart:~$    (press tab)
  clear    flash    gpio     help     history  i2c      resize   shell
uart:~$ i2c read I2C_2 36
00000000: 82 00 00 ff 80 7f 00 ff  00 00 c1 0a c8 5b 0c 62 |........ .....[.b|
```

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/net/openthread/shell/README.html
original_path: samples/net/openthread/shell/README.html
---

# OpenThread shell

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/openthread/shell/README.rst/..)

## Overview

This sample allows testing the Thread protocol and the underlying IEEE 802.15.4 drivers for various
boards using the OpenThread shell.

## Building and Running

Verify that the board and chip you are targeting provide IEEE 802.15.4 support.

For instance you can use Nordic’s nRF52840 DK.

```shell
west build -b nrf52840dk/nrf52840 samples/net/openthread/shell
```

### Sample console interaction

```shell
uart:~$ ot scan
| PAN  | MAC Address      | Ch | dBm | LQI |
+------+------------------+----+-----+-----+
| fe09 | abcdef1234567890 | 15 | -78 |  60 |
Done
```

## See also

[Network Statistics Library](../../../../doxygen/html/group__net__stats.md)

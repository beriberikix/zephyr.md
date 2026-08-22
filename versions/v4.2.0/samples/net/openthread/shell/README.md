---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/net/openthread/shell/README.html
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

There are configuration files for different boards and setups in the shell directory:

- `prj.conf`
  Generic config file.
- `overlay-ot-rcp-host-nxp.conf`
  This overlay config enables support of OpenThread RCP host running on NXP chips over IMU interface.

Build shell application like this:

```shell
west build -b <board to use> samples/net/openthread/shell -- -DCONF_FILE=<config file to use>
```

Example building for Nordic’s nRF52840 DK.

```shell
west build -b nrf52840dk/nrf52840 samples/net/openthread/shell -- -DCONF_FILE="prj.conf"
```

Example building for NXP’s RW612 FRDM (RCP host).

```shell
west build -b frdm_rw612 samples/net/openthread/shell -- -DCONF_FILE="prj.conf overlay-ot-rcp-host-nxp.conf"
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

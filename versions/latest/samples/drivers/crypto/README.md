---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/crypto/README.html
original_path: samples/drivers/crypto/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Crypto

## Overview

An example to illustrate the usage of [crypto APIs](../../../services/crypto/api/index.md#crypto-api).

## Building and Running

This project outputs to the console. It can be built and executed
on QEMU as follows:

```shell
west build -b qemu_x86 samples/drivers/crypto
west build -t run
```

### Sample Output

```shell
[general] [INF] main: Encryption Sample

[general] [INF] cbc_mode: CBC Mode

[general] [INF] cbc_mode: cbc mode ENCRYPT - Match

[general] [INF] cbc_mode: cbc mode DECRYPT - Match

[general] [INF] ctr_mode: CTR Mode

[general] [INF] ctr_mode: ctr mode ENCRYPT - Match

[general] [INF] ctr_mode: ctr mode DECRYPT - Match

[general] [INF] ccm_mode: CCM Mode

[general] [INF] ccm_mode: CCM mode ENCRYPT - Match

[general] [INF] ccm_mode: CCM mode DECRYPT - Match
```

Exit QEMU by pressing `CTRL+A` `x`.

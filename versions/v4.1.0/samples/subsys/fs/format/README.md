---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/fs/format/README.html
original_path: samples/subsys/fs/format/README.html
---

# Format filesystem

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/fs/format/README.rst/..)

## Overview

This sample shows how to format different storage
devices for different file systems. There are 2 scenarios prepared for this
sample:

- littleFS on flash device
- FAT file system on RAM disk

## Building and running

To run this sample, build it for the desired board and scenario and flash it.

The Flash scenario is supported on the nrf52dk/nrf52832 board.
The RAM disk scenario is supported on the mimxrt1064\_evk board.
To build the RAM disk sample, the configuration `prj_ram.conf` needs to be used by setting
`CONF_FILE=prj_ram.conf`.

The Flash sample for the nrf 52DK board can be built as follow:

```shell
west build -b nrf52dk/nrf52832 samples/subsys/fs/format
west flash
```

The RAM disk sample for the MIMXRT1064-EVK board can be built as follow:

```shell
west build -b mimxrt1064_evk samples/subsys/fs/format -- -DCONF_FILE="prj_ram.conf"
west flash
```

### Sample Output

When the sample runs successfully you should see following message on the screen:

```shell
I: LittleFS version 2.4, disk version 2.0
I: FS at flash-controller@4001e000:0x7a000 is 6 0x1000-byte blocks with 512 cycle
I: sizes: rd 16 ; pr 16 ; ca 64 ; la 32
I: Format successful
```

## See also

[File System APIs](../../../../doxygen/html/group__file__system__api.md)

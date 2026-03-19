---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/demand_paging/README.html
original_path: samples/subsys/demand_paging/README.html
---

# Demand paging

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/demand_paging/README.rst/..)

## Overview

This sample demonstrates how demand paging can be leveraged to deal with
firmware bigger than the available RAM if XIP is not possible. Select code
can be tagged to be loaded into memory on demand, and also be automatically
evicted for more code to be executed when memory is exhausted.

## Requirements

This demo requires the presence of a supported hardware MMU and a backing
store implementation with access to the compiled Zephyr binary.
For demonstration purposes, the ondemand\_semihost backing store is used on
a QEMU ARM64 target with a hardcoded small RAM configuration.

## Building and Running

This application can be built and executed on QEMU as follows:

```shell
west build -b qemu_cortex_a53 samples/subsys/demand_paging
west build -t run
```

### Sample Output

```shell
*** Booting Zephyr OS build v3.7.0-2108-g5975c3785356 ***
Calling huge body of code that doesn't fit in memory
free memory pages: from 37 to 0, 987 page faults
Calling it a second time
free memory pages: from 0 to 0, 987 page faults
Done.
```

Exit QEMU by pressing `CTRL+A` `x`.

To actually view the underlying demand paging subsystem at work, debug
prints can be enabled using [`CONFIG_LOG`](../../../kconfig.md#CONFIG_LOG "CONFIG_LOG") and
[`CONFIG_KERNEL_LOG_LEVEL_DBG`](../../../kconfig.md#CONFIG_KERNEL_LOG_LEVEL_DBG "CONFIG_KERNEL_LOG_LEVEL_DBG") in the config file.

## See also

[Demand Paging APIs](../../../doxygen/html/group__mem-demand-paging.md)

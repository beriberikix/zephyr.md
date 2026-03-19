---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/psa/its/README.html
original_path: samples/psa/its/README.html
---

# PSA Internal Trusted Storage API

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/psa/its/README.rst/..)

## Overview

This sample demonstrates usage of the
[PSA Internal Trusted Storage (ITS) API](https://arm-software.github.io/psa-api/storage/1.0/overview/architecture.html#the-internal-trusted-storage-api),
which is part of the [PSA Secure Storage API](https://arm-software.github.io/psa-api/storage/),
for storing and retrieving persistent data.

## Requirements

An implementation of the PSA ITS API must be present for this sample to build.
It can be provided by:

- [Trusted Firmware-M (TF-M)](../../../services/tfm/index.md#tfm), for `*/ns` [board targets](../../../glossary.md#term-board-target).
- The [secure storage subsystem](../../../services/secure_storage.md#secure-storage), for the other board targets.

## Building

This sample is located in [samples/psa/its](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/psa/its).

Different configurations are defined in the `sample.yaml` file.
You can use them to build the sample, depending on the PSA ITS provider, as follows:

TF-Msecure storage subsystem

For board targets with TF-M:

> ```shell
> # From the root of the zephyr repository
> west build -b <ns_board_target> -T sample.psa.its.tfm samples/psa/its
> ```

For board targets without TF-M.

If the board target to compile for has an entropy driver (preferable):

```shell
# From the root of the zephyr repository
west build -b <board_target> -T sample.psa.its.secure_storage.entropy_driver samples/psa/its
```

Or, to use an insecure entropy source (only for testing):

```shell
# From the root of the zephyr repository
west build -b <board_target> -T sample.psa.its.secure_storage.entropy_not_secure samples/psa/its
```

To flash it, see [Flashing: west flash](../../../develop/west/build-flash-debug.md#west-flashing).

## See also

[PSA Secure Storage API](../../../doxygen/html/group__psa__secure__storage.md)

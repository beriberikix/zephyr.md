---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/psa/persistent_key/README.html
original_path: samples/psa/persistent_key/README.html
---

# PSA Crypto persistent key

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/psa/persistent_key/README.rst/..)

## Overview

This sample demonstrates usage of persistent keys in the [PSA Crypto API](../../../services/crypto/psa_crypto.md#psa-crypto).

## Requirements

In addition to the PSA Crypto API, an implementation of the
[PSA Internal Trusted Storage (ITS) API](https://arm-software.github.io/psa-api/storage/1.0/overview/architecture.html#the-internal-trusted-storage-api)
(for storage of the persistent keys) must be present for this sample to work.
It can be provided by:

- [Trusted Firmware-M (TF-M)](../../../services/tfm/index.md#tfm), for `*/ns` [board targets](../../../glossary.md#term-board-target).
- The [secure storage subsystem](../../../services/secure_storage.md#secure-storage), for the other board targets.

## Building

This sample is located in [samples/psa/persistent\_key](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/psa/persistent_key).

Different configurations are defined in the `sample.yaml` file.
You can use them to build the sample, depending on the PSA ITS provider, as follows:

TF-Msecure storage subsystem

For board targets with TF-M:

> ```shell
> # From the root of the zephyr repository
> west build -b <ns_board_target> -T sample.psa.persistent_key.tfm samples/psa/persistent_key
> ```

For board targets without TF-M.

If the board target to compile for has an entropy driver (preferable):

```shell
# From the root of the zephyr repository
west build -b <board_target> -T sample.psa.persistent_key.secure_storage.entropy_driver samples/psa/persistent_key
```

Or, to use an insecure entropy source (only for testing):

```shell
# From the root of the zephyr repository
west build -b <board_target> -T sample.psa.persistent_key.secure_storage.entropy_not_secure samples/psa/persistent_key
```

To flash it, see [Flashing: west flash](../../../develop/west/build-flash-debug.md#west-flashing).

## API reference

[PSA Crypto key management API reference](https://arm-software.github.io/psa-api/crypto/1.2/api/keys/index.html)

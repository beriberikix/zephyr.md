---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/subsys/uuid/README.html
original_path: samples/subsys/uuid/README.html
---

# UUID

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/uuid/README.rst/..)

## Overview

This sample app demonstrates the use of the [UUID](../../../doxygen/html/group__uuid.md) utilities to generate and manipulate
UUIDs accordingly to IETF RFC 9562.

The following functionality is demonstrated:

- UUIDv4 generation
- UUIDv5 generation from namespace and data
- UUID conversion from/to string and to base64 and base64 URL safe formats

## Requirements

This sample relies on the following modules:

- MbedTLS for the UUIDv5 hash functions
- Base64 for the base64 encoding of UUIDs
- Entropy source for the pseudo-random generation of UUIDv4

## Building and Running

Use the standard `west` commands to build and flash this application.
For example, for `native_sim`:

```shell
west build -b native_sim samples/subsys/uuid
west build -t run
```

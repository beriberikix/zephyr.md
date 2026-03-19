---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/modules/nanopb/README.html
original_path: samples/modules/nanopb/README.html
---

# Nanopb

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/modules/nanopb/README.rst/..)

## Overview

A simple protocol buffer sample using [Nanopb](../../../services/serialization/nanopb.md#nanopb-reference) for serializing structured data
to platform independent raw buffers or streams.

The structured data to encode/decode is presented as follows:

```proto
syntax = "proto3";

message SimpleMessage {
    int32 lucky_number = 1;
    bytes buffer = 2;
    int32 unlucky_number = 3;
}
```

## Configuration

This sample uses two configuration options to modify the behavior.

- `CONFIG_SAMPLE_BUFFER_SIZE` sets the `buffer` field’s size
- `CONFIG_SAMPLE_UNLUCKY_NUMBER` either enables or disables the `unlucky_number`
  field.

## Building and Running

This application can be built as follows:

```shell
west build -b qemu_x86 samples/modules/nanopb
west build -t run
```

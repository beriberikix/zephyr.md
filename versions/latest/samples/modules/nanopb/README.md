---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/modules/nanopb/README.html
original_path: samples/modules/nanopb/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Nanopb sample

## Overview

A simple protocol buffer sample using Nanopb for serializing structured data
to platform independent raw buffers or streams.

## Requirements

Nanopb uses the protocol buffer compiler to generate source and header files,
make sure the `protoc` executable is installed and available.

UbuntumacOSWindows

Use `apt` to install dependency:

> ```shell
> sudo apt install protobuf-compiler
> ```

Use `brew` to install dependency:

> ```shell
> brew install protobuf
> ```

Use `choco` to install dependency:

> ```shell
> choco install protoc
> ```

Additionally Nanopb is an optional module and needs to be added explicitly to the workspace:

```shell
west config manifest.project-filter -- +nanopb
west update
```

## Building and Running

This application can be built as follows:

```shell
west build -b qemu_x86 samples/modules/nanopb
west build -t run
```

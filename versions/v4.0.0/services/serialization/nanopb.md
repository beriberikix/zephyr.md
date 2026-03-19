---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/serialization/nanopb.html
original_path: services/serialization/nanopb.html
---

# Nanopb

[Nanopb](https://jpa.kapsi.fi/nanopb/) is a C implementation of Google’s
[Protocol Buffers](https://protobuf.dev/).

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

Additionally, Nanopb is an optional module and needs to be added explicitly to the workspace:

```shell
west config manifest.project-filter -- +nanopb
west update
```

## Configuration

Make sure to include `nanopb` within your `CMakeLists.txt` file as follows:

```cmake
list(APPEND CMAKE_MODULE_PATH ${ZEPHYR_BASE}/modules/nanopb)
include(nanopb)
```

Adding `proto` files can be done with the `zephyr_nanopb_sources()` CMake function which
ensures the generated header and source files are created before building the specified target.

Nanopb has [generator options](https://jpa.kapsi.fi/nanopb/docs/reference.html#generator-options)
that can be used to configure messages or fields. This allows to set fixed sizes or skip fields
entirely.

The internal CMake generator has an extension to configure `*.options.in` files automatically
with CMake variables.

See [samples/modules/nanopb/src/simple.options.in](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/modules/nanopb/src/simple.options.in) and
[samples/modules/nanopb/CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/modules/nanopb/CMakeLists.txt) for usage example.

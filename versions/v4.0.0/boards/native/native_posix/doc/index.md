---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/native/native_posix/doc/index.html
original_path: boards/native/native_posix/doc/index.html
---

# Native POSIX execution (native\_posix)

## [Overview](#id1)

Warning

`native_posix` is deprecated in favour of [native\_sim](../../native_sim/doc/index.md#native-sim), and will be removed
in the 4.2 release.

Note

For native\_posix users, if needed, [native\_sim](../../native_sim/doc/index.md#native-sim) includes a compatibility mode
`CONFIG_NATIVE_SIM_NATIVE_POSIX_COMPAT`,
which will set its configuration to mimic a native\_posix-like configuration.

`native_posix` is the predecessor of [native\_sim](../../native_sim/doc/index.md#native-sim).
Just like with [native\_sim](../../native_sim/doc/index.md#native-sim) you can build your Zephyr application
with the Zephyr kernel, creating a normal Linux executable with your host tooling,
and can debug and instrument it like any other Linux program.

But unlike with [native\_sim](../../native_sim/doc/index.md#native-sim) you are limited to only using the host C library.
[native\_sim](../../native_sim/doc/index.md#native-sim) supports all `native_posix` use cases.

This board does not intend to simulate any particular HW, but it provides
a few peripherals such as an Ethernet driver, display, UART, etc., to enable
developing and testing application code which would require them.
This board supports the same [peripherals](../../native_sim/doc/index.md#native-sim-peripherals)
[and backends as native\_sim](../../native_sim/doc/index.md#native-sim-backends).

## [Host system dependencies](#id2)

Please check the
[Posix Arch Dependencies](../../doc/arch_soc.md#posix-arch-deps)

## [Important limitations](#id3)

This board inherits
[the limitations of its architecture](../../doc/arch_soc.md#posix-arch-limitations)

Moreover, being limited to build only with the host C library, it is not possible to build
applications with the [Zephyr POSIX OS abstraction](../../../../services/portability/posix/index.md#posix-support), as there would be symbol
collisions between the host OS and this abstraction layer.

## [How to use it](#id4)

To build, simply specify the `native_posix` board as target:

```shell
west build -b native_posix samples/hello_world
```

Now you have a Linux executable, `./build/zephyr/zephyr.exe`, you can use just like any
other Linux program.

You can run, debug, build it with sanitizers or with coverage just like with
[native\_sim](../../native_sim/doc/index.md#native-sim).
Please check [native\_sim’s how to](../../native_sim/doc/index.md#native-sim-how-to-use) for more info.

## [32 and 64bit versions](#id5)

Just like [native\_sim](../../native_sim/doc/index.md#native-sim), `native_posix` comes with two targets:
A 32 bit and 64 bit version.
The 32 bit version, `native_posix`, is the default target, which will compile
your code for the ILP32 ABI (i386 in a x86 or x86\_64 system) where pointers
and longs are 32 bits.
This mimics the ABI of most embedded systems Zephyr targets,
and is therefore normally best to test and debug your code, as some bugs are
dependent on the size of pointers and longs.
This target requires either a 64 bit system with multilib support installed or
one with a 32bit userspace.

The 64 bit version, `native_posix/native/64`, compiles your code targeting the
LP64 ABI (x86-64 in x86 systems), where pointers and longs are 64 bits.
You can use this target if you cannot compile or run 32 bit binaries.

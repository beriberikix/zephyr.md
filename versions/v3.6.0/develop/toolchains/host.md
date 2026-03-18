---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/toolchains/host.html
original_path: develop/toolchains/host.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Host Toolchains

In some specific configurations, like when building for non-MCU x86 targets on
a Linux host, you may be able to reuse the native development tools provided
by your operating system.

To use your host gcc, set the [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT)
[environment variable](../env_vars.md#env-vars) to `host`. To use clang, set
[`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `llvm`.

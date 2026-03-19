---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/develop/toolchains/host.html
original_path: develop/toolchains/host.html
---

# Host Toolchains

In some specific configurations, like when building for non-MCU x86 targets on
a Linux host, you may be able to reuse the native development tools provided
by your operating system.

To use your host gcc, set the [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT)
[environment variable](../env_vars.md#env-vars) to `host`. To use clang, set
[`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `llvm`.

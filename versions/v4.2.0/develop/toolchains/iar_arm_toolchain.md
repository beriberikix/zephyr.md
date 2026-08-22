---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/develop/toolchains/iar_arm_toolchain.html
original_path: develop/toolchains/iar_arm_toolchain.html
---

# IAR Arm Toolchain

1. Download and install a release v9.70 or newer of [IAR Arm Toolchain](https://www.iar.com/products/architectures/arm/) on your host (IAR Embedded Workbench or IAR Build Tools, perpetual or subscription licensing)
2. Make sure you have [Zephyr SDK](zephyr_sdk.md#toolchain-zephyr-sdk) installed on your host.
3. [Set these environment variables](../env_vars.md#env-vars):

   > - Set [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `iar`.
   > - Set `IAR_TOOLCHAIN_PATH` to the toolchain installation directory.
4. The cloud licensed variant of the IAR Toolchain needs the `IAR_LMS_BEARER_TOKEN` environment
   variable to be set to a valid `license bearer token` (subscription licensing).

For example:

```shell
# Linux (default installation path):
export IAR_TOOLCHAIN_PATH=/opt/iar/cxarm-<version>/arm
export ZEPHYR_TOOLCHAIN_VARIANT=iar
export IAR_LMS_BEARER_TOKEN="<BEARER-TOKEN>"
```

```batch
# Windows:
set IAR_TOOLCHAIN_PATH=c:\<path>\cxarm-<version>\arm
set ZEPHYR_TOOLCHAIN_VARIANT=iar
set IAR_LMS_BEARER_TOKEN="<BEARER-TOKEN>"
```

Note

Known limitations:

- The IAR Toolchain uses `ilink` for linking and depends on Zephyr’s CMAKE\_LINKER\_GENERATOR. `ilink` is incompatible with Zephyr’s linker script template, which works with GNU ld.
- The GNU Assembler distributed with the Zephyr SDK is used for `.S-files`.
- C library support for `Minimal libc` only. C++ is not supported.
- Some Zephyr subsystems or modules may contain C or assembly code that relies on GNU intrinsics and have not yet been updated to work fully with `iar`.
- TrustedFirmware is not supported

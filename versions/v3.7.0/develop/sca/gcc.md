---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/develop/sca/gcc.html
original_path: develop/sca/gcc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# GCC static analysis support

Static analysis was introduced in [GCC](https://gcc.gnu.org/) 10 and it is enabled
with the option `-fanalyzer`. This option performs a much more expensive and thorough
analysis of the code than traditional warnings.

## Run GCC static analysis

To run GCC static analysis, [west build](../west/build-flash-debug.md#west-building) should be
called with a `-DZEPHYR_SCA_VARIANT=gcc` parameter, e.g.

```shell
west build -b qemu_x86 samples/userspace/hello_world_user -- -DZEPHYR_SCA_VARIANT=gcc
```

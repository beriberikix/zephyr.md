---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/develop/sca/sparse.html
original_path: develop/sca/sparse.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Sparse support

[Sparse](https://www.kernel.org/doc/html/latest/dev-tools/sparse.html)
is a static code analysis tool.
Apart from performing common code analysis tasks it also supports an
`address_space` attribute, which allows introduction of distinct address
spaces in C code with subsequent verification that pointers to different
address spaces do not get confused. Additionally it supports a `force`
attribute which should be used to cast pointers between different address
spaces. At the moment Zephyr introduces a single custom address space
`__cache` used to identify pointers from the cached address range on the
Xtensa architecture. This helps identify cases where cached and uncached
addresses are confused.

## Running with sparse

To run a sparse verification build [west build](../west/build-flash-debug.md#west-building) should be
called with a `-DZEPHYR_SCA_VARIANT=sparse` parameter, e.g.

```shell
west build -d hello -b intel_adsp/cavs25 zephyr/samples/hello_world -- -DZEPHYR_SCA_VARIANT=sparse
```

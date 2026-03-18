---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/sca/cpptest.html
original_path: develop/sca/cpptest.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Parasoft C/C++test support

Parasoft [C/C++test](https://www.parasoft.com/products/parasoft-c-ctest/) is a software testing
and static analysis tool for C and C++. It is a commercial software and you must acquire a
commercial license to use it.

Documentation of C/C++test can be found at [https://docs.parasoft.com/](https://docs.parasoft.com/). Please refer to the
documentation for how to use it.

## Generating Build Data Files

To use C/C++test, `cpptestscan` must be found in your [`PATH`](../env_vars.md#envvar-PATH) environment variable. And
[west build](../west/build-flash-debug.md#west-building) should be called with a `-DZEPHYR_SCA_VARIANT=cpptest`
parameter, e.g.

```shell
west build -b qemu_cortex_m3 zephyr/samples/hello_world -- -DZEPHYR_SCA_VARIANT=cpptest
```

A `.bdf` file will be generated as `build/sca/cpptest/cpptestscan.bdf`.

## Generating a report file

Please refer to Parasoft C/C++test documentation for more details.

To import and generate a report file, something like the following should work.

```shell
cpptestcli -data out -localsettings local.conf -bdf build/sca/cpptest/cpptestscan.bdf -config "builtin://Recommended Rules" -report out/report
```

You might need to set `bdf.import.c.compiler.exec`, `bdf.import.cpp.compiler.exec`, and
`bdf.import.linker.exec` to the toolchain [west build](../west/build-flash-debug.md#west-building) used.

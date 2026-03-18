---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/basic/sys_heap/README.html
original_path: samples/basic/sys_heap/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# System heap

## Overview

A simple sample that can be used with any [supported board](../../../boards/index.md#boards) and
prints system heap usage to the console.

## Building

This application can be built on [native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim) as follows:

```shell
west build -b native_sim samples/basic/sys_heap
```

To build for another board, change “native\_sim” above to that board’s name.

## Running

Run build/zephyr/zephyr.exe

## Sample Output

```shell
System heap sample

allocated 0, free 196, max allocated 0, heap size 256
allocated 156, free 36, max allocated 156, heap size 256
allocated 100, free 92, max allocated 156, heap size 256
allocated 0, free 196, max allocated 156, heap size 256
```

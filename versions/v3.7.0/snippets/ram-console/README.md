---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/snippets/ram-console/README.html
original_path: snippets/ram-console/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# RAM Console Snippet (ram-console)

```shell
west build -S ram-console [...]
```

## Overview

This snippet redirects console output to a RAM buffer. The RAM console
buffer is a global array located in RAM region by default, whose address
is unknown before building. The RAM console driver also supports using
a dedicated section for the RAM console buffer with prefined address.

## How to enable RAM console buffer section

Add board dts overlay to this snippet to add property `zephyr,ram-console`
in the chosen node and memory-region node with compatible string
[`zephyr,memory-region`](../../build/dts/api/bindings/base/zephyr%2Cmemory-region.md#std-dtcompatible-zephyr-memory-region) as the following:

```dts
/ {
    chosen {
        zephyr,ram-console = &snippet_ram_console;
    };

   snippet_ram_console: memory@93d00000 {
        compatible = "zephyr,memory-region";
        reg = <0x93d00000 DT_SIZE_K(4)>;
        zephyr,memory-region = "RAM_CONSOLE";
   };
};
```

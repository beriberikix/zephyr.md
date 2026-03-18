---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/boards/intel_adsp/code_relocation/README.html
original_path: samples/boards/intel_adsp/code_relocation/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Intel ADSP CAVS Code relocation

## Overview

A simple sample that shows code relocation working for Intel ADSP CAVS
boards (v18 and v25). The interesting bit is the custom linker file.
As rimage (the tool used to sign the image) mandates that elf files
sections TEXT, DATA and BSS be contiguous, some work is done in the
linker script to ensure that.

## Building and Running

This application can be built and executed as follows:

```shell
west build -b intel_adsp_cavs25 samples/hello_world
```

### Sample Output

```shell
main location: 0xbe0105e4
Calling relocated code
Relocated code! reloc location 0xbe008010
maybe_bss location: 0x9e004218 maybe_bss value: 0
```

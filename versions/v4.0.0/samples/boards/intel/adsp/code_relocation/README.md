---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/boards/intel/adsp/code_relocation/README.html
original_path: samples/boards/intel/adsp/code_relocation/README.html
---

# Code relocation

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/intel/adsp/code_relocation/README.rst/..)

## Overview

A simple sample that shows code relocation working for Intel ADSP CAVS
boards (v18 and v25). The interesting bit is the custom linker file.
As rimage (the tool used to sign the image) mandates that elf files
sections TEXT, DATA and BSS be contiguous, some work is done in the
linker script to ensure that.

## Building and Running

This application can be built and executed as follows:

```shell
west build -b intel_adsp/cavs25 samples/boards/intel/adsp/code_relocation
```

### Sample Output

```shell
main location: 0xbe0105e4
Calling relocated code
Relocated code! reloc location 0xbe008010
maybe_bss location: 0x9e004218 maybe_bss value: 0
```

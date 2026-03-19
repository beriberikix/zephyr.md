---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/arch/semihost.html
original_path: hardware/arch/semihost.html
---

# Semihosting Guide

## Overview

Semihosting is a mechanism that enables code running on ARM and RISC-V targets
to communicate and use the Input/Output facilities on a host computer that is
running a debugger or emulator.

More complete documentation on the available functionality is available at the
[ARM Github documentation](https://github.com/ARM-software/abi-aa/blob/main/semihosting/semihosting.rst).

The RISC-V functionality borrows from the ARM definitions, as described at the
[RISC-V Github documentation](https://github.com/riscv/riscv-semihosting-spec/blob/main/riscv-semihosting-spec.adoc).

## File Operations

Semihosting enables files on the host computer to be opened, read, and modified
by an application. This can be useful when attempting to validate the behaviour
of code across datasets that are larger than what can fit into ROM of an
emulated platform. File paths can be either absolute, or relative to the
directory of the running process.

```c
const char *path = "./data.bin";
long file_len, bytes_read, fd;
uint8_t buffer[16];

/* Open the data file for reading */
fd = semihost_open(path, SEMIHOST_OPEN_RB);
if (fd < 0) {
   return -ENOENT;
}
/* Read all data from the file */
file_len = semihost_flen(fd);
while(file_len > 0) {
   bytes_read = semihost_read(fd, buffer, MIN(file_len, sizeof(buffer)));
   if (bytes_read < 0) {
      break;
   }
   /* Process read data */
   do_data_processing(buffer, bytes_read);
   /* Update remaining length */
   file_len -= bytes_read;
}
/* Close the file */
semihost_close(fd);
```

# Additional Functionality

Additional functionality is available by running semihosting instructions
directly with [`semihost_exec()`](../../doxygen/html/group__semihost.md#gab8d683d2011f6683956c47a4b129faf4) with one of the instructions defined
in [`semihost_instr`](../../doxygen/html/group__semihost.md#gadf61e00be557b7cb4457f7ea6f8da86d). For complete documentation on the required
arguments and return codes, see the [ARM Github documentation](https://github.com/ARM-software/abi-aa/blob/main/semihosting/semihosting.rst).

## API Reference

[Semihosting APIs](../../doxygen/html/group__semihost.md)

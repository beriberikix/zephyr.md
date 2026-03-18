---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/arch/semihost.html
original_path: hardware/arch/semihost.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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
directly with [`semihost_exec()`](#c.semihost_exec) with one of the instructions defined
in [`semihost_instr`](#c.semihost_instr). For complete documentation on the required
arguments and return codes, see the [ARM Github documentation](https://github.com/ARM-software/abi-aa/blob/main/semihosting/semihosting.rst).

## API Reference

*group* semihost
:   Enums

    enum semihost\_instr
    :   Semihosting instructions.

        *Values:*

        enumerator SEMIHOST\_OPEN = 0x01
        :   Open a file or stream on the host system.

        enumerator SEMIHOST\_ISTTY = 0x09
        :   Check whether a file is associated with a stream/terminal.

        enumerator SEMIHOST\_WRITE = 0x05
        :   Write to a file or stream.

        enumerator SEMIHOST\_READ = 0x06
        :   Read from a file at the current cursor position.

        enumerator SEMIHOST\_CLOSE = 0x02
        :   Closes a file on the host which has been opened by SEMIHOST\_OPEN.

        enumerator SEMIHOST\_FLEN = 0x0C
        :   Get the length of a file.

        enumerator SEMIHOST\_SEEK = 0x0A
        :   Set the file cursor to a given position in a file.

        enumerator SEMIHOST\_TMPNAM = 0x0D
        :   Get a temporary absolute file path to create a temporary file.

        enumerator SEMIHOST\_REMOVE = 0x0E
        :   Remove a file on the host system.

            Possibly insecure!

        enumerator SEMIHOST\_RENAME = 0x0F
        :   Rename a file on the host system.

            Possibly insecure!

        enumerator SEMIHOST\_WRITEC = 0x03
        :   Write one character to the debug terminal.

        enumerator SEMIHOST\_WRITE0 = 0x04
        :   Write a NULL terminated string to the debug terminal.

        enumerator SEMIHOST\_READC = 0x07
        :   Read one character from the debug terminal.

        enumerator SEMIHOST\_CLOCK = 0x10

        enumerator SEMIHOST\_ELAPSED = 0x30

        enumerator SEMIHOST\_TICKFREQ = 0x31

        enumerator SEMIHOST\_TIME = 0x11

        enumerator SEMIHOST\_ERRNO = 0x13
        :   Retrieve the errno variable from semihosting operations.

        enumerator SEMIHOST\_GET\_CMDLINE = 0x15
        :   Get commandline parameters for the application to run with.

        enumerator SEMIHOST\_HEAPINFO = 0x16

        enumerator SEMIHOST\_ISERROR = 0x08

        enumerator SEMIHOST\_SYSTEM = 0x12

    enum semihost\_open\_mode
    :   Modes to open a file with.

        Behaviour corresponds to equivalent fopen strings. i.e. SEMIHOST\_OPEN\_RB\_PLUS == “rb+”

        *Values:*

        enumerator SEMIHOST\_OPEN\_R = 0

        enumerator SEMIHOST\_OPEN\_RB = 1

        enumerator SEMIHOST\_OPEN\_R\_PLUS = 2

        enumerator SEMIHOST\_OPEN\_RB\_PLUS = 3

        enumerator SEMIHOST\_OPEN\_W = 4

        enumerator SEMIHOST\_OPEN\_WB = 5

        enumerator SEMIHOST\_OPEN\_W\_PLUS = 6

        enumerator SEMIHOST\_OPEN\_WB\_PLUS = 7

        enumerator SEMIHOST\_OPEN\_A = 8

        enumerator SEMIHOST\_OPEN\_AB = 9

        enumerator SEMIHOST\_OPEN\_A\_PLUS = 10

        enumerator SEMIHOST\_OPEN\_AB\_PLUS = 11

    Functions

    long semihost\_exec(enum [semihost\_instr](#c.semihost_instr) instr, void \*args)
    :   Manually execute a semihosting instruction.

        Parameters:
        :   - **instr** – instruction code to run
            - **args** – instruction specific arguments

        Returns:
        :   integer return code of instruction

    char semihost\_poll\_in(void)
    :   Read a byte from the console.

        Returns:
        :   char byte read from the console.

    void semihost\_poll\_out(char c)
    :   Write a byte to the console.

        Parameters:
        :   - **c** – byte to write to console

    long semihost\_open(const char \*path, long mode)
    :   Open a file on the host system.

        Parameters:
        :   - **path** – file path to open. Can be absolute or relative to current directory of the running process.
            - **mode** – value from [semihost\_open\_mode](#group__semihost_1ga425c53a045590978b0b3235d545780f7).

        Return values:
        :   - **handle** – positive handle on success.
            - **-1** – on failure.

    long semihost\_close(long fd)
    :   Close a file.

        Parameters:
        :   - **fd** – handle returned by [semihost\_open](#group__semihost_1ga497b911ba4e6b40e4e5808fa9484f5a4).

        Return values:
        :   - **0** – on success.
            - **-1** – on failure.

    long semihost\_flen(long fd)
    :   Query the size of a file.

        Parameters:
        :   - **fd** – handle returned by [semihost\_open](#group__semihost_1ga497b911ba4e6b40e4e5808fa9484f5a4).

        Return values:
        :   - **positive** – file size on success.
            - **-1** – on failure.

    long semihost\_seek(long fd, long offset)
    :   Seeks to an absolute position in a file.

        Parameters:
        :   - **fd** – handle returned by [semihost\_open](#group__semihost_1ga497b911ba4e6b40e4e5808fa9484f5a4).
            - **offset** – offset from the start of the file in bytes.

        Return values:
        :   - **0** – on success.
            - **-errno** – negative error code on failure.

    long semihost\_read(long fd, void \*buf, long len)
    :   Read the contents of a file into a buffer.

        Parameters:
        :   - **fd** – handle returned by [semihost\_open](#group__semihost_1ga497b911ba4e6b40e4e5808fa9484f5a4).
            - **buf** – buffer to read data into.
            - **len** – number of bytes to read.

        Return values:
        :   - **read** – number of bytes read on success.
            - **-errno** – negative error code on failure.

    long semihost\_write(long fd, const void \*buf, long len)
    :   Write the contents of a buffer into a file.

        Parameters:
        :   - **fd** – handle returned by [semihost\_open](#group__semihost_1ga497b911ba4e6b40e4e5808fa9484f5a4).
            - **buf** – buffer to write data from.
            - **len** – number of bytes to write.

        Return values:
        :   - **0** – on success.
            - **-errno** – negative error code on failure.

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/flash_shell/README.html
original_path: samples/drivers/flash_shell/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Flash shell

## Overview

This is a simple shell module that allows arbitrary boards with flash
driver support to explore the flash device.

## Building and Running

This project can be built and executed on as follows:

```shell
west build -b qemu_x86 samples/drivers/flash_shell
west build -t run
```

### Sample Output

```shell
uart:~$ flash page_info 0
Page for address 0x0:
start offset: 0x0
size: 4096
index: 0
uart:~$ flash erase 0x1000
Erase success.
uart:~$ flash write 0x1000 0x12345678 0x9abcdef0
Write OK.
Verified.
uart:~$ flash write 0x1000 0x11111111
Write internal ERROR!
uart:~$ flash read 0x1000 0x10
00001000: 78 56 34 12 f0 de bc 9a  ff ff ff ff ff ff ff ff |xV4..... ........|

uart:~$ flash write 0x101c 0xabcd1234
Write OK.
Verified.
uart:~$ flash read 0x1000 0x20
00001000: 78 56 34 12 f0 de bc 9a  ff ff ff ff ff ff ff ff |xV4..... ........|
00001010: ff ff ff ff ff ff ff ff  ff ff ff ff 34 12 cd ab |........ ....4...|
```

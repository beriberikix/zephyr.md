---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/zbus/dyn_channel/README.html
original_path: samples/subsys/zbus/dyn_channel/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Dynamic channel

## Overview

This sample implements an application using zbus to illustrate the way zbus supports dynamically allocated channels.

## Building and Running

This project outputs to the console. It can be built and executed
on QEMU as follows:

```shell
# From the root of the zephyr repository
west build -b qemu_x86 samples/subsys/zbus/dyn_channel
west build -t run
```

### Sample Output

```shell
W: size=01
W: Content
W: 00                      |.
W: size=02
W: Content
W: 01 01                   |..
W: size=03
W: Content
W: 00 00 00                |...
W: size=04
W: Content
W: 03 03 03 03             |....
W: size=05
W: Content
W: 00 00 00 00 00          |.....
W: size=06
W: Content
W: 05 05 05 05 05 05       |......
W: size=07
W: Content
W: 00 00 00 00 00 00 00    |.......
W: size=08
W: Content
W: 07 07 07 07 07 07 07 07 |........
W: size=09
W: Content
W: 00 00 00 00 00 00 00 00 |........
W: 00                      |.
W: size=10
W: Content
W: 09 09 09 09 09 09 09 09 |........
W: 09 09                   |..
W: size=11
W: Content
W: 00 00 00 00 00 00 00 00 |........
W: 00 00 00                |...
W: size=12
W: Content
W: 0b 0b 0b 0b 0b 0b 0b 0b |........
W: 0b 0b 0b 0b             |....
W: size=13
W: Content
W: 00 00 00 00 00 00 00 00 |........
W: 00 00 00 00 00          |.....
W: size=14
W: Content
W: 0d 0d 0d 0d 0d 0d 0d 0d |........
W: 0d 0d 0d 0d 0d 0d       |......
W: size=15
W: Content
W: 00 00 00 00 00 00 00 00 |........
W: 00 00 00 00 00 00 00    |.......
W: size=16
W: Content
W: 0f 0f 0f 0f 0f 0f 0f 0f |........
W: 0f 0f 0f 0f 0f 0f 0f 0f |........
```

Exit QEMU by pressing `CTRL+A` `x`.

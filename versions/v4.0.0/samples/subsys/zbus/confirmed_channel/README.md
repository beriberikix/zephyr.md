---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/subsys/zbus/confirmed_channel/README.html
original_path: samples/subsys/zbus/confirmed_channel/README.html
---

# Confirmed channel

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/zbus/confirmed_channel/README.rst/..)

## Overview

This sample implements a simple way of using confirmed channels in zbus.
The confirmed channel can only be published when all the subscribers consume the message.

## Building and Running

This project outputs to the console. It can be built and executed
on QEMU as follows:

```shell
# From the root of the zephyr repository
west build -b qemu_x86 samples/subsys/zbus/confirmed_channel
west build -t run
```

### Sample Output

```shell
I: From listener -> Confirmed message payload = 0
I: From bar_sub2 subscriber -> Confirmed message payload = 0
I: From bar_sub1 subscriber -> Confirmed message payload = 0
I: From bar_sub3 subscriber -> Confirmed message payload = 0
I: From listener -> Confirmed message payload = 1
I: From bar_sub2 subscriber -> Confirmed message payload = 1
I: From bar_sub1 subscriber -> Confirmed message payload = 1
I: From bar_sub3 subscriber -> Confirmed message payload = 1
I: From listener -> Confirmed message payload = 2
I: From bar_sub2 subscriber -> Confirmed message payload = 2
I: From bar_sub1 subscriber -> Confirmed message payload = 2
I: From bar_sub3 subscriber -> Confirmed message payload = 2
I: From listener -> Confirmed message payload = 3
I: From bar_sub2 subscriber -> Confirmed message payload = 3
I: From bar_sub1 subscriber -> Confirmed message payload = 3
I: From bar_sub3 subscriber -> Confirmed message payload = 3
<continues>
```

Exit QEMU by pressing `CTRL`+`A` `x`.

## See also

[Zbus APIs](../../../../doxygen/html/group__zbus__apis.md)

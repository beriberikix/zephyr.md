---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/zbus/hello_world/README.html
original_path: samples/subsys/zbus/hello_world/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# zbus Hello World

## Overview

This sample implements a simple hello world application using zbus to make the threads talk to each other.

## Building and Running

This project outputs to the console. It can be built and executed
on QEMU as follows:

```shell
# From the root of the zephyr repository
west build -b qemu_x86 samples/subsys/zbus/hello_world
west build -t run
```

### Sample Output

```shell
D: Sensor sample started raw reading, version 0.1-2!
D: Channel list:
D: 0 - Channel acc_data:
D:       Message size: 12
D:       Observers:
D:       - my_listener
D:       - my_subscriber
D: 1 - Channel version:
D:       Message size: 4
D:       Observers:
D: Observers list:
D: 0 - Listener my_listener
D: 1 - Subscriber my_subscriber
D: START processing channel acc_data change
D: From listener -> Acc x=1, y=1, z=1
D: FINISH processing channel acc_data change
D: From subscriber -> Acc x=1, y=1, z=1
D: START processing channel acc_data change
D: From listener -> Acc x=2, y=2, z=2
D: FINISH processing channel acc_data change
D: From subscriber -> Acc x=2, y=2, z=2
```

Exit QEMU by pressing `CTRL+A` `x`.

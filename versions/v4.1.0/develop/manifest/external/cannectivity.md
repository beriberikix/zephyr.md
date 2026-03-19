---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/develop/manifest/external/cannectivity.html
original_path: develop/manifest/external/cannectivity.html
---

# CANnectivity USB to CAN adapter firmware

## Introduction

[CANnectivity](https://github.com/CANnectivity/cannectivity) is an open source firmware for Universal Serial Bus (USB) to Controller Area Network
(CAN) adapters.

The firmware implements the Geschwister Schneider USB/CAN device protocol (often referred to as
“gs\_usb”). This protocol is supported by the Linux kernel SocketCAN [gs\_usb driver](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/net/can/usb/gs_usb.c), by
[python-can](https://python-can.readthedocs.io/en/stable/interfaces/gs_usb.html), and by many other software packages.

The firmware, which is based on Zephyr RTOS, allows turning your favorite microcontroller
development board into a full-fledged USB to CAN adapter.

CANnectivity is licensed under the Apache-2.0 license.

## Usage with Zephyr

The CANnectivity firmware repository is a Zephyr [module](../../modules.md#modules) which allows for reuse of
its components (i.e. the “gs\_usb” protocol implementation) outside of the CANnectivity firmware
application.

To pull in CANnectivity as a Zephyr module, either add it as a West project in the `west.yaml`
file or pull it in by adding a submanifest (e.g. `zephyr/submanifests/cannectivity.yaml`) file
with the following content and run `west update`:

```yaml
manifest:
  projects:
    - name: cannectivity
      url: https://github.com/CANnectivity/cannectivity.git
      revision: main
      path: custom/cannectivity # adjust the path as needed
```

Once CANnectivity is added as a Zephyr module, the “gs\_usb” implementation can be reused outside of
the CANnectivity firmware application by including its header:

```c
#include <cannectivity/usb/class/gs_usb.h>
```

Please see the header file for the API details.

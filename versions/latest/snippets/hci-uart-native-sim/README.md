---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/snippets/hci-uart-native-sim/README.html
original_path: snippets/hci-uart-native-sim/README.html
---

# Native Simulator support for hci\_uart Snippet (hci-uart-native-sim)

```shell
west build -S hci-uart-native-sim [...]
```

## Overview

This snippet allows to use hci\_uart connected to the host computer
with the Native Simulator. It is useful for testing with a real
Bluetooth controller, such as a device running Zephyr.

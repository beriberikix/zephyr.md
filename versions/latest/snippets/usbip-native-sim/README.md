---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/snippets/usbip-native-sim/README.html
original_path: snippets/usbip-native-sim/README.html
---

# USB/IP on Native Simulator Snippet (usbip-native-sim)

```shell
west build -S usbip-native-sim [...]
```

## Overview

This snippet allows to configure USB device samples with USB/IP support on a
native simulator. When building samples with this snippet, you need to provide
samples DTC overlays using the EXTRA\_DTC\_OVERLAY\_FILE argument.

This snippet is experimental, the behavior may change without notice.

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/snippets/wifi-ipv6/README.html
original_path: snippets/wifi-ipv6/README.html
---

# Wi-Fi IPv6 Snippet (wifi-ipv6)

```shell
west build -S wifi-ipv6 [...]
```

## Overview

This snippet enables IPv6 Wi-Fi support in supported networking samples.
The sample execution is postponed until Wi-Fi connectivity is established.

Use Wi-Fi shell to connect to the Wi-Fi network:

```shell
wifi connect -s <SSID> -k <key_management> -p <passphrase>
```

## Requirements

Hardware support for:

- [`CONFIG_WIFI`](../../kconfig.md#CONFIG_WIFI "CONFIG_WIFI")
- [`CONFIG_WIFI_USE_NATIVE_NETWORKING`](../../kconfig.md#CONFIG_WIFI_USE_NATIVE_NETWORKING "CONFIG_WIFI_USE_NATIVE_NETWORKING")

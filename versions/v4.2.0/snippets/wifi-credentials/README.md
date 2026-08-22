---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/snippets/wifi-credentials/README.html
original_path: snippets/wifi-credentials/README.html
---

# Wi-Fi Credentials Snippet (wifi-credential)

```shell
west build  -S wifi-credentials [...]
```

Can also be used along with the [Wi-Fi Enterprise Snippet (wifi-enterprise)](../wifi-enterprise/README.md#snippet-wifi-enterprise) snippet.

```shell
west build  -S "wifi-enterprise,wifi-credentials" [...]
```

## Overview

This snippet enables Wi-Fi credentials support.

## Requirements

Hardware support for:

- [`CONFIG_WIFI`](../../kconfig.md#CONFIG_WIFI "CONFIG_WIFI")
- [`CONFIG_WIFI_USE_NATIVE_NETWORKING`](../../kconfig.md#CONFIG_WIFI_USE_NATIVE_NETWORKING "CONFIG_WIFI_USE_NATIVE_NETWORKING")
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT`](../../kconfig.md#CONFIG_WIFI_NM_WPA_SUPPLICANT "CONFIG_WIFI_NM_WPA_SUPPLICANT")
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](../../kconfig.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE "CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE")

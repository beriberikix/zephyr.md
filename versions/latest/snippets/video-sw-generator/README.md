---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/snippets/video-sw-generator/README.html
original_path: snippets/video-sw-generator/README.html
---

# Video Software Generator Snippet (video-sw-generator)

```shell
west build -S video-sw-generator [...]
```

## Overview

This snippet instantiate a fake video source generating a test pattern continuously
for test purpose. It is selected as the `zephyr,camera` [Devicetree](../../build/dts/index.md#devicetree) chosen node.

## Requirements

No hardware support is required besides sufficient memory for the video resolution
declared by [`CONFIG_VIDEO_BUFFER_POOL_SZ_MAX`](../../kconfig.md#CONFIG_VIDEO_BUFFER_POOL_SZ_MAX "CONFIG_VIDEO_BUFFER_POOL_SZ_MAX").

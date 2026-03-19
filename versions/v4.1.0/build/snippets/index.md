---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/snippets/index.html
original_path: build/snippets/index.html
---

# Snippets

Snippets are a way to save build system settings in one place, and then use
those settings when you build any Zephyr application. This lets you save common
configuration separately when it applies to multiple different applications.

Some example use cases for snippets are:

- changing your board’s console backend from a “real” UART to a USB CDC-ACM UART
- enabling frequently-used debugging options
- applying interrelated configuration settings to your “main” CPU and a
  co-processor core on an AMP SoC

The following pages document this feature.

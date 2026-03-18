---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/snippets/index.html
original_path: build/snippets/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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

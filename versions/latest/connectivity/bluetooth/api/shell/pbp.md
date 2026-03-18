---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/shell/pbp.html
original_path: connectivity/bluetooth/api/shell/pbp.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Public Broadcast Profile Shell

This document describes how to run the Public Broadcast Profile functionality.
PBP does not have an associated service. Its purpose is to enable a faster, more
efficient discovery of Broadcast Sources that are transmitting audio with commonly used codec configurations.

## Using the PBP Shell

When the Bluetooth stack has been initialized (`bt init`), the Public Broadcast Profile is ready to run.
To set the Public Broadcast Announcement features call `pbp set_features`.

```shell
pbp --help
pbp - Bluetooth PBP shell commands
Subcommands:
  set_features    :Set the Public Broadcast Announcement features
```

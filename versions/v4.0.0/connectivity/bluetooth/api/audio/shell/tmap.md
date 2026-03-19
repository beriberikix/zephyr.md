---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/audio/shell/tmap.html
original_path: connectivity/bluetooth/api/audio/shell/tmap.html
---

# Bluetooth: Telephone and Media Audio Profile Shell

This document describes how to run the Telephone and Media Audio Profile functionality.
Unlike most other low-layer profiles, TMAP is a profile that exists and has a service (TMAS) on all
devices. Thus both the initiator and acceptor (or central and peripheral) should do a discovery of
the remote device’s TMAS to see what TMAP roles they support.

## Using the TMAP Shell

When the Bluetooth stack has been initialized (`bt init`), the TMAS can be registered by
calling `tmap init`.

```shell
tmap --help
tmap - Bluetooth TMAP shell commands
Subcommands:
  init          :Initialize and register the TMAS
  discover      :Discover TMAS on remote device
```

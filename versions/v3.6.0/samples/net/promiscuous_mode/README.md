---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/promiscuous_mode/README.html
original_path: samples/net/promiscuous_mode/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Promiscuous mode

## Overview

This application will enable promiscuous mode for every network
interface in the system. It will then start to listen for incoming
network packets and show information about them.

The application will also provide a shell so that user can enable
or disable promiscuous mode at runtime. The commands are called
`promisc on` and `promisc off`.

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

There are multiple ways to use this application. In this example QEMU
is used:

```shell
west build -b qemu_x86 samples/net/promiscuous_mode -- -DCONF_FILE=<config file to use>
```

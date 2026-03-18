---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/pm/overview.html
original_path: services/pm/overview.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Overview

The interfaces and APIs provided by the power management subsystem
are designed to be architecture and SOC independent. This enables power
management implementations to be easily adapted to different SOCs and
architectures.

The architecture and SOC independence is achieved by separating the core PM
infrastructure from implementations of the SOC specific components.
Thus a coherent abstraction is presented to the rest of the OS and the application layer.

The power management features are classified into the following categories.

- System Power Management
- Device Power Management

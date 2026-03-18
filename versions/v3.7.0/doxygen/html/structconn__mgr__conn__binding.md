---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structconn__mgr__conn__binding.html
original_path: doxygen/html/structconn__mgr__conn__binding.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

conn\_mgr\_conn\_binding Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Connection Manager Connectivity Implementation API](group__conn__mgr__connectivity__impl.md)

Connectivity Manager network interface binding structure.
[More...](#details)

`#include <[conn_mgr_connectivity_impl.h](conn__mgr__connectivity__impl_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_if](structnet__if.md) \* | [iface](#a59bd71867b19e002c310d85496833e8f) |
|  | The network interface the connectivity implementation is bound to. |
| const struct [conn\_mgr\_conn\_impl](structconn__mgr__conn__impl.md) \* | [impl](#a288749353194206b8d8766f8f17aff48) |
|  | The connectivity implementation the network device is bound to. |
| void \* | [ctx](#ad9102e2cf44b5940b21b1d160fea7611) |
|  | Pointer to private, per-iface connectivity context. |
| Generic connectivity state | |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a9b842340ebe872f30935b8f7e75d3605) |
|  | Connectivity flags. |
| int | [timeout](#a8474461cf7b00132441227aae07511ab) |
|  | Timeout (seconds). |

## Detailed Description

Connectivity Manager network interface binding structure.

Binds a conn\_mgr connectivity implementation to an iface / network device. Stores per-iface state for the connectivity implementation.

## Field Documentation

## [◆ ](#ad9102e2cf44b5940b21b1d160fea7611)ctx

| void\* conn\_mgr\_conn\_binding::ctx |
| --- |

Pointer to private, per-iface connectivity context.

## [◆ ](#a9b842340ebe872f30935b8f7e75d3605)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) conn\_mgr\_conn\_binding::flags |
| --- |

Connectivity flags.

Public boolean state and configuration values supported by all bindings. See [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f "Per-iface connectivity flags.") for options.

## [◆ ](#a59bd71867b19e002c310d85496833e8f)iface

| struct [net\_if](structnet__if.md)\* conn\_mgr\_conn\_binding::iface |
| --- |

The network interface the connectivity implementation is bound to.

## [◆ ](#a288749353194206b8d8766f8f17aff48)impl

| const struct [conn\_mgr\_conn\_impl](structconn__mgr__conn__impl.md)\* conn\_mgr\_conn\_binding::impl |
| --- |

The connectivity implementation the network device is bound to.

## [◆ ](#a8474461cf7b00132441227aae07511ab)timeout

| int conn\_mgr\_conn\_binding::timeout |
| --- |

Timeout (seconds).

Indicates to the connectivity implementation how long it should attempt to establish connectivity for during a connection attempt before giving up.

The connectivity implementation should give up on establishing connectivity after this timeout, even if persistence is enabled.

Set to [CONN\_MGR\_IF\_NO\_TIMEOUT](group__conn__mgr__connectivity.md#ga605eee24f4419b5cd6a50a0272979da7 "CONN_MGR_IF_NO_TIMEOUT") to indicate that no timeout should be used.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[conn\_mgr\_connectivity\_impl.h](conn__mgr__connectivity__impl_8h_source.md)

- [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

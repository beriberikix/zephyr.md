---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structconn__mgr__conn__api.html
original_path: doxygen/html/structconn__mgr__conn__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

conn\_mgr\_conn\_api Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Connection Manager Connectivity API](group__conn__mgr__connectivity.md) » [Connection Manager Connectivity Implementation API](group__conn__mgr__connectivity__impl.md)

Connectivity Manager Connectivity API structure.
[More...](#details)

`#include <[conn_mgr_connectivity_impl.h](conn__mgr__connectivity__impl_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [connect](#a92064a4752f0c9621c5c6a745708a66e) )(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding) |
|  | When called, the connectivity implementation should start attempting to establish connectivity (association with a network) for the bound iface pointed to by if\_conn->iface. |
| int(\* | [disconnect](#aee0d0fc9ef3361c8859b69128a087ba5) )(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding) |
|  | When called, the connectivity implementation should disconnect (disassociate), or stop any in-progress attempts to associate to a network, the bound iface pointed to by if\_conn->iface. |
| void(\* | [init](#ad2bb08d518e2f797002ca5257889a59e) )(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding) |
|  | Called once for each iface that has been bound to a connectivity implementation using this API. |
| int(\* | [set\_opt](#a5636cced185825bd6c6997b427fd6121) )(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding, int optname, const void \*optval, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) optlen) |
|  | Implementation callback for conn\_mgr\_if\_set\_opt. |
| int(\* | [get\_opt](#a15d4bd909af1a2d3348fdec822bca7b7) )(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding, int optname, void \*optval, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*optlen) |
|  | Implementation callback for conn\_mgr\_if\_get\_opt. |

## Detailed Description

Connectivity Manager Connectivity API structure.

Used to provide generic access to network association parameters and procedures

## Field Documentation

## [◆ ](#a92064a4752f0c9621c5c6a745708a66e)connect

| int(\* conn\_mgr\_conn\_api::connect) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding) |
| --- |

When called, the connectivity implementation should start attempting to establish connectivity (association with a network) for the bound iface pointed to by if\_conn->iface.

Must be non-blocking.

Called by [conn\_mgr\_if\_connect](group__conn__mgr__connectivity.md#ga575d367c95592fd9f4ead694ff94543f "conn_mgr_if_connect").

## [◆ ](#aee0d0fc9ef3361c8859b69128a087ba5)disconnect

| int(\* conn\_mgr\_conn\_api::disconnect) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding) |
| --- |

When called, the connectivity implementation should disconnect (disassociate), or stop any in-progress attempts to associate to a network, the bound iface pointed to by if\_conn->iface.

Must be non-blocking.

Called by [conn\_mgr\_if\_disconnect](group__conn__mgr__connectivity.md#gada2b5271b3e5dbcab629e1538b3d8eb4 "conn_mgr_if_disconnect").

## [◆ ](#a15d4bd909af1a2d3348fdec822bca7b7)get\_opt

| int(\* conn\_mgr\_conn\_api::get\_opt) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding, int optname, void \*optval, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*optlen) |
| --- |

Implementation callback for conn\_mgr\_if\_get\_opt.

Used to retrieve implementation-specific connectivity settings.

Calls to conn\_mgr\_if\_get\_opt on an iface will result in calls to this callback with the [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md "Connectivity Manager network interface binding structure.") struct bound to that iface.

It is up to the connectivity implementation to interpret optname. Options can be specific to the bound iface (pointed to by if\_conn->iface), or can apply to the whole connectivity implementation.

See the description of conn\_mgr\_if\_get\_opt for more details. get\_opt implementations should conform to that description.

## [◆ ](#ad2bb08d518e2f797002ca5257889a59e)init

| void(\* conn\_mgr\_conn\_api::init) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding) |
| --- |

Called once for each iface that has been bound to a connectivity implementation using this API.

Connectivity implementations should use this callback to perform any required per-bound-iface initialization.

Implementations may choose to gracefully handle invalid buffer lengths with partial writes, rather than raise errors, if deemed appropriate.

## [◆ ](#a5636cced185825bd6c6997b427fd6121)set\_opt

| int(\* conn\_mgr\_conn\_api::set\_opt) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding, int optname, const void \*optval, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) optlen) |
| --- |

Implementation callback for conn\_mgr\_if\_set\_opt.

Used to set implementation-specific connectivity settings.

Calls to conn\_mgr\_if\_set\_opt on an iface will result in calls to this callback with the [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md "Connectivity Manager network interface binding structure.") struct bound to that iface.

It is up to the connectivity implementation to interpret optname. Options can be specific to the bound iface (pointed to by if\_conn->iface), or can apply to the whole connectivity implementation.

See the description of conn\_mgr\_if\_set\_opt for more details. set\_opt implementations should conform to that description.

Implementations may choose to gracefully handle invalid buffer lengths with partial reads, rather than raise errors, if deemed appropriate.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[conn\_mgr\_connectivity\_impl.h](conn__mgr__connectivity__impl_8h_source.md)

- [conn\_mgr\_conn\_api](structconn__mgr__conn__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

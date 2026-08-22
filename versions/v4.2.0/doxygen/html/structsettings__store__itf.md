---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structsettings__store__itf.html
original_path: doxygen/html/structsettings__store__itf.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings\_store\_itf Struct Reference

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Settings](group__settings.md) » [Settings backend interface](group__settings__backend.md)

Backend handler functions.
[More...](#details)

`#include <[zephyr/settings/settings.h](settings_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [csi\_load](#a8c08da2cd010f5d73689e84d02d12734) )(struct [settings\_store](structsettings__store.md) \*cs, const struct [settings\_load\_arg](structsettings__load__arg.md) \*arg) |
|  | Loads values from storage limited to subtree defined by subtree. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [csi\_load\_one](#ae3492100b922be0ef0f44022044ed151) )(struct [settings\_store](structsettings__store.md) \*cs, const char \*name, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_len) |
|  | Loads one value from storage that corresponds to the key defined by name. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [csi\_get\_val\_len](#ace444937a6c762d88c0143871cb71600) )(struct [settings\_store](structsettings__store.md) \*cs, const char \*name) |
|  | Gets the value's length associated to the Key defined by name. |
| int(\* | [csi\_save\_start](#af6aae0b06cdc935975f19eb4c56eb991) )(struct [settings\_store](structsettings__store.md) \*cs) |
|  | Handler called before an export operation. |
| int(\* | [csi\_save](#af97b8a3e2bdac663dd3872117251f0d2) )(struct [settings\_store](structsettings__store.md) \*cs, const char \*name, const char \*value, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) val\_len) |
|  | Save a single key-value pair to storage. |
| int(\* | [csi\_save\_end](#a90c2506cb06e5d80dffc6c08c6007bce) )(struct [settings\_store](structsettings__store.md) \*cs) |
|  | Handler called after an export operation. |
| void \*(\* | [csi\_storage\_get](#a01440145124432463ada9a7e1badf727) )(struct [settings\_store](structsettings__store.md) \*cs) |

## Detailed Description

Backend handler functions.

Sources are registered using a call to [settings\_src\_register](group__settings__backend.md#gad16bb70588cf69873f8872d7bf90e1c6 "settings_src_register"). Destinations are registered using a call to [settings\_dst\_register](group__settings__backend.md#ga37bcada0be44b023cd3759e519e69d01 "settings_dst_register").

## Field Documentation

## [◆ ](#ace444937a6c762d88c0143871cb71600)csi\_get\_val\_len

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* settings\_store\_itf::csi\_get\_val\_len) (struct [settings\_store](structsettings__store.md) \*cs, const char \*name) |
| --- |

Gets the value's length associated to the Key defined by name.

It returns 0 if the Key/Value doesn't exist.

Parameters:

- cs[in] - Corresponding backend handler node.
- name[in] - Key in string format.

## [◆ ](#a8c08da2cd010f5d73689e84d02d12734)csi\_load

| int(\* settings\_store\_itf::csi\_load) (struct [settings\_store](structsettings__store.md) \*cs, const struct [settings\_load\_arg](structsettings__load__arg.md) \*arg) |
| --- |

Loads values from storage limited to subtree defined by subtree.

Parameters:

- cs[in] - Corresponding backend handler node,
- arg[in] - Structure that holds additional data for data loading.

Note
:   Backend is expected not to provide duplicates of the entities. It means that if the backend does not contain any functionality to really delete old keys, it has to filter out old entities and call load callback only on the final entity.

## [◆ ](#ae3492100b922be0ef0f44022044ed151)csi\_load\_one

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* settings\_store\_itf::csi\_load\_one) (struct [settings\_store](structsettings__store.md) \*cs, const char \*name, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_len) |
| --- |

Loads one value from storage that corresponds to the key defined by name.

Parameters:

- cs[in] - Corresponding backend handler node.
- name[in] - Key in string format.
- buf[in] - Buffer where data should be copied.
- buf\_len[in] - Length of buf.

## [◆ ](#af97b8a3e2bdac663dd3872117251f0d2)csi\_save

| int(\* settings\_store\_itf::csi\_save) (struct [settings\_store](structsettings__store.md) \*cs, const char \*name, const char \*value, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) val\_len) |
| --- |

Save a single key-value pair to storage.

Parameters:

- cs[in] - Corresponding backend handler node
- name[in] - Key in string format
- value[in] - Binary value
- val\_len[in] - Length of value in bytes.

## [◆ ](#a90c2506cb06e5d80dffc6c08c6007bce)csi\_save\_end

| int(\* settings\_store\_itf::csi\_save\_end) (struct [settings\_store](structsettings__store.md) \*cs) |
| --- |

Handler called after an export operation.

Parameters:

- cs[in] - Corresponding backend handler node Get pointer to the storage instance used by the backend.

Parameters:

- cs[in] - Corresponding backend handler node

## [◆ ](#af6aae0b06cdc935975f19eb4c56eb991)csi\_save\_start

| int(\* settings\_store\_itf::csi\_save\_start) (struct [settings\_store](structsettings__store.md) \*cs) |
| --- |

Handler called before an export operation.

Parameters:

- cs[in] - Corresponding backend handler node

## [◆ ](#a01440145124432463ada9a7e1badf727)csi\_storage\_get

| void \*(\* settings\_store\_itf::csi\_storage\_get) (struct [settings\_store](structsettings__store.md) \*cs) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/settings/[settings.h](settings_8h_source.md)

- [settings\_store\_itf](structsettings__store__itf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

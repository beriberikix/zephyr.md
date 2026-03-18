---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsettings__store__itf.html
original_path: doxygen/html/structsettings__store__itf.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings\_store\_itf Struct Reference

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Settings](group__settings.md) » [Settings backend interface](group__settings__backend.md)

Backend handler functions.
[More...](#details)

`#include <[settings.h](settings_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [csi\_load](#a8c08da2cd010f5d73689e84d02d12734) )(struct [settings\_store](structsettings__store.md) \*cs, const struct [settings\_load\_arg](structsettings__load__arg.md) \*arg) |
|  | Loads values from storage limited to subtree defined by subtree. |
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

## [◆ ](#a8c08da2cd010f5d73689e84d02d12734)csi\_load

| int(\* settings\_store\_itf::csi\_load) (struct [settings\_store](structsettings__store.md) \*cs, const struct [settings\_load\_arg](structsettings__load__arg.md) \*arg) |
| --- |

Loads values from storage limited to subtree defined by subtree.

Parameters:

- cs - Corresponding backend handler node,
- arg - Structure that holds additional data for data loading.

Note
:   Backend is expected not to provide duplicates of the entities. It means that if the backend does not contain any functionality to really delete old keys, it has to filter out old entities and call load callback only on the final entity.

## [◆ ](#af97b8a3e2bdac663dd3872117251f0d2)csi\_save

| int(\* settings\_store\_itf::csi\_save) (struct [settings\_store](structsettings__store.md) \*cs, const char \*name, const char \*value, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) val\_len) |
| --- |

Save a single key-value pair to storage.

Parameters:

- cs - Corresponding backend handler node
- name - Key in string format
- value - Binary value
- val\_len - Length of value in bytes.

## [◆ ](#a90c2506cb06e5d80dffc6c08c6007bce)csi\_save\_end

| int(\* settings\_store\_itf::csi\_save\_end) (struct [settings\_store](structsettings__store.md) \*cs) |
| --- |

Handler called after an export operation.

Parameters:

- cs - Corresponding backend handler node Get pointer to the storage instance used by the backend.

Parameters:

- cs - Corresponding backend handler node

## [◆ ](#af6aae0b06cdc935975f19eb4c56eb991)csi\_save\_start

| int(\* settings\_store\_itf::csi\_save\_start) (struct [settings\_store](structsettings__store.md) \*cs) |
| --- |

Handler called before an export operation.

Parameters:

- cs - Corresponding backend handler node

## [◆ ](#a01440145124432463ada9a7e1badf727)csi\_storage\_get

| void \*(\* settings\_store\_itf::csi\_storage\_get) (struct [settings\_store](structsettings__store.md) \*cs) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/settings/[settings.h](settings_8h_source.md)

- [settings\_store\_itf](structsettings__store__itf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

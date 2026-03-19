---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/its_8h.html
original_path: doxygen/html/its_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

its.h File Reference

The secure storage ITS implementation.
[More...](#details)

`#include "[its/common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_source.md)"`

[Go to the source code of this file.](its_8h_source.md)

| Functions | |
| --- | --- |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_its\_set](#a3d6f3a7b47866ebcbfe9eb4a5ca99758) ([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_length, const void \*p\_data, [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) create\_flags) |
|  | See [psa\_its\_set()](internal__trusted__storage_8h.md#a01e5344273e6d776d1f456c4d54a2ed8 "Creates a new or modifies an existing entry."), to which this function is analogous. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_its\_get](#a806bb5b9698a0f90b80b294d5f44645e) ([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_size, void \*p\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*p\_data\_length) |
|  | See [psa\_its\_get()](internal__trusted__storage_8h.md#a387d450b2a21673fba6c56e66c74b5f7 "Retrieves data associated with the provided uid."), to which this function is analogous. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_its\_get\_info](#a8588925b41cf848d473a7e50087df606) ([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, struct [psa\_storage\_info\_t](structpsa__storage__info__t.md) \*p\_info) |
|  | See [psa\_its\_get\_info()](internal__trusted__storage_8h.md#ae4efe6e7f9088fdf8ef4e126045a432b "Retrieves the metadata of a given entry."), to which this function is analogous. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_its\_remove](#a2d3337b1eb55deda25a8c75ea8d74ff5) ([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid) |
|  | See [psa\_its\_remove()](internal__trusted__storage_8h.md#abd70b9f9bc063e3651f315408f4ae04c "Removes the provided uid and its associated data."), to which this function is analogous. |

## Detailed Description

The secure storage ITS implementation.

The functions declared in this header implement the PSA ITS API when the secure storage subsystem is enabled. They must not be called directly, and this header must not be included other than when providing a custom implementation (

```
CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_CUSTOM
```

).

## Function Documentation

## [◆ ](#a806bb5b9698a0f90b80b294d5f44645e)secure\_storage\_its\_get()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_its\_get | ( | [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_offset*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_size*, |
|  |  | void \* | *p\_data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *p\_data\_length* ) |

See [psa\_its\_get()](internal__trusted__storage_8h.md#a387d450b2a21673fba6c56e66c74b5f7 "Retrieves data associated with the provided uid."), to which this function is analogous.

## [◆ ](#a8588925b41cf848d473a7e50087df606)secure\_storage\_its\_get\_info()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_its\_get\_info | ( | [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) | *uid*, |
| --- | --- | --- | --- |
|  |  | struct [psa\_storage\_info\_t](structpsa__storage__info__t.md) \* | *p\_info* ) |

See [psa\_its\_get\_info()](internal__trusted__storage_8h.md#ae4efe6e7f9088fdf8ef4e126045a432b "Retrieves the metadata of a given entry."), to which this function is analogous.

## [◆ ](#a2d3337b1eb55deda25a8c75ea8d74ff5)secure\_storage\_its\_remove()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_its\_remove | ( | [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) | *uid* | ) |  |
| --- | --- | --- | --- | --- | --- |

See [psa\_its\_remove()](internal__trusted__storage_8h.md#abd70b9f9bc063e3651f315408f4ae04c "Removes the provided uid and its associated data."), to which this function is analogous.

## [◆ ](#a3d6f3a7b47866ebcbfe9eb4a5ca99758)secure\_storage\_its\_set()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_its\_set | ( | [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_length*, |
|  |  | const void \* | *p\_data*, |
|  |  | [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) | *create\_flags* ) |

See [psa\_its\_set()](internal__trusted__storage_8h.md#a01e5344273e6d776d1f456c4d54a2ed8 "Creates a new or modifies an existing entry."), to which this function is analogous.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [its.h](its_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

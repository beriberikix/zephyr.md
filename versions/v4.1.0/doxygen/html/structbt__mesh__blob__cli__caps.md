---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__blob__cli__caps.html
original_path: doxygen/html/structbt__mesh__blob__cli__caps.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_cli\_caps Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB Transfer Client model API](group__bt__mesh__blob__cli.md)

Transfer capabilities of a Target node.
[More...](#details)

`#include <[blob_cli.h](blob__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [max\_size](#ae16411b1a36854d6f638a2bca1dc4c3b) |
|  | Max BLOB size. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [min\_block\_size\_log](#ac446317efdeca9edbb7df924d4e5a995) |
|  | Logarithmic representation of the minimum block size. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_block\_size\_log](#a5d44b3b9bf7e47af2e6ba930b2826b15) |
|  | Logarithmic representation of the maximum block size. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_chunks](#a318c96b89597dfdf9b68fbc8b999af11) |
|  | Max number of chunks per block. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_chunk\_size](#ad149164240e7c20a57a28c25109079df) |
|  | Max chunk size. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mtu\_size](#a89d6e1bbc55086cee410835edd6baf3a) |
|  | Max MTU size. |
| enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) | [modes](#a1c848a3a2a2ece3764df5cbf6cbfec6b) |
|  | Supported transfer modes. |

## Detailed Description

Transfer capabilities of a Target node.

## Field Documentation

## [◆ ](#a5d44b3b9bf7e47af2e6ba930b2826b15)max\_block\_size\_log

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_cli\_caps::max\_block\_size\_log |
| --- |

Logarithmic representation of the maximum block size.

## [◆ ](#ad149164240e7c20a57a28c25109079df)max\_chunk\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_cli\_caps::max\_chunk\_size |
| --- |

Max chunk size.

## [◆ ](#a318c96b89597dfdf9b68fbc8b999af11)max\_chunks

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_cli\_caps::max\_chunks |
| --- |

Max number of chunks per block.

## [◆ ](#ae16411b1a36854d6f638a2bca1dc4c3b)max\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_blob\_cli\_caps::max\_size |
| --- |

Max BLOB size.

## [◆ ](#ac446317efdeca9edbb7df924d4e5a995)min\_block\_size\_log

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_cli\_caps::min\_block\_size\_log |
| --- |

Logarithmic representation of the minimum block size.

## [◆ ](#a1c848a3a2a2ece3764df5cbf6cbfec6b)modes

| enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) bt\_mesh\_blob\_cli\_caps::modes |
| --- |

Supported transfer modes.

## [◆ ](#a89d6e1bbc55086cee410835edd6baf3a)mtu\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_cli\_caps::mtu\_size |
| --- |

Max MTU size.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob\_cli.h](blob__cli_8h_source.md)

- [bt\_mesh\_blob\_cli\_caps](structbt__mesh__blob__cli__caps.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

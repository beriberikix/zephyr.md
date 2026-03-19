---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structhttp__parser__settings.html
original_path: doxygen/html/structhttp__parser__settings.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_parser\_settings Struct Reference

`#include <[parser.h](parser_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) | [on\_message\_begin](#ac44144daecc8e8adbd477b7e6a794e26) |
| [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) | [on\_url](#a9c24dfa900b49bf3439bbfba572b42fb) |
| [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) | [on\_status](#a6d0f0203f3461a8889ad471de119c993) |
| [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) | [on\_header\_field](#acfb3fd7947c5ff3e16649c71aa13bff2) |
| [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) | [on\_header\_value](#a2af4e9085fa79ee52b31e626179bc561) |
| [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) | [on\_headers\_complete](#a743b24c8f33e0f1cf60a96c824c42071) |
| [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) | [on\_body](#aaa145d7c24c91f471b2079ecb6368ae4) |
| [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) | [on\_message\_complete](#afdd5beef93a4a7b32bc61ae088da64d2) |
| [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) | [on\_chunk\_header](#a497cf8f9d68e06e54684b71ee0f9f828) |
| [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) | [on\_chunk\_complete](#ac1c8453573094795ef41d4ba26e78846) |

## Field Documentation

## [◆ ](#aaa145d7c24c91f471b2079ecb6368ae4)on\_body

| [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) http\_parser\_settings::on\_body |
| --- |

## [◆ ](#ac1c8453573094795ef41d4ba26e78846)on\_chunk\_complete

| [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) http\_parser\_settings::on\_chunk\_complete |
| --- |

## [◆ ](#a497cf8f9d68e06e54684b71ee0f9f828)on\_chunk\_header

| [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) http\_parser\_settings::on\_chunk\_header |
| --- |

## [◆ ](#acfb3fd7947c5ff3e16649c71aa13bff2)on\_header\_field

| [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) http\_parser\_settings::on\_header\_field |
| --- |

## [◆ ](#a2af4e9085fa79ee52b31e626179bc561)on\_header\_value

| [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) http\_parser\_settings::on\_header\_value |
| --- |

## [◆ ](#a743b24c8f33e0f1cf60a96c824c42071)on\_headers\_complete

| [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) http\_parser\_settings::on\_headers\_complete |
| --- |

## [◆ ](#ac44144daecc8e8adbd477b7e6a794e26)on\_message\_begin

| [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) http\_parser\_settings::on\_message\_begin |
| --- |

## [◆ ](#afdd5beef93a4a7b32bc61ae088da64d2)on\_message\_complete

| [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) http\_parser\_settings::on\_message\_complete |
| --- |

## [◆ ](#a6d0f0203f3461a8889ad471de119c993)on\_status

| [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) http\_parser\_settings::on\_status |
| --- |

## [◆ ](#a9c24dfa900b49bf3439bbfba572b42fb)on\_url

| [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) http\_parser\_settings::on\_url |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[parser.h](parser_8h_source.md)

- [http\_parser\_settings](structhttp__parser__settings.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

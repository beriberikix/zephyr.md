---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structlog__link__api.html
original_path: doxygen/html/structlog__link__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_link\_api Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Log link API](group__log__link.md)

`#include <[log_link.h](log__link_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [initiate](#a82eb7351ca56f7b7f4215f5188697e29) )(const struct [log\_link](structlog__link.md) \*link, struct [log\_link\_config](structlog__link__config.md) \*config) |
| int(\* | [activate](#a153036e50cbab5c9bf4e62aeee5b3361) )(const struct [log\_link](structlog__link.md) \*link) |
| int(\* | [get\_domain\_name](#a7c08926ee7f33796c9627ede345a02dc) )(const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*length) |
| int(\* | [get\_source\_name](#a1f770c5f70d77aa69b825a91df15f5bc) )(const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*length) |
| int(\* | [get\_levels](#ae09ac3bf464a5372d8161c36f881906e) )(const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*runtime\_level) |
| int(\* | [set\_runtime\_level](#a994ea743a12677bdd4bf2d1eb51e6331) )(const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |

## Field Documentation

## [◆ ](#a153036e50cbab5c9bf4e62aeee5b3361)activate

| int(\* log\_link\_api::activate) (const struct [log\_link](structlog__link.md) \*link) |
| --- |

## [◆ ](#a7c08926ee7f33796c9627ede345a02dc)get\_domain\_name

| int(\* log\_link\_api::get\_domain\_name) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*length) |
| --- |

## [◆ ](#ae09ac3bf464a5372d8161c36f881906e)get\_levels

| int(\* log\_link\_api::get\_levels) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*runtime\_level) |
| --- |

## [◆ ](#a1f770c5f70d77aa69b825a91df15f5bc)get\_source\_name

| int(\* log\_link\_api::get\_source\_name) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*length) |
| --- |

## [◆ ](#a82eb7351ca56f7b7f4215f5188697e29)initiate

| int(\* log\_link\_api::initiate) (const struct [log\_link](structlog__link.md) \*link, struct [log\_link\_config](structlog__link__config.md) \*config) |
| --- |

## [◆ ](#a994ea743a12677bdd4bf2d1eb51e6331)set\_runtime\_level

| int(\* log\_link\_api::set\_runtime\_level) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_link.h](log__link_8h_source.md)

- [log\_link\_api](structlog__link__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

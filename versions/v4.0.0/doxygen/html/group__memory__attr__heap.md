---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__memory__attr__heap.html
original_path: doxygen/html/group__memory__attr__heap.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Memory heaps based on memory attributes

[Memory Management APIs](group__mem__mgmt.md)

Memory heaps based on memory attributes.
[More...](#details)

| Functions | |
| --- | --- |
| int | [mem\_attr\_heap\_pool\_init](#ga85301dfc19493a84e89f965ed793d576) (void) |
|  | Init the memory pool. |
| void \* | [mem\_attr\_heap\_alloc](#gac03747a12f19735fc1a66d324b19f367) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) attr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate memory with a specified attribute and size. |
| void \* | [mem\_attr\_heap\_aligned\_alloc](#ga6ef058b960a23ae8c0e57a71f5518dab) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) attr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate aligned memory with a specified attribute, size and alignment. |
| void | [mem\_attr\_heap\_free](#ga2a7ef3301abfdd263d86f529dc1ea0f8) (void \*block) |
|  | Free the allocated memory. |
| const struct [mem\_attr\_region\_t](structmem__attr__region__t.md) \* | [mem\_attr\_heap\_get\_region](#gac0d2db398f90a5bc76677c23552fba99) (void \*addr) |
|  | Get a specific memory region descriptor for a provided address. |

## Detailed Description

Memory heaps based on memory attributes.

## Function Documentation

## [◆ ](#ga6ef058b960a23ae8c0e57a71f5518dab)mem\_attr\_heap\_aligned\_alloc()

| void \* mem\_attr\_heap\_aligned\_alloc | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *attr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *align*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[mem_attr_heap.h](mem__attr__heap_8h.md)>`

Allocate aligned memory with a specified attribute, size and alignment.

Allocates a block of memory of the specified size in bytes and with a specified capability / attribute. Takes an additional parameter specifying a power of two alignment in bytes.

Parameters
:   | attr | capability / attribute requested for the memory block. |
    | --- | --- |
    | align | power of two alignment for the returned pointer in bytes. |
    | bytes | requested size of the allocation in bytes. |

Return values
:   | ptr | a valid pointer to the allocated memory. |
    | --- | --- |
    | NULL | if no memory is available with that attribute and size. |

## [◆ ](#gac03747a12f19735fc1a66d324b19f367)mem\_attr\_heap\_alloc()

| void \* mem\_attr\_heap\_alloc | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *attr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[mem_attr_heap.h](mem__attr__heap_8h.md)>`

Allocate memory with a specified attribute and size.

Allocates a block of memory of the specified size in bytes and with a specified capability / attribute. The attribute is used to select the correct memory heap to allocate memory from.

Parameters
:   | attr | capability / attribute requested for the memory block. |
    | --- | --- |
    | bytes | requested size of the allocation in bytes. |

Return values
:   | ptr | a valid pointer to the allocated memory. |
    | --- | --- |
    | NULL | if no memory is available with that attribute and size. |

## [◆ ](#ga2a7ef3301abfdd263d86f529dc1ea0f8)mem\_attr\_heap\_free()

| void mem\_attr\_heap\_free | ( | void \* | *block* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mem_attr_heap.h](mem__attr__heap_8h.md)>`

Free the allocated memory.

Used to free the passed block of memory that must be the return value of a previously call to [mem\_attr\_heap\_alloc](#gac03747a12f19735fc1a66d324b19f367) or [mem\_attr\_heap\_aligned\_alloc](#ga6ef058b960a23ae8c0e57a71f5518dab).

Parameters
:   | block | block to free, must be a pointer to a block allocated by [mem\_attr\_heap\_alloc](#gac03747a12f19735fc1a66d324b19f367) or [mem\_attr\_heap\_aligned\_alloc](#ga6ef058b960a23ae8c0e57a71f5518dab). |
    | --- | --- |

## [◆ ](#gac0d2db398f90a5bc76677c23552fba99)mem\_attr\_heap\_get\_region()

| const struct [mem\_attr\_region\_t](structmem__attr__region__t.md) \* mem\_attr\_heap\_get\_region | ( | void \* | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mem_attr_heap.h](mem__attr__heap_8h.md)>`

Get a specific memory region descriptor for a provided address.

Finds the memory region descriptor struct controlling the provided pointer.

Parameters
:   | addr | address to be found, must be a pointer to a block allocated by [mem\_attr\_heap\_alloc](#gac03747a12f19735fc1a66d324b19f367) or [mem\_attr\_heap\_aligned\_alloc](#ga6ef058b960a23ae8c0e57a71f5518dab). |
    | --- | --- |

Return values
:   | str | pointer to a memory region structure the address belongs to. |
    | --- | --- |

## [◆ ](#ga85301dfc19493a84e89f965ed793d576)mem\_attr\_heap\_pool\_init()

| int mem\_attr\_heap\_pool\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mem_attr_heap.h](mem__attr__heap_8h.md)>`

Init the memory pool.

This must be the first function to be called to initialize the memory pools from all the memory regions with the a software attribute.

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EALREADY | if the pool was already initialized. |
    | -ENOMEM | too many regions already allocated. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

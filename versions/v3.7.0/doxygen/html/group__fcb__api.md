---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__fcb__api.html
original_path: doxygen/html/group__fcb__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fcb API

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Flash Circular Buffer (FCB)](group__fcb.md)

Flash Circular Buffer APIs.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef int(\* | [fcb\_walk\_cb](#gaeed5144438ee00d83c9b3d3b4b7490ea)) (struct [fcb\_entry\_ctx](structfcb__entry__ctx.md) \*loc\_ctx, void \*arg) |
|  | FCB Walk callback function type. |

| Functions | |
| --- | --- |
| int | [fcb\_init](#gab304f3e9e28f6229d7ddbe638eda2f70) (int f\_area\_id, struct [fcb](structfcb.md) \*fcbp) |
|  | Initialize FCB instance. |
| int | [fcb\_append](#gad567d124d8b0fe181ed54cfbe33b315c) (struct [fcb](structfcb.md) \*fcbp, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, struct [fcb\_entry](structfcb__entry.md) \*loc) |
|  | Appends an entry to circular buffer. |
| int | [fcb\_append\_finish](#gaae445e8376db192ce45fff9dcf95c954) (struct [fcb](structfcb.md) \*fcbp, struct [fcb\_entry](structfcb__entry.md) \*append\_loc) |
|  | Finishes entry append operation. |
| int | [fcb\_walk](#gad50e579ec9430a23ef5525e74ceb21b2) (struct [fcb](structfcb.md) \*fcbp, struct [flash\_sector](structflash__sector.md) \*sector, [fcb\_walk\_cb](#gaeed5144438ee00d83c9b3d3b4b7490ea) cb, void \*cb\_arg) |
|  | Walk over all entries in the FCB sector. |
| int | [fcb\_getnext](#ga7908a252a09ebbb98b60a505220072bc) (struct [fcb](structfcb.md) \*fcbp, struct [fcb\_entry](structfcb__entry.md) \*loc) |
|  | Get next fcb entry location. |
| int | [fcb\_rotate](#gad2fb288645e678dd6ea05b0871d5e774) (struct [fcb](structfcb.md) \*fcbp) |
|  | Rotate fcb sectors. |
| int | [fcb\_append\_to\_scratch](#ga22b2bab8af3004c93e5d40659ccfec29) (struct [fcb](structfcb.md) \*fcbp) |
|  | Start using the scratch block. |
| int | [fcb\_free\_sector\_cnt](#gaa9beaa3f5a6cc52b7e460d5670fdaabf) (struct [fcb](structfcb.md) \*fcbp) |
|  | Get free sector count. |
| int | [fcb\_is\_empty](#gade8af12645d769ce3b27848976ada32a) (struct [fcb](structfcb.md) \*fcbp) |
|  | Check whether FCB has any data. |
| int | [fcb\_offset\_last\_n](#gac15df95c0d9bed45c9da39802411598d) (struct [fcb](structfcb.md) \*fcbp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) entries, struct [fcb\_entry](structfcb__entry.md) \*last\_n\_entry) |
|  | Finds the fcb entry that gives back up to n entries at the end. |
| int | [fcb\_clear](#gaab78da410b7e709854e29219eb02a0c9) (struct [fcb](structfcb.md) \*fcbp) |
|  | Clear fcb instance storage. |

## Detailed Description

Flash Circular Buffer APIs.

## Typedef Documentation

## [◆ ](#gaeed5144438ee00d83c9b3d3b4b7490ea)fcb\_walk\_cb

| typedef int(\* fcb\_walk\_cb) (struct [fcb\_entry\_ctx](structfcb__entry__ctx.md) \*loc\_ctx, void \*arg) |
| --- |

`#include <[fcb.h](fcb_8h.md)>`

FCB Walk callback function type.

Type of function which is expected to be called while walking over fcb entries thanks to a [fcb\_walk](#gad50e579ec9430a23ef5525e74ceb21b2) call.

Entry data can be read using [flash\_area\_read()](group__flash__area__api.md#ga7c55704b0c0061a4715470676114b127 "Read flash area data."), using loc\_ctx fields as arguments. If cb wants to stop the walk, it should return non-zero value.

Parameters
:   | [in] | loc\_ctx | entry location information (full context) |
    | --- | --- | --- |
    | [in,out] | arg | callback context, transferred from [fcb\_walk](#gad50e579ec9430a23ef5525e74ceb21b2). |

Returns
:   0 continue walking, non-zero stop walking.

## Function Documentation

## [◆ ](#gad567d124d8b0fe181ed54cfbe33b315c)fcb\_append()

| int fcb\_append | ( | struct [fcb](structfcb.md) \* | *fcbp*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, |
|  |  | struct [fcb\_entry](structfcb__entry.md) \* | *loc* ) |

`#include <[fcb.h](fcb_8h.md)>`

Appends an entry to circular buffer.

When writing the contents for the entry, use loc->fe\_sector and loc->fe\_data\_off with [flash\_area\_write()](group__flash__area__api.md#gaa56052f8d6bf4f6966752bc21f5cceb8 "Write data to flash area.") to fcb [flash\_area](structflash__area.md "Flash partition."). When you're finished, call [fcb\_append\_finish()](#gaae445e8376db192ce45fff9dcf95c954) with loc as argument.

Parameters
:   | [in] | fcbp | FCB instance structure. |
    | --- | --- | --- |
    | [in] | len | Length of data which are expected to be written as the entry payload. |
    | [out] | loc | entry location information |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#gaae445e8376db192ce45fff9dcf95c954)fcb\_append\_finish()

| int fcb\_append\_finish | ( | struct [fcb](structfcb.md) \* | *fcbp*, |
| --- | --- | --- | --- |
|  |  | struct [fcb\_entry](structfcb__entry.md) \* | *append\_loc* ) |

`#include <[fcb.h](fcb_8h.md)>`

Finishes entry append operation.

Parameters
:   | [in] | fcbp | FCB instance structure. |
    | --- | --- | --- |
    | [in] | append\_loc | entry location information |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#ga22b2bab8af3004c93e5d40659ccfec29)fcb\_append\_to\_scratch()

| int fcb\_append\_to\_scratch | ( | struct [fcb](structfcb.md) \* | *fcbp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fcb.h](fcb_8h.md)>`

Start using the scratch block.

Take one of the scratch blocks into use. So a scratch sector becomes active sector to which entries can be appended.

Parameters
:   | [in] | fcbp | FCB instance structure. |
    | --- | --- | --- |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#gaab78da410b7e709854e29219eb02a0c9)fcb\_clear()

| int fcb\_clear | ( | struct [fcb](structfcb.md) \* | *fcbp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fcb.h](fcb_8h.md)>`

Clear fcb instance storage.

Parameters
:   | [in] | fcbp | FCB instance structure. |
    | --- | --- | --- |

Returns
:   0 on success; non-zero on failure

## [◆ ](#gaa9beaa3f5a6cc52b7e460d5670fdaabf)fcb\_free\_sector\_cnt()

| int fcb\_free\_sector\_cnt | ( | struct [fcb](structfcb.md) \* | *fcbp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fcb.h](fcb_8h.md)>`

Get free sector count.

Parameters
:   | [in] | fcbp | FCB instance structure. |
    | --- | --- | --- |

Returns
:   Number of free sectors.

## [◆ ](#ga7908a252a09ebbb98b60a505220072bc)fcb\_getnext()

| int fcb\_getnext | ( | struct [fcb](structfcb.md) \* | *fcbp*, |
| --- | --- | --- | --- |
|  |  | struct [fcb\_entry](structfcb__entry.md) \* | *loc* ) |

`#include <[fcb.h](fcb_8h.md)>`

Get next fcb entry location.

Function to obtain fcb entry location in relation to entry pointed by

loc. If loc->fe\_sector is set and loc->fe\_elem\_off is not 0 function fetches next fcb entry location. If loc->fe\_sector is NULL function fetches the oldest entry location within FCB storage. loc->fe\_sector is set and loc->fe\_elem\_off is 0 function fetches the first entry location in the fcb sector.

Parameters
:   | [in] | fcbp | FCB instance structure. |
    | --- | --- | --- |
    | [in,out] | loc | entry location information |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#gab304f3e9e28f6229d7ddbe638eda2f70)fcb\_init()

| int fcb\_init | ( | int | *f\_area\_id*, |
| --- | --- | --- | --- |
|  |  | struct [fcb](structfcb.md) \* | *fcbp* ) |

`#include <[fcb.h](fcb_8h.md)>`

Initialize FCB instance.

Parameters
:   | [in] | f\_area\_id | ID of flash area where fcb storage resides. |
    | --- | --- | --- |
    | [in,out] | fcbp | FCB instance structure. |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#gade8af12645d769ce3b27848976ada32a)fcb\_is\_empty()

| int fcb\_is\_empty | ( | struct [fcb](structfcb.md) \* | *fcbp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fcb.h](fcb_8h.md)>`

Check whether FCB has any data.

Parameters
:   | [in] | fcbp | FCB instance structure. |
    | --- | --- | --- |

Returns
:   Positive value if fcb is empty, otherwise 0.

## [◆ ](#gac15df95c0d9bed45c9da39802411598d)fcb\_offset\_last\_n()

| int fcb\_offset\_last\_n | ( | struct [fcb](structfcb.md) \* | *fcbp*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *entries*, |
|  |  | struct [fcb\_entry](structfcb__entry.md) \* | *last\_n\_entry* ) |

`#include <[fcb.h](fcb_8h.md)>`

Finds the fcb entry that gives back up to n entries at the end.

Parameters
:   | [in] | fcbp | FCB instance structure. |
    | --- | --- | --- |
    | [in] | entries | number of fcb entries the user wants to get |
    | [out] | last\_n\_entry | last\_n\_entry the [fcb\_entry](structfcb__entry.md "FCB entry info structure.") to be returned |

Returns
:   0 on there are any fcbs available; -ENOENT otherwise

## [◆ ](#gad2fb288645e678dd6ea05b0871d5e774)fcb\_rotate()

| int fcb\_rotate | ( | struct [fcb](structfcb.md) \* | *fcbp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fcb.h](fcb_8h.md)>`

Rotate fcb sectors.

Function erases the data from oldest sector. Upon that the next sector becomes the oldest. Active sector is also switched if needed.

Parameters
:   | [in] | fcbp | FCB instance structure. |
    | --- | --- | --- |

## [◆ ](#gad50e579ec9430a23ef5525e74ceb21b2)fcb\_walk()

| int fcb\_walk | ( | struct [fcb](structfcb.md) \* | *fcbp*, |
| --- | --- | --- | --- |
|  |  | struct [flash\_sector](structflash__sector.md) \* | *sector*, |
|  |  | [fcb\_walk\_cb](#gaeed5144438ee00d83c9b3d3b4b7490ea) | *cb*, |
|  |  | void \* | *cb\_arg* ) |

`#include <[fcb.h](fcb_8h.md)>`

Walk over all entries in the FCB sector.

Parameters
:   | [in] | sector | fcb sector to be walked. If null, traverse entire storage. |
    | --- | --- | --- |
    | [in] | fcbp | FCB instance structure. |
    | [in] | cb | pointer to the function which gets called for every entry. If cb wants to stop the walk, it should return non-zero value. |
    | [in,out] | cb\_arg | callback context, transferred to the callback implementation. |

Returns
:   0 on success, negative on failure (or transferred form callback return-value), positive transferred form callback return-value

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

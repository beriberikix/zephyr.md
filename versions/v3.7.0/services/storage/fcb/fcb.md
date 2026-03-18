---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/storage/fcb/fcb.html
original_path: services/storage/fcb/fcb.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Flash Circular Buffer (FCB)

Flash circular buffer provides an abstraction through which you can treat
flash like a FIFO. You append entries to the end, and read data from the
beginning.

Note

As of Zephyr release 2.1 the [NVS](../nvs/nvs.md#nvs-api) storage API is
recommended over FCB for use as a back-end for the [settings API](../../settings/index.md#settings-api).

## Description

Entries in the flash contain the length of the entry, the data within
the entry, and checksum over the entry contents.

Storage of entries in flash is done in a FIFO fashion. When you
request space for the next entry, space is located at the end of the
used area. When you start reading, the first entry served is the
oldest entry in flash.

Entries can be appended to the end of the area until storage space is
exhausted. You have control over what happens next; either erase oldest
block of data, thereby freeing up some space, or stop writing new data
until existing data has been collected. FCB treats underlying storage as
an array of flash sectors; when it erases old data, it does this a
sector at a time.

Entries in the flash are checksummed. That is how FCB detects whether
writing entry to flash completed ok. It will skip over entries which
don’t have a valid checksum.

## Usage

To add an entry to circular buffer:

- Call [`fcb_append()`](#c.fcb_append) to get the location where data can be written. If
  this fails due to lack of space, you can call [`fcb_rotate()`](#c.fcb_rotate) to erase
  the oldest sector which will make the space. And then call
  [`fcb_append()`](#c.fcb_append) again.
- Use [`flash_area_write()`](../flash_map/flash_map.md#c.flash_area_write "flash_area_write") to write entry contents.
- Call [`fcb_append_finish()`](#c.fcb_append_finish) when done. This completes the writing of the
  entry by calculating the checksum.

To read contents of the circular buffer:

- Call [`fcb_walk()`](#c.fcb_walk) with a pointer to your callback function.
- Within callback function copy in data from the entry using
  [`flash_area_read()`](../flash_map/flash_map.md#c.flash_area_read "flash_area_read"). You can tell when all data from within a sector
  has been read by monitoring the returned entry’s area pointer. Then you
  can call [`fcb_rotate()`](#c.fcb_rotate), if you’re done with that data.

Alternatively:

- Call [`fcb_getnext()`](#c.fcb_getnext) with 0 in entry offset to get the pointer to
  the oldest entry.
- Use [`flash_area_read()`](../flash_map/flash_map.md#c.flash_area_read "flash_area_read") to read entry contents.
- Call [`fcb_getnext()`](#c.fcb_getnext) with pointer to current entry to get the next one.
  And so on.

## API Reference

The FCB subsystem APIs are provided by `fcb.h`:

### Data structures

*group* Flash Circular Buffer Data Structures
:   Defines

    FCB\_MAX\_LEN
    :   Max length of element (16,383).

    FCB\_ENTRY\_FA\_DATA\_OFF(entry)
    :   Helper macro for calculating the data offset related to the fcb [flash\_area](../flash_map/flash_map.md#structflash__area) start offset.

        Parameters:
        :   - **entry** – fcb entry structure

    FCB\_FLAGS\_CRC\_DISABLED
    :   Flag to disable CRC for the fcb\_entries in flash.

    struct fcb\_entry
    :   *#include <fcb.h>*

        FCB entry info structure.

        This data structure describes the element location in the flash.

        You would use it to figure out what parameters to pass to [flash\_area\_read()](../flash_map/flash_map.md#group__flash__area__api_1ga7c55704b0c0061a4715470676114b127) to read element contents. Or to [flash\_area\_write()](../flash_map/flash_map.md#group__flash__area__api_1gaa56052f8d6bf4f6966752bc21f5cceb8) when adding a new element. Entry location is pointer to area (within fcb->f\_sectors), and offset within that area.

        Public Members

        struct [flash\_sector](../flash_map/flash_map.md#c.flash_sector "flash_sector") \*fe\_sector
        :   Pointer to info about sector where data are placed.

        uint32\_t fe\_elem\_off
        :   Offset from the start of the sector to beginning of element.

        uint32\_t fe\_data\_off
        :   Offset from the start of the sector to the start of element.

        uint16\_t fe\_data\_len
        :   Size of data area in fcb entry.

    struct fcb\_entry\_ctx
    :   *#include <fcb.h>*

        Structure for transferring complete information about FCB entry location within flash memory.

        Public Members

        struct [fcb\_entry](#c.fcb_entry) loc
        :   FCB entry info.

        const struct [flash\_area](../flash_map/flash_map.md#c.flash_area "flash_area") \*fap
        :   Flash area where the entry is placed.

    struct fcb
    :   *#include <fcb.h>*

        FCB instance structure.

        The following data structure describes the FCB itself. First part should be filled in by the user before calling [fcb\_init](#group__fcb__api_1gab304f3e9e28f6229d7ddbe638eda2f70). The second part is used by FCB for its internal bookkeeping.

        Public Members

        uint32\_t f\_magic
        :   Magic value, should not be 0xFFFFFFFF.

            It is xored with inversion of f\_erase\_value and placed in the beginning of FCB flash sector. FCB uses this when determining whether sector contains valid data or not. Giving it value of 0xFFFFFFFF means leaving bytes of the filed in “erased” state.

        uint8\_t f\_version
        :   Current version number of the data.

        uint8\_t f\_sector\_cnt
        :   Number of elements in sector array.

        uint8\_t f\_scratch\_cnt
        :   Number of sectors to keep empty.

            This can be used if you need to have scratch space for garbage collecting when FCB fills up.

        struct [flash\_sector](../flash_map/flash_map.md#c.flash_sector "flash_sector") \*f\_sectors
        :   Array of sectors, must be contiguous.

        struct [k\_mutex](../../../kernel/services/synchronization/mutexes.md#c.k_mutex "k_mutex") f\_mtx
        :   Locking for accessing the FCB data, internal state.

        struct [flash\_sector](../flash_map/flash_map.md#c.flash_sector "flash_sector") \*f\_oldest
        :   Pointer to flash sector containing the oldest data, internal state.

        struct [fcb\_entry](#c.fcb_entry) f\_active
        :   internal state

        uint16\_t f\_active\_id
        :   Flash location where the newest data is, internal state.

        uint8\_t f\_align
        :   writes to flash have to aligned to this, internal state

        const struct [flash\_area](../flash_map/flash_map.md#c.flash_area "flash_area") \*fap
        :   Flash area used by the fcb instance, internal state.

            This can be transfer to FCB user

        uint8\_t f\_erase\_value
        :   The value flash takes when it is erased.

            This is read from flash parameters and initialized upon call to fcb\_init.

### API functions

*group* fcb API
:   Flash Circular Buffer APIs.

    Typedefs

    typedef int (\*fcb\_walk\_cb)(struct [fcb\_entry\_ctx](#c.fcb_entry_ctx) \*loc\_ctx, void \*arg)
    :   FCB Walk callback function type.

        Type of function which is expected to be called while walking over fcb entries thanks to a [fcb\_walk](#group__fcb__api_1gad50e579ec9430a23ef5525e74ceb21b2) call.

        Entry data can be read using [flash\_area\_read()](../flash_map/flash_map.md#group__flash__area__api_1ga7c55704b0c0061a4715470676114b127), using loc\_ctx fields as arguments. If cb wants to stop the walk, it should return non-zero value.

        Param loc\_ctx:
        :   **[in]** entry location information (full context)

        Param arg:
        :   **[inout]** callback context, transferred from [fcb\_walk](#group__fcb__api_1gad50e579ec9430a23ef5525e74ceb21b2).

        Return:
        :   0 continue walking, non-zero stop walking.

    Functions

    int fcb\_init(int f\_area\_id, struct [fcb](#c.fcb) \*fcbp)
    :   Initialize FCB instance.

        Parameters:
        :   - **f\_area\_id** – **[in]** ID of flash area where fcb storage resides.
            - **fcbp** – **[inout]** FCB instance structure.

        Returns:
        :   0 on success, non-zero on failure.

    int fcb\_append(struct [fcb](#c.fcb) \*fcbp, uint16\_t len, struct [fcb\_entry](#c.fcb_entry) \*loc)
    :   Appends an entry to circular buffer.

        When writing the contents for the entry, use loc->fe\_sector and loc->fe\_data\_off with [flash\_area\_write()](../flash_map/flash_map.md#group__flash__area__api_1gaa56052f8d6bf4f6966752bc21f5cceb8) to fcb [flash\_area](../flash_map/flash_map.md#structflash__area). When you’re finished, call [fcb\_append\_finish()](#group__fcb__api_1gaae445e8376db192ce45fff9dcf95c954) with loc as argument.

        Parameters:
        :   - **fcbp** – **[in]** FCB instance structure.
            - **len** – **[in]** Length of data which are expected to be written as the entry payload.
            - **loc** – **[out]** entry location information

        Returns:
        :   0 on success, non-zero on failure.

    int fcb\_append\_finish(struct [fcb](#c.fcb) \*fcbp, struct [fcb\_entry](#c.fcb_entry) \*append\_loc)
    :   Finishes entry append operation.

        Parameters:
        :   - **fcbp** – **[in]** FCB instance structure.
            - **append\_loc** – **[in]** entry location information

        Returns:
        :   0 on success, non-zero on failure.

    int fcb\_walk(struct [fcb](#c.fcb) \*fcbp, struct [flash\_sector](../flash_map/flash_map.md#c.flash_sector "flash_sector") \*sector, [fcb\_walk\_cb](#c.fcb_walk_cb) cb, void \*cb\_arg)
    :   Walk over all entries in the FCB sector.

        Parameters:
        :   - **sector** – **[in]** fcb sector to be walked. If null, traverse entire storage.
            - **fcbp** – **[in]** FCB instance structure.
            - **cb** – **[in]** pointer to the function which gets called for every entry. If cb wants to stop the walk, it should return non-zero value.
            - **cb\_arg** – **[inout]** callback context, transferred to the callback implementation.

        Returns:
        :   0 on success, negative on failure (or transferred form callback return-value), positive transferred form callback return-value

    int fcb\_getnext(struct [fcb](#c.fcb) \*fcbp, struct [fcb\_entry](#c.fcb_entry) \*loc)
    :   Get next fcb entry location.

        Function to obtain fcb entry location in relation to entry pointed by

        loc. If loc->fe\_sector is set and loc->fe\_elem\_off is not 0 function fetches next fcb entry location. If loc->fe\_sector is NULL function fetches the oldest entry location within FCB storage. loc->fe\_sector is set and loc->fe\_elem\_off is 0 function fetches the first entry location in the fcb sector.

        Parameters:
        :   - **fcbp** – **[in]** FCB instance structure.
            - **loc** – **[inout]** entry location information

        Returns:
        :   0 on success, non-zero on failure.

    int fcb\_rotate(struct [fcb](#c.fcb) \*fcbp)
    :   Rotate fcb sectors.

        Function erases the data from oldest sector. Upon that the next sector becomes the oldest. Active sector is also switched if needed.

        Parameters:
        :   - **fcbp** – **[in]** FCB instance structure.

    int fcb\_append\_to\_scratch(struct [fcb](#c.fcb) \*fcbp)
    :   Start using the scratch block.

        Take one of the scratch blocks into use. So a scratch sector becomes active sector to which entries can be appended.

        Parameters:
        :   - **fcbp** – **[in]** FCB instance structure.

        Returns:
        :   0 on success, non-zero on failure.

    int fcb\_free\_sector\_cnt(struct [fcb](#c.fcb) \*fcbp)
    :   Get free sector count.

        Parameters:
        :   - **fcbp** – **[in]** FCB instance structure.

        Returns:
        :   Number of free sectors.

    int fcb\_is\_empty(struct [fcb](#c.fcb) \*fcbp)
    :   Check whether FCB has any data.

        Parameters:
        :   - **fcbp** – **[in]** FCB instance structure.

        Returns:
        :   Positive value if fcb is empty, otherwise 0.

    int fcb\_offset\_last\_n(struct [fcb](#c.fcb) \*fcbp, uint8\_t entries, struct [fcb\_entry](#c.fcb_entry) \*last\_n\_entry)
    :   Finds the fcb entry that gives back up to n entries at the end.

        Parameters:
        :   - **fcbp** – **[in]** FCB instance structure.
            - **entries** – **[in]** number of fcb entries the user wants to get
            - **last\_n\_entry** – **[out]** last\_n\_entry the [fcb\_entry](#structfcb__entry) to be returned

        Returns:
        :   0 on there are any fcbs available; -ENOENT otherwise

    int fcb\_clear(struct [fcb](#c.fcb) \*fcbp)
    :   Clear fcb instance storage.

        Parameters:
        :   - **fcbp** – **[in]** FCB instance structure.

        Returns:
        :   0 on success; non-zero on failure

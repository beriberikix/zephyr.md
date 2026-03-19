---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/storage/fcb/fcb.html
original_path: services/storage/fcb/fcb.html
---

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

- Call [`fcb_append()`](../../../doxygen/html/group__fcb__api.md#gad567d124d8b0fe181ed54cfbe33b315c) to get the location where data can be written. If
  this fails due to lack of space, you can call [`fcb_rotate()`](../../../doxygen/html/group__fcb__api.md#gad2fb288645e678dd6ea05b0871d5e774) to erase
  the oldest sector which will make the space. And then call
  [`fcb_append()`](../../../doxygen/html/group__fcb__api.md#gad567d124d8b0fe181ed54cfbe33b315c) again.
- Use [`flash_area_write()`](../../../doxygen/html/group__flash__area__api.md#gaa56052f8d6bf4f6966752bc21f5cceb8) to write entry contents.
- Call [`fcb_append_finish()`](../../../doxygen/html/group__fcb__api.md#gaae445e8376db192ce45fff9dcf95c954) when done. This completes the writing of the
  entry by calculating the checksum.

To read contents of the circular buffer:

- Call [`fcb_walk()`](../../../doxygen/html/group__fcb__api.md#gad50e579ec9430a23ef5525e74ceb21b2) with a pointer to your callback function.
- Within callback function copy in data from the entry using
  [`flash_area_read()`](../../../doxygen/html/group__flash__area__api.md#ga7c55704b0c0061a4715470676114b127). You can tell when all data from within a sector
  has been read by monitoring the returned entry’s area pointer. Then you
  can call [`fcb_rotate()`](../../../doxygen/html/group__fcb__api.md#gad2fb288645e678dd6ea05b0871d5e774), if you’re done with that data.

Alternatively:

- Call [`fcb_getnext()`](../../../doxygen/html/group__fcb__api.md#ga7908a252a09ebbb98b60a505220072bc) with 0 in entry offset to get the pointer to
  the oldest entry.
- Use [`flash_area_read()`](../../../doxygen/html/group__flash__area__api.md#ga7c55704b0c0061a4715470676114b127) to read entry contents.
- Call [`fcb_getnext()`](../../../doxygen/html/group__fcb__api.md#ga7908a252a09ebbb98b60a505220072bc) with pointer to current entry to get the next one.
  And so on.

## API Reference

The FCB subsystem APIs are provided by `fcb.h`:

### Data structures

[Flash Circular Buffer Data Structures](../../../doxygen/html/group__fcb__data__structures.md)

### API functions

[fcb API](../../../doxygen/html/group__fcb__api.md)

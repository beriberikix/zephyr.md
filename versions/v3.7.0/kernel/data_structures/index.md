---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/data_structures/index.html
original_path: kernel/data_structures/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Data Structures

Zephyr provides a library of common general purpose data structures
used within the kernel, but useful by application code in general.
These include list and balanced tree structures for storing ordered
data, and a ring buffer for managing “byte stream” data in a clean
way.

Note that in general, the collections are implemented as “intrusive”
data structures. The “node” data is the only struct used by the
library code, and it does not store a pointer or other metadata to
indicate what user data is “owned” by that node. Instead, the
expectation is that the node will be itself embedded within a
user-defined struct. Macros are provided to retrieve a user struct
address from the embedded node pointer in a clean way. The purpose
behind this design is to allow the collections to be used in contexts
where dynamic allocation is disallowed (i.e. there is no need to
allocate node objects because the memory is provided by the user).

Note also that these libraries are uniformly unsynchronized; access to
them is not threadsafe by default. These are data structures, not
synchronization primitives. The expectation is that any locking
needed will be provided by the user.

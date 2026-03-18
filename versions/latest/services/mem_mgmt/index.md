---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/mem_mgmt/index.html
original_path: services/mem_mgmt/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Memory Attributes

It is possible in the devicetree to mark the memory regions with attributes by
using the `zephyr,memory-attr` property. This property and the related memory
region can then be retrieved at run-time by leveraging a provided helper
library.

The set of general attributes that can be specified in the property are defined
and explained in [include/zephyr/dt-bindings/memory-attr/memory-attr.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/memory-attr/memory-attr.h).

For example, to mark a memory region in the devicetree as non-volatile, cacheable,
out-of-order:

```devicetree
mem: memory@10000000 {
    compatible = "mmio-sram";
    reg = <0x10000000 0x1000>;
    zephyr,memory-attr = <( DT_MEM_NON_VOLATILE | DT_MEM_CACHEABLE | DT_MEM_OOO )>;
};
```

Note

The `zephyr,memory-attr` usage does not result in any memory region
actually created. When it is needed to create an actual section out of the
devicetree defined memory region, it is possible to use the compatible
[`zephyr,memory-region`](../../build/dts/api/bindings/base/zephyr%2Cmemory-region.md#std-dtcompatible-zephyr-memory-region) that will result (only when supported
by the architecture) in a new linker section and region.

The `zephyr,memory-attr` property can also be used to set
architecture-specific and software-specific custom attributes that can be
interpreted at run time. This is leveraged, among other things, to create MPU
regions out of devicetree defined memory regions, for example:

```devicetree
mem: memory@10000000 {
    compatible = "mmio-sram";
    reg = <0x10000000 0x1000>;
    zephyr,memory-region = "NOCACHE_REGION";
    zephyr,memory-attr = <( DT_MEM_ARM(ATTR_MPU_RAM_NOCACHE) )>;
};
```

See [include/zephyr/dt-bindings/memory-attr/memory-attr-arm.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/memory-attr/memory-attr-arm.h) and
[Arm Cortex-M Developer Guide](../../hardware/arch/arm_cortex_m.md#arm-cortex-m-developer-guide) for more details about MPU usage.

The conventional and recommended way to deal and manage with memory regions
marked with attributes is by using the provided `mem-attr` helper library by
enabling [`CONFIG_MEM_ATTR`](../../kconfig.md#CONFIG_MEM_ATTR "CONFIG_MEM_ATTR"). When this option is enabled the
list of memory regions and their attributes are compiled in a user-accessible
array and a set of functions is made available that can be used to query, probe
and act on regions and attributes (see next section for more details).

Note

The `zephyr,memory-attr` property is only a descriptive property of the
capabilities of the associated memory region, but it does not result in any
actual setting for the memory to be set. The user, code or subsystem willing
to use this information to do some work (for example creating an MPU region
out of the property) must use either the provided `mem-attr` library or
the usual devicetree helpers to perform the required work / setting.

A test for the `mem-attr` library and its usage is provided in
`tests/subsys/mem_mgmt/mem_attr/`.

## Migration guide from zephyr,memory-region-mpu

When the `zephyr,memory-attr` property was introduced, the
`zephyr,memory-region-mpu` property was removed and deprecated.

The developers that are still using the deprecated property can move to the new
one by renaming the property and changing its value according to the following list:

```text
"RAM"         -> <( DT_ARM_MPU(ATTR_MPU_RAM) )>
"RAM_NOCACHE" -> <( DT_ARM_MPU(ATTR_MPU_RAM_NOCACHE) )>
"FLASH"       -> <( DT_ARM_MPU(ATTR_MPU_FLASH) )>
"PPB"         -> <( DT_ARM_MPU(ATTR_MPU_PPB) )>
"IO"          -> <( DT_ARM_MPU(ATTR_MPU_IO) )>
"EXTMEM"      -> <( DT_ARM_MPU(ATTR_MPU_EXTMEM) )>
```

## Memory Attributes Heap Allocator

It is possible to leverage the memory attribute property `zephyr,memory-attr`
to define and create a set of memory heaps from which the user can allocate
memory from with certain attributes / capabilities.

When the [`CONFIG_MEM_ATTR_HEAP`](../../kconfig.md#CONFIG_MEM_ATTR_HEAP "CONFIG_MEM_ATTR_HEAP") is set, every region marked
with one of the memory attributes listed in in
[include/zephyr/dt-bindings/memory-attr/memory-attr-sw.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/memory-attr/memory-attr-sw.h) is added
to a pool of memory heaps used for dynamic allocation of memory buffers with
certain attributes.

Here a non exhaustive list of possible attributes:

```text
DT_MEM_SW_ALLOC_CACHE
DT_MEM_SW_ALLOC_NON_CACHE
DT_MEM_SW_ALLOC_DMA
```

For example we can define several memory regions with different attributes and
use the appropriate attribute to indicate that it is possible to dynamically
allocate memory from those regions:

```devicetree
mem_cacheable: memory@10000000 {
    compatible = "mmio-sram";
    reg = <0x10000000 0x1000>;
    zephyr,memory-attr = <( DT_MEM_CACHEABLE | DT_MEM_SW_ALLOC_CACHE )>;
};

mem_non_cacheable: memory@20000000 {
    compatible = "mmio-sram";
    reg = <0x20000000 0x1000>;
    zephyr,memory-attr = <( DT_MEM_NON_CACHEABLE | ATTR_SW_ALLOC_NON_CACHE )>;
};

mem_cacheable_big: memory@30000000 {
    compatible = "mmio-sram";
    reg = <0x30000000 0x10000>;
    zephyr,memory-attr = <( DT_MEM_CACHEABLE | DT_MEM_OOO | DT_MEM_SW_ALLOC_CACHE )>;
};

mem_cacheable_dma: memory@40000000 {
    compatible = "mmio-sram";
    reg = <0x40000000 0x10000>;
    zephyr,memory-attr = <( DT_MEM_CACHEABLE      | DT_MEM_DMA |
                            DT_MEM_SW_ALLOC_CACHE | DT_MEM_SW_ALLOC_DMA )>;
};
```

The user can then dynamically carve memory out of those regions using the
provided functions, the library will take care of allocating memory from the
correct heap depending on the provided attribute and size:

```c
// Init the pool
mem_attr_heap_pool_init();

// Allocate 0x100 bytes of cacheable memory from `mem_cacheable`
block = mem_attr_heap_alloc(DT_MEM_SW_ALLOC_CACHE, 0x100);

// Allocate 0x200 bytes of non-cacheable memory aligned to 32 bytes
// from `mem_non_cacheable`
block = mem_attr_heap_aligned_alloc(ATTR_SW_ALLOC_NON_CACHE, 0x100, 32);

// Allocate 0x100 bytes of cacheable and dma-able memory from `mem_cacheable_dma`
block = mem_attr_heap_alloc(DT_MEM_SW_ALLOC_CACHE | DT_MEM_SW_ALLOC_DMA, 0x100);
```

When several regions are marked with the same attributes, the memory is allocated:

1. From the regions where the `zephyr,memory-attr` property has the requested
   property (or properties).
2. Among the regions as at point 1, from the smallest region if there is any
   unallocated space left for the requested size
3. If there is not enough space, from the next bigger region able to
   accommodate the requested size

The following example shows the point 3:

```c
// This memory is allocated from `mem_non_cacheable`
block = mem_attr_heap_alloc(DT_MEM_SW_ALLOC_CACHE, 0x100);

// This memory is allocated from `mem_cacheable_big`
block = mem_attr_heap_alloc(DT_MEM_SW_ALLOC_CACHE, 0x5000);
```

Note

The framework is assuming that the memory regions used to create the heaps
are usable by the code and available at init time. The user must take of
initializing and setting the memory area before calling
[`mem_attr_heap_pool_init()`](#c.mem_attr_heap_pool_init).

That means that the region must be correctly configured in terms of MPU /
MMU (if needed) and that an actual heap can be created out of it, for
example by leveraging the `zephyr,memory-region` property to create a
proper linker section to accommodate the heap.

## API Reference

*group* memory\_attr\_interface
:   Memory-Attr Interface.

    Defines

    DT\_MEMORY\_ATTR\_FOREACH\_STATUS\_OKAY\_NODE(fn)
    :   Invokes `fn` for every status `okay` node in the tree with property `zephyr,memory-attr`.

        The macro `fn` must take one parameter, which will be a node identifier with the `zephyr,memory-attr` property. The macro is expanded once for each node in the tree with status `okay`. The order that nodes are visited in is not specified.

        Parameters:
        :   - **fn** – macro to invoke

    Functions

    size\_t mem\_attr\_get\_regions(const struct [mem\_attr\_region\_t](#c.mem_attr_region_t) \*\*region)
    :   Get the list of memory regions.

        Get the list of enabled memory regions with their memory-attribute as gathered by DT.

        Parameters:
        :   - **region** – Pointer to pointer to the list of memory regions.

        Return values:
        :   **Number** – of memory regions returned in the parameter.

    int mem\_attr\_check\_buf(void \*addr, size\_t size, uint32\_t attr)
    :   Check if a buffer has correct size and attributes.

        This function is used to check if a given buffer with a given set of attributes fully match a memory region in terms of size and attributes.

        This is usually used to verify that a buffer has the expected attributes (for example the buffer is cacheable / non-cacheable or belongs to RAM / FLASH, etc…) and it has been correctly allocated.

        The expected set of attributes for the buffer is and-matched against the full set of attributes for the memory region it belongs to (bitmask). So the buffer is considered matching when at least that set of attributes are valid for the memory region (but the region can be marked also with other attributes besides the one passed as parameter).

        Parameters:
        :   - **addr** – Virtual address of the user buffer.
            - **size** – Size of the user buffer.
            - **attr** – Expected / desired attribute for the buffer.

        Return values:
        :   - **0** – if the buffer has the correct size and attribute.
            - **-ENOSYS** – if the operation is not supported (for example if the MMU is enabled).
            - **-ENOTSUP** – if the wrong parameters were passed.
            - **-EINVAL** – if the buffer has the wrong set of attributes.
            - **-ENOSPC** – if the buffer is too big for the region it belongs to.
            - **-ENOBUFS** – if the buffer is entirely allocated outside a memory region.

    struct mem\_attr\_region\_t
    :   *#include <mem\_attr.h>*

        memory-attr region structure.

        This structure represents the data gathered from DT about a memory-region marked with memory attributes.

        Public Members

        const char \*dt\_name
        :   Memory node full name.

        uintptr\_t dt\_addr
        :   Memory region physical address.

        size\_t dt\_size
        :   Memory region size.

        uint32\_t dt\_attr
        :   Memory region attributes.

*group* memory\_attr\_heap
:   Memory heaps based on memory attributes.

    Functions

    int mem\_attr\_heap\_pool\_init(void)
    :   Init the memory pool.

        This must be the first function to be called to initialize the memory pools from all the memory regions with the a software attribute.

        Return values:
        :   - **0** – on success.
            - **-EALREADY** – if the pool was already initialized.
            - **-ENOMEM** – too many regions already allocated.

    void \*mem\_attr\_heap\_alloc(uint32\_t attr, size\_t bytes)
    :   Allocate memory with a specified attribute and size.

        Allocates a block of memory of the specified size in bytes and with a specified capability / attribute. The attribute is used to select the correct memory heap to allocate memory from.

        Parameters:
        :   - **attr** – capability / attribute requested for the memory block.
            - **bytes** – requested size of the allocation in bytes.

        Return values:
        :   - **ptr** – a valid pointer to the allocated memory.
            - **NULL** – if no memory is available with that attribute and size.

    void \*mem\_attr\_heap\_aligned\_alloc(uint32\_t attr, size\_t align, size\_t bytes)
    :   Allocate aligned memory with a specified attribute, size and alignment.

        Allocates a block of memory of the specified size in bytes and with a specified capability / attribute. Takes an additional parameter specifying a power of two alignment in bytes.

        Parameters:
        :   - **attr** – capability / attribute requested for the memory block.
            - **align** – power of two alignment for the returned pointer in bytes.
            - **bytes** – requested size of the allocation in bytes.

        Return values:
        :   - **ptr** – a valid pointer to the allocated memory.
            - **NULL** – if no memory is available with that attribute and size.

    void mem\_attr\_heap\_free(void \*block)
    :   Free the allocated memory.

        Used to free the passed block of memory that must be the return value of a previously call to [mem\_attr\_heap\_alloc](#group__memory__attr__heap_1gac03747a12f19735fc1a66d324b19f367) or [mem\_attr\_heap\_aligned\_alloc](#group__memory__attr__heap_1ga6ef058b960a23ae8c0e57a71f5518dab).

        Parameters:
        :   - **block** – block to free, must be a pointer to a block allocated by [mem\_attr\_heap\_alloc](#group__memory__attr__heap_1gac03747a12f19735fc1a66d324b19f367) or [mem\_attr\_heap\_aligned\_alloc](#group__memory__attr__heap_1ga6ef058b960a23ae8c0e57a71f5518dab).

    const struct [mem\_attr\_region\_t](#c.mem_attr_region_t) \*mem\_attr\_heap\_get\_region(void \*addr)
    :   Get a specific memory region descriptor for a provided address.

        Finds the memory region descriptor struct controlling the provided pointer.

        Parameters:
        :   - **addr** – address to be found, must be a pointer to a block allocated by [mem\_attr\_heap\_alloc](#group__memory__attr__heap_1gac03747a12f19735fc1a66d324b19f367) or [mem\_attr\_heap\_aligned\_alloc](#group__memory__attr__heap_1ga6ef058b960a23ae8c0e57a71f5518dab).

        Return values:
        :   **str** – pointer to a memory region structure the address belongs to.

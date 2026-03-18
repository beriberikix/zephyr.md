---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/memory_management/virtual_memory.html
original_path: kernel/memory_management/virtual_memory.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Virtual Memory

Virtual memory (VM) in Zephyr provides developers with the ability to fine tune
access to memory. To utilize virtual memory, the platform must support
Memory Management Unit (MMU) and it must be enabled in the build. Due to
the target of Zephyr mainly being embedded systems, virtual memory
support in Zephyr differs a bit from that in traditional operating
systems:

Mapping of Kernel Image
:   Default is to do 1:1 mapping for the kernel image (including code and data)
    between physical and virtual memory address spaces, if demand paging
    is not enabled. Deviation from this requires careful manipulation of
    linker script.

Secondary Storage
:   Basic virtual memory support does not utilize secondary storage to
    extend usable memory. The maximum usable memory is the same as
    the physical memory.

    - [Demand Paging](demand_paging.md#memory-management-api-demand-paging) enables utilizing
      secondary storage as a backing store for virtual memory, thus
      allowing larger usable memory than the available physical memory.
      Note that demand paging needs to be explicitly enabled.
    - Although the virtual memory space can be larger than physical
      memory space, without enabling demand paging, all virtually
      mapped memory must be backed by physical memory.

## Kconfigs

### Required

These are the Kconfigs that need to be enabled or defined for kernel to support
virtual memory.

- [`CONFIG_MMU`](../../kconfig.md#CONFIG_MMU "CONFIG_MMU"): must be enabled for virtual memory support in
  kernel.
- [`CONFIG_MMU_PAGE_SIZE`](../../kconfig.md#CONFIG_MMU_PAGE_SIZE "CONFIG_MMU_PAGE_SIZE"): size of a memory page. Default is 4KB.
- [`CONFIG_KERNEL_VM_BASE`](../../kconfig.md#CONFIG_KERNEL_VM_BASE "CONFIG_KERNEL_VM_BASE"): base address of virtual address space.
- [`CONFIG_KERNEL_VM_SIZE`](../../kconfig.md#CONFIG_KERNEL_VM_SIZE "CONFIG_KERNEL_VM_SIZE"): size of virtual address space.
  Default is 8MB.
- [`CONFIG_KERNEL_VM_OFFSET`](../../kconfig.md#CONFIG_KERNEL_VM_OFFSET "CONFIG_KERNEL_VM_OFFSET"): kernel image starts at this offset
  from [`CONFIG_KERNEL_VM_BASE`](../../kconfig.md#CONFIG_KERNEL_VM_BASE "CONFIG_KERNEL_VM_BASE").

### Optional

- [`CONFIG_KERNEL_DIRECT_MAP`](../../kconfig.md#CONFIG_KERNEL_DIRECT_MAP "CONFIG_KERNEL_DIRECT_MAP"): permits 1:1 mappings between
  virtual and physical addresses, instead of kernel choosing addresses within
  the virtual address space. This is useful for mapping device MMIO regions for
  more precise access control.

## Memory Map Overview

This is an overview of the memory map of the virtual memory address space.
Note that the `Z_*` macros, which are used in code, may have different
meanings depending on architecture and Kconfigs, which will be explained
below.

```text
+--------------+ <- K_MEM_VIRT_RAM_START
| Undefined VM | <- architecture specific reserved area
+--------------+ <- K_MEM_KERNEL_VIRT_START
| Mapping for  |
| main kernel  |
| image        |
|              |
|              |
+--------------+ <- K_MEM_VM_FREE_START
|              |
| Unused,      |
| Available VM |
|              |
|..............| <- grows downward as more mappings are made
| Mapping      |
+--------------+
| Mapping      |
+--------------+
| ...          |
+--------------+
| Mapping      |
+--------------+ <- memory mappings start here
| Reserved     | <- special purpose virtual page(s) of size K_MEM_VM_RESERVED
+--------------+ <- K_MEM_VIRT_RAM_END
```

- `K_MEM_VIRT_RAM_START` is the beginning of the virtual memory address space.
  This needs to be page aligned. Currently, it is the same as
  [`CONFIG_KERNEL_VM_BASE`](../../kconfig.md#CONFIG_KERNEL_VM_BASE "CONFIG_KERNEL_VM_BASE").
- `K_MEM_VIRT_RAM_SIZE` is the size of the virtual memory address space.
  This needs to be page aligned. Currently, it is the same as
  [`CONFIG_KERNEL_VM_SIZE`](../../kconfig.md#CONFIG_KERNEL_VM_SIZE "CONFIG_KERNEL_VM_SIZE").
- `K_MEM_VIRT_RAM_END` is simply (`K_MEM_VIRT_RAM_START` + `K_MEM_VIRT_RAM_SIZE`).
- `K_MEM_KERNEL_VIRT_START` is the same as `z_mapped_start` specified in the linker
  script. This is the virtual address of the beginning of the kernel image at
  boot time.
- `K_MEM_KERNEL_VIRT_END` is the same as `z_mapped_end` specified in the linker
  script. This is the virtual address of the end of the kernel image at boot time.
- `K_MEM_VM_FREE_START` is the beginning of the virtual address space where addresses
  can be allocated for memory mapping. This depends on whether
  [`CONFIG_ARCH_MAPS_ALL_RAM`](../../kconfig.md#CONFIG_ARCH_MAPS_ALL_RAM "CONFIG_ARCH_MAPS_ALL_RAM") is enabled.

  - If it is enabled, which means all physical memory are mapped in virtual
    memory address space, and it is the same as
    ([`CONFIG_SRAM_BASE_ADDRESS`](../../kconfig.md#CONFIG_SRAM_BASE_ADDRESS "CONFIG_SRAM_BASE_ADDRESS") + [`CONFIG_SRAM_SIZE`](../../kconfig.md#CONFIG_SRAM_SIZE "CONFIG_SRAM_SIZE")).
  - If it is disabled, `K_MEM_VM_FREE_START` is the same `K_MEM_KERNEL_VIRT_END` which
    is the end of the kernel image.
- `K_MEM_VM_RESERVED` is an area reserved to support kernel functions. For example,
  some addresses are reserved to support demand paging.

## Virtual Memory Mappings

### Setting up Mappings at Boot

In general, most supported architectures set up the memory mappings at boot as
following:

- `.text` section is read-only and executable. It is accessible in
  both kernel and user modes.
- `.rodata` section is read-only and non-executable. It is accessible
  in both kernel and user modes.
- Other kernel sections, such as `.data`, `.bss` and `.noinit`, are
  read-write and non-executable. They are only accessible in kernel mode.

  - Stacks for user mode threads are automatically granted read-write access
    to their corresponding user mode threads during thread creation.
  - Global variables, by default, are not accessible to user mode threads.
    Refer to [Memory Domains and Partitions](../usermode/memory_domain.md#memory-domain) on how to
    use global variables in user mode threads, and on how to share data
    between user mode threads.

Caching modes for these mappings are architecture specific. They can be
none, write-back, or write-through.

Note that SoCs have their own additional mappings required to boot where
these mappings are defined under their own SoC configurations. These mappings
usually include device MMIO regions needed to setup the hardware.

### Mapping Anonymous Memory

The unused physical memory can be mapped in virtual address space on demand.
This is conceptually similar to memory allocation from heap, but these
mappings must be aligned on page size and have finer access control.

- [`k_mem_map()`](#c.k_mem_map) can be used to map unused physical memory:

  - The requested size must be multiple of page size.
  - The address returned is inside the virtual address space between
    `K_MEM_VM_FREE_START` and `K_MEM_VIRT_RAM_END`.
  - The mapped region is not guaranteed to be physically contiguous in memory.
  - Guard pages immediately before and after the mapped virtual region are
    automatically allocated to catch access issue due to buffer underrun
    or overrun.
- The mapped region can be unmapped (i.e. freed) via [`k_mem_unmap()`](#c.k_mem_unmap):

  - Caution must be exercised to give the pass the same region size to
    both [`k_mem_map()`](#c.k_mem_map) and [`k_mem_unmap()`](#c.k_mem_unmap). The unmapping
    function does not check if it is a valid mapped region before unmapping.

## API Reference

*group* Kernel Memory Management
:   Kernel Memory Management.

    Caching mode definitions.

    These are mutually exclusive.

    K\_MEM\_CACHE\_NONE
    :   No caching.

        Most drivers want this.

    K\_MEM\_CACHE\_WT
    :   Write-through caching.

        Used by certain drivers.

    K\_MEM\_CACHE\_WB
    :   Full write-back caching.

        Any RAM mapped wants this.

    K\_MEM\_CACHE\_MASK
    :   Reserved bits for cache modes in k\_map() flags argument.

    Region permission attributes.

    Default is read-only, no user, no exec

    K\_MEM\_PERM\_RW
    :   Region will have read/write access (and not read-only).

    K\_MEM\_PERM\_EXEC
    :   Region will be executable (normally forbidden).

    K\_MEM\_PERM\_USER
    :   Region will be accessible to user mode (normally supervisor-only).

    Region mapping behaviour attributes

    K\_MEM\_DIRECT\_MAP
    :   Region will be mapped to 1:1 virtual and physical address.

    k\_mem\_map() control flags

    K\_MEM\_MAP\_UNINIT
    :   The mapped region is not guaranteed to be zeroed.

        This may improve performance. The associated page frames may contain indeterminate data, zeroes, or even sensitive information.

        This may not be used with K\_MEM\_PERM\_USER as there are no circumstances where this is safe.

    K\_MEM\_MAP\_LOCK
    :   Region will be pinned in memory and never paged.

        Such memory is guaranteed to never produce a page fault due to page-outs or copy-on-write once the mapping call has returned. Physical page frames will be pre-fetched as necessary and pinned.

    Functions

    size\_t k\_mem\_free\_get(void)
    :   Return the amount of free memory available.

        The returned value will reflect how many free RAM page frames are available. If demand paging is enabled, it may still be possible to allocate more.

        The information reported by this function may go stale immediately if concurrent memory mappings or page-ins take place.

        Returns:
        :   Free physical RAM, in bytes

    static inline void \*k\_mem\_map(size\_t size, uint32\_t flags)
    :   Map anonymous memory into Zephyr’s address space.

        This function effectively increases the data space available to Zephyr. The kernel will choose a base virtual address and return it to the caller. The memory will have access permissions for all contexts set per the provided flags argument.

        If user thread access control needs to be managed in any way, do not enable K\_MEM\_PERM\_USER flags here; instead manage the region’s permissions with memory domain APIs after the mapping has been established. Setting K\_MEM\_PERM\_USER here will allow all user threads to access this memory which is usually undesirable.

        Unless K\_MEM\_MAP\_UNINIT is used, the returned memory will be zeroed.

        The mapped region is not guaranteed to be physically contiguous in memory. Physically contiguous buffers should be allocated statically and pinned at build time.

        Pages mapped in this way have write-back cache settings.

        The returned virtual memory pointer will be page-aligned. The size parameter, and any base address for re-mapping purposes must be page- aligned.

        Note that the allocation includes two guard pages immediately before and after the requested region. The total size of the allocation will be the requested size plus the size of these two guard pages.

        Many K\_MEM\_MAP\_\* flags have been implemented to alter the behavior of this function, with details in the documentation for these flags.

        Parameters:
        :   - **size** – Size of the memory mapping. This must be page-aligned.
            - **flags** – K\_MEM\_PERM\_\*, K\_MEM\_MAP\_\* control flags.

        Returns:
        :   The mapped memory location, or NULL if insufficient virtual address space, insufficient physical memory to establish the mapping, or insufficient memory for paging structures.

    static inline void k\_mem\_unmap(void \*addr, size\_t size)
    :   Un-map mapped memory.

        This removes a memory mapping for the provided page-aligned region. Associated page frames will be free and the kernel may re-use the associated virtual address region. Any paged out data pages may be discarded.

        Calling this function on a region which was not mapped to begin with is undefined behavior.

        Parameters:
        :   - **addr** – Page-aligned memory region base virtual address
            - **size** – Page-aligned memory region size

    size\_t k\_mem\_region\_align(uintptr\_t \*aligned\_addr, size\_t \*aligned\_size, uintptr\_t addr, size\_t size, size\_t align)
    :   Given an arbitrary region, provide a aligned region that covers it.

        The returned region will have both its base address and size aligned to the provided alignment value.

        Parameters:
        :   - **aligned\_addr** – **[out]** Aligned address
            - **aligned\_size** – **[out]** Aligned region size
            - **addr** – **[in]** Region base address
            - **size** – **[in]** Region size
            - **align** – **[in]** What to align the address and size to

        Return values:
        :   **offset** – between aligned\_addr and addr

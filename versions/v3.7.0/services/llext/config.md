---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/llext/config.html
original_path: services/llext/config.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Configuration

The following Kconfig options are available for the LLEXT subsystem:

## Heap size

The LLEXT subsystem needs a static heap to be allocated for extension related
data. The following option controls this allocation.

[`CONFIG_LLEXT_HEAP_SIZE`](../../kconfig.md#CONFIG_LLEXT_HEAP_SIZE "CONFIG_LLEXT_HEAP_SIZE")

> Size of the LLEXT heap in kilobytes.

Note

When [user mode](../../kernel/usermode/index.md#usermode-api) is enabled, the heap size must be
large enough to allow the extension sections to be allocated with the
alignment required by the architecture.

## ELF object type

The LLEXT subsystem supports loading different types of extensions; the type
can be set by choosing among the following Kconfig options:

[`CONFIG_LLEXT_TYPE_ELF_OBJECT`](../../kconfig.md#CONFIG_LLEXT_TYPE_ELF_OBJECT "CONFIG_LLEXT_TYPE_ELF_OBJECT")

> Build and expect relocatable files as binary object type for the LLEXT
> subsystem. A single compiler invocation is used to generate the object
> file.

[`CONFIG_LLEXT_TYPE_ELF_RELOCATABLE`](../../kconfig.md#CONFIG_LLEXT_TYPE_ELF_RELOCATABLE "CONFIG_LLEXT_TYPE_ELF_RELOCATABLE")

> Build and expect relocatable (partially linked) files as the binary
> object type for the LLEXT subsystem. These object files are generated
> by the linker by combining multiple object files into a single one.

[`CONFIG_LLEXT_TYPE_ELF_SHAREDLIB`](../../kconfig.md#CONFIG_LLEXT_TYPE_ELF_SHAREDLIB "CONFIG_LLEXT_TYPE_ELF_SHAREDLIB")

> Build and expect shared libraries as binary object type for the LLEXT
> subsystem. The standard linking process is used to generate the shared
> library from multiple object files.
>
> Note
>
> This is not currently supported on ARM architectures.

## Minimize allocations

The LLEXT subsystem loading mechanism, by default, uses a seek/read abstraction
and copies all data into allocated memory; this is done to allow the extension
to be loaded from any storage medium. Sometimes, however, data is already in a
buffer in RAM and copying it is not necessary. The following option allows the
LLEXT subsystem to optimize memory footprint in this case.

[`CONFIG_LLEXT_STORAGE_WRITABLE`](../../kconfig.md#CONFIG_LLEXT_STORAGE_WRITABLE "CONFIG_LLEXT_STORAGE_WRITABLE")

> Allow the extension to be loaded by directly referencing section data
> into the ELF buffer. To be effective, this requires the use of an ELF
> loader that supports the `peek` functionality, such as the
> [`llext_buf_loader`](api.md#c.llext_buf_loader "llext_buf_loader").
>
> Warning
>
> The application must ensure that the buffer used to load the
> extension remains allocated until the extension is unloaded.
>
> Note
>
> This will directly modify the contents of the buffer during the link
> phase. Once the extension is unloaded, the buffer must be reloaded
> before it can be used again in a call to [`llext_load()`](api.md#c.llext_load "llext_load").
>
> Note
>
> This is currently required by the Xtensa architecture. Further
> information on this topic is available on GitHub issue [#75341](https://github.com/zephyrproject-rtos/zephyr/issues/75341).

## Using SLID for symbol lookups

When an extension is loaded, the LLEXT subsystem must find the address of all
the symbols residing in the main application that the extension references.
To this end, the main binary contains a LLEXT-dedicated symbol table, filled
with one symbol-name-to-address mapping entry for each symbol exported by the
main application to extensions. This table can then be searched into by the
LLEXT linker at extension load time. This process is pretty slow due to the
nature of string comparisons, and the size consumed by the table can become
significant as the number of exported symbols increases.

[`CONFIG_LLEXT_EXPORT_BUILTINS_BY_SLID`](../../kconfig.md#CONFIG_LLEXT_EXPORT_BUILTINS_BY_SLID "CONFIG_LLEXT_EXPORT_BUILTINS_BY_SLID")

> Perform an extra processing step on the Zephyr binary and on all
> extensions being built, converting every string in the symbol tables to
> a pointer-sized hash called Symbol Link Identifier (SLID), which is
> stored in the binary.
>
> This speeds up the symbol lookup process by allowing usage of
> integer-based comparisons rather than string-based ones. Another
> benefit of SLID-based linking is that storing symbol names in the
> binary is no longer necessary, which provides a significant decrease in
> symbol table size.
>
> Note
>
> This option is not currently compatible with the [LLEXT EDK](build.md#llext-build-edk).
>
> Note
>
> Using a different value for this option in the main binary and in
> extensions is not supported. For example, if the main application
> is built with `CONFIG_LLEXT_EXPORT_BUILTINS_BY_SLID=y`, it is
> forbidden to load an extension that was compiled with
> `CONFIG_LLEXT_EXPORT_BUILTINS_BY_SLID=n`.

## EDK configuration

Options influencing the generation and behavior of the LLEXT EDK are described
in [LLEXT EDK Kconfig options](build.md#llext-kconfig-edk).

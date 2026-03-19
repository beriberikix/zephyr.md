---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/llext/load.html
original_path: services/llext/load.html
---

# Loading extensions

Once an extension is built and the ELF file is available, it can be loaded into
the Zephyr application using the LLEXT API, which provides a way to load the
extension into memory, access its symbols and call its functions.

## Loading an extension

An extension may be loaded using any implementation of a [`llext_loader`](../../doxygen/html/structllext__loader.md)
which has a set of function pointers that provide the necessary functionality
to read the ELF data. A loader also provides some minimal context (memory)
needed by the [`llext_load()`](../../doxygen/html/group__llext__apis.md#ga0a4c3db30bc3ec7aa8a9b0e076af7157) function. An implementation over a buffer
containing an ELF in addressable memory in memory is available as
[`llext_buf_loader`](../../doxygen/html/structllext__buf__loader.md).

The extensions are loaded with a call to the [`llext_load()`](../../doxygen/html/group__llext__apis.md#ga0a4c3db30bc3ec7aa8a9b0e076af7157) function,
passing in the extension name and the configured loader. Once that completes
successfully, the extension is loaded into memory and is ready to be used.

Note

When [User Mode](../../kernel/usermode/index.md#usermode-api) is enabled, the extension will not be
included in any user memory domain. To allow access from user mode, the
[`llext_add_domain()`](../../doxygen/html/group__llext__apis.md#ga64b13edf15b7c233b49c9c8edff884e6) function must be called.

## Initializing and cleaning up the extension

The extension may define a number of initialization functions that must be
called after loading but before any function in it can be used; this is typical
in languages such as C++ that provide the concept of object constructors. The
same is true for cleanup functions that must be called before unloading the
extension.

LLEXT supports calling the functions listed in the `.preinit_array` and
`.init_array` sections of the ELF file with the [`llext_bringup()`](../../doxygen/html/group__llext__apis.md#ga01c0c23dba5ff1aa9da42c7895cc7fab)
function, and the functions listed in the `.fini_array` section with the
[`llext_teardown()`](../../doxygen/html/group__llext__apis.md#gae061bb6100ad394fcaca7751ff3dadba) function. These APIs are compatible with
[User Mode](../../kernel/usermode/index.md#usermode-api), and thus can be called from either kernel or
user context.

Important

The code run by these functions is fully determined by the contents of the
ELF file. This may have security implications if its origin is untrusted.

If the extension requires a dedicated thread, the [`llext_bootstrap()`](../../doxygen/html/group__llext__apis.md#ga809f7a7976b4436dad31aa03d9ea3729)
function can be used to minimize boilerplate code. This function has a
signature that is compatible with the [`k_thread_create()`](../../doxygen/html/group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367) API, and will
call [`llext_bringup()`](../../doxygen/html/group__llext__apis.md#ga01c0c23dba5ff1aa9da42c7895cc7fab), then a user-specified function in the same
context, and finally [`llext_teardown()`](../../doxygen/html/group__llext__apis.md#gae061bb6100ad394fcaca7751ff3dadba) before returning.

## Accessing code and data

To interact with the newly loaded extension, the host application must use the
[`llext_find_sym()`](../../doxygen/html/group__llext__apis.md#gac0982fad15a62723a5cad3f7edd6ba3e) function to get the address of the exported symbol.
The returned `void *` can then be cast to the appropriate type and used.

A wrapper for calling a function with no arguments is provided in
[`llext_call_fn()`](../../doxygen/html/group__llext__apis.md#gad50ad281c70093da99851723fc6af470).

## Cleaning up after use

The [`llext_unload()`](../../doxygen/html/group__llext__apis.md#gad3df7ed4d436846504c0047166eb929e) function must be called to free the memory used by
the extension once it is no longer required. After this call completes, all
pointers to symbols in the extension that were obtained will be invalid.

# Troubleshooting

This feature is being actively developed and as such it is possible that some
issues may arise. Since linking does modify the binary code, in case of errors
the results are difficult to predict. Some common issues may be:

- Results from [`llext_find_sym()`](../../doxygen/html/group__llext__apis.md#gac0982fad15a62723a5cad3f7edd6ba3e) point to an invalid address;
- Constants and variables defined in the extension do not have the expected
  values;
- Calling a function defined in an extension results in a hard fault, or memory
  in the main application is corrupted after returning from it.

If any of this happens, the following tips may help understand the issue:

- Make sure `CONFIG_LLEXT_LOG_LEVEL` is set to `DEBUG`, then
  obtain a log of the [`llext_load()`](../../doxygen/html/group__llext__apis.md#ga0a4c3db30bc3ec7aa8a9b0e076af7157) invocation.
- If possible, disable memory protection (MMU/MPU) and see if this results in
  different behavior.
- Try to simplify the extension to the minimum possible code that reproduces
  the issue.
- Use a debugger to inspect the memory and registers to try to understand what
  is happening.

  Note

  When using GDB, the `add_symbol_file` command may be used to load the
  debugging information and symbols from the ELF file. Make sure to specify
  the proper offset (usually the start of the `.text` section, reported
  as `region 0` in the debug logs.)

If the issue persists, please open an issue in the GitHub repository, including
all the above information.

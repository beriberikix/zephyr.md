---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/file_system/index.html
original_path: services/file_system/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# File Systems

Zephyr RTOS Virtual Filesystem Switch (VFS) allows applications to mount multiple
file systems at different mount points (e.g., `/fatfs` and `/lfs`). The
mount point data structure contains all the necessary information required
to instantiate, mount, and operate on a file system. The File system Switch
decouples the applications from directly accessing an individual file system’s
specific API or internal functions by introducing file system registration
mechanisms.

In Zephyr, any file system implementation or library can be plugged into or
pulled out through a file system registration API. Each file system
implementation must have a globally unique integer identifier; use
[`FS_TYPE_EXTERNAL_BASE`](#c.@337371300175243001036343124231261052246236353024.FS_TYPE_EXTERNAL_BASE) to avoid clashes with in-tree identifiers.

```c
int fs_register(int type, const struct fs_file_system_t *fs);

int fs_unregister(int type, const struct fs_file_system_t *fs);
```

Zephyr RTOS supports multiple instances of a file system by making use of
the mount point as the disk volume name, which is used by the file system library
while formatting or mounting a disk.

A file system is declared as:

```c
static struct fs_mount_t mp = {
.type = FS_FATFS,
.mnt_point = FATFS_MNTP,
.fs_data = &fat_fs,
};
```

where

- `FS_FATFS` is the file system type like FATFS or LittleFS.
- `FATFS_MNTP` is the mount point where the file system will be mounted.
- `fat_fs` is the file system data which will be used by fs\_mount() API.

## Samples

Samples for the VFS are mainly supplied in `samples/subsys/fs`, although various examples of the
VFS usage are provided as important functionalities in samples for different subsystems.
Here is the list of samples worth looking at:

- `samples/subsys/fs/fat_fs` is an example of FAT file system usage with SDHC media;
- `samples/subsys/shell/fs` is an example of Shell fs subsystem, using internal flash partition
  :   formatted to LittleFS;
- `samples/subsys/usb/mass/` example of USB Mass Storage device that uses FAT FS driver with RAM
  :   or SPI connected FLASH, or LittleFS in flash, depending on the sample configuration.

## API Reference

Related code samples

[File system manipulation](../../samples/subsys/fs/fs_sample/README.md#fs "Use file system API with various filesystems and storage devices.")
:   Use file system API with various filesystems and storage devices.

[File system shell](../../samples/subsys/shell/fs/README.md#shell-fs "Access a LittleFS file system partition in flash using the file system shell.")
:   Access a LittleFS file system partition in flash using the file system shell.

[Format filesystem](../../samples/subsys/fs/format/README.md#fs-format "Format different storage devices for different file systems.")
:   Format different storage devices for different file systems.

[LittleFS filesystem](../../samples/subsys/fs/littlefs/README.md#littlefs "Use file system API over LittleFS.")
:   Use file system API over LittleFS.

[USB Mass Storage](../../samples/subsys/usb/mass/README.md#usb-mass "Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.")
:   Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.

*group* file\_system\_api
:   File System APIs.

    fs\_open open and creation mode flags

    FS\_O\_READ
    :   Open for read flag.

    FS\_O\_WRITE
    :   Open for write flag.

    FS\_O\_RDWR
    :   Open for read-write flag combination.

    FS\_O\_MODE\_MASK
    :   Bitmask for read and write flags.

    FS\_O\_CREATE
    :   Create file if it does not exist.

    FS\_O\_APPEND
    :   Open/create file for append.

    FS\_O\_FLAGS\_MASK
    :   Bitmask for open/create flags.

    FS\_O\_MASK
    :   Bitmask for open flags.

    fs\_seek whence parameter values

    FS\_SEEK\_SET
    :   Seek from the beginning of file.

    FS\_SEEK\_CUR
    :   Seek from a current position.

    FS\_SEEK\_END
    :   Seek from the end of file.

    Defines

    FS\_MOUNT\_FLAG\_NO\_FORMAT
    :   Flag prevents formatting device if requested file system not found.

    FS\_MOUNT\_FLAG\_READ\_ONLY
    :   Flag makes mounted file system read-only.

    FS\_MOUNT\_FLAG\_AUTOMOUNT
    :   Flag used in pre-defined mount structures that are to be mounted on startup.

        This flag has no impact in user-defined mount structures.

    FS\_MOUNT\_FLAG\_USE\_DISK\_ACCESS
    :   Flag requests file system driver to use Disk Access API.

        When the flag is set to the [fs\_mount\_t.flags](#structfs__mount__t_1ac5bd11869b64cfe1794b446d388c7116) prior to fs\_mount call, a file system needs to use the Disk Access API, otherwise mount callback for the driver should return -ENOSUP; when the flag is not set the file system driver should use Flash API by default, unless it only supports Disc Access API. When file system will use Disk Access API and the flag is not set, the mount callback for the file system should set the flag on success.

    FSTAB\_ENTRY\_DT\_MOUNT\_FLAGS(node\_id)
    :   Get the common mount flags for an fstab entry.

        Parameters:
        :   - **node\_id** – the node identifier for a child entry in a zephyr,fstab node.

        Returns:
        :   a value suitable for initializing an [fs\_mount\_t](#structfs__mount__t) flags member.

    FS\_FSTAB\_ENTRY(node\_id)
    :   The name under which a zephyr,fstab entry mount structure is defined.

        Parameters:
        :   - **node\_id** – the node identifier for a child entry in a zephyr,fstab node.

    FS\_FSTAB\_DECLARE\_ENTRY(node\_id)
    :   Generate a declaration for the externally defined fstab entry.

        This will evaluate to the name of a struct [fs\_mount\_t](#structfs__mount__t) object.

        Parameters:
        :   - **node\_id** – the node identifier for a child entry in a zephyr,fstab node.

    Enums

    enum fs\_dir\_entry\_type
    :   Enumeration for directory entry types.

        *Values:*

        enumerator FS\_DIR\_ENTRY\_FILE = 0
        :   Identifier for file entry.

        enumerator FS\_DIR\_ENTRY\_DIR
        :   Identifier for directory entry.

    enum [anonymous]
    :   Enumeration to uniquely identify file system types.

        Zephyr supports in-tree file systems and external ones. Each requires a unique identifier used to register the file system implementation and to associate a mount point with the file system type. This anonymous enum defines global identifiers for the in-tree file systems.

        External file systems should be registered using unique identifiers starting at `FS_TYPE_EXTERNAL_BASE`. It is the responsibility of applications that use external file systems to ensure that these identifiers are unique if multiple file system implementations are used by the application.

        *Values:*

        enumerator FS\_FATFS = 0
        :   Identifier for in-tree FatFS file system.

        enumerator FS\_LITTLEFS
        :   Identifier for in-tree LittleFS file system.

        enumerator FS\_EXT2
        :   Identifier for in-tree Ext2 file system.

        enumerator FS\_TYPE\_EXTERNAL\_BASE
        :   Base identifier for external file systems.

    Functions

    static inline void fs\_file\_t\_init(struct [fs\_file\_t](#c.fs_file_t) \*zfp)
    :   Initialize [fs\_file\_t](#structfs__file__t) object.

        Initializes the [fs\_file\_t](#structfs__file__t) object; the function needs to be invoked on object before first use with fs\_open.

        Parameters:
        :   - **zfp** – Pointer to file object

    static inline void fs\_dir\_t\_init(struct [fs\_dir\_t](#c.fs_dir_t) \*zdp)
    :   Initialize [fs\_dir\_t](#structfs__dir__t) object.

        Initializes the [fs\_dir\_t](#structfs__dir__t) object; the function needs to be invoked on object before first use with fs\_opendir.

        Parameters:
        :   - **zdp** – Pointer to file object

    int fs\_open(struct [fs\_file\_t](#c.fs_file_t) \*zfp, const char \*file\_name, fs\_mode\_t flags)
    :   Open or create file.

        Opens or possibly creates a file and associates a stream with it. Successfully opened file, when no longer in use, should be closed with [fs\_close()](#group__file__system__api_1ga4811679c25021e9f763824e06292e043).

        `flags` can be 0 or a binary combination of one or more of the following identifiers:

        - `FS_O_READ` open for read
        - `FS_O_WRITE` open for write
        - `FS_O_RDWR` open for read/write (`[FS_O_READ](#group__file__system__api_1gafd1228407bcf929a175cc18802cda4b2) | [FS_O_WRITE](#group__file__system__api_1ga0e86c5413b46133e824deaa89b16ee8d)`)
        - `FS_O_CREATE` create file if it does not exist
        - `FS_O_APPEND` move to end of file before each write

        Warning

        If `flags` are set to 0 the function will open file, if it exists and is accessible, but you will have no read/write access to it.

        Parameters:
        :   - **zfp** – Pointer to a file object
            - **file\_name** – The name of a file to open
            - **flags** – The mode flags

        Return values:
        :   - **0** – on success;
            - **-EBUSY** – when zfp is already used;
            - **-EINVAL** – when a bad file name is given;
            - **-EROFS** – when opening read-only file for write, or attempting to create a file on a system that has been mounted with the FS\_MOUNT\_FLAG\_READ\_ONLY flag;
            - **-ENOENT** – when the file does not exist at the path;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – an other negative errno code, depending on a file system back-end.

    int fs\_close(struct [fs\_file\_t](#c.fs_file_t) \*zfp)
    :   Close file.

        Flushes the associated stream and closes the file.

        Parameters:
        :   - **zfp** – Pointer to the file object

        Return values:
        :   - **0** – on success;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – a negative errno code on error.

    int fs\_unlink(const char \*path)
    :   Unlink file.

        Deletes the specified file or directory

        Parameters:
        :   - **path** – Path to the file or directory to delete

        Return values:
        :   - **0** – on success;
            - **-EINVAL** – when a bad file name is given;
            - **-EROFS** – if file is read-only, or when file system has been mounted with the FS\_MOUNT\_FLAG\_READ\_ONLY flag;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – an other negative errno code on error.

    int fs\_rename(const char \*from, const char \*to)
    :   Rename file or directory.

        Performs a rename and / or move of the specified source path to the specified destination. The source path can refer to either a file or a directory. All intermediate directories in the destination path must already exist. If the source path refers to a file, the destination path must contain a full filename path, rather than just the new parent directory. If an object already exists at the specified destination path, this function causes it to be unlinked prior to the rename (i.e., the destination gets clobbered).

        Note

        Current implementation does not allow moving files between mount points.

        Parameters:
        :   - **from** – The source path
            - **to** – The destination path

        Return values:
        :   - **0** – on success;
            - **-EINVAL** – when a bad file name is given, or when rename would cause move between mount points;
            - **-EROFS** – if file is read-only, or when file system has been mounted with the FS\_MOUNT\_FLAG\_READ\_ONLY flag;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – an other negative errno code on error.

    ssize\_t fs\_read(struct [fs\_file\_t](#c.fs_file_t) \*zfp, void \*ptr, size\_t size)
    :   Read file.

        Reads up to `size` bytes of data to `ptr` pointed buffer, returns number of bytes read. A returned value may be lower than `size` if there were fewer bytes available than requested.

        Parameters:
        :   - **zfp** – Pointer to the file object
            - **ptr** – Pointer to the data buffer
            - **size** – Number of bytes to be read

        Return values:
        :   - **>=0** – a number of bytes read, on success;
            - **-EBADF** – when invoked on zfp that represents unopened/closed file;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – a negative errno code on error.

    ssize\_t fs\_write(struct [fs\_file\_t](#c.fs_file_t) \*zfp, const void \*ptr, size\_t size)
    :   Write file.

        Attempts to write `size` number of bytes to the specified file. If a negative value is returned from the function, the file pointer has not been advanced. If the function returns a non-negative number that is lower than `size`, the global `errno` variable should be checked for an error code, as the device may have no free space for data.

        Parameters:
        :   - **zfp** – Pointer to the file object
            - **ptr** – Pointer to the data buffer
            - **size** – Number of bytes to be written

        Return values:
        :   - **>=0** – a number of bytes written, on success;
            - **-EBADF** – when invoked on zfp that represents unopened/closed file;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – an other negative errno code on error.

    int fs\_seek(struct [fs\_file\_t](#c.fs_file_t) \*zfp, off\_t offset, int whence)
    :   Seek file.

        Moves the file position to a new location in the file. The `offset` is added to file position based on the `whence` parameter.

        Parameters:
        :   - **zfp** – Pointer to the file object
            - **offset** – Relative location to move the file pointer to
            - **whence** – Relative location from where offset is to be calculated.

              - `FS_SEEK_SET` for the beginning of the file;
              - `FS_SEEK_CUR` for the current position;
              - `FS_SEEK_END` for the end of the file.

        Return values:
        :   - **0** – on success;
            - **-EBADF** – when invoked on zfp that represents unopened/closed file;
            - **-ENOTSUP** – if not supported by underlying file system driver;
            - **<0** – an other negative errno code on error.

    off\_t fs\_tell(struct [fs\_file\_t](#c.fs_file_t) \*zfp)
    :   Get current file position.

        Retrieves and returns the current position in the file stream.

        The current revision does not validate the file object.

        Parameters:
        :   - **zfp** – Pointer to the file object

        Return values:
        :   - **>=** – 0 a current position in file;
            - **-EBADF** – when invoked on zfp that represents unopened/closed file;
            - **-ENOTSUP** – if not supported by underlying file system driver;
            - **<0** – an other negative errno code on error.

    int fs\_truncate(struct [fs\_file\_t](#c.fs_file_t) \*zfp, off\_t length)
    :   Truncate or extend an open file to a given size.

        Truncates the file to the new length if it is shorter than the current size of the file. Expands the file if the new length is greater than the current size of the file. The expanded region would be filled with zeroes.

        Note

        In the case of expansion, if the volume got full during the expansion process, the function will expand to the maximum possible length and return success. Caller should check if the expanded size matches the requested length.

        Parameters:
        :   - **zfp** – Pointer to the file object
            - **length** – New size of the file in bytes

        Return values:
        :   - **0** – on success;
            - **-EBADF** – when invoked on zfp that represents unopened/closed file;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – an other negative errno code on error.

    int fs\_sync(struct [fs\_file\_t](#c.fs_file_t) \*zfp)
    :   Flush cached write data buffers of an open file.

        The function flushes the cache of an open file; it can be invoked to ensure data gets written to the storage media immediately, e.g. to avoid data loss in case if power is removed unexpectedly.

        Note

        Closing a file will cause caches to be flushed correctly so the function need not be called when the file is being closed.

        Parameters:
        :   - **zfp** – Pointer to the file object

        Return values:
        :   - **0** – on success;
            - **-EBADF** – when invoked on zfp that represents unopened/closed file;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – a negative errno code on error.

    int fs\_mkdir(const char \*path)
    :   Directory create.

        Creates a new directory using specified path.

        Parameters:
        :   - **path** – Path to the directory to create

        Return values:
        :   - **0** – on success;
            - **-EEXIST** – if entry of given name exists;
            - **-EROFS** – if `path` is within read-only directory, or when file system has been mounted with the FS\_MOUNT\_FLAG\_READ\_ONLY flag;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – an other negative errno code on error

    int fs\_opendir(struct [fs\_dir\_t](#c.fs_dir_t) \*zdp, const char \*path)
    :   Directory open.

        Opens an existing directory specified by the path.

        Parameters:
        :   - **zdp** – Pointer to the directory object
            - **path** – Path to the directory to open

        Return values:
        :   - **0** – on success;
            - **-EINVAL** – when a bad directory path is given;
            - **-EBUSY** – when zdp is already used;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – a negative errno code on error.

    int fs\_readdir(struct [fs\_dir\_t](#c.fs_dir_t) \*zdp, struct [fs\_dirent](#c.fs_dirent) \*entry)
    :   Directory read entry.

        Reads directory entries of an open directory. In end-of-dir condition, the function will return 0 and set the `entry->name[0]` to 0.

        Note

        : Most existing underlying file systems do not generate POSIX special directory entries “.” or “..”. For consistency the abstraction layer will remove these from lower layer results so higher layers see consistent results.

        Parameters:
        :   - **zdp** – Pointer to the directory object
            - **entry** – Pointer to zfs\_dirent structure to read the entry into

        Return values:
        :   - **0** – on success or end-of-dir;
            - **-ENOENT** – when no such directory found;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – a negative errno code on error.

    int fs\_closedir(struct [fs\_dir\_t](#c.fs_dir_t) \*zdp)
    :   Directory close.

        Closes an open directory.

        Parameters:
        :   - **zdp** – Pointer to the directory object

        Return values:
        :   - **0** – on success;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – a negative errno code on error.

    int fs\_mount(struct [fs\_mount\_t](#c.fs_mount_t) \*mp)
    :   Mount filesystem.

        Perform steps needed for mounting a file system like calling the file system specific mount function and adding the mount point to mounted file system list.

        Note

        Current implementation of ELM FAT driver allows only following mount points: “/RAM:”,”/NAND:”,”/CF:”,”/SD:”,”/SD2:”,”/USB:”,”/USB2:”,”/USB3:” or mount points that consist of single digit, e.g: “/0:”, “/1:” and so forth.

        Parameters:
        :   - **mp** – Pointer to the [fs\_mount\_t](#structfs__mount__t) structure. Referenced object is not changed if the mount operation failed. A reference is captured in the fs infrastructure if the mount operation succeeds, and the application must not mutate the structure contents until fs\_unmount is successfully invoked on the same pointer.

        Return values:
        :   - **0** – on success;
            - **-ENOENT** – when file system type has not been registered;
            - **-ENOTSUP** – when not supported by underlying file system driver; when `FS_MOUNT_FLAG_USE_DISK_ACCESS` is set but driver does not support it.
            - **-EROFS** – if system requires formatting but `FS_MOUNT_FLAG_READ_ONLY` has been set;
            - **<0** – an other negative errno code on error.

    int fs\_unmount(struct [fs\_mount\_t](#c.fs_mount_t) \*mp)
    :   Unmount filesystem.

        Perform steps needed to unmount a file system like calling the file system specific unmount function and removing the mount point from mounted file system list.

        Parameters:
        :   - **mp** – Pointer to the [fs\_mount\_t](#structfs__mount__t) structure

        Return values:
        :   - **0** – on success;
            - **-EINVAL** – if no system has been mounted at given mount point;
            - **-ENOTSUP** – when not supported by underlying file system driver;
            - **<0** – an other negative errno code on error.

    int fs\_readmount(int \*index, const char \*\*name)
    :   Get path of mount point at index.

        This function iterates through the list of mount points and returns the directory name of the mount point at the given `index`. On success `index` is incremented and `name` is set to the mount directory name. If a mount point with the given `index` does not exist, `name` will be set to `NULL`.

        Parameters:
        :   - **index** – Pointer to mount point index
            - **name** – Pointer to pointer to path name

        Return values:
        :   - **0** – on success;
            - **-ENOENT** – if there is no mount point with given index.

    int fs\_stat(const char \*path, struct [fs\_dirent](#c.fs_dirent) \*entry)
    :   File or directory status.

        Checks the status of a file or directory specified by the `path`.

        Note

        The file on a storage device may not be updated until it is closed.

        Parameters:
        :   - **path** – Path to the file or directory
            - **entry** – Pointer to the zfs\_dirent structure to fill if the file or directory exists.

        Return values:
        :   - **0** – on success;
            - **-EINVAL** – when a bad directory or file name is given;
            - **-ENOENT** – when no such directory or file is found;
            - **-ENOTSUP** – when not supported by underlying file system driver;
            - **<0** – negative errno code on error.

    int fs\_statvfs(const char \*path, struct [fs\_statvfs](#c.fs_statvfs) \*stat)
    :   Retrieves statistics of the file system volume.

        Returns the total and available space in the file system volume.

        Parameters:
        :   - **path** – Path to the mounted directory
            - **stat** – Pointer to the zfs\_statvfs structure to receive the fs statistics.

        Return values:
        :   - **0** – on success;
            - **-EINVAL** – when a bad path to a directory, or a file, is given;
            - **-ENOTSUP** – when not implemented by underlying file system driver;
            - **<0** – an other negative errno code on error.

    int fs\_mkfs(int fs\_type, uintptr\_t dev\_id, void \*cfg, int flags)
    :   Create fresh file system.

        Parameters:
        :   - **fs\_type** – Type of file system to create.
            - **dev\_id** – Id of storage device.
            - **cfg** – Backend dependent init object. If NULL then default configuration is used.
            - **flags** – Additional flags for file system implementation.

        Return values:
        :   - **0** – on success;
            - **<0** – negative errno code on error.

    int fs\_register(int type, const struct [fs\_file\_system\_t](#c.fs_file_system_t) \*fs)
    :   Register a file system.

        Register file system with virtual file system. Number of allowed file system types to be registered is controlled with the CONFIG\_FILE\_SYSTEM\_MAX\_TYPES Kconfig option.

        Parameters:
        :   - **type** – Type of file system (ex: `FS_FATFS`)
            - **fs** – Pointer to File system

        Return values:
        :   - **0** – on success;
            - **-EALREADY** – when a file system of a given type has already been registered;
            - **-ENOSCP** – when there is no space left, in file system registry, to add this file system type.

    int fs\_unregister(int type, const struct [fs\_file\_system\_t](#c.fs_file_system_t) \*fs)
    :   Unregister a file system.

        Unregister file system from virtual file system.

        Parameters:
        :   - **type** – Type of file system (ex: `FS_FATFS`)
            - **fs** – Pointer to File system

        Return values:
        :   - **0** – on success;
            - **-EINVAL** – when file system of a given type has not been registered.

    struct fs\_mount\_t
    :   *#include <fs.h>*

        File system mount info structure.

        Public Members

        [sys\_dnode\_t](../../kernel/data_structures/dlist.md#c.sys_dnode_t "sys_dnode_t") node
        :   Entry for the fs\_mount\_list list.

        int type
        :   File system type.

        const char \*mnt\_point
        :   Mount point directory name (ex: “/fatfs”).

        void \*fs\_data
        :   Pointer to file system specific data.

        void \*storage\_dev
        :   Pointer to backend storage device.

        size\_t mountp\_len
        :   Length of Mount point string.

        const struct [fs\_file\_system\_t](#c.fs_file_system_t) \*fs
        :   Pointer to File system interface of the mount point.

        uint8\_t flags
        :   Mount flags.

    struct fs\_dirent
    :   *#include <fs.h>*

        Structure to receive file or directory information.

        Used in functions that read the directory entries to get file or directory information.

        Public Members

        enum [fs\_dir\_entry\_type](#c.fs_dir_entry_type) type
        :   File/directory type (FS\_DIR\_ENTRY\_FILE or FS\_DIR\_ENTRY\_DIR).

        char name[12 + 1]
        :   Name of file or directory.

        size\_t size
        :   Size of file (0 if directory).

    struct fs\_statvfs
    :   *#include <fs.h>*

        Structure to receive volume statistics.

        Used to retrieve information about total and available space in the volume.

        Public Members

        unsigned long f\_bsize
        :   Optimal transfer block size.

        unsigned long f\_frsize
        :   Allocation unit size.

        unsigned long f\_blocks
        :   Size of FS in f\_frsize units.

        unsigned long f\_bfree
        :   Number of free blocks.

    struct fs\_file\_t
    :   *#include <fs\_interface.h>*

        File object representing an open file.

        The object needs to be initialized with [fs\_file\_t\_init()](#group__file__system__api_1gad44be87cbda3ddc48021ed16d515f564).

        Public Members

        void \*filep
        :   Pointer to file object structure.

        const struct [fs\_mount\_t](#c.fs_mount_t) \*mp
        :   Pointer to mount point structure.

        fs\_mode\_t flags
        :   Open/create flags.

    struct fs\_dir\_t
    :   *#include <fs\_interface.h>*

        Directory object representing an open directory.

        The object needs to be initialized with [fs\_dir\_t\_init()](#group__file__system__api_1gacd31440cd0b10308e55a0484828ea2f3).

        Public Members

        void \*dirp
        :   Pointer to directory object structure.

        const struct [fs\_mount\_t](#c.fs_mount_t) \*mp
        :   Pointer to mount point structure.

    struct fs\_file\_system\_t
    :   *#include <fs\_sys.h>*

        File System interface structure.

        File operations

        int (\*open)(struct [fs\_file\_t](#c.fs_file_t) \*filp, const char \*fs\_path, fs\_mode\_t flags)
        :   Opens or creates a file, depending on flags given.

            Param filp:
            :   File to open/create.

            Param fs\_path:
            :   Path to the file.

            Param flags:
            :   Flags for opening/creating the file.

            Return:
            :   0 on success, negative errno code on fail.

        ssize\_t (\*read)(struct [fs\_file\_t](#c.fs_file_t) \*filp, void \*dest, size\_t nbytes)
        :   Reads nbytes number of bytes.

            Param filp:
            :   File to read from.

            Param dest:
            :   Destination buffer.

            Param nbytes:
            :   Number of bytes to read.

            Return:
            :   Number of bytes read on success, negative errno code on fail.

        ssize\_t (\*write)(struct [fs\_file\_t](#c.fs_file_t) \*filp, const void \*src, size\_t nbytes)
        :   Writes nbytes number of bytes.

            Param filp:
            :   File to write to.

            Param src:
            :   Source buffer.

            Param nbytes:
            :   Number of bytes to write.

            Return:
            :   Number of bytes written on success, negative errno code on fail.

        int (\*lseek)(struct [fs\_file\_t](#c.fs_file_t) \*filp, off\_t off, int whence)
        :   Moves the file position to a new location in the file.

            Param filp:
            :   File to move.

            Param off:
            :   Relative offset from the position specified by whence.

            Param whence:
            :   Position in the file. Possible values: SEEK\_CUR, SEEK\_SET, SEEK\_END.

            Return:
            :   New position in the file or negative errno code on fail.

        off\_t (\*tell)(struct [fs\_file\_t](#c.fs_file_t) \*filp)
        :   Retrieves the current position in the file.

            Param filp:
            :   File to get the current position from.

            Return:
            :   Current position in the file or negative errno code on fail.

        int (\*truncate)(struct [fs\_file\_t](#c.fs_file_t) \*filp, off\_t length)
        :   Truncates/expands the file to the new length.

            Param filp:
            :   File to truncate/expand.

            Param length:
            :   New length of the file.

            Return:
            :   0 on success, negative errno code on fail.

        int (\*sync)(struct [fs\_file\_t](#c.fs_file_t) \*filp)
        :   Flushes the cache of an open file.

            Param filp:
            :   File to flush.

            Return:
            :   0 on success, negative errno code on fail.

        int (\*close)(struct [fs\_file\_t](#c.fs_file_t) \*filp)
        :   Flushes the associated stream and closes the file.

            Param filp:
            :   File to close.

            Return:
            :   0 on success, negative errno code on fail.

        Directory operations

        int (\*opendir)(struct [fs\_dir\_t](#c.fs_dir_t) \*dirp, const char \*fs\_path)
        :   Opens an existing directory specified by the path.

            Param dirp:
            :   Directory to open.

            Param fs\_path:
            :   Path to the directory.

            Return:
            :   0 on success, negative errno code on fail.

        int (\*readdir)(struct [fs\_dir\_t](#c.fs_dir_t) \*dirp, struct [fs\_dirent](#c.fs_dirent) \*entry)
        :   Reads directory entries of an open directory.

            Param dirp:
            :   Directory to read from.

            Param entry:
            :   Next directory entry in the dirp directory.

            Return:
            :   0 on success, negative errno code on fail.

        int (\*closedir)(struct [fs\_dir\_t](#c.fs_dir_t) \*dirp)
        :   Closes an open directory.

            Param dirp:
            :   Directory to close.

            Return:
            :   0 on success, negative errno code on fail.

        File system level operations

        int (\*mount)(struct [fs\_mount\_t](#c.fs_mount_t) \*mountp)
        :   Mounts a file system.

            Param mountp:
            :   Mount point.

            Return:
            :   0 on success, negative errno code on fail.

        int (\*unmount)(struct [fs\_mount\_t](#c.fs_mount_t) \*mountp)
        :   Unmounts a file system.

            Param mountp:
            :   Mount point.

            Return:
            :   0 on success, negative errno code on fail.

        int (\*unlink)(struct [fs\_mount\_t](#c.fs_mount_t) \*mountp, const char \*name)
        :   Deletes the specified file or directory.

            Param mountp:
            :   Mount point.

            Param name:
            :   Path to the file or directory to delete.

            Return:
            :   0 on success, negative errno code on fail.

        int (\*rename)(struct [fs\_mount\_t](#c.fs_mount_t) \*mountp, const char \*from, const char \*to)
        :   Renames a file or directory.

            Param mountp:
            :   Mount point.

            Param from:
            :   Path to the file or directory to rename.

            Param to:
            :   New name of the file or directory.

            Return:
            :   0 on success, negative errno code on fail.

        int (\*mkdir)(struct [fs\_mount\_t](#c.fs_mount_t) \*mountp, const char \*name)
        :   Creates a new directory using specified path.

            Param mountp:
            :   Mount point.

            Param name:
            :   Path to the directory to create.

            Return:
            :   0 on success, negative errno code on fail.

        int (\*stat)(struct [fs\_mount\_t](#c.fs_mount_t) \*mountp, const char \*path, struct [fs\_dirent](#c.fs_dirent) \*entry)
        :   Checks the status of a file or directory specified by the path.

            Param mountp:
            :   Mount point.

            Param path:
            :   Path to the file or directory.

            Param entry:
            :   Directory entry.

            Return:
            :   0 on success, negative errno code on fail.

        int (\*statvfs)(struct [fs\_mount\_t](#c.fs_mount_t) \*mountp, const char \*path, struct [fs\_statvfs](#c.fs_statvfs) \*stat)
        :   Returns the total and available space on the file system volume.

            Param mountp:
            :   Mount point.

            Param path:
            :   Path to the file or directory.

            Param stat:
            :   File system statistics.

            Return:
            :   0 on success, negative errno code on fail.

        int (\*mkfs)(uintptr\_t dev\_id, void \*cfg, int flags)
        :   Formats a device to specified file system type.

            Available only if  [`CONFIG_FILE_SYSTEM_MKFS`](../../kconfig.md#CONFIG_FILE_SYSTEM_MKFS "CONFIG_FILE_SYSTEM_MKFS") is enabled.

            Note

            This operation destroys existing data on the target device.

            Param dev\_id:
            :   Device identifier.

            Param cfg:
            :   File system configuration.

            Param flags:
            :   Formatting flags.

            Return:
            :   0 on success, negative errno code on fail.

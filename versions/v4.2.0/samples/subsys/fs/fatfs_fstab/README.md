---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/subsys/fs/fatfs_fstab/README.html
original_path: samples/subsys/fs/fatfs_fstab/README.html
---

# Fatfs filesystem fstab

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/fs/fatfs_fstab/README.rst/..)

## Overview

This sample shows how to define a fatfs fstab entry in the devicetree.
This scenario uses a fatfs on a RAM disk. The sample is run on the
`native_sim` board.

## Building and running

To run this sample, build it for the `native_sim` board
and afterwards run the generated executable file within the build folder.

The RAM disk sample for the `native_sim` board can be built as follows:

```shell
west build -b native_sim samples/subsys/fs/fatfs_fstab -- -DDTC_OVERLAY_FILE=fatfs_fstab.overlay
```

### Sample Output

When the sample runs successfully you should see following message on the screen:
.. code-block:: console

> I: Filesystem access successful

## See also

[File System APIs](../../../../doxygen/html/group__file__system__api.md)

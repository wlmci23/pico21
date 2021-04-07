# Disk, disk, sleuth! II

## Problem Description

All we know is the file with the flag is named `down-at-the-bottom.txt`... Disk image: [dds2-alpine.flag.img.gz](https://mercury.picoctf.net/static/6cd5ca45d75250451931cea538fb38c0/dds2-alpine.flag.img.gz)

## Hints

1. The sleuthkit has some great tools for this challenge as well.
2. Sleuthkit docs here are so helpful: TSK Tool Overview
3. This disk can also be booted with qemu!

## Solution

This time, we actually have to inspect the file system of the disk image to find the contents of a specific file. We use two Sleuthkit tools to do this.

By running `file` on the image, we find the start sector as 2048.

```
dds2-alpine.flag.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0x10,81,1), startsector 2048, 260096 sectors
```

Next, we use `fls` to inspect the contents of the root directory.

```bash
fls dds2-alpine.flag.img -o 2048
```

```
d/d 11: lost+found
r/r 12: .dockerenv
d/d 20321:      bin
d/d 4065:       boot
d/d 6097:       dev
d/d 2033:       etc
d/d 26417:      home
d/d 8129:       lib
d/d 14225:      media
d/d 16257:      mnt
d/d 18289:      opt
d/d 16258:      proc
d/d 18290:      root
d/d 16259:      run
d/d 18292:      sbin
d/d 12222:      srv
d/d 16260:      sys
d/d 18369:      tmp
d/d 12223:      usr
d/d 14229:      var
V/V 32513:      $OrphanFiles
```

Each directory and file is linked to an inode which can be used to refer to it without needing the full path. In this case, the inode number of /bin/ is 20321.

We can get the contents of a specific directory which is not root by specifying its inode.

```bash
fls dds2-alpine.flag.img -o 2048 6097
```

```
r/r 6098:       console
d/d 6099:       pts
d/d 6100:       shm
```

We look around in these directories until we find the file with the given name. It turns out that it is in the /root/ directory, or inode 18291.

```bash
fls dds2-alpine.flag.img -o 2048 18290
```

```
r/r 18291:      down-at-the-bottom.txt
```

Now that we've found the file, we use `icat` to extract its contents.

```bash
icat dds2-alpine.flag.img -o 2048 18291
```

```
   _     _     _     _     _     _     _     _     _     _     _     _     _
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
 ( p ) ( i ) ( c ) ( o ) ( C ) ( T ) ( F ) ( { ) ( f ) ( 0 ) ( r ) ( 3 ) ( n )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
   _     _     _     _     _     _     _     _     _     _     _     _     _
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
 ( s ) ( 1 ) ( c ) ( 4 ) ( t ) ( 0 ) ( r ) ( _ ) ( n ) ( 0 ) ( v ) ( 1 ) ( c )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
   _     _     _     _     _     _     _     _     _     _     _
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
 ( 3 ) ( _ ) ( f ) ( f ) ( 2 ) ( 7 ) ( f ) ( 1 ) ( 3 ) ( 9 ) ( } )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
```

Now it's just a matter of writing down the letters in these bubbles. This is trivial and left as an exercise to the reader.

## Flag

picoCTF{f0r3ns1c4t0r_n0v1c3_ff27f139}

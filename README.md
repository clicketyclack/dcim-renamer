# dcim-renamer
Ever ended up with a bunch of DCIM files? Ever want to rename them after the DCIM numbering restarts?



## Creating testdata.

Prepare test data using exiv2.

`$ exiv2 -M"add Iptc.Application2.Credit String Mr. Smith" image.jpg`


### Testdata directory layout.

* `DCIM/` Root with a few canon samples.
 * `Sports event/` Multiple images with the same timestamp due to burst shooting.
 * `Wedding/` Two cameras with mismatched image sequence numbers. Adding datetimes and body name to the file names will help here.
 * `At the zoo/` A "zoo" of camera makers / models. Put images here after bug reports.

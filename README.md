# dcim-renamer

Have you ever shot so many DCIM files that the numbering restarted, leaving you with multiple copies of `IMG_0001.JPG`?

Have you ever accidentally merged / overwritten DCIM files from multiple sources such as your DSLR and your cell?

Have you ever copied / transferred your DCIM files then realized that your file manager has reset the timestamp of the files, making sorting a pain?

This script will help you rename your images from this:

```
DCIM/At the zoo/IMG_6035.jpg
DCIM/IMG_0071.JPG
DCIM/IMG_0072.JPG
DCIM/IMG_0080.JPG
DCIM/Sports event/IMG_0071.JPG
DCIM/Sports event/IMG_0072.JPG
DCIM/Sports event/IMG_0073.JPG
DCIM/Wedding/IMG_5301.JPG
DCIM/Wedding/IMG_5302.JPG
DCIM/Wedding/IMG_5303.JPG
DCIM/Wedding/IMG_5304.JPG
DCIM/Wedding/IMG_5305.JPG
DCIM/Wedding/IMG_7001.JPG
DCIM/Wedding/IMG_7002.JPG
DCIM/Wedding/IMG_7003.JPG
DCIM/Wedding/IMG_7004.JPG
DCIM/Wedding/IMG_7005.JPG
DCIM/Wedding/IMG_7006.JPG
```

to this:

```
DCIM/2017_02_30_024414_7Dmk1_Second_IMG_0072.jpg
DCIM/2017_07_30_024414_7Dmk1_First_IMG_0071.jpg
DCIM/2018_08_30_024414_80D_IMG_0080.jpg
DCIM/At the zoo/2018_12_27_174947_600D_IMG_6035.jpg
DCIM/Sports event/2015_05_05_151515_D800_IMG_0071.jpg
DCIM/Sports event/2015_05_05_151515_D800_IMG_0072.jpg
DCIM/Sports event/2015_05_05_151515_D800_IMG_0073.jpg
DCIM/Wedding/2014_08_04_175830_70D_IMG_7001.jpg
DCIM/Wedding/2014_08_04_175840_5Dmk3_IMG_5301.jpg
DCIM/Wedding/2014_08_04_175850_70D_IMG_7002.jpg
DCIM/Wedding/2014_08_04_175900_5Dmk3_IMG_5302.jpg
DCIM/Wedding/2014_08_04_175910_5Dmk3_IMG_5303.jpg
DCIM/Wedding/2014_08_04_175920_70D_IMG_7003.jpg
DCIM/Wedding/2014_08_04_175930_70D_IMG_7004.jpg
DCIM/Wedding/2014_08_04_175940_70D_IMG_7005.jpg
DCIM/Wedding/2014_08_04_175950_5Dmk3_IMG_5304.jpg
DCIM/Wedding/2014_08_04_180000_5Dmk3_IMG_5305.jpg
DCIM/Wedding/2014_08_04_180010_70D_IMG_7006.jpg
```

### Usage

1. Backup all your files before running a script that may recursively clobber your photo collection!

2. Run the `dcim_renamer.py` script on a directory.
The script will generate (hopefully) appropriate `mv` commands.
Usually you will want to redirect the output to a `.sh` script, as follows: `./dcim_renamer.py  DCIM/ > /tmp/rename.sh`

3. Review the script for sanity checks. Depending on your platform you may need to replace `mv` with `move` and rename the output to `.bat`. You may also want to search/replace the command for interactive prompts before each rename.

4. Run the script.

5. ~~Restore your images from backup~~ Just kidding. But see the warranty notes<sup>1</sup>. Remember that you are running a script from the internet on your photo collection.


<sup>1</sup> This program is distributed in the
hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.



## Creating testdata.

Since we don't want to check in a bunch of 30MB raw images from an actual
camera, the testdata images should be small (32x32px) images with manually
crafted exiv2 tags. Hint: tags can be set as follows:

`$ exiv2 -M"add Iptc.Application2.Credit String Mr. Smith" image.jpg`


### Testdata directory layout.

* `DCIM/` Root with a few canon samples.
 * `Sports event/` Multiple images with the same timestamp due to burst shooting.
 * `Wedding/` Two cameras with mismatched image sequence numbers. Adding datetimes and body name to the file names will help here.
 * `At the zoo/` A "zoo" of camera makers / models. Put images here if you want testdata to accompany your bug report.

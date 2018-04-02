Convert [haveibeenpwned.com Pwned Passwords](https://haveibeenpwned.com/Passwords) 7z files to binary form, **saving space** but still being able to **quickly search inside them**.

Check [my blog entry for this project](https://circulosmeos.wordpress.com/2018/01/24/checking-passwords-against-size-reduced-haveibeenpwned-com-hashes-files/) for a step-by-step guide.

Both scripts are compatible with Python 2 (checked with 2.7) and Python 3 (checked with 3.6).

Conversion
==========

Convert the 7z file to binary form, using Python:
    
     $ python pwned-compact-to-binary.py    

New files with extension .bin and almost the same size of the .7z ones will be created.   
Bear in mind that the conversion process can take a while, even though the 7z extraction is done to memory — not to disk. But *it must be done just once*.

Use
===

Now you can check your passwords from another program just checking the output of *pwned-pass-binary-fast.py*
    
	$ python pwned-pass-binary-fast.py doors
	$ echo $?
		0
	$ python pwned-pass-binary-fast.py HardPasswordNotYetPawned
	$ echo $?
		1

If you prefer to have verbose output to screen, just change "VERBOSE = 0" to "VERBOSE = 1" in the code.

	$ python pwned-pass-binary-fast.py doors
		Searching for SHA1 hash: 0183EC9633DE16663259AD61FDC1D0F4CC363D6A
		Searching in: pwned-passwords-update-1.bin
		Searching in: pwned-passwords-update-2.bin
		Searching in: pwned-passwords-1.0.bin
		Found: 'doors' as 0183EC9633DE16663259AD61FDC1D0F4CC363D6A

Windows users
=============

Please note that in order to use the last version of haveibeenpwned password files, which have a size of about 9 GiB, you need to use a Python compiled for 64 bits. (The situation can be more complex (the requirement is LFS support) but hopefully that will suffice).

Attributions
============

*pwned-pass-binary-fast.py* is based on [pwned-pass-fast.py by alexanderzobnin](https://gist.github.com/alexanderzobnin/09db0c9f74754d32d3c2538d4d6a3b0d).

License
=======

Licensed as [GPL v3](http://www.gnu.org/licenses/gpl-3.0.en.html) or higher.   

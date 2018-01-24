Convert [haveibeenpwned.com Pwned Passwords](https://haveibeenpwned.com/Passwords) 7z files to binary form, **saving space** but still being able to **quickly search inside them**.
  
Conversion
==========

Convert the 7z files to binary form, using Python 3:
    
     $ python3 pwned-compact-to-binary.py    

New files with extension .bin and almost the same size of the .7z ones will be created.   
Bear in mind that the conversion process can take a while, even though the 7z extraction is done to memory — not to disk. But *it must be done just once*.

Use
===

Now you can check your passwords from another program just checking the output of Python 2 *pwned-pass-binary-fast.py*
    
	$ python2 pwned-pass-binary-fast.py doors
	$ echo $?
		0
	$ python2 pwned-pass-binary-fast.py HardPasswordNotYetPawned
	$ echo $?
		1

If you prefer to have verbose output to screen, just change "VERBOSE = 0" to "VERBOSE = 1" in the code.

	$ python2 pwned-pass-binary-fast.py doors
		Searching for SHA1 hash: 0183EC9633DE16663259AD61FDC1D0F4CC363D6A
		Searching in: pwned-passwords-update-1.bin
		Searching in: pwned-passwords-update-2.bin
		Searching in: pwned-passwords-1.0.bin
		Found: 'doors' as 0183EC9633DE16663259AD61FDC1D0F4CC363D6A

License
=======

Licensed as [GPL v3](http://www.gnu.org/licenses/gpl-3.0.en.html) or higher.   

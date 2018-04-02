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
	$ python pwned-pass-binary-fast.py 0183ec9633de16663259AD61FDC1D0F4CC363D6A
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

Or to see the internals of the search: "VERBOSE = 2"

	$ python pwned-pass-binary-fast.py doors
		Searching for SHA1 hash: 0183EC9633DE16663259AD61FDC1D0F4CC363D6A
		Searching in: pwned-passwords-ordered-2.0.bin
		File size is: 10032736840 bytes, hash length is 20 bytes, number of hashes is 501636842
		Go to 7FF3E1D4D11B156A5C2FB897D314362479576D30 hash position #250818421
		Go to 3FF3FA7DDC91F46B93C55C859D495F186F480C7A hash position #125409210
		Go to 1FF998781C8BFAB20D1140A9671875D5E17EE6B9 hash position #62704605
		Go to 0FFB53791D1A86DFA57FC3AC3C4199BE9C859B06 hash position #31352302
		Go to 07FE8D5828102B988DFE7C8054209A390D4A23EC hash position #15676151
		Go to 03FF6DAED2CD942DB1DFFC959EAE152932DEB51C hash position #7838075
		Go to 01FF9A346471B34F8FF66976E9DB69132EDA6CA1 hash position #3919037
		Go to 00FFD18385B13F5E011F06C830A121CB663F1091 hash position #1959518
		Go to 017FCB873483675BD33452CC3E0C2D19CA30316B hash position #2939277
		Go to 01BFB326A8EB501C19A43EABB42D114E98A5A945 hash position #3429157
		Go to 019FBA3D10EEE2C08D292CE67890B8E9F1121A4B hash position #3184217
		Go to 018FC7CB89E94022531679CD710B1745BFB6ECE9 hash position #3061747
		Go to 0187CB09921BA96697920FCC41ADEAB4323C3668 hash position #3000512
		Go to 0183D0AAC505528F38EB7299D34849C2A0BE7DF4 hash position #2969894
		Go to 0185CD87A5DC8F68DE33673A9C8FCD7E744CF158 hash position #2985203
		Go to 0184CE81658F51AF0DF23E1ECAFE069CFA6A526B hash position #2977548
		Go to 0184515E2F4A2E6F232AC2B5C42C64F98B174BEC hash position #2973721
		Go to 018410D0182632392B1E5FD08973CF35F6B62DD0 hash position #2971807
		Go to 0183F01FC37DE6E7CB89CB58B207C1F570CDCB1D hash position #2970850
		Go to 0183E0FB4A438C012BF469A568C66D3C0E4C294E hash position #2970372
		Go to 0183E8615A471B2622377E4B6CCA1FF308B58C0F hash position #2970611
		Go to 0183EC7C158E5E093510A848205DE8C9DCFA4C63 hash position #2970730
		Go to 0183EE1BD2924C5CA8EBF18C233BFBDE83D7AFF7 hash position #2970790
		Go to 0183ED589580B469D1635C318D3758BB3FBBE1B7 hash position #2970760
		Go to 0183ECC524CA3708CC72F0D6FA9C6EDBE119D039 hash position #2970745
		Go to 0183EC9633DE16663259AD61FDC1D0F4CC363D6A hash position #2970737
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

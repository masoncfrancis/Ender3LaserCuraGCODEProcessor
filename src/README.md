# Usage Instructions

The file to process should be passed in as an argument.
```
$ python3 e3proc.py test-file.gcode
```

The script will prompt the user for a destination file path where the processed file will be saved.
```
Please enter destination file path (any existing file will be overwritten):
```

When the script has completed successfully, the script will exit.
```
File processed successfully. Exiting...
```

### Notes

The current version of the script does not allow the user to select options,
and does not completely process the GCODE file. At this time it only sets the
to turn on and off at appropriate moments. Other modifications (e.g. setting Z axis height) 
still need to be made manually in the file.

### Licence
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

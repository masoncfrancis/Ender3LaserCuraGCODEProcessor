# Ender 3 Laser Cura GCODE Processor

## Software operation

1. Call software with file to process as argument
2. Software prompts user for destination file path
3. Software processes file, outputting it to destination file path

## File modifications

* Laser should be raised up to 100mm
* Whenever the print head moves where it wouldn't be extruding, it should turn off the laser
  * G1 is laser engraving, G0 is laser off
* At the end, keep Z where it goes

## Software Architecture

* Dictionaries to manage different values

# convertLineToDict
```
convertLineToDict(line: str):
  dict = {}
  splitted = line.split()
  
  for item in splitted:
    pass
```
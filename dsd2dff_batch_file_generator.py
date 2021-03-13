import os
import pathlib

desktop = pathlib.Path.home() / 'Desktop'

# Locate the downloaded dff2dsf.exe file
executable = "C:/YOUR/PATH/TO/dff2dsf.exe"

# Locate the folder with the .DFF files (for conversion)
inputLocation = "D:/DFF/MUSIC/FOLDER/PATH"

# Locate the output folder (where the .DSF files will be placed)
outputLocation = "D:/OUTPUT/FOLDER/PATH"

# Outputs the .CMD file to your desktop
scriptFile = str(desktop) + "/start_conversion.cmd"

open(scriptFile, "w").close()

pause_added = 0


# Pauses after the 1st conversion to let you know if anything weird is happening
# Press any key to continue after the first file if nothing is going crazy
for root, dirnames, filenames in os.walk(inputLocation):
    for filename in filenames:
        with open(scriptFile, "a") as script:
            if filename.endswith(".dff"):
                script.write(f'{executable} "{inputLocation}/{filename}" "{outputLocation}/{filename.replace("dff", "dsf")}"\n')
                if pause_added == 0:
                    script.write("PAUSE\n")
                    pause_added = 1

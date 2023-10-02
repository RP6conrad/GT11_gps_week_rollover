# GT11_gps_week_rollover
 Simple python sketch for adjust the date from .sbp files (GT11)
 As from 2019, the gps-week roll over will set the date back for 1024 weeks (19,6 years).
 Logfiles (.sbp) from the Locosys / Amaryllo GT11 will have wrong dates in all frames.
 The sbp_fix.py will search for all *.sbp files and adjust the date with +1024 weeks. 
 The new filename is then *_new.sbp !
 I compiled a Windows version, it is in the "dist" directory.
 For Mac / Linux, you have to install python and run the sketch.

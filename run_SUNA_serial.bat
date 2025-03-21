::This batch file executes the commands for continuously running the SUNA
::Change COMX to appropriate COM port on system

:repeat_forever

start python3 SUNA_serial.py COMX
TIMEOUT /T 900

goto repeat_forever
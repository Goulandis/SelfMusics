python GetNames.py
set d=%date:~0,4%
git add .
echo %date:~0,4%.%date:~5,2%.%date:~8,2% %time:~0,2%:%time:~3,2%
pause
git commit -m "%date:~0,4%.%date:~5,2%.%date:~8,2% %time:~0,2%:%time:~3,2%"
git push
pause
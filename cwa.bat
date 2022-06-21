set drive=%cd:~0,2%
set cwd=%cd%
%~d0
cd %~dp0
cd .\python_script
pdm run python .\download_sub.py %1 %2 %3
%drive%
cd %cwd%

echo "Start windows build"
"%PYTHON%"  -m pip install . -vv
if errorlevel 1 exit 1

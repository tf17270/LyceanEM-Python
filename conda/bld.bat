echo "Start windows build"
cmake ../
cmake --build .
if errorlevel 1 exit 1

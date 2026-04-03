clear
echo ""
echo "Vermillion-Skies RPC-Bot installer"
echo "Starting script..."
md %cd%\RPCBot
echo "Created RPCBot directory"
cd %cd%\RPCBot
md assets
echo "Created assets directory"
cd assets
md statuses
echo "Created statuses directory"
mkdir subscripts
echo "Created subscripts directory"
cd ..
echo "Creating python environment..."
md %cd%\env
py -m venv %cd%\env
echo "Environment created"
CALL %cd%\env\Scripts\activate.bat
echo "Activated environment"
py -m pip install --upgrade pip
py -m pip install pypresence tk requests
echo "Installed dependencies"
echo "downloading latest stable files..."
cd assets
curl "https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/presencebot.py" -o "presencebot.py"
cd subscripts
curl "https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/subscripts/statedit.py" -o "statedit.py"
curl "https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/subscripts/statmake.py" -o "statmake.py"
curl "https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/subscripts/subscriptloader.py" -o "subscriptloader.py"
cd ..
cd statuses
curl "https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/statuses/statustemp.txt" -o "statustemp.txt"
cd ..
cd ..
curl "https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/install/updater.bat" -o "updater.bat"
curl "https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/install/startbot.bat" -o "startbot.bat"
cd assets
echo "Finished installing files"
echo "Make sure to follow the instructions on GitHub to setup the app properly"
echo "Ending the installer script"
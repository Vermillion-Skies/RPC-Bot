clear
echo ""
echo "Vermillion-Skies RPC-Bot installer"
echo "Starting script..."
mkdir RPCBot/
echo "Created RPCBot directory"
cd RPCBot/
mkdir assets/
echo "Created assets directory"
mkdir assets/statuses/
echo "Created statuses directory"
mkdir assets/subscripts/
echo "Created subscripts directory"
echo "Creating python environment..."
python3 -m venv env
echo "Environment created"
source env/bin/activate
echo "Activated environment"
pip install --upgrade pip
pip install pypresence tk requests
echo "Installed dependencies"
echo "downloading latest stable files..."
cd assets/
wget --content-disposition https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/presencebot.py
cd subscripts/
wget --content-disposition https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/subscripts/statedit.py
wget --content-disposition https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/subscripts/statmake.py
wget --content-disposition https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/subscripts/subscriptloader.py
cd ..
cd statuses/
wget --content-disposition https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/statuses/statustemp.txt
cd ..
cd ..
wget --content-disposition https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/install/updater.sh
chmod +x updater.sh
wget --content-disposition https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/install/startbot.sh
chmod +x startbot.sh
cd assets/
echo "Finished installing files"
echo "Make sure to follow the instructions on GitHub to setup the app properly"
echo "Ending the installer script"
mkdir RPCBot/
cd RPCBot/
mkdir assets/
mkdir assets/statuses/
mkdir assets/subscripts/
python3 -m venv env
source env/bin/activate
pip install pypresence tk requests
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
wget --content-disposition https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/updater.sh
cd assets/
echo "Finished installing files, loading program..."
python3 presencebot.py
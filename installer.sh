mkdir RPCBot/
cd RPCBot/
mkdir assets/
mkdir assets/statuses/
mkdir assets/subscripts/
python3 -m venv env
source env/bin/activate
pip install pypresence tk
echo "downloading latest stable files..."
cd assets/
wget https://github.com/Vermillion-Skies/RPC-Bot/blob/main/presencebot.py
cd subscripts/
wget https://github.com/Vermillion-Skies/RPC-Bot/blob/main/subscripts/statedit.py
wget https://github.com/Vermillion-Skies/RPC-Bot/blob/main/subscripts/statmake.py
wget https://github.com/Vermillion-Skies/RPC-Bot/blob/main/subscripts/subscriptloader.py
cd ..
cd statuses/
wget https://github.com/Vermillion-Skies/RPC-Bot/blob/main/statuses/statustemp.txt
cd ..
echo "Finished installing files, loading program..."
python3 presencebot.py
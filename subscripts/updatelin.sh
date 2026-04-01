rm -r assets/subscripts/
rm assets/presencebot.py
echo "Successfully removed old files"
cd assets/
mkdir subscripts/
echo "Created new subscripts folder"
echo "Installing lastest stable files..."
wget --content-disposition https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/presencebot.py
cd subscripts/
wget --content-disposition https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/subscripts/statedit.py
wget --content-disposition https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/subscripts/statmake.py
wget --content-disposition https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/subscripts/subscriptloader.py
cd ..
echo "Successfully installed latest files"
echo "Closing updater script..."
del %cd%\assets\subscripts\
del %cd%\assets\presencebot.py
echo "Successfully removed old files"
cd %cd%\assets\
md %cd%\subscripts\
echo "Created new subscripts folder"
echo "Installing lastest stable files..."
curl "https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/presencebot.py" -o "presencebot.py"
cd subscripts\
curl "https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/subscripts/statedit.py" -o "statedit.py"
curl "https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/subscripts/statmake.py" -o "statmake.py"
curl "https://raw.githubusercontent.com/Vermillion-Skies/RPC-Bot/main/subscripts/subscriptloader.py" -o "subscriptloader.py"
cd ..
echo "Successfully installed latest files"
echo "Closing updater script..."
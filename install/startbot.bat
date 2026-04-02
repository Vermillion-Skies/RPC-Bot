CALL %cd%\env\Scripts\activate.bat
cd %cd%\assets
py %cd%\presencebot.py
cd ../
CALL %cd%\env\Scripts\deactivate.bat
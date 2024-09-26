cd %USERPROFILE%\Desktop
rmdir /S /Q "handson"
mkdir handson
cd handson
python -m venv venv
call venv\Scripts\activate.bat
pip install openai


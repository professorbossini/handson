cd "C:\Insight Files"
rmdir /S /Q handson_aluno
mkdir handson_aluno
cd handson_aluno
python -m venv venv
call venv\Scripts\activate.bat
pip install openai
pip install python-dotenv


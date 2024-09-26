taskkill /F /IM Code.exe
cd "C:\Insight Files\handson_aluno"
del /F /Q app_aluno.py
del /F /Q .env
copy "C:\Insight Files\app_aluno.py" "C:\Insight Files\handson_aluno"
copy "C:\Insight Files\.env" "C:\Insight Files\handson_aluno"
code .

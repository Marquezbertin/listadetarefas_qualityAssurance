@echo off
echo Executando testes com Selenium...
python -m unittest discover -s "tests\Testes E2E" -p "*.py"
pause
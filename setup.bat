@echo off
title Windows Cleanup Tool Setup
echo [+] Admin huququ yoxlanilir...
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [XETA] Zehmet olmasa Admin olaraq bashladin!
    pause
    exit
)
echo [+] Python yoxlanilir...
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [!] Python tapilmadi. Yuklenmelidir...
    pause
    exit
)
echo [OK] main.py bashladilir...
python main.py
pause
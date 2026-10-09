@echo off
setlocal EnableExtensions
cd /d "%~dp0"
set "BOOK_TARGET=%~1"
if not defined BOOK_TARGET set "BOOK_TARGET=book"
if /I "%BOOK_TARGET%"=="book" goto book
if /I "%BOOK_TARGET%"=="notes" goto book
if /I "%BOOK_TARGET%"=="example" goto example
if /I "%BOOK_TARGET%"=="all" goto all
echo Usage: %~nx0 [book^|notes^|example^|all]
exit /b 2

:book
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0build-book.ps1" -Target book
if errorlevel 1 goto failed
goto finished

:example
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0build-book.ps1" -Target example
if errorlevel 1 goto failed
goto finished

:all
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0build-book.ps1" -Target book
if errorlevel 1 goto failed
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0build-book.ps1" -Target example
if errorlevel 1 goto failed
goto finished

:failed
echo [ERROR] Build failed. Check output\pdf for the log.
if "%~1"=="" pause
exit /b 1

:finished
if "%~1"=="" pause
exit /b 0

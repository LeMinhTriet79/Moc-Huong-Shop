@echo off
echo ========================================================
echo        AROMATICS PLATFORM - STOP SCRIPT
echo ========================================================

cd aromatics-platform

echo Stopping all services and removing containers...
call docker-compose -f docker-compose.infra.yml down

echo ========================================================
echo System stopped successfully.
echo ========================================================
pause

@echo off
echo ========================================================
echo        AROMATICS PLATFORM - START SCRIPT
echo ========================================================

cd aromatics-platform

echo [1/3] Compiling and building all microservices...
call mvn clean install -DskipTests

echo [2/3] Building docker images...
call docker-compose -f docker-compose.infra.yml build

echo [3/3] Starting all services via Docker Compose...
call docker-compose -f docker-compose.infra.yml up -d

echo ========================================================
echo System is starting up in the background!
echo Monitor services via: docker ps
echo Grafana Dashboard: http://localhost:3000
echo API Gateway: http://localhost:8080
echo ========================================================
pause

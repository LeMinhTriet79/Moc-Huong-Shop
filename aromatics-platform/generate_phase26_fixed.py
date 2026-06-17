import os

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"

# 1. Update docker-compose.yml
compose_path = f"{base_platform}/docker-compose.yml"
if os.path.exists(compose_path):
    with open(compose_path, "r", encoding="utf-8") as f:
        compose_content = f.read()
    
    if "prometheus:" not in compose_content:
        monitoring_services = """
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
    networks:
      - aromatics-network

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    depends_on:
      - prometheus
    networks:
      - aromatics-network
"""
        compose_content = compose_content.replace("networks:", monitoring_services + "\nnetworks:")
        with open(compose_path, "w", encoding="utf-8") as f:
            f.write(compose_content)

# 2. Create prometheus.yml
prom_dir = f"{base_platform}/prometheus"
os.makedirs(prom_dir, exist_ok=True)
prom_content = """global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'aromatics-services'
    metrics_path: '/actuator/prometheus'
    static_configs:
      - targets: 
        - 'api-gateway:8080'
        - 'identity-service:8081'
        - 'catalog-service:8082'
        - 'order-service:8083'
"""
with open(f"{prom_dir}/prometheus.yml", "w", encoding="utf-8") as f:
    f.write(prom_content)

print("Phase 26 Monitoring logic generated.")

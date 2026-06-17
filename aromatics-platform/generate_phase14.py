import os
import re

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"
services = ["identity-service", "catalog-service", "cart-service", "order-service", "promotion-service", "payment-service", "notification-service", "api-gateway"]

monitor_deps = """
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
            <groupId>io.micrometer</groupId>
            <artifactId>micrometer-tracing-bridge-brave</artifactId>
        </dependency>
        <dependency>
            <groupId>io.zipkin.reporter2</groupId>
            <artifactId>zipkin-reporter-brave</artifactId>
        </dependency>
"""

actuator_yml = """
management:
  endpoints:
    web:
      exposure:
        include: "*"
  tracing:
    sampling:
      probability: 1.0
"""

for svc in services:
    # 1. Add dependencies
    pom_path = f"{base_platform}/{svc}/pom.xml"
    if os.path.exists(pom_path):
        with open(pom_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "spring-boot-starter-actuator" not in content:
            content = re.sub(r'(</dependencies>)', monitor_deps + r'\1', content, 1)
            with open(pom_path, "w", encoding="utf-8") as f:
                f.write(content)
                
    # 2. Add application.yml
    yml_path = f"{base_platform}/{svc}/src/main/resources/application.yml"
    if os.path.exists(yml_path):
        with open(yml_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "management:" not in content:
            with open(yml_path, "a", encoding="utf-8") as f:
                f.write(actuator_yml)

print("Phase 14 monitoring logic generated.")

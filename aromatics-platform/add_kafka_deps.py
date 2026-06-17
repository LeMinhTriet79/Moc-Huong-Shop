import os
import re

deps = """
        <dependency>
            <groupId>org.springframework.kafka</groupId>
            <artifactId>spring-kafka</artifactId>
        </dependency>
"""

services = ["order-service", "payment-service", "notification-service"]

for svc in services:
    pom_path = f"g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/{svc}/pom.xml"
    with open(pom_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "spring-kafka" not in content:
        content = re.sub(r'(</dependencies>)', deps + r'\1', content, 1)
        with open(pom_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added spring-kafka to {svc}")
    else:
        print(f"spring-kafka already exists in {svc}")

import os
import re

deps = """
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-circuitbreaker-resilience4j</artifactId>
        </dependency>
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

services = [
    "cart-service",
    "catalog-service",
    "identity-service",
    "notification-service",
    "order-service",
    "payment-service",
    "promotion-service"
]

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"

for service in services:
    pom_path = os.path.join(base_dir, service, "pom.xml")
    if os.path.exists(pom_path):
        with open(pom_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if resilience4j is already there
        if "spring-cloud-starter-circuitbreaker-resilience4j" not in content:
            # Inject dependencies before the closing </dependencies> tag (the first one)
            # Find the first </dependencies> which belongs to <dependencies> not <dependencyManagement>
            match = re.search(r'</dependencies>', content)
            if match:
                index = match.start()
                new_content = content[:index] + deps + content[index:]
                with open(pom_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Added to {service}")
            else:
                print(f"Could not find </dependencies> in {service}")
        else:
            print(f"Dependencies already exist in {service}")

import os
import re

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"
services = {
    "catalog-service": "com/minhtriet/se3979/catalogservice/controller/ProductController.java",
    "order-service": "com/minhtriet/se3979/orderservice/controller/OrderController.java"
}

swagger_dep = """
        <dependency>
            <groupId>org.springdoc</groupId>
            <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
            <version>2.3.0</version>
        </dependency>
"""

for svc, controller_path in services.items():
    # 1. Add dependency
    pom_path = f"{base_platform}/{svc}/pom.xml"
    with open(pom_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "springdoc-openapi-starter-webmvc-ui" not in content:
        content = re.sub(r'(</dependencies>)', swagger_dep + r'\1', content, 1)
        with open(pom_path, "w", encoding="utf-8") as f:
            f.write(content)
            
    # 2. Add swagger annotations
    ctrl_full_path = f"{base_platform}/{svc}/src/main/java/{controller_path}"
    with open(ctrl_full_path, "r", encoding="utf-8") as f:
        ctrl_content = f.read()
        
    if "io.swagger.v3.oas.annotations" not in ctrl_content:
        ctrl_content = ctrl_content.replace(
            "import org.springframework.web.bind.annotation.*;",
            "import org.springframework.web.bind.annotation.*;\nimport io.swagger.v3.oas.annotations.Operation;\nimport io.swagger.v3.oas.annotations.tags.Tag;"
        )
        ctrl_content = ctrl_content.replace(
            "@RestController",
            f'@Tag(name = "{svc.split("-")[0].capitalize()} API", description = "Endpoints for managing {svc.split("-")[0]}")\n@RestController'
        )
        ctrl_content = ctrl_content.replace(
            "@PostMapping",
            '@Operation(summary = "Create a new record")\n    @PostMapping'
        )
        ctrl_content = ctrl_content.replace(
            "@GetMapping",
            '@Operation(summary = "Retrieve records")\n    @GetMapping'
        )
        with open(ctrl_full_path, "w", encoding="utf-8") as f:
            f.write(ctrl_content)

print("Phase 17 swagger logic generated.")

import os

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"

# 1. Update project_report.md
report_path = f"{base_platform}/doc/project_report.md"
with open(report_path, "a", encoding="utf-8") as f:
    f.write("""

## 4. Các Giai Đoạn Cải Tiến Đã Hoàn Thành (Phase 12 - Phase 16)
- **Phase 12:** Đã tích hợp `GlobalExceptionHandler` bắt lỗi tập trung và `spring-boot-starter-validation` để validate DTOs, đảm bảo bad request bị chặn ngay tại controller.
- **Phase 13:** Đã cấu hình `spring-boot-starter-cache` và `spring-boot-starter-data-redis` cho `Catalog Service`, giúp tăng tốc các truy vấn lấy danh sách sản phẩm.
- **Phase 14:** Cấu hình **Spring Boot Actuator** kèm **Zipkin** và **Micrometer** để có thể giám sát health check và distributed tracing cho toàn bộ hệ thống.
- **Phase 15:** Đã viết Unit Test cho logic của `OrderService` sử dụng Mockito và JUnit 5.
- **Phase 16:** Hoàn thiện Pipeline CI/CD thông qua GitHub Actions và chuẩn hóa kịch bản chạy toàn diện (MySQL, Redis, Kafka, Zipkin) qua `docker-compose.yml`.
""")

# 2. GitHub Actions Workflow
github_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/.github/workflows"
os.makedirs(github_dir, exist_ok=True)
workflow_content = """name: Java CI with Maven

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up JDK 21
      uses: actions/setup-java@v3
      with:
        java-version: '21'
        distribution: 'temurin'
        cache: maven
    - name: Build and Test Order Service
      run: cd aromatics-platform/order-service && mvn -B package --file pom.xml
"""
with open(f"{github_dir}/ci.yml", "w", encoding="utf-8") as f:
    f.write(workflow_content)

print("Phase 16 CI/CD logic generated.")

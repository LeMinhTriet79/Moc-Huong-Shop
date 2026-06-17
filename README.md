# Mộc Hương Shop (Aromatics Platform) - Cloud-Native Enterprise Architecture

Dự án Hệ thống Thương Mại Điện Tử Mộc Hương Shop được thiết kế dựa trên kiến trúc **Microservices** tiên tiến nhất, đạt tiêu chuẩn triển khai cho **Cloud-Native Enterprise**. 

## Kiến Trúc Tổng Thể

- **Ngôn ngữ & Framework:** Java 21, Spring Boot 3, Spring Cloud
- **Quản lý Dữ Liệu:** MySQL (RDBMS), Redis (Caching & Rate Limiting), Elasticsearch (Full-Text Search)
- **Giao Tiếp Bất Đồng Bộ:** Apache Kafka (Event-Driven Architecture)
- **Kiến Trúc Triển Khai:** Docker Compose, Kubernetes (K8s Manifests sẵn sàng)
- **Monitoring & Tracing:** Prometheus, Grafana, Zipkin, Micrometer

### Danh Sách Các Microservices
1. **API Gateway:** Điều phối truy cập, kiểm tra bảo mật (JWT) & Rate Limiting.
2. **Service Registry (Eureka):** Quản lý định tuyến và tìm kiếm service.
3. **Config Server:** Quản lý cấu hình tập trung từ xa cho toàn bộ hệ thống.
4. **Identity Service:** Quản lý người dùng, phân quyền (RBAC), sinh token (JWT).
5. **Catalog Service:** Quản lý sản phẩm. Hỗ trợ truy vấn siêu tốc qua Elasticsearch và GraphQL.
6. **Cart Service:** Quản lý giỏ hàng lưu bằng Redis với tốc độ truy xuất tính bằng phần nghìn giây.
7. **Order Service:** Quản lý đơn hàng, đảm bảo tính nhất quán dữ liệu qua Transactional Outbox Pattern.
8. **Promotion Service:** Áp dụng mã giảm giá và các chiến dịch khuyến mãi.
9. **Payment Service:** Xử lý thanh toán.
10. **Notification Service:** Hệ thống nhận event từ Kafka để đẩy email/thông báo.

## Hướng Dẫn Cài Đặt và Chạy Dự Án

### Yêu Cầu Hệ Thống
- **Java JDK 21+**
- **Maven 3.8+**
- **Docker Desktop** (Đã kích hoạt Kubernetes nếu muốn chạy K8s)

### Chạy Dự Án Bằng 1-Click (Dành cho Developer mới)
Dự án được trang bị sẵn script tự động hóa. Tại thư mục gốc của dự án, bạn có thể gọi các tập lệnh sau:

- **Bật Hệ Thống:** Nhấp đúp vào `start-all.bat` (Hoặc mở Command Prompt và gõ lệnh `start-all.bat`). Script sẽ tự động build toàn bộ mã nguồn Java và khởi tạo mạng lưới Docker Containers.
- **Tắt Hệ Thống:** Nhấp đúp vào `stop-all.bat`. Toàn bộ container và tài nguyên sẽ được dọn dẹp sạch sẽ.

### Truy Cập Các Giao Diện Giám Sát
- **Swagger UI (Danh sách API REST):** http://localhost:8080/swagger-ui.html
- **Eureka Server (Danh sách Service):** http://localhost:8761
- **Zipkin (Distributed Tracing):** http://localhost:9411
- **Grafana (Monitoring Metrics):** http://localhost:3000 (Tài khoản/Mật khẩu: `admin/admin`)

## Chặng Đường Phát Triển
Dự án đã trải qua 32 Phase nâng cấp, từ kiến trúc cơ bản đến bảo mật Enterprise, CI/CD, Event-Driven và GitOps. Xem chi tiết báo cáo tại: [doc/project_report.md](aromatics-platform/doc/project_report.md)

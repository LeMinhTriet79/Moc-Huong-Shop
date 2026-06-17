# Tài Liệu Báo Cáo Giai Đoạn Phát Triển - Mộc Hương Shop (Aromatics Platform)

Tài liệu này tổng hợp toàn bộ những gì hệ thống đã được triển khai, kiến trúc và các tính năng đã hoàn thiện từ Phase 1 đến Phase 11.

## 1. Tổng Quan Kiến Trúc
Hệ thống Mộc Hương Shop được thiết kế theo kiến trúc **Microservices**, sử dụng **Spring Boot 3**, **Spring Cloud**, và điều phối bằng **Docker**.

### Các Components Lõi:
1. **Service Registry (Eureka Server):** Đóng vai trò làm Directory cho các Microservices đăng ký và khám phá lẫn nhau.
2. **API Gateway:** Điểm entry duy nhất cho toàn bộ request từ Client. Cấu hình bảo mật JWT và điều hướng tới các Service con.
3. **Identity Service:** Chịu trách nhiệm quản lý User, Xác thực (Register, Login, JWT), Quản lý Address và Wishlist.
4. **Catalog Service:** Quản lý kho Sản phẩm, Danh mục, Biến thể và Review.
5. **Cart Service:** Quản lý Giỏ hàng của người dùng, sử dụng **Redis** để đảm bảo tốc độ cao.
6. **Promotion Service:** Quản lý Mã giảm giá (Coupons, Vouchers) và chiến dịch khuyến mãi.
7. **Order Service:** Quản lý Đơn hàng, Checkout, và theo dõi trạng thái vận chuyển.
8. **Payment Service:** Tích hợp thanh toán và xử lý IPN/Webhook từ VNPay.
9. **Notification Service:** Quản lý gửi Email và Thông báo.

---

## 2. Các Giai Đoạn Đã Hoàn Thành (Phase 1 - Phase 11)

### Phase 1-7: Khởi Tạo Cơ Sở Hạ Tầng & Dựng Khung (Skeleton)
- Khởi tạo thành công **Eureka Server** (`service-registry`) và **API Gateway**.
- Khởi tạo cấu trúc dự án chuẩn cho 7 microservices con (`identity`, `catalog`, `cart`, `promotion`, `order`, `payment`, `notification`).
- Thiết lập **MySQL** (cho dữ liệu có cấu trúc) và **Redis** (cho Giỏ hàng và Caching).
- Tích hợp **Flyway** để quản lý DB Migration tự động cho tất cả các Service có sử dụng Database.
- Đóng gói toàn bộ bằng **Docker Compose** để chạy lên nhanh chóng.

### Phase 8: Giao Tiếp & Chịu Lỗi (Inter-Service Communication)
- Tích hợp **Spring Cloud OpenFeign** để các Service có thể giao tiếp đồng bộ với nhau (Ví dụ: OrderService gọi CatalogService để check giá).
- Tích hợp **Resilience4j** (Circuit Breaker) để đảm bảo tính chịu lỗi, chống sụp đổ dây chuyền khi một service con bị chết.

### Phase 9: Triển Khai Logic Cốt Lõi (Core Business Logic)
- **Identity Service:** Triển khai các API lấy/cập nhật thông tin User, thêm địa chỉ (`Address`), thêm danh sách yêu thích (`Wishlist`).
- **Catalog Service:** Triển khai API lấy danh sách Sản phẩm, tạo Sản phẩm mới (`Product`).
- **Cart Service:** Triển khai API Thêm vào Giỏ hàng, Lấy thông tin Giỏ hàng, và Xóa Giỏ hàng lưu trữ 100% trên **Redis** (`CartRedisRepository`).
- **Order Service:** Triển khai API Tạo đơn hàng, tính toán tổng số tiền dựa trên chi tiết sản phẩm.
- **Promotion Service:** Triển khai API check và lấy thông tin Mã giảm giá.

### Phase 10: Xử Lý Bất Đồng Bộ (Event-Driven Architecture)
- Tích hợp hệ thống Message Broker **Apache Kafka**.
- **Order Service (Producer):** Tự động phát ra một sự kiện (event) `order-created` lên Kafka ngay khi người dùng tạo đơn hàng thành công.
- **Payment Service (Consumer):** Lắng nghe event `order-created` để tự động chuẩn bị phiên giao dịch.
- **Notification Service (Consumer):** Lắng nghe event `order-created` để gửi email/tin nhắn thông báo đến người dùng.

### Phase 11: Bảo Mật Tập Trung tại API Gateway
- Chuyển quyền xác thực Token từ các Microservice con lên tập trung tại **API Gateway**.
- Triển khai **JwtAuthenticationFilter** ở cấp độ Gateway để đánh chặn các request không có token hợp lệ trước khi chúng kịp chạm đến các Service con.

---

## 3. Kế Hoạch Cải Tiến Tiếp Theo
Sau khi hoàn thành bộ khung xương Microservices chuẩn, hệ thống đã sẵn sàng cho các pha cải tiến và vận hành:
1. **Kiểm thử tự động (Unit Test / Integration Test):** Cần phủ Test Coverage cho các luồng Core (Tạo Đơn Hàng, Thanh Toán).
2. **CI/CD Pipeline:** Tích hợp GitHub Actions để tự động build Docker Image và Deploy lên Server.
3. **Centralized Logging & Monitoring:** Tích hợp ELK Stack (Elasticsearch, Logstash, Kibana) và Prometheus + Grafana để giám sát logs và metrics sức khỏe của hệ thống.

*Tài liệu được tự động tạo sau khi hoàn tất toàn bộ tiến trình triển khai kỹ thuật.*


## 4. Các Giai Đoạn Cải Tiến Đã Hoàn Thành (Phase 12 - Phase 16)
- **Phase 12:** Đã tích hợp `GlobalExceptionHandler` bắt lỗi tập trung và `spring-boot-starter-validation` để validate DTOs, đảm bảo bad request bị chặn ngay tại controller.
- **Phase 13:** Đã cấu hình `spring-boot-starter-cache` và `spring-boot-starter-data-redis` cho `Catalog Service`, giúp tăng tốc các truy vấn lấy danh sách sản phẩm.
- **Phase 14:** Cấu hình **Spring Boot Actuator** kèm **Zipkin** và **Micrometer** để có thể giám sát health check và distributed tracing cho toàn bộ hệ thống.
- **Phase 15:** Đã viết Unit Test cho logic của `OrderService` sử dụng Mockito và JUnit 5.
- **Phase 16:** Hoàn thiện Pipeline CI/CD thông qua GitHub Actions và chuẩn hóa kịch bản chạy toàn diện (MySQL, Redis, Kafka, Zipkin) qua `docker-compose.yml`.

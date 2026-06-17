import os
import re

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"

# 1. Add Elasticsearch dependency to catalog-service
catalog_pom = f"{base_platform}/catalog-service/pom.xml"
es_dep = """
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-elasticsearch</artifactId>
        </dependency>
"""
with open(catalog_pom, "r", encoding="utf-8") as f:
    pom_content = f.read()

if "spring-boot-starter-data-elasticsearch" not in pom_content:
    pom_content = re.sub(r'(</dependencies>)', es_dep + r'\1', pom_content, 1)
    with open(catalog_pom, "w", encoding="utf-8") as f:
        f.write(pom_content)

# 2. Add Elasticsearch document and repository
es_dir = f"{base_platform}/catalog-service/src/main/java/com/minhtriet/se3979/catalogservice/elasticsearch"
os.makedirs(es_dir, exist_ok=True)

doc_content = """package com.minhtriet.se3979.catalogservice.elasticsearch;

import org.springframework.data.annotation.Id;
import org.springframework.data.elasticsearch.annotations.Document;
import org.springframework.data.elasticsearch.annotations.Field;
import org.springframework.data.elasticsearch.annotations.FieldType;

@Document(indexName = "products")
public class ProductDocument {

    @Id
    private String id;

    @Field(type = FieldType.Text, name = "name")
    private String name;

    @Field(type = FieldType.Text, name = "description")
    private String description;

    // Constructors, Getters, Setters
    public ProductDocument() {}

    public ProductDocument(String id, String name, String description) {
        this.id = id;
        this.name = name;
        this.description = description;
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
}
"""
with open(f"{es_dir}/ProductDocument.java", "w", encoding="utf-8") as f:
    f.write(doc_content)

repo_content = """package com.minhtriet.se3979.catalogservice.elasticsearch;

import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

import java.util.List;

public interface ProductSearchRepository extends ElasticsearchRepository<ProductDocument, String> {
    List<ProductDocument> findByNameOrDescription(String name, String description);
}
"""
with open(f"{es_dir}/ProductSearchRepository.java", "w", encoding="utf-8") as f:
    f.write(repo_content)

# 3. Update project_report.md
report_path = f"{base_platform}/doc/project_report.md"
with open(report_path, "a", encoding="utf-8") as f:
    f.write("""
## 6. Các Giai Đoạn Cải Tiến Kiến Trúc Cấp Cao (Phase 21 - Phase 24)
- **Phase 21 (RBAC Security):** Tích hợp Spring Security, bổ sung JWT filter và dùng `@PreAuthorize` để phân rạch ròi quyền hạn (Role: USER, ADMIN) tại các Endpoint quan trọng.
- **Phase 22 (Spring Cloud Config):** Khởi tạo `config-server` đóng vai trò quản lý cấu hình tập trung cho toàn bộ hệ thống Microservices. Các service con sẽ kéo cấu hình động khi khởi động.
- **Phase 23 (Jasypt Secrets Management):** Ứng dụng thư viện Jasypt để mã hóa toàn bộ dữ liệu nhạy cảm (như mật khẩu DB) dưới dạng chuỗi `ENC(...)` trong các file cấu hình.
- **Phase 24 (Elasticsearch):** Tích hợp Elasticsearch vào Catalog Service. Định nghĩa `ProductDocument` và `ProductSearchRepository` nhằm phục vụ tính năng tìm kiếm Full-Text với tốc độ cực nhanh và chính xác.
""")

print("Phase 24 Elasticsearch logic generated.")

import os
import re

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"
catalog_pom = f"{base_platform}/catalog-service/pom.xml"

cache_deps = """
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-cache</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
"""

with open(catalog_pom, "r", encoding="utf-8") as f:
    pom_content = f.read()

if "spring-boot-starter-cache" not in pom_content:
    pom_content = re.sub(r'(</dependencies>)', cache_deps + r'\1', pom_content, 1)
    with open(catalog_pom, "w", encoding="utf-8") as f:
        f.write(pom_content)

main_class = f"{base_platform}/catalog-service/src/main/java/com/minhtriet/se3979/catalogservice/CatalogServiceApplication.java"
with open(main_class, "r", encoding="utf-8") as f:
    main_content = f.read()

if "@EnableCaching" not in main_content:
    main_content = main_content.replace(
        "import org.springframework.boot.autoconfigure.SpringBootApplication;",
        "import org.springframework.boot.autoconfigure.SpringBootApplication;\nimport org.springframework.cache.annotation.EnableCaching;"
    ).replace(
        "@SpringBootApplication",
        "@SpringBootApplication\n@EnableCaching"
    )
    with open(main_class, "w", encoding="utf-8") as f:
        f.write(main_content)

impl_class = f"{base_platform}/catalog-service/src/main/java/com/minhtriet/se3979/catalogservice/service/impl/ProductServiceImpl.java"
with open(impl_class, "r", encoding="utf-8") as f:
    impl_content = f.read()

if "@Cacheable" not in impl_content:
    impl_content = impl_content.replace(
        "import org.springframework.stereotype.Service;",
        "import org.springframework.stereotype.Service;\nimport org.springframework.cache.annotation.Cacheable;\nimport org.springframework.cache.annotation.CacheEvict;"
    ).replace(
        "public List<ProductResponse> getAllProducts() {",
        "@Cacheable(value = \"products\")\n    public List<ProductResponse> getAllProducts() {"
    ).replace(
        "public ProductResponse getProductById(Long id) {",
        "@Cacheable(value = \"products\", key = \"#id\")\n    public ProductResponse getProductById(Long id) {"
    ).replace(
        "public ProductResponse createProduct(ProductRequest request) {",
        "@CacheEvict(value = \"products\", allEntries = true)\n    public ProductResponse createProduct(ProductRequest request) {"
    )
    
    # Needs implements Serializable for ProductResponse to be cached in Redis
    resp_class = f"{base_platform}/catalog-service/src/main/java/com/minhtriet/se3979/catalogservice/dto/response/ProductResponse.java"
    with open(resp_class, "r", encoding="utf-8") as f:
        resp_content = f.read()
    if "implements java.io.Serializable" not in resp_content:
        resp_content = resp_content.replace(
            "public class ProductResponse {",
            "public class ProductResponse implements java.io.Serializable {"
        )
        with open(resp_class, "w", encoding="utf-8") as f:
            f.write(resp_content)

    with open(impl_class, "w", encoding="utf-8") as f:
        f.write(impl_content)

print("Phase 13 caching logic generated.")

import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/catalog-service/src/main/java/com/minhtriet/se3979/catalogservice"
packages = ["entity", "repository", "service", "controller", "dto"]

for p in packages:
    os.makedirs(os.path.join(base_dir, p), exist_ok=True)

entities = {
    "Category": """package com.minhtriet.se3979.catalogservice.entity;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "categories")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class Category {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String slug;
    private String description;
    private String imageUrl;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
""",
    "Product": """package com.minhtriet.se3979.catalogservice.entity;

import jakarta.persistence.*;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Entity
@Table(name = "products")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class Product {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long categoryId;
    private String name;
    private String slug;
    private String shortDescription;
    private String description;
    private BigDecimal basePrice;
    private Boolean isPublished;
    private BigDecimal ratingAvg;
    private Integer totalSold;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
""",
    "ProductVariant": """package com.minhtriet.se3979.catalogservice.entity;

import jakarta.persistence.*;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Entity
@Table(name = "product_variants")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class ProductVariant {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long productId;
    private String sku;
    private String name;
    private BigDecimal price;
    private Integer stockQuantity;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
""",
    "ProductImage": """package com.minhtriet.se3979.catalogservice.entity;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "product_images")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class ProductImage {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long productId;
    private String imageUrl;
    private Boolean isPrimary;
    private LocalDateTime createdAt;
}
""",
    "Review": """package com.minhtriet.se3979.catalogservice.entity;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "reviews")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class Review {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long productId;
    private Long userId;
    private Integer rating;
    private String comment;
    private String imagesJson;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
"""
}

for name, content in entities.items():
    with open(os.path.join(base_dir, "entity", f"{name}.java"), "w") as f:
        f.write(content)

for name in entities.keys():
    repo_content = f"""package com.minhtriet.se3979.catalogservice.repository;

import com.minhtriet.se3979.catalogservice.entity.{name};
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface {name}Repository extends JpaRepository<{name}, Long> {{
}}
"""
    with open(os.path.join(base_dir, "repository", f"{name}Repository.java"), "w") as f:
        f.write(repo_content)

print("Files generated.")

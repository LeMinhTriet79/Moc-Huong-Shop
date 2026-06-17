import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/promotion-service/src/main/java/com/minhtriet/se3979/promotionservice"
packages = ["entity", "repository", "service", "controller", "dto"]

for p in packages:
    os.makedirs(os.path.join(base_dir, p), exist_ok=True)

entities = {
    "Coupon": """package com.minhtriet.se3979.promotionservice.entity;

import jakarta.persistence.*;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Entity
@Table(name = "coupons")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class Coupon {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String code;
    private String discountType; // PERCENTAGE, FIXED
    private BigDecimal discountValue;
    private BigDecimal minOrderValue;
    private Integer maxUsages;
    private LocalDateTime startDate;
    private LocalDateTime endDate;
}
""",
    "FlashSale": """package com.minhtriet.se3979.promotionservice.entity;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "flash_sales")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class FlashSale {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long productId;
    private Integer discountPercentage;
    private Integer maxQuantity;
    private LocalDateTime startDate;
    private LocalDateTime endDate;
}
""",
    "ComboDeal": """package com.minhtriet.se3979.promotionservice.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "combo_deals")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class ComboDeal {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long mainProductId;
    private Long bundledProductId;
    private Integer discountPercentage;
}
"""
}

for name, content in entities.items():
    with open(os.path.join(base_dir, "entity", f"{name}.java"), "w") as f:
        f.write(content)

for name in entities.keys():
    repo_content = f"""package com.minhtriet.se3979.promotionservice.repository;

import com.minhtriet.se3979.promotionservice.entity.{name};
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface {name}Repository extends JpaRepository<{name}, Long> {{
}}
"""
    with open(os.path.join(base_dir, "repository", f"{name}Repository.java"), "w") as f:
        f.write(repo_content)

print("Promotion components generated.")

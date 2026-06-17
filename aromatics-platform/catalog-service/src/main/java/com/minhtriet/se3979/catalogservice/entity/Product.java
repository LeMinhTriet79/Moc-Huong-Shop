package com.minhtriet.se3979.catalogservice.entity;

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

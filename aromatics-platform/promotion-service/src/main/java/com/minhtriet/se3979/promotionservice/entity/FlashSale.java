package com.minhtriet.se3979.promotionservice.entity;

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

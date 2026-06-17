package com.minhtriet.se3979.promotionservice.entity;

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

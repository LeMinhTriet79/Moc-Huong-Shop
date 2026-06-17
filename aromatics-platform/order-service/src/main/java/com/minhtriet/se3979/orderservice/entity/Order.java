package com.minhtriet.se3979.orderservice.entity;

import jakarta.persistence.*;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Entity
@Table(name = "orders")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class Order {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long userId;
    private String orderNumber;
    private String status;
    private BigDecimal totalAmount;
    private BigDecimal shippingFee;
    private BigDecimal discountAmount;
    private String paymentMethod;
    private String shippingAddress;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}

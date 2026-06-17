package com.minhtriet.se3979.paymentservice.entity;

import jakarta.persistence.*;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Entity
@Table(name = "transactions")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class Transaction {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String transactionId;
    private Long orderId;
    private BigDecimal amount;
    private String paymentMethod;
    private String status;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}

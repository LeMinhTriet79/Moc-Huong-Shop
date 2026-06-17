package com.minhtriet.se3979.paymentservice.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "payment_methods")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class PaymentMethod {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String code;
    private String name;
    private Boolean isActive;
}

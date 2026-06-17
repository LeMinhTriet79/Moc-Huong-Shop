package com.minhtriet.se3979.promotionservice.entity;

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

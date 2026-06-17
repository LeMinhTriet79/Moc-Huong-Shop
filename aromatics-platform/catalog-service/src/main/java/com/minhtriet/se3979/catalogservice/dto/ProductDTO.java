package com.minhtriet.se3979.catalogservice.dto;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class ProductDTO {
    private Long id;
    private String name;
    private BigDecimal basePrice;
    private String imageUrl;
}

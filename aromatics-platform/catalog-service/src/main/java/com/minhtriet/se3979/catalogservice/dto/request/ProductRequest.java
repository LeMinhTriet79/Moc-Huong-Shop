package com.minhtriet.se3979.catalogservice.dto.request;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class ProductRequest {
    private String name;
    private String description;
    private BigDecimal price;
    private Long categoryId;
}

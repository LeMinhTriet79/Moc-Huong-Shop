package com.minhtriet.se3979.cartservice.dto;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class CartItemDTO {
    private Long productId;
    private Long variantId;
    private String name;
    private BigDecimal price;
    private Integer quantity;
}

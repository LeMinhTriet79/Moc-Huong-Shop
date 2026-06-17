package com.minhtriet.se3979.cartservice.dto.response;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class CartItemResponse {
    private Long productId;
    private Integer quantity;
    private BigDecimal price;
}

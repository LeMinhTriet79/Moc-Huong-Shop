package com.minhtriet.se3979.cartservice.dto.request;
import lombok.*;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class CartItemRequest {
    private Long productId;
    private Integer quantity;
}

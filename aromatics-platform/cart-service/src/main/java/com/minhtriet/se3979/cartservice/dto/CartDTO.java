package com.minhtriet.se3979.cartservice.dto;
import lombok.*;
import java.math.BigDecimal;
import java.util.List;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class CartDTO {
    private String userId;
    private List<CartItemDTO> items;
    private BigDecimal totalPrice;
}

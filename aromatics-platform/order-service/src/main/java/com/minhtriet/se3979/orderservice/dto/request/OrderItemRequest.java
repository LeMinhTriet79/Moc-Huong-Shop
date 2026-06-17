package com.minhtriet.se3979.orderservice.dto.request;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class OrderItemRequest {
    private Long productId;
    private Integer quantity;
    private BigDecimal price;
}

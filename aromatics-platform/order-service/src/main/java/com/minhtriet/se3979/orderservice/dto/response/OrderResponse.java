package com.minhtriet.se3979.orderservice.dto.response;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class OrderResponse {
    private Long id;
    private Long userId;
    private BigDecimal totalAmount;
    private String status;
    private LocalDateTime createdAt;
}

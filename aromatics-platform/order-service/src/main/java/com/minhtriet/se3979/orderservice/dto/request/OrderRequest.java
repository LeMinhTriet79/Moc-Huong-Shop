package com.minhtriet.se3979.orderservice.dto.request;
import lombok.*;
import java.util.List;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class OrderRequest {
    private Long userId;
    private Long addressId;
    private Long paymentMethodId;
    private String couponCode;
    private List<OrderItemRequest> items;
}

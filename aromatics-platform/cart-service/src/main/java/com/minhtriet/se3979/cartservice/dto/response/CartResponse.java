package com.minhtriet.se3979.cartservice.dto.response;
import lombok.*;
import java.util.List;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class CartResponse {
    private String id; // userId
    private List<CartItemResponse> items;
}

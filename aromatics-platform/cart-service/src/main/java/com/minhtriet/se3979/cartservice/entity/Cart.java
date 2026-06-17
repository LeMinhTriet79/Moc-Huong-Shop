package com.minhtriet.se3979.cartservice.entity;

import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

import java.util.List;

@RedisHash("Cart")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class Cart {
    @Id
    private String id; // userId
    private List<CartItem> items;
}

package com.minhtriet.se3979.cartservice.service;
import com.minhtriet.se3979.cartservice.dto.request.CartItemRequest;
import com.minhtriet.se3979.cartservice.dto.response.CartResponse;
public interface CartService {
    CartResponse getCart(String userId);
    CartResponse addToCart(String userId, CartItemRequest request);
    void clearCart(String userId);
}

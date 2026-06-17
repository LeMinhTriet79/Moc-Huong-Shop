package com.minhtriet.se3979.cartservice.controller;
import com.minhtriet.se3979.cartservice.dto.request.CartItemRequest;
import com.minhtriet.se3979.cartservice.dto.response.CartResponse;
import com.minhtriet.se3979.cartservice.service.CartService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/cart")
@RequiredArgsConstructor
public class CartController {
    private final CartService cartService;

    @GetMapping("/{userId}")
    public ResponseEntity<CartResponse> getCart(@PathVariable String userId) {
        return ResponseEntity.ok(cartService.getCart(userId));
    }

    @PostMapping("/{userId}/items")
    public ResponseEntity<CartResponse> addToCart(@PathVariable String userId, @RequestBody CartItemRequest request) {
        return ResponseEntity.ok(cartService.addToCart(userId, request));
    }

    @DeleteMapping("/{userId}")
    public ResponseEntity<Void> clearCart(@PathVariable String userId) {
        cartService.clearCart(userId);
        return ResponseEntity.ok().build();
    }
}

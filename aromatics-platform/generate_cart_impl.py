import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/cart-service/src/main/java/com/minhtriet/se3979/cartservice"

os.makedirs(os.path.join(base_dir, "dto", "request"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "dto", "response"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "service", "impl"), exist_ok=True)

with open(os.path.join(base_dir, "dto", "request", "CartItemRequest.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.cartservice.dto.request;
import lombok.*;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class CartItemRequest {
    private Long productId;
    private Integer quantity;
}
""")

with open(os.path.join(base_dir, "dto", "response", "CartResponse.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.cartservice.dto.response;
import lombok.*;
import java.util.List;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class CartResponse {
    private String id; // userId
    private List<CartItemResponse> items;
}
""")

with open(os.path.join(base_dir, "dto", "response", "CartItemResponse.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.cartservice.dto.response;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class CartItemResponse {
    private Long productId;
    private Integer quantity;
    private BigDecimal price;
}
""")

with open(os.path.join(base_dir, "service", "CartService.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.cartservice.service;
import com.minhtriet.se3979.cartservice.dto.request.CartItemRequest;
import com.minhtriet.se3979.cartservice.dto.response.CartResponse;
public interface CartService {
    CartResponse getCart(String userId);
    CartResponse addToCart(String userId, CartItemRequest request);
    void clearCart(String userId);
}
""")

with open(os.path.join(base_dir, "service", "impl", "CartServiceImpl.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.cartservice.service.impl;
import com.minhtriet.se3979.cartservice.dto.request.CartItemRequest;
import com.minhtriet.se3979.cartservice.dto.response.CartItemResponse;
import com.minhtriet.se3979.cartservice.dto.response.CartResponse;
import com.minhtriet.se3979.cartservice.entity.Cart;
import com.minhtriet.se3979.cartservice.entity.CartItem;
import com.minhtriet.se3979.cartservice.repository.CartRedisRepository;
import com.minhtriet.se3979.cartservice.service.CartService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class CartServiceImpl implements CartService {
    private final CartRedisRepository cartRepository;

    @Override
    public CartResponse getCart(String userId) {
        Cart cart = cartRepository.findById(userId).orElse(new Cart(userId, new ArrayList<>()));
        return mapToResponse(cart);
    }

    @Override
    public CartResponse addToCart(String userId, CartItemRequest request) {
        Cart cart = cartRepository.findById(userId).orElse(new Cart(userId, new ArrayList<>()));
        // check if item exists
        boolean found = false;
        for (CartItem item : cart.getItems()) {
            if (item.getProductId().equals(request.getProductId())) {
                item.setQuantity(item.getQuantity() + request.getQuantity());
                found = true;
                break;
            }
        }
        if (!found) {
            cart.getItems().add(new CartItem(request.getProductId(), request.getQuantity(), BigDecimal.ZERO)); // price will be fetched from catalog
        }
        cartRepository.save(cart);
        return mapToResponse(cart);
    }

    @Override
    public void clearCart(String userId) {
        cartRepository.deleteById(userId);
    }

    private CartResponse mapToResponse(Cart cart) {
        List<CartItemResponse> items = cart.getItems().stream().map(i -> CartItemResponse.builder()
                .productId(i.getProductId())
                .quantity(i.getQuantity())
                .price(i.getPrice())
                .build()).collect(Collectors.toList());
        return CartResponse.builder().id(cart.getId()).items(items).build();
    }
}
""")

with open(os.path.join(base_dir, "controller", "CartController.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.cartservice.controller;
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
""")
print("Cart service implementation completed.")

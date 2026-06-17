package com.minhtriet.se3979.cartservice.service.impl;
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

import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/cart-service/src/main/java/com/minhtriet/se3979/cartservice"
packages = ["dto", "controller", "service", "redis"]

for p in packages:
    os.makedirs(os.path.join(base_dir, p), exist_ok=True)

dto = """package com.minhtriet.se3979.cartservice.dto;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class CartItemDTO {
    private Long productId;
    private Long variantId;
    private String name;
    private BigDecimal price;
    private Integer quantity;
}
"""

cart_dto = """package com.minhtriet.se3979.cartservice.dto;
import lombok.*;
import java.math.BigDecimal;
import java.util.List;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class CartDTO {
    private String userId;
    private List<CartItemDTO> items;
    private BigDecimal totalPrice;
}
"""

repo = """package com.minhtriet.se3979.cartservice.redis;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class CartRedisRepository {
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;
    // basic operations
}
"""

service = """package com.minhtriet.se3979.cartservice.service;
import com.minhtriet.se3979.cartservice.redis.CartRedisRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CartService {
    @Autowired
    private CartRedisRepository cartRedisRepository;
}
"""

controller = """package com.minhtriet.se3979.cartservice.controller;
import com.minhtriet.se3979.cartservice.service.CartService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/cart")
public class CartController {
    @Autowired
    private CartService cartService;
}
"""

with open(os.path.join(base_dir, "dto", "CartItemDTO.java"), "w") as f:
    f.write(dto)
with open(os.path.join(base_dir, "dto", "CartDTO.java"), "w") as f:
    f.write(cart_dto)
with open(os.path.join(base_dir, "redis", "CartRedisRepository.java"), "w") as f:
    f.write(repo)
with open(os.path.join(base_dir, "service", "CartService.java"), "w") as f:
    f.write(service)
with open(os.path.join(base_dir, "controller", "CartController.java"), "w") as f:
    f.write(controller)

print("Cart components generated.")

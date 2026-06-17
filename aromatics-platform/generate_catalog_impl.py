import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/catalog-service/src/main/java/com/minhtriet/se3979/catalogservice"

os.makedirs(os.path.join(base_dir, "dto", "request"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "dto", "response"), exist_ok=True)

with open(os.path.join(base_dir, "dto", "request", "ProductRequest.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.catalogservice.dto.request;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class ProductRequest {
    private String name;
    private String description;
    private BigDecimal price;
    private Long categoryId;
}
""")

with open(os.path.join(base_dir, "dto", "response", "ProductResponse.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.catalogservice.dto.response;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class ProductResponse {
    private Long id;
    private String name;
    private String description;
    private BigDecimal price;
    private String sku;
}
""")

with open(os.path.join(base_dir, "service", "ProductService.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.catalogservice.service;
import com.minhtriet.se3979.catalogservice.dto.request.ProductRequest;
import com.minhtriet.se3979.catalogservice.dto.response.ProductResponse;
import java.util.List;
public interface ProductService {
    List<ProductResponse> getAllProducts();
    ProductResponse getProductById(Long id);
    ProductResponse createProduct(ProductRequest request);
}
""")

with open(os.path.join(base_dir, "service", "impl", "ProductServiceImpl.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.catalogservice.service.impl;
import com.minhtriet.se3979.catalogservice.dto.request.ProductRequest;
import com.minhtriet.se3979.catalogservice.dto.response.ProductResponse;
import com.minhtriet.se3979.catalogservice.entity.Product;
import com.minhtriet.se3979.catalogservice.repository.ProductRepository;
import com.minhtriet.se3979.catalogservice.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class ProductServiceImpl implements ProductService {
    private final ProductRepository productRepository;

    @Override
    public List<ProductResponse> getAllProducts() {
        return productRepository.findAll().stream().map(p -> ProductResponse.builder().id(p.getId()).name(p.getName()).description(p.getDescription()).price(p.getBasePrice()).sku(p.getSku()).build()).collect(Collectors.toList());
    }

    @Override
    public ProductResponse getProductById(Long id) {
        Product p = productRepository.findById(id).orElseThrow(() -> new RuntimeException("Not found"));
        return ProductResponse.builder().id(p.getId()).name(p.getName()).description(p.getDescription()).price(p.getBasePrice()).sku(p.getSku()).build();
    }

    @Override
    public ProductResponse createProduct(ProductRequest request) {
        Product p = new Product();
        p.setName(request.getName());
        p.setDescription(request.getDescription());
        p.setBasePrice(request.getPrice());
        p.setSku(UUID.randomUUID().toString());
        p = productRepository.save(p);
        return ProductResponse.builder().id(p.getId()).name(p.getName()).description(p.getDescription()).price(p.getBasePrice()).sku(p.getSku()).build();
    }
}
""")

with open(os.path.join(base_dir, "controller", "ProductController.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.catalogservice.controller;
import com.minhtriet.se3979.catalogservice.dto.request.ProductRequest;
import com.minhtriet.se3979.catalogservice.dto.response.ProductResponse;
import com.minhtriet.se3979.catalogservice.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/catalog/products")
@RequiredArgsConstructor
public class ProductController {
    private final ProductService productService;

    @GetMapping
    public ResponseEntity<List<ProductResponse>> getAll() {
        return ResponseEntity.ok(productService.getAllProducts());
    }

    @GetMapping("/{id}")
    public ResponseEntity<ProductResponse> getById(@PathVariable Long id) {
        return ResponseEntity.ok(productService.getProductById(id));
    }

    @PostMapping
    public ResponseEntity<ProductResponse> create(@RequestBody ProductRequest request) {
        return ResponseEntity.ok(productService.createProduct(request));
    }
}
""")
print("Catalog service implementation completed.")

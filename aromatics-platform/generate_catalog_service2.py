import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/catalog-service/src/main/java/com/minhtriet/se3979/catalogservice"

dto_content = """package com.minhtriet.se3979.catalogservice.dto;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class ProductDTO {
    private Long id;
    private String name;
    private BigDecimal basePrice;
    private String imageUrl;
}
"""

service_content = """package com.minhtriet.se3979.catalogservice.service;
import com.minhtriet.se3979.catalogservice.entity.Product;
import com.minhtriet.se3979.catalogservice.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class ProductService {
    @Autowired
    private ProductRepository productRepository;

    public List<Product> getAllProducts() {
        return productRepository.findAll();
    }
}
"""

controller_content = """package com.minhtriet.se3979.catalogservice.controller;
import com.minhtriet.se3979.catalogservice.entity.Product;
import com.minhtriet.se3979.catalogservice.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/catalog/products")
public class ProductController {
    @Autowired
    private ProductService productService;

    @GetMapping
    public List<Product> getAllProducts() {
        return productService.getAllProducts();
    }
}
"""

with open(os.path.join(base_dir, "dto", "ProductDTO.java"), "w") as f:
    f.write(dto_content)

with open(os.path.join(base_dir, "service", "ProductService.java"), "w") as f:
    f.write(service_content)

with open(os.path.join(base_dir, "controller", "ProductController.java"), "w") as f:
    f.write(controller_content)

print("Service and Controller generated.")

package com.minhtriet.se3979.catalogservice.service.impl;
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
        return productRepository.findAll().stream().map(p -> ProductResponse.builder().id(p.getId()).name(p.getName()).description(p.getDescription()).price(p.getBasePrice()).sku(p.getSlug()).build()).collect(Collectors.toList());
    }

    @Override
    public ProductResponse getProductById(Long id) {
        Product p = productRepository.findById(id).orElseThrow(() -> new RuntimeException("Not found"));
        return ProductResponse.builder().id(p.getId()).name(p.getName()).description(p.getDescription()).price(p.getBasePrice()).sku(p.getSlug()).build();
    }

    @Override
    public ProductResponse createProduct(ProductRequest request) {
        Product p = new Product();
        p.setName(request.getName());
        p.setDescription(request.getDescription());
        p.setBasePrice(request.getPrice());
        p.setSlug(UUID.randomUUID().toString());
        p = productRepository.save(p);
        return ProductResponse.builder().id(p.getId()).name(p.getName()).description(p.getDescription()).price(p.getBasePrice()).sku(p.getSlug()).build();
    }
}

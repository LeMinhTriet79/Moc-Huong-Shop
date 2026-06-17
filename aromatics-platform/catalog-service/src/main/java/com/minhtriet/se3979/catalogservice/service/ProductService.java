package com.minhtriet.se3979.catalogservice.service;
import com.minhtriet.se3979.catalogservice.dto.request.ProductRequest;
import com.minhtriet.se3979.catalogservice.dto.response.ProductResponse;
import java.util.List;
public interface ProductService {
    List<ProductResponse> getAllProducts();
    ProductResponse getProductById(Long id);
    ProductResponse createProduct(ProductRequest request);
}

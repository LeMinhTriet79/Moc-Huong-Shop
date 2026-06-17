package com.minhtriet.se3979.catalogservice.service;
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

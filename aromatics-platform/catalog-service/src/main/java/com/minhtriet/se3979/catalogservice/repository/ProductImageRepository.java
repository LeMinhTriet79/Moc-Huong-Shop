package com.minhtriet.se3979.catalogservice.repository;

import com.minhtriet.se3979.catalogservice.entity.ProductImage;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductImageRepository extends JpaRepository<ProductImage, Long> {
}

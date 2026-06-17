package com.minhtriet.se3979.promotionservice.repository;

import com.minhtriet.se3979.promotionservice.entity.FlashSale;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FlashSaleRepository extends JpaRepository<FlashSale, Long> {
}

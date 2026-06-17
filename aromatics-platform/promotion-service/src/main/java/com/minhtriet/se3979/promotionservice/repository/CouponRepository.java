package com.minhtriet.se3979.promotionservice.repository;

import com.minhtriet.se3979.promotionservice.entity.Coupon;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CouponRepository extends JpaRepository<Coupon, Long> {
    java.util.Optional<Coupon> findByCode(String code);
}

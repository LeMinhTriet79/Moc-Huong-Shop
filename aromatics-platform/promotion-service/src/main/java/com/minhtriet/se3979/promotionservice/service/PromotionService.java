package com.minhtriet.se3979.promotionservice.service;
import com.minhtriet.se3979.promotionservice.entity.Coupon;
import com.minhtriet.se3979.promotionservice.repository.CouponRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class PromotionService {
    @Autowired
    private CouponRepository couponRepository;

    public List<Coupon> getAllCoupons() {
        return couponRepository.findAll();
    }
}

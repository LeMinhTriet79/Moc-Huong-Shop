package com.minhtriet.se3979.promotionservice.service;
import com.minhtriet.se3979.promotionservice.dto.response.CouponResponse;

public interface CouponService {
    CouponResponse getCouponByCode(String code);
}

package com.minhtriet.se3979.promotionservice.service.impl;
import com.minhtriet.se3979.promotionservice.dto.response.CouponResponse;
import com.minhtriet.se3979.promotionservice.entity.Coupon;
import com.minhtriet.se3979.promotionservice.repository.CouponRepository;
import com.minhtriet.se3979.promotionservice.service.CouponService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class CouponServiceImpl implements CouponService {
    private final CouponRepository couponRepository;

    @Override
    public CouponResponse getCouponByCode(String code) {
        Coupon c = couponRepository.findByCode(code).orElseThrow(() -> new RuntimeException("Coupon not found"));
        return CouponResponse.builder()
                .code(c.getCode())
                .discountType(c.getDiscountType())
                .discountValue(c.getDiscountValue())
                .minOrderValue(c.getMinOrderValue())
                .maxDiscountAmount(null)
                .usageLimit(c.getMaxUsages())
                .usedCount(0)
                .startDate(c.getStartDate())
                .endDate(c.getEndDate())
                .build();
    }
}

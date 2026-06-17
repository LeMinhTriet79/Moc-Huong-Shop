package com.minhtriet.se3979.promotionservice.controller;
import com.minhtriet.se3979.promotionservice.dto.response.CouponResponse;
import com.minhtriet.se3979.promotionservice.service.CouponService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/promotion/coupons")
@RequiredArgsConstructor
public class CouponController {
    private final CouponService couponService;

    @GetMapping("/{code}")
    public ResponseEntity<CouponResponse> getCoupon(@PathVariable String code) {
        return ResponseEntity.ok(couponService.getCouponByCode(code));
    }
}

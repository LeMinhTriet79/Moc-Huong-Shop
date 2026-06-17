package com.minhtriet.se3979.promotionservice.controller;
import com.minhtriet.se3979.promotionservice.entity.Coupon;
import com.minhtriet.se3979.promotionservice.service.PromotionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/promotion")
public class PromotionController {
    @Autowired
    private PromotionService promotionService;

    @GetMapping("/coupons")
    public List<Coupon> getAllCoupons() {
        return promotionService.getAllCoupons();
    }
}

import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/promotion-service/src/main/java/com/minhtriet/se3979/promotionservice"

service_content = """package com.minhtriet.se3979.promotionservice.service;
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
"""

controller_content = """package com.minhtriet.se3979.promotionservice.controller;
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
"""

with open(os.path.join(base_dir, "service", "PromotionService.java"), "w") as f:
    f.write(service_content)

with open(os.path.join(base_dir, "controller", "PromotionController.java"), "w") as f:
    f.write(controller_content)

print("Promotion Service and Controller generated.")

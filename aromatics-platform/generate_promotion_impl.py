import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/promotion-service/src/main/java/com/minhtriet/se3979/promotionservice"

os.makedirs(os.path.join(base_dir, "dto", "response"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "service", "impl"), exist_ok=True)

with open(os.path.join(base_dir, "dto", "response", "CouponResponse.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.promotionservice.dto.response;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class CouponResponse {
    private String code;
    private String discountType;
    private BigDecimal discountValue;
    private BigDecimal minOrderValue;
    private BigDecimal maxDiscountAmount;
    private Integer usageLimit;
    private Integer usedCount;
    private LocalDateTime startDate;
    private LocalDateTime endDate;
}
""")

with open(os.path.join(base_dir, "service", "CouponService.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.promotionservice.service;
import com.minhtriet.se3979.promotionservice.dto.response.CouponResponse;

public interface CouponService {
    CouponResponse getCouponByCode(String code);
}
""")

with open(os.path.join(base_dir, "service", "impl", "CouponServiceImpl.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.promotionservice.service.impl;
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
                .maxDiscountAmount(c.getMaxDiscountAmount())
                .usageLimit(c.getUsageLimit())
                .usedCount(c.getUsedCount())
                .startDate(c.getStartDate())
                .endDate(c.getEndDate())
                .build();
    }
}
""")

with open(os.path.join(base_dir, "controller", "CouponController.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.promotionservice.controller;
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
""")
print("Promotion service implementation completed.")

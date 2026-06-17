package com.minhtriet.se3979.catalogservice.dto.response;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class ProductResponse implements java.io.Serializable {
    private Long id;
    private String name;
    private String description;
    private BigDecimal price;
    private String sku;
}

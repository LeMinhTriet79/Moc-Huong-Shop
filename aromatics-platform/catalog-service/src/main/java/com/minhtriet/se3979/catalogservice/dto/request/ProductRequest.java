package com.minhtriet.se3979.catalogservice.dto.request;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class ProductRequest {
    @jakarta.validation.constraints.NotBlank(message="Name is required") private String name;
    private String description;
    @jakarta.validation.constraints.NotNull(message="Price is required") private java.math.BigDecimal price;
    private Long categoryId;
}

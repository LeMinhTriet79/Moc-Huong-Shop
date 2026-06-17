package com.minhtriet.se3979.identityservice.dto.response;
import lombok.*;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class AddressResponse {
    private Long id;
    private String fullName;
    private String phoneNumber;
    private String province;
    private String district;
    private String ward;
    private String detailedAddress;
    private Boolean isDefault;
}

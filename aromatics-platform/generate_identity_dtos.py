import os
import re

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/identity-service/src/main/java/com/minhtriet/se3979/identityservice"

# DTOs
dto_dir = os.path.join(base_dir, "dto")

with open(os.path.join(dto_dir, "response", "AddressResponse.java"), "w") as f:
    f.write("""package com.minhtriet.se3979.identityservice.dto.response;
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
""")

with open(os.path.join(dto_dir, "request", "WishlistRequest.java"), "w") as f:
    f.write("""package com.minhtriet.se3979.identityservice.dto.request;
import lombok.*;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class WishlistRequest {
    private Long productId;
}
""")

with open(os.path.join(dto_dir, "response", "WishlistResponse.java"), "w") as f:
    f.write("""package com.minhtriet.se3979.identityservice.dto.response;
import lombok.*;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class WishlistResponse {
    private Long id;
    private Long productId;
}
""")

print("Identity service address & wishlist DTOs created.")

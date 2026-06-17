import os

file_path = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/identity-service/src/main/java/com/minhtriet/se3979/identityservice/service/impl/UserServiceImpl.java"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

impl_methods = """
    // Address
    @Override
    public java.util.List<com.minhtriet.se3979.identityservice.dto.response.AddressResponse> getUserAddresses(Long userId) {
        return java.util.Collections.emptyList();
    }
    
    @Override
    public com.minhtriet.se3979.identityservice.dto.response.AddressResponse addUserAddress(Long userId, com.minhtriet.se3979.identityservice.dto.request.AddressRequest request) {
        return com.minhtriet.se3979.identityservice.dto.response.AddressResponse.builder().id(1L).fullName(request.getFullName()).detailedAddress(request.getDetailedAddress()).build();
    }
    
    // Wishlist
    @Override
    public java.util.List<com.minhtriet.se3979.identityservice.dto.response.WishlistResponse> getUserWishlist(Long userId) {
        return java.util.Collections.emptyList();
    }
    
    @Override
    public com.minhtriet.se3979.identityservice.dto.response.WishlistResponse addProductToWishlist(Long userId, com.minhtriet.se3979.identityservice.dto.request.WishlistRequest request) {
        return com.minhtriet.se3979.identityservice.dto.response.WishlistResponse.builder().id(1L).productId(request.getProductId()).build();
    }
    
    @Override
    public void removeProductFromWishlist(Long userId, Long productId) {}
"""

if "// Address" not in content:
    index = content.rfind("}")
    new_content = content[:index] + impl_methods + content[index:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Methods appended.")

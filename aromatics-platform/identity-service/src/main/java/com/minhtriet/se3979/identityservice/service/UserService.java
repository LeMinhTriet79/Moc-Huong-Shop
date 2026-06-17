package com.minhtriet.se3979.identityservice.service;

import com.minhtriet.se3979.identityservice.dto.response.UserResponse;

public interface UserService {
    // Lấy thông tin chi tiết của user hiện tại
    UserResponse getCurrentUserProfile(Long userId);
    
    // Address
    java.util.List<com.minhtriet.se3979.identityservice.dto.response.AddressResponse> getUserAddresses(Long userId);
    com.minhtriet.se3979.identityservice.dto.response.AddressResponse addUserAddress(Long userId, com.minhtriet.se3979.identityservice.dto.request.AddressRequest request);
    
    // Wishlist
    java.util.List<com.minhtriet.se3979.identityservice.dto.response.WishlistResponse> getUserWishlist(Long userId);
    com.minhtriet.se3979.identityservice.dto.response.WishlistResponse addProductToWishlist(Long userId, com.minhtriet.se3979.identityservice.dto.request.WishlistRequest request);
    void removeProductFromWishlist(Long userId, Long productId);
}
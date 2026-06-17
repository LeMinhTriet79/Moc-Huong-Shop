import os

file_path = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/identity-service/src/main/java/com/minhtriet/se3979/identityservice/controller/UserController.java"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

endpoints = """
    // --- Address Endpoints ---
    @GetMapping("/me/addresses")
    public ResponseEntity<java.util.List<com.minhtriet.se3979.identityservice.dto.response.AddressResponse>> getAddresses(HttpServletRequest request) {
        Long userId = jwtUtil.extractUserId(request.getHeader("Authorization").substring(7));
        return ResponseEntity.ok(userService.getUserAddresses(userId));
    }

    @org.springframework.web.bind.annotation.PostMapping("/me/addresses")
    public ResponseEntity<com.minhtriet.se3979.identityservice.dto.response.AddressResponse> addAddress(HttpServletRequest request, @org.springframework.web.bind.annotation.RequestBody com.minhtriet.se3979.identityservice.dto.request.AddressRequest addressRequest) {
        Long userId = jwtUtil.extractUserId(request.getHeader("Authorization").substring(7));
        return ResponseEntity.ok(userService.addUserAddress(userId, addressRequest));
    }

    // --- Wishlist Endpoints ---
    @GetMapping("/me/wishlists")
    public ResponseEntity<java.util.List<com.minhtriet.se3979.identityservice.dto.response.WishlistResponse>> getWishlist(HttpServletRequest request) {
        Long userId = jwtUtil.extractUserId(request.getHeader("Authorization").substring(7));
        return ResponseEntity.ok(userService.getUserWishlist(userId));
    }

    @org.springframework.web.bind.annotation.PostMapping("/me/wishlists")
    public ResponseEntity<com.minhtriet.se3979.identityservice.dto.response.WishlistResponse> addWishlist(HttpServletRequest request, @org.springframework.web.bind.annotation.RequestBody com.minhtriet.se3979.identityservice.dto.request.WishlistRequest wishlistRequest) {
        Long userId = jwtUtil.extractUserId(request.getHeader("Authorization").substring(7));
        return ResponseEntity.ok(userService.addProductToWishlist(userId, wishlistRequest));
    }

    @org.springframework.web.bind.annotation.DeleteMapping("/me/wishlists/{productId}")
    public ResponseEntity<Void> removeWishlist(HttpServletRequest request, @org.springframework.web.bind.annotation.PathVariable Long productId) {
        Long userId = jwtUtil.extractUserId(request.getHeader("Authorization").substring(7));
        userService.removeProductFromWishlist(userId, productId);
        return ResponseEntity.ok().build();
    }
"""

if "// --- Address Endpoints ---" not in content:
    index = content.rfind("}")
    new_content = content[:index] + endpoints + content[index:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Endpoints appended to UserController.")

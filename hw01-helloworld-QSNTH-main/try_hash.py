import hashlib

def pure_hash_test():
    """純SHA-256 哈希測試函數"""
    print("=== 純 SHA-256 哈希測試 ===\n")
    
    # 定義測試用的明文密碼
    password_original = "123456"    # 原始密碼
    password_same = "123456"        # 和原始密碼相同
    password_different = "123457"   # 仅差一個字元的密碼
    password_long = "1234567890abcdef"  # 更長的密碼
    
    # 計算各明文的 SHA-256 哈希值
    def get_sha256_hash(plain_text):
        """将明文轉為SHA-256 哈希值"""
        # 將字串轉為位元組（hashlib 要求輸入為位元组）
        text_bytes = plain_text.encode('utf-8')
        # 計算哈希並轉為十六進位字串（易讀格式）
        hash_result = hashlib.sha256(text_bytes).hexdigest()
        return hash_result
    
    # 獲取各密碼的哈希值
    hash_original = get_sha256_hash(password_original)
    hash_same = get_sha256_hash(password_same)
    hash_different = get_sha256_hash(password_different)
    hash_long = get_sha256_hash(password_long)

    # 列印測試結果
    print(f"1. 明文 '{password_original}' 的哈希值:\n{hash_original}\n")
    print(f"2. 相同明文 '{password_same}' 的哈希值:\n{hash_same}")
    print(f" → 相同明文哈希值是否一致: {hash_original == hash_same}\n")
    print(f"3. 差異明文 '{password_different}' 的哈希值:\n{hash_different}")
    print(f" → 差異明文哈希值是否一致: {hash_original == hash_different}\n")
    print(f"4. 長明文 '{password_long}' 的哈希值（長度仍固定）：\n{hash_long}")
    print(f" → 哈希值長度: {len(hash_long)} 個字元【SHA-256 固定64位】\n")
    
    # 驗證「單向不可逆」特性（無法從哈希值反推明文）
    print("5. 哈希特性：無法從哈希值反推出原始明文！")
    print("註：没有任何函數能直接將上述哈希值還原為'123456")

if __name__ == "__main__":
    # 執行測試
    pure_hash_test()
import argparse
import hashlib
import sys

CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def do_hash(password: str) -> str:
    """計算並返回給定密碼的 SHA-512 哈希值（使用 utf-16be 編碼）"""
    text_bytes = password.encode('utf-16be')
    return hashlib.sha1(text_bytes).hexdigest()

def int_to_base36(n: int) -> str:
    if n == 0:
        return '0'
    digits = []
    base = 36
    while n > 0:
        n, rem = divmod(n, base)
        digits.append(CHARS[rem])
    return ''.join(reversed(digits))

def generate_base36_strings(length: int):
    max_n = 36 ** length
    for n in range(max_n):
        s = int_to_base36(n).rjust(length, '0')
        yield s

def main():
    parser = argparse.ArgumentParser(description='Generate base36 strings and print SHA-512 hashes.')
    parser.add_argument('--start-length', type=int, default=7, help='起始長度（含）')
    parser.add_argument('--end-length', type=int, default=10, help='結束長度（含）')
    parser.add_argument('--max', type=int, default=0, help='最大輸出數量（0 表示不限制；預設 100000）')
    parser.add_argument('--outfile', type=str, help='可選：將輸出寫入檔案，減少終端輸出')
    parser.add_argument('--all', action='store_true', help='允許遍歷完整範圍（非常大，危險，通常不建議）')
    args = parser.parse_args()

    if args.all and not args.outfile:
        print('拒絕在終端輸出完整範圍；若確實要執行請加上 --outfile FILE', file=sys.stderr)
        sys.exit(1)

    start_len = args.start_length
    end_len = args.end_length
    if start_len < 1 or end_len < start_len:
        print('長度參數不合法', file=sys.stderr)
        sys.exit(1)

    max_count = args.max if args.max > 0 else None
    count = 0

    out = open(args.outfile, 'w') if args.outfile else None

    try:
        for length in range(start_len, end_len + 1):
            for s in generate_base36_strings(length):
                line = f"原始密碼: {s}\nSHA-512 哈希值: {do_hash(s)}\n"
                if out:
                    out.write(line)
                else:
                    print(line, end='')

                count += 1
                if max_count is not None and count >= max_count:
                    return
    finally:
        if out:
            out.close()

if __name__ == '__main__':
    main()